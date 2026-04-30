// ui.js — bind controls to engine state.

export class UI {
  constructor({ engine, audio, onPreset, onReset, onDistChange, onNChange }) {
    this.engine = engine;
    this.audio = audio;

    this.kSlider = document.getElementById("k-slider");
    this.kReadout = document.getElementById("k-readout");
    this.distSelect = document.getElementById("dist-select");
    this.nSelect = document.getElementById("n-select");
    this.audioToggle = document.getElementById("audio-toggle");

    this.kSlider.addEventListener("input", () => {
      const K = parseFloat(this.kSlider.value);
      this.engine.setK(K);
      this.updateKReadout();
    });

    this.distSelect.addEventListener("change", () => {
      onDistChange(this.distSelect.value);
    });
    this.nSelect.addEventListener("change", () => {
      onNChange(parseInt(this.nSelect.value, 10));
    });

    this.audioToggle.addEventListener("change", () => {
      if (this.audioToggle.checked) this.audio.enable(this.engine);
      else this.audio.disable();
    });

    document.querySelectorAll("[data-preset]").forEach((b) => {
      b.addEventListener("click", () => onPreset(b.dataset.preset));
    });

    document.getElementById("reset-btn").addEventListener("click", onReset);

    this.updateKReadout();
  }

  updateKReadout() {
    this.kReadout.textContent = this.engine.K.toFixed(3);
  }

  setK(K) {
    this.kSlider.value = K;
    this.engine.setK(K);
    this.updateKReadout();
  }

  updateHeader({ r, clusters }) {
    document.getElementById("r-readout").textContent = r.toFixed(3);
    document.getElementById("cluster-readout").textContent = clusters;
  }
}
