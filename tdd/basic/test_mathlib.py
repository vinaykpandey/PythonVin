import pytest
import sys
#math is inbuilt python lib
""""
import math
dir(math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']

"""
# test cases for standard math

import math

def test_sqrt():
    num = 25
    sqrt_num = 5
    assert math.sqrt(num) == sqrt_num

def testsquare():
    num = 7
    square_num = 49
    assert  num*num == square_num



# test cases for mathlib

from . import mathlib

def test_sum():
    total = mathlib.sum(4, 5)
    assert total == 9