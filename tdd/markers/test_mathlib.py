import pytest
import sys
from . import mathlib

@pytest.mark.skip(reason="I don't want to run this at this moment")
def test_sum():
    total = mathlib.sum(4, 5)
    assert total == 9

@pytest.mark.skipif(sys.version_info < (3, 4), reason="Version is older")
def test_subtract():
    sub_total = mathlib.subtract(11, 5)
    assert sub_total == 6

@pytest.mark.vinay
def test_multiply():
    res = mathlib.multiply(3, 4)
    assert res == 12
