-- framework_core.hs — the synchronization-cost framework's structural side
-- in pure Haskell. Companion to framework_core.py.
--
-- Why Haskell: the framework's structural claims become machine-checkable
-- type-level statements. Ω_Λ :: Rational is precisely the claim — exact,
-- typed, and evaluated to 13/19 with no float in the chain. The Stern-Brocot
-- tree is a single infinite value, not a generator function. Purity is
-- enforced by the typesystem, not by convention.
--
-- Build and run:
--     ghc -O2 framework_core.hs && ./framework_core
--
-- Or with cabal/stack/runhaskell as you prefer.

module Main where

import Data.Ratio  ((%), numerator, denominator)
import Text.Printf (printf)

-- ── Tier 0: the mediant primitive ─────────────────────────────────────────

type Pair = (Integer, Integer)

mediant :: Pair -> Pair -> Pair
mediant (a, b) (c, d) = (a + c, b + d)

-- ── Tier 1: the Stern-Brocot tree as an infinite lazy value ───────────────
-- The entire tree is a single value of type SB. Lazy evaluation never
-- forces more than the finite portion that is observed.

data SB = Node Pair SB SB

sternBrocot :: Pair -> Pair -> SB
sternBrocot left right = Node m (sternBrocot left m) (sternBrocot m right)
  where
    m = mediant left right

tree :: SB
tree = sternBrocot (0, 1) (1, 0)

inorder :: Int -> SB -> [Pair]
inorder 0 _              = []
inorder n (Node m l r)   = inorder (n - 1) l ++ [m] ++ inorder (n - 1) r

-- ── Tier 1: Farey counting via Euler's totient ────────────────────────────

totient :: Integer -> Integer
totient n = toInteger . length $ [k | k <- [1 .. n], gcd n k == 1]

fareyCount :: Integer -> Integer
fareyCount n = 1 + sum (map totient [1 .. n])

-- ── Tier 3: structural constants ──────────────────────────────────────────

phi :: Double
phi = (1 + sqrt 5) / 2

phiSq :: Double
phiSq = phi + 1                                -- φ² = φ + 1, the recursion

kCritical :: Double
kCritical = 2 / pi                              -- K_c = 2/π for uniform g(0) = 1

-- ── Tier 4: the dimensionless predictions ─────────────────────────────────
-- Each is a value, Rational where the answer is an exact rational and
-- Double where transcendentals (log) are involved. The type signature is
-- the framework claim.

omegaLambda :: Rational
omegaLambda = fareyCount 6 % (fareyCount 6 + 2 * 3)            -- 13 / 19

duty :: Integer -> Rational
duty q = 1 % (q ^ (3 :: Int))

sin2ThetaW :: Rational
sin2ThetaW = duty 3 / (duty 2 + duty 3)                         -- 8 / 35

alphaRatio :: Rational
alphaRatio = duty 2 / duty 3                                    -- 27 / 8

nS :: Double
nS = 1 - log phiSq / 27.4                                       -- ≈ 0.9649

kleinModes :: Int
kleinModes = 4

-- ── Tier 5: address ───────────────────────────────────────────────────────

treeDepth :: Double -> Double -> Double
treeDepth omegaPlanck h0 = log (omegaPlanck / h0) / log phiSq

-- ── Reporting ─────────────────────────────────────────────────────────────

showRat :: Rational -> String
showRat r = show (numerator r) ++ "/" ++ show (denominator r)

main :: IO ()
main = do
  putStrLn "Synchronization-cost framework — structural predictions"
  putStrLn (replicate 60 '=')
  printf "  |F_6|        = %d\n"          (fareyCount 6)
  printf "  q_2 * q_3    = %d\n"          (2 * 3 :: Integer)
  printf "  Ω_Λ          = %-6s  ≈ %.6f   observed: 0.685 ± 0.007 (Planck 2018)\n"
         (showRat omegaLambda) (fromRational omegaLambda :: Double)
  printf "  sin²θ_W      = %-6s  ≈ %.6f   observed: 0.2312 (PDG)\n"
         (showRat sin2ThetaW) (fromRational sin2ThetaW :: Double)
  printf "  α_s/α_2      = %-6s  = %.6f   observed: ≈ 3.05 at M_Z (running)\n"
         (showRat alphaRatio) (fromRational alphaRatio :: Double)
  printf "  n_s          =        ≈ %.6f   observed: 0.9649 ± 0.0042\n" nS
  printf "  K_c          =        = %.6f   (= 2/π)\n"           kCritical
  printf "  φ²           =        = %.6f   (= φ + 1)\n"          phiSq
  printf "  Klein modes  = %d\n"          kleinModes
  putStrLn ""
  putStrLn "Stern-Brocot tree, in-order to depth 3:"
  mapM_ (\(p, q) -> printf "  %d/%d\n" p q) (inorder 3 tree)
