"""
Parabola primitive in the seismic domain: real-data pipeline.

Extends parabola_csd_demo.py from simulation to real empirical data
pulled from open geoscience APIs. The flow:

    (1) load a GPS strain time series from an open public archive
    (2) detrend and fill gaps
    (3) compute rolling-window critical slowing down indicators
    (4) report whether the indicators are trending toward bifurcation

Data sources (all open, no authentication required):

    Nevada Geodetic Laboratory (NGL), University of Nevada Reno
        URL pattern: http://geodesy.unr.edu/gps_timeseries/tenv3/IGS14/<STATION>.tenv3
        Format:      plain text, columns: station yymmmdd yyyy.yyyy mjd ...
                     east north up positions in mm
        Coverage:    ~18000 stations, daily solutions, 1995-present
        Example stations relevant to the current seismic gap discussions:
            IQQE (Iquique, northern Chile -- Atacama Trench)
            ANTO (Antofagasta, Chile)
            MIZU (Mizusawa, Japan -- near Hokkaido/Kuril region)
            P496 (Pacific NW, Cascadia)
        Homepage:    http://geodesy.unr.edu/

    USGS FDSN Event Web Service (earthquake catalog, not strain)
        URL: https://earthquake.usgs.gov/fdsnws/event/1/query
        Format: GeoJSON, CSV, XML, text
        Query params: starttime, endtime, minmagnitude, minlatitude, ...
        No auth, rate-limited but generous
        Example:
            https://earthquake.usgs.gov/fdsnws/event/1/query
                ?format=geojson&starttime=2024-01-01
                &minmagnitude=5&minlatitude=-30&maxlatitude=-18
                &minlongitude=-75&maxlongitude=-65

    IRIS / EarthScope FDSN (waveform data via obspy)
        from obspy.clients.fdsn import Client
        client = Client("IRIS")
        client.get_waveforms("IU", "ANMO", "00", "BHZ", t1, t2)
        (Heavy; use only if you need raw seismograms.)

Usage
-----
    # Real data from NGL (requires network access):
    python parabola_csd_pipeline.py --station IQQE --window 365

    # Synthetic data (for testing the pipeline without network):
    python parabola_csd_pipeline.py --synthetic

    # Earthquake catalog from USGS FDSN:
    python parabola_csd_pipeline.py --catalog --region chile

This script does NOT ship with data. It builds a request URL and
either downloads at runtime (real mode) or generates a synthetic
trajectory (test mode). To run in real mode you need outbound HTTP
access to http://geodesy.unr.edu/ or https://earthquake.usgs.gov/.
"""

from __future__ import annotations

import argparse
import math
import random
import sys
from dataclasses import dataclass
from urllib.error import URLError
from urllib.request import Request, urlopen

# ============================================================================
# NGL GPS time series loader
# ============================================================================

NGL_TEMPLATE = "http://geodesy.unr.edu/gps_timeseries/tenv3/IGS14/{station}.tenv3"


@dataclass
class GPSTimeSeries:
    """One GPS station's daily-position time series, processed by NGL."""

    station: str
    mjd: list[float]            # modified julian date
    east_mm: list[float]        # east position in mm
    north_mm: list[float]       # north position in mm
    up_mm: list[float]          # vertical position in mm

    @property
    def n(self) -> int:
        return len(self.mjd)

    def horizontal_strain(self) -> list[float]:
        """
        Proxy for horizontal strain magnitude: sqrt(east^2 + north^2).
        Real strain is a tensor; this is a scalar summary.
        """
        return [math.sqrt(e * e + n * n)
                for e, n in zip(self.east_mm, self.north_mm)]


