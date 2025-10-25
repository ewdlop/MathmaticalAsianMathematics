#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Data 解析延拓 (Analytic Continuation of Data)

This module demonstrates the concept of analytic continuation through:
1. Riemann zeta function ζ(s) and its analytic continuation
2. Data sampling and interpolation to demonstrate continuation
3. Visualization of how functions extend beyond their original domain

Key examples:
- ζ(-1) = -1/12 (the famous 1 + 2 + 3 + 4 + ... = -1/12 result)
- Demonstrating how the zeta function extends from Re(s) > 1 to the entire complex plane
- Sampling data points and using analytic continuation principles

Usage:
    python 抽樣.py --demo zeta
    python 抽樣.py --demo factorial
    python 抽樣.py --demo sampling
"""

import argparse
import numpy as np
from typing import List, Tuple, Optional

try:
    import mpmath as mp
except ImportError as e:
    raise SystemExit("This script requires 'mpmath'. Install via: pip install mpmath") from e


def riemann_zeta_continuation(s: complex, prec: int = 50) -> complex:
    """
    Compute Riemann zeta function ζ(s) using mpmath's analytic continuation.
    
    The zeta function is originally defined for Re(s) > 1 as:
        ζ(s) = Σ(n=1 to ∞) 1/n^s
    
    But through analytic continuation, it extends to all complex s ≠ 1.
    
    Famous examples:
        ζ(-1) = -1/12  (gives 1 + 2 + 3 + 4 + ... = -1/12)
        ζ(0) = -1/2
        ζ(2) = π²/6
    
    Args:
        s: Complex number where to evaluate ζ(s)
        prec: Precision in decimal digits
    
    Returns:
        Value of ζ(s) via analytic continuation
    """
    mp.mp.dps = prec
    return complex(mp.zeta(s))


def demonstrate_zeta_values(values: Optional[List[float]] = None) -> None:
    """
    Demonstrate famous values of the Riemann zeta function.
    
    Args:
        values: List of values to evaluate. Defaults to [-1, 0, 2, -3]
    """
    if values is None:
        values = [-1, 0, 2, -3, -0.5]
    
    print("\n=== Riemann Zeta Function - Analytic Continuation ===")
    print("Original definition: ζ(s) = Σ(n=1 to ∞) 1/n^s for Re(s) > 1")
    print("Through analytic continuation, extends to all s ≠ 1\n")
    
    for s in values:
        zeta_val = riemann_zeta_continuation(s)
        print(f"ζ({s:6.2f}) = {zeta_val.real:20.10f} + {zeta_val.imag:20.10f}i")
    
    print("\nFamous result: 1 + 2 + 3 + 4 + ... = ζ(-1) = -1/12")
    print("This is through analytic continuation, not ordinary summation!")


def sample_and_continue(func, sample_points: np.ndarray, 
                       continuation_points: np.ndarray,
                       prec: int = 50) -> Tuple[np.ndarray, np.ndarray]:
    """
    Sample a function at given points and demonstrate analytic continuation.
    
    This demonstrates the concept of taking known values in one domain
    and extending them to another domain through analytic principles.
    
    Args:
        func: Function to sample (should accept mpmath types)
        sample_points: Points where function is well-defined
        continuation_points: Points to extend to via continuation
        prec: Precision for calculations
    
    Returns:
        Tuple of (sampled_values, continued_values)
    """
    mp.mp.dps = prec
    
    # Sample at well-defined points
    sampled = np.array([complex(func(x)) for x in sample_points])
    
    # Evaluate at continuation points
    continued = np.array([complex(func(x)) for x in continuation_points])
    
    return sampled, continued


def demonstrate_factorial_continuation():
    """
    Demonstrate how factorial extends to negative numbers through Gamma function.
    
    n! = Γ(n+1) extends factorial from natural numbers to all complex numbers
    except negative integers (where Γ has poles).
    """
    print("\n=== Factorial Analytic Continuation via Gamma Function ===")
    print("Factorial n! is defined for n ≥ 0")
    print("Through Γ(n+1), we extend to all numbers except negative integers\n")
    
    test_values = [5, 3.5, 0.5, -0.5, -1.5]
    
    for x in test_values:
        try:
            mp.mp.dps = 50
            if x >= 0 or not float(x).is_integer():
                gamma_val = mp.gamma(x + 1)
                print(f"{x:6.2f}! = Γ({x+1:6.2f}) = {gamma_val}")
            else:
                print(f"{x:6.2f}! = undefined (pole of Gamma function)")
        except Exception as e:
            print(f"{x:6.2f}! = error: {e}")


def demonstrate_sampling():
    """
    Demonstrate data sampling and interpolation as a discrete analogue
    of analytic continuation.
    """
    print("\n=== Data Sampling and Continuation ===")
    print("Sampling the Riemann zeta function at various points")
    print("and showing how values continue beyond the original domain\n")
    
    # Sample in the convergent region (Re(s) > 1)
    convergent_points = np.linspace(2, 5, 5)
    
    # Continuation points (including Re(s) ≤ 1, but avoiding s=1 pole)
    continuation_points = np.linspace(-3, 0.5, 5)
    
    print("Convergent region (Re(s) > 1):")
    for s in convergent_points:
        zeta_val = riemann_zeta_continuation(s)
        print(f"  s = {s:5.2f}: ζ(s) = {zeta_val.real:15.10f}")
    
    print("\nContinuation region (Re(s) ≤ 1):")
    for s in continuation_points:
        zeta_val = riemann_zeta_continuation(s)
        print(f"  s = {s:5.2f}: ζ(s) = {zeta_val.real:15.10f}")


def demonstrate_sum_identity():
    """
    Demonstrate the famous identity: 1 + 2 + 3 + 4 + ... = -1/12
    
    This comes from ζ(-1) = -1/12 through analytic continuation.
    """
    print("\n=== The Famous Sum Identity ===")
    print("Direct sum: S = 1 + 2 + 3 + 4 + ... (diverges to +∞)")
    print("\nBut through analytic continuation of ζ(s) = Σ(1/n^s):")
    print("We can assign a 'regularized' value to this divergent series")
    
    zeta_minus_1 = riemann_zeta_continuation(-1)
    print(f"\nζ(-1) = {zeta_minus_1.real:.15f}")
    print("\nThis is used in:")
    print("- Quantum field theory (Casimir effect)")
    print("- String theory (critical dimension)")
    print("- Regularization of divergent series")
    print("\n詩曰：")
    print("說是無窮，卻被 ζ(−1) 惡整成 −1⁄12；")
    print("時間在哭，空間在笑，")
    print("真空的能量還得繳稅給正則化的帝王。")


def main():
    """Main entry point with command-line interface."""
    parser = argparse.ArgumentParser(
        description="Data 解析延拓 - Demonstrate analytic continuation concepts"
    )
    parser.add_argument(
        "--demo",
        type=str,
        choices=["zeta", "factorial", "sampling", "sum", "all"],
        default="all",
        help="Which demonstration to run"
    )
    parser.add_argument(
        "--prec",
        type=int,
        default=50,
        help="Precision in decimal digits (default: 50)"
    )
    
    args = parser.parse_args()
    
    print("=" * 70)
    print("Data 解析延拓 (Analytic Continuation of Data)")
    print("=" * 70)
    
    if args.demo in ["zeta", "all"]:
        demonstrate_zeta_values()
    
    if args.demo in ["sum", "all"]:
        demonstrate_sum_identity()
    
    if args.demo in ["factorial", "all"]:
        demonstrate_factorial_continuation()
    
    if args.demo in ["sampling", "all"]:
        demonstrate_sampling()
    
    print("\n" + "=" * 70)
    print("解析延拓：將數學從已知的領域延伸到未知的世界")
    print("Analytic Continuation: Extending mathematics from known to unknown realms")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
