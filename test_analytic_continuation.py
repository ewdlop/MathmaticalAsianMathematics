#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test suite for Data 解析延拓 (Analytic Continuation) implementations
"""

import sys
import math
from typing import Callable


def test_factorial_general():
    """Test factorial_general.py"""
    print("\n=== Testing factorial_general.py ===")
    
    # Import the module
    try:
        sys.path.insert(0, '/home/runner/work/MathmaticalAsianMathematics/MathmaticalAsianMathematics')
        import factorial_general as fg
    except ImportError as e:
        print(f"❌ Failed to import factorial_general: {e}")
        return False
    
    tests_passed = 0
    tests_failed = 0
    
    # Test 1: Integer factorial (should use math.factorial)
    try:
        result = fg.factorial_general(5)
        expected = 120
        if result == expected:
            print(f"✓ Test 1 passed: 5! = {result}")
            tests_passed += 1
        else:
            print(f"✗ Test 1 failed: Expected {expected}, got {result}")
            tests_failed += 1
    except Exception as e:
        print(f"✗ Test 1 failed with exception: {e}")
        tests_failed += 1
    
    # Test 2: Half-integer factorial (0.5! = sqrt(pi)/2)
    try:
        result = float(fg.factorial_general(0.5))
        expected = math.sqrt(math.pi) / 2
        if abs(result - expected) < 1e-10:
            print(f"✓ Test 2 passed: 0.5! ≈ {result:.10f}")
            tests_passed += 1
        else:
            print(f"✗ Test 2 failed: Expected {expected:.10f}, got {result:.10f}")
            tests_failed += 1
    except Exception as e:
        print(f"✗ Test 2 failed with exception: {e}")
        tests_failed += 1
    
    # Test 3: Negative non-integer
    try:
        result = float(fg.factorial_general(-0.5))
        expected = math.sqrt(math.pi)  # Γ(0.5) = sqrt(pi)
        if abs(result - expected) < 1e-10:
            print(f"✓ Test 3 passed: -0.5! ≈ {result:.10f}")
            tests_passed += 1
        else:
            print(f"✗ Test 3 failed: Expected {expected:.10f}, got {result:.10f}")
            tests_failed += 1
    except Exception as e:
        print(f"✗ Test 3 failed with exception: {e}")
        tests_failed += 1
    
    # Test 4: Negative integer (should raise ValueError)
    try:
        result = fg.factorial_general(-2)
        print(f"✗ Test 4 failed: Should have raised ValueError for -2!")
        tests_failed += 1
    except ValueError:
        print(f"✓ Test 4 passed: Correctly raised ValueError for -2!")
        tests_passed += 1
    except Exception as e:
        print(f"✗ Test 4 failed with unexpected exception: {e}")
        tests_failed += 1
    
    print(f"\nfactorial_general.py: {tests_passed} passed, {tests_failed} failed")
    return tests_failed == 0


def test_sampling():
    """Test 抽樣.py"""
    print("\n=== Testing 抽樣.py ===")
    
    # Import the module
    try:
        sys.path.insert(0, '/home/runner/work/MathmaticalAsianMathematics/MathmaticalAsianMathematics')
        import 抽樣 as sampling
    except ImportError as e:
        print(f"❌ Failed to import 抽樣: {e}")
        return False
    
    tests_passed = 0
    tests_failed = 0
    
    # Test 1: Zeta(-1) = -1/12
    try:
        result = sampling.riemann_zeta_continuation(-1)
        expected = -1/12
        if abs(result.real - expected) < 1e-10:
            print(f"✓ Test 1 passed: ζ(-1) = {result.real:.10f} ≈ -1/12")
            tests_passed += 1
        else:
            print(f"✗ Test 1 failed: Expected {expected:.10f}, got {result.real:.10f}")
            tests_failed += 1
    except Exception as e:
        print(f"✗ Test 1 failed with exception: {e}")
        tests_failed += 1
    
    # Test 2: Zeta(0) = -1/2
    try:
        result = sampling.riemann_zeta_continuation(0)
        expected = -0.5
        if abs(result.real - expected) < 1e-10:
            print(f"✓ Test 2 passed: ζ(0) = {result.real:.10f}")
            tests_passed += 1
        else:
            print(f"✗ Test 2 failed: Expected {expected:.10f}, got {result.real:.10f}")
            tests_failed += 1
    except Exception as e:
        print(f"✗ Test 2 failed with exception: {e}")
        tests_failed += 1
    
    # Test 3: Zeta(2) = π²/6
    try:
        result = sampling.riemann_zeta_continuation(2)
        expected = (math.pi ** 2) / 6
        if abs(result.real - expected) < 1e-10:
            print(f"✓ Test 3 passed: ζ(2) = {result.real:.10f} ≈ π²/6")
            tests_passed += 1
        else:
            print(f"✗ Test 3 failed: Expected {expected:.10f}, got {result.real:.10f}")
            tests_failed += 1
    except Exception as e:
        print(f"✗ Test 3 failed with exception: {e}")
        tests_failed += 1
    
    # Test 4: Zeta at a positive value > 1
    try:
        result = sampling.riemann_zeta_continuation(3)
        # ζ(3) is Apéry's constant ≈ 1.202...
        expected = 1.2020569031595942854
        if abs(result.real - expected) < 1e-10:
            print(f"✓ Test 4 passed: ζ(3) = {result.real:.10f}")
            tests_passed += 1
        else:
            print(f"✗ Test 4 failed: Expected {expected:.10f}, got {result.real:.10f}")
            tests_failed += 1
    except Exception as e:
        print(f"✗ Test 4 failed with exception: {e}")
        tests_failed += 1
    
    print(f"\n抽樣.py: {tests_passed} passed, {tests_failed} failed")
    return tests_failed == 0


def main():
    """Run all tests"""
    print("=" * 70)
    print("Running Tests for Data 解析延拓 (Analytic Continuation)")
    print("=" * 70)
    
    all_passed = True
    
    if not test_factorial_general():
        all_passed = False
    
    if not test_sampling():
        all_passed = False
    
    print("\n" + "=" * 70)
    if all_passed:
        print("✓ All tests passed!")
    else:
        print("✗ Some tests failed")
    print("=" * 70 + "\n")
    
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