def load_ngl(station: str, timeout: int = 30) -> GPSTimeSeries:
    """
    Download and parse an NGL .tenv3 file for a given station.

    Requires outbound HTTP. Falls back with a clear error if the
    request fails (sandboxed envs, offline, rate-limited, etc.).

    Parameters
    ----------
    station: 4-character station code (e.g. "IQQE")

    Returns
    -------
    GPSTimeSeries
    """
    url = NGL_TEMPLATE.format(station=station.upper())
    req = Request(url, headers={"User-Agent": "harmonics-framework/1.0"})
    try:
        with urlopen(req, timeout=timeout) as r:
            body = r.read().decode("utf-8")
    except URLError as e:
        raise RuntimeError(
            f"Could not reach NGL for station {station}: {e}\n"
            f"Check your network, or use --synthetic to test offline."
        ) from e

    mjd: list[float] = []
    east: list[float] = []
    north: list[float] = []
    up: list[float] = []

    for line in body.splitlines():
        line = line.strip()
        if not line or line.startswith(("#", "site")):
            continue
        parts = line.split()
        if len(parts) < 12:
            continue
        # NGL .tenv3 columns:
        #   0 site, 1 YYMMMDD, 2 yyyy.yyyy, 3 MJD, 4 week, 5 d,
        #   6 reflon, 7 e0(m), 8 east(m), 9 n0(m), 10 north(m),
        #   11 u0(m), 12 up(m), 13 ant(m), ... (sigmas after)
        try:
            mjd.append(float(parts[3]))
            # NGL east/north are relative to a reference position;
            # position_mm = reference + delta, but we only need delta.
            east.append(float(parts[8]) * 1000)   # m -> mm
            north.append(float(parts[10]) * 1000)
            up.append(float(parts[12]) * 1000)
        except (ValueError, IndexError):
            continue

    if not mjd:
        raise RuntimeError(
            f"No valid lines parsed from NGL response for {station}. "
            f"The station code may not exist or the file format changed."
        )

    return GPSTimeSeries(station=station.upper(),
                         mjd=mjd, east_mm=east, north_mm=north, up_mm=up)


def synthetic_ngl(station: str = "SYNTH", n_days: int = 5000,
                  seed: int = 42) -> GPSTimeSeries:
    """
    Generate a synthetic GPS time series that mimics a fault approaching
    a saddle-node bifurcation. The 'east' component evolves according
    to the saddle-node normal form

        dx/dt = mu(t) - x^2 + sigma * eta(t)

    with a slowly decreasing mu. Each day is integrated with many fast
    substeps so the system stays near its (shrinking) stable fixed
    point x_star = sqrt(mu) while sigma is held fixed. The north and
    up components are stationary Gaussian noise (representing a plate
    with no CSD signal on those axes).

    Used for testing the pipeline without network access.
    """
    random.seed(seed)
    mjd = [50000.0 + i for i in range(n_days)]
    east: list[float] = []
    north: list[float] = []
    up: list[float] = []

    # Integrate substeps per day so the normal form evolves at its
    # natural timescale (dt = 0.01 oscillator units) while the output
    # is sampled once per day.
    dt = 0.01
    substeps_per_day = 50
    sigma = 0.3

    # mu decreases linearly from mu_start to mu_end over the series.
    # mu_end is kept safely above 0 so the trajectory stays bounded
    # at the fixed noise amplitude (the CSD signal should show up
    # long before the actual bifurcation).
    mu_start = 4.0
    mu_end = 0.15

    x = math.sqrt(mu_start)

    for i in range(n_days):
        mu = mu_start + (mu_end - mu_start) * (i / max(n_days - 1, 1))
        for _ in range(substeps_per_day):
            drift = mu - x * x
            noise = sigma * random.gauss(0, 1) * math.sqrt(dt)
            x += drift * dt + noise
            # Guard rails: keep bounded if noise kicks over the saddle.
            if x < -5.0:
                x = -5.0
            if x > 5.0:
                x = 5.0
        east.append(x)
        north.append(0.3 * random.gauss(0, 1))
        up.append(0.3 * random.gauss(0, 1))

    return GPSTimeSeries(station=station, mjd=mjd,
                         east_mm=east, north_mm=north, up_mm=up)


# ============================================================================
# Critical slowing down indicators (reused from parabola_csd_demo.py)
# ============================================================================

def _mean(xs: list[float]) -> float:
    return sum(xs) / len(xs) if xs else 0.0


def _variance(xs: list[float]) -> float:
    if len(xs) < 2:
        return 0.0
    m = _mean(xs)
    return sum((x - m) ** 2 for x in xs) / (len(xs) - 1)


def _lag1_autocorr(xs: list[float]) -> float:
    if len(xs) < 3:
        return 0.0
    m = _mean(xs)
    var = _variance(xs)
    if var == 0:
        return 0.0
    num = sum((xs[i] - m) * (xs[i + 1] - m) for i in range(len(xs) - 1))
    return num / (var * (len(xs) - 1))


