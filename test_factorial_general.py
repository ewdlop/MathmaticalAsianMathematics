#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test suite for factorial_general,py

Tests the analytic continuation fix for IndexOutOfBound errors.
"""

import sys
import math
import os

# Import the module by executing it
# The filename has a comma instead of a period, so we use exec
file_path = "/home/runner/work/MathmaticalAsianMathematics/MathmaticalAsianMathematics/factorial_general,py"

# Read and execute the file to get the functions
with open(file_path, 'r') as f:
    code = f.read()
    namespace = {}
    exec(code, namespace)
    factorial_general = namespace['factorial_general']


def test_small_positive_integers():
    """Test that small positive integers use exact factorial"""
    assert factorial_general(5) == 120
    assert factorial_general(10) == 3628800
    assert factorial_general(0) == 1


def test_negative_non_integers():
    """Test that negative non-integers work via Gamma function"""
    result = factorial_general(-0.5)
    # (-0.5)! = Gamma(0.5) = sqrt(pi)
    assert abs(float(result) - math.sqrt(math.pi)) < 1e-10


def test_negative_integers_raise_error():
    """Test that negative integers raise ValueError (Gamma poles)"""
    try:
        factorial_general(-1)
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert "Factorial undefined for negative integers" in str(e)
    
    try:
        factorial_general(-5)
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert "Factorial undefined for negative integers" in str(e)


def test_large_integers_use_gamma():
    """Test that large integers use Gamma (analytic continuation) to avoid string conversion errors"""
    # With default threshold=1000, these should use Gamma
    result_5000 = factorial_general(5000)
    result_100000 = factorial_general(100000)
    
    # Should be able to convert to string without error (as mpf objects)
    str(result_5000)
    str(result_100000)
    
    # Results should be large positive numbers
    assert float(result_5000) > 0
    assert float(result_100000) > 0


def test_threshold_boundary():
    """Test behavior at threshold boundary"""
    # Just below threshold - should use exact factorial
    result_999 = factorial_general(999, threshold=1000)
    assert isinstance(result_999, int)
    
    # At threshold - should use Gamma
    result_1000 = factorial_general(1000, threshold=1000)
    # mpmath returns mpf type
    assert hasattr(result_1000, 'ae')  # mpmath mpf objects have .ae method


def test_custom_threshold():
    """Test that custom threshold works"""
    # With lower threshold, smaller values should use Gamma
    result = factorial_general(100, threshold=50)
    assert hasattr(result, 'ae')  # mpmath mpf type
    
    # With higher threshold, larger values can use exact factorial
    result = factorial_general(100, threshold=200)
    assert isinstance(result, int)


def test_non_integer_values():
    """Test various non-integer values"""
    # 0.5! = Gamma(1.5) = sqrt(pi)/2
    result = factorial_general(0.5)
    expected = math.sqrt(math.pi) / 2
    assert abs(float(result) - expected) < 1e-10
    
    # Test other non-integers
    result = factorial_general(3.5)
    assert float(result) > 0


def test_precision_parameter():
    """Test that precision parameter affects result"""
    result_low = factorial_general(-0.5, prec=10)
    result_high = factorial_general(-0.5, prec=100)
    
    # Both should be close to sqrt(pi), but high precision should be more accurate
    sqrt_pi = math.sqrt(math.pi)
    assert abs(float(result_high) - sqrt_pi) <= abs(float(result_low) - sqrt_pi)


def test_no_index_out_of_bounds():
    """
    Test the main fix: large factorials should not cause IndexOutOfBounds
    when converting to string (Python's limit is 4300 digits by default)
    """
    # These used to cause "Exceeds the limit (4300 digits) for integer string conversion"
    # Now they should work using analytic continuation (Gamma function)
    
    test_values = [5000, 10000, 100000, 1000000]
    
    for value in test_values:
        result = factorial_general(value)
        # Should be able to convert to string without error
        result_str = str(result)
        # Should be in scientific notation and manageable
        assert 'e' in result_str.lower()
        # Should represent a very large number
        assert float(result) > 0


if __name__ == "__main__":
    print("Running tests...")
    
    # Run each test
    tests = [
        test_small_positive_integers,
        test_negative_non_integers,
        test_negative_integers_raise_error,
        test_large_integers_use_gamma,
        test_threshold_boundary,
        test_custom_threshold,
        test_non_integer_values,
        test_precision_parameter,
        test_no_index_out_of_bounds
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            print(f"Running {test.__name__}... ", end='')
            test()
            print("PASSED")
            passed += 1
        except Exception as e:
            print(f"FAILED: {e}")
            failed += 1
    
    print(f"\n{passed} passed, {failed} failed")
    sys.exit(0 if failed == 0 else 1)
