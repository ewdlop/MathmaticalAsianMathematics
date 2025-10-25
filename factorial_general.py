#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Factorial with negative indices via Gamma extension.
- n >= 0 integer: uses math.factorial (fast, exact integer)
- n  negative non-integer: uses Gamma(n+1) with reflection handling
- n  negative integer: raises ValueError (Gamma pole)

Also includes a simple benchmark that varies precision p (decimal digits)
for Gamma-based evaluation, to observe practical runtime scaling.

Usage examples:
  python neg_factorial.py --x -0.5
  python neg_factorial.py --x -3.7 --prec 80
  python neg_factorial.py --x 150
  python neg_factorial.py --bench --x -0.5 --prec-list 30 60 120 240

Notes:
- For integer n >= 0, math.factorial is exact and very fast (near-optimal).
- For non-integers, we rely on mpmath.gamma with mp.dps = precision (decimal digits).
"""

import argparse
import math
import time
from typing import Iterable, List, Tuple

try:
    import mpmath as mp
except ImportError as e:
    raise SystemExit("This script requires 'mpmath'. Install via: pip install mpmath") from e


def is_int_like(x: float, tol: float = 0.0) -> bool:
    """Return True if x is an integer within tolerance tol."""
    if tol == 0.0:
        return float(x).is_integer()
    return abs(x - round(x)) <= tol


def factorial_general(x: float, prec: int = 50):
    """
    Compute factorial for real x via:
      - if x is integer and x >= 0: exact math.factorial(int(x))
      - if x is negative integer: raise ValueError (Gamma pole)
      - else: Gamma(x + 1) with mp.dps = prec

    Complexity remarks (informal, practical):
      - integer n >= 0: CPython's math.factorial uses efficient algorithms; for large n
        bit-complexity is ~ O(M(n log n) log n) in theory; in practice extremely fast.
      - non-integer: mpmath's gamma is based on advanced approximations (e.g., Lanczos-like);
        for p-digit precision, typical cost ~ O(M(p) log p) ≈ O(p (log p)^2) with FFT-backed bigfloats.
    """
    # Integer branch
    if is_int_like(x):
        n = int(round(x))
        if n < 0:
            raise ValueError(f"Factorial undefined for negative integers (pole at x={n}).")
        return math.factorial(n)

    # Non-integer branch via Gamma
    mp.mp.dps = max(prec, 20)
    z = mp.mpf(x) + 1  # compute Gamma(x+1)
    # mpmath.gamma already handles reflection internally with good stability.
    return mp.gamma(z)


def benchmark_gamma(x: float, prec_list: Iterable[int]) -> List[Tuple[int, float]]:
    """
    Benchmark Gamma(x+1) at various decimal precisions.
    Returns a list of (precision, seconds).
    """
    results = []
    # Warmup
    mp.mp.dps = 50
    _ = mp.gamma(x + 1)

    for p in prec_list:
        mp.mp.dps = p
        t0 = time.perf_counter()
        _ = mp.gamma(x + 1)
        dt = time.perf_counter() - t0
        results.append((p, dt))
    return results


def main():
    parser = argparse.ArgumentParser(description="Factorial with negative indices via Gamma.")
    parser.add_argument("--x", type=float, default=-0.5,
                        help="Input x for x! (supports real numbers). Default: -0.5")
    parser.add_argument("--prec", type=int, default=50,
                        help="Decimal digits for non-integer Gamma evaluation. Default: 50")
    parser.add_argument("--bench", action="store_true",
                        help="Run a simple benchmark over a list of precisions.")
    parser.add_argument("--prec-list", type=int, nargs="*", default=[30, 60, 120, 240],
                        help="Precision list for --bench. Decimal digits.")
    args, unknown = parser.parse_known_args() # Use parse_known_args to ignore unknown arguments

    x = args.x
    if args.bench:
        print(f"[Benchmark] Evaluating Gamma(x+1) at x={x} for precisions: {args.prec_list}")
        res = benchmark_gamma(x, args.prec_list)
        for p, dt in res:
            print(f"  p={p:4d} digits  ->  {dt:.6f} s")
        return

    try:
        val = factorial_general(x, prec=args.prec)
        print(f"{x}!  =  {val}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