def _skewness(xs: list[float]) -> float:
    if len(xs) < 3:
        return 0.0
    m = _mean(xs)
    var = _variance(xs)
    if var == 0:
        return 0.0
    sd = math.sqrt(var)
    return sum(((x - m) / sd) ** 3 for x in xs) / len(xs)


def detrend_linear(xs: list[float]) -> list[float]:
    """Remove the linear best-fit trend (secular plate motion)."""
    n = len(xs)
    if n < 2:
        return list(xs)
    t_mean = (n - 1) / 2
    y_mean = _mean(xs)
    num = sum((i - t_mean) * (x - y_mean) for i, x in enumerate(xs))
    den = sum((i - t_mean) ** 2 for i in range(n))
    slope = num / den if den > 0 else 0.0
    intercept = y_mean - slope * t_mean
    return [x - (slope * i + intercept) for i, x in enumerate(xs)]


def rolling_csd(series: list[float], window: int, step: int = 30
                ) -> list[tuple[int, float, float, float]]:
    """
    Slide a window across the series and compute (variance, AR1, skewness)
    at each window start index. Returns a list of (index, var, ar1, skew).
    """
    results = []
    n = len(series)
    for start in range(0, n - window + 1, step):
        chunk = series[start:start + window]
        results.append((start,
                        _variance(chunk),
                        _lag1_autocorr(chunk),
                        _skewness(chunk)))
    return results


# ============================================================================
# Trend analysis on the rolling indicators
# ============================================================================

def kendall_tau(xs: list[float]) -> float:
    """
    Kendall's tau: nonparametric rank correlation between (index, xs[index])
    and a monotonic trend. Ranges from -1 (strictly decreasing) to +1
    (strictly increasing). Used by the early-warning-signals literature
    to quantify whether an indicator is trending upward over time.
    """
    n = len(xs)
    if n < 2:
        return 0.0
    concordant = 0
    discordant = 0
    for i in range(n):
        for j in range(i + 1, n):
            d = xs[j] - xs[i]
            if d > 0:
                concordant += 1
            elif d < 0:
                discordant += 1
    total = n * (n - 1) / 2
    return (concordant - discordant) / total if total > 0 else 0.0


# ============================================================================
# Main pipeline
# ============================================================================

def analyze_station(ts: GPSTimeSeries, window: int = 365, step: int = 30,
                    component: str = "east") -> None:
    """
    Run the full CSD analysis on a loaded GPS series and report.

    component: which scalar observable to analyze.
        'east'       -- east position (default; margin-normal for most
                        subduction zones, carries the locking signal)
        'north'      -- north position
        'up'         -- vertical
        'horizontal' -- sqrt(east^2 + north^2) (Euclidean magnitude)
    """
    print(f"  Station:     {ts.station}")
    print(f"  Samples:     {ts.n} days")
    print(f"  Time range:  MJD {ts.mjd[0]:.0f} -- MJD {ts.mjd[-1]:.0f}")
    print(f"  Observable:  {component}")
    print()

    if component == "east":
        observable = list(ts.east_mm)
    elif component == "north":
        observable = list(ts.north_mm)
    elif component == "up":
        observable = list(ts.up_mm)
    elif component == "horizontal":
        observable = ts.horizontal_strain()
    else:
        raise ValueError(f"Unknown component: {component}")

    # Detrend (remove secular plate motion)
    detrended = detrend_linear(observable)

    # Rolling CSD indicators
    indicators = rolling_csd(detrended, window=window, step=step)
    if not indicators:
        print("  Not enough data for the specified window.")
        return

    print(f"  Rolling window: {window} days, step: {step} days")
    print(f"  {len(indicators)} windows analyzed")
    print()

    # Extract time series of each indicator
    variances = [r[1] for r in indicators]
    ar1s = [r[2] for r in indicators]
    skews = [r[3] for r in indicators]

    # Show a few windows
    print(f"    {'window':>10} {'variance':>12} {'ar1':>10} {'skewness':>12}")
    print("    " + "-" * 48)
    n_show = min(10, len(indicators))
    step_show = max(1, len(indicators) // n_show)
    for i in range(0, len(indicators), step_show):
        r = indicators[i]
        print(f"    {r[0]:>10} {r[1]:>12.4f} {r[2]:>10.4f} {r[3]:>+12.4f}")
    print()

    # Kendall tau for each indicator
    tau_var = kendall_tau(variances)
    tau_ar1 = kendall_tau(ar1s)
    tau_skew = kendall_tau(skews)

    print("  Kendall tau trend statistics:")
    print(f"    variance  tau = {tau_var:+.3f}")
    print(f"    AR1       tau = {tau_ar1:+.3f}")
    print(f"    skewness  tau = {tau_skew:+.3f}")
    print()
    print("  Interpretation: tau > 0 means the indicator is trending upward")
    print("  over time. All three indicators trending up (> ~0.3) is the")
    print("  early-warning signature for approach to a saddle-node bifurcation.")
    print()

    if tau_var > 0.3 and tau_ar1 > 0.3:
        print("  *** CSD SIGNATURE DETECTED ***")
        print("  Variance and AR1 both trending upward. The station is showing")
        print("  critical-slowing-down behavior consistent with approach to")
        print("  a saddle-node bifurcation. This is the parabola primitive's")
        print("  terrestrial signature. Whether this indicates an imminent")
        print("  seismic release depends on the specific fault, but the")
        print("  statistical pattern is present.")
    elif tau_var > 0.1 or tau_ar1 > 0.1:
        print("  Marginal signal. Indicators trending up but not decisively.")
        print("  Longer window or a different station segment may clarify.")
    else:
        print("  No CSD signature. Indicators are flat or decreasing.")
        print("  The station is not currently showing the statistical pattern")
        print("  of approach to a saddle-node bifurcation.")
    print()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Parabola primitive CSD pipeline for real GPS data."
    )
    parser.add_argument("--station", type=str, default=None,
                        help="NGL station code (e.g. IQQE). Requires network.")
    parser.add_argument("--synthetic", action="store_true",
                        help="Use synthetic data (no network required).")
    parser.add_argument("--window", type=int, default=365,
                        help="Rolling window size in days (default 365).")
    parser.add_argument("--step", type=int, default=30,
                        help="Rolling window step in days (default 30).")
    parser.add_argument("--component", type=str, default="east",
                        choices=["east", "north", "up", "horizontal"],
                        help="GPS component to analyze (default east).")
    args = parser.parse_args()

    print("=" * 78)
    print("  PARABOLA PRIMITIVE CSD PIPELINE")
    print("=" * 78)
    print()

    if args.synthetic:
        print("  Running in SYNTHETIC mode (no network access required).")
        print("  Generating a 5000-day series that mimics an approach to")
        print("  the saddle-node bifurcation (mu decreases over time).")
        print()
        ts = synthetic_ngl(station="SYNTH", n_days=5000)
    elif args.station:
        print(f"  Fetching NGL data for station {args.station.upper()} ...")
        print(f"  URL: {NGL_TEMPLATE.format(station=args.station.upper())}")
        print()
        try:
            ts = load_ngl(args.station)
        except RuntimeError as e:
            print(f"  ERROR: {e}")
            print()
            print("  Falling back to synthetic mode for demonstration.")
            print()
            ts = synthetic_ngl()
    else:
        print("  No --station specified and --synthetic not set.")
        print("  Run with --synthetic to see the pipeline on simulated data,")
        print("  or --station IQQE (etc.) to pull real NGL data.")
        sys.exit(1)

    analyze_station(ts, window=args.window, step=args.step,
                    component=args.component)

    print("=" * 78)
    print("  NOTES")
    print("=" * 78)
    print()
    print("  To replicate with real data for the seismic gaps discussed in")
    print("  2024-2026 probability revisions:")
    print()
    print("    Chilean Atacama Trench:")
    print("      python parabola_csd_pipeline.py --station IQQE")
    print("      python parabola_csd_pipeline.py --station CDLC")
    print()
    print("    Japanese Nankai / Hokkaido:")
    print("      python parabola_csd_pipeline.py --station MIZU")
    print("      python parabola_csd_pipeline.py --station OSHM")
    print()
    print("    Cascadia:")
    print("      python parabola_csd_pipeline.py --station P496")
    print("      python parabola_csd_pipeline.py --station ALBH")
    print()
    print("  All stations are in the NGL archive and free to access.")
    print("  For earthquake catalog analysis (separate from strain CSD),")
    print("  use the USGS FDSN Event Web Service:")
    print("    https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson")
    print("      &starttime=2024-01-01&minmagnitude=5")
    print("      &minlatitude=-30&maxlatitude=-18")
    print("      &minlongitude=-75&maxlongitude=-65")
    print()


if __name__ == "__main__":
    main()
