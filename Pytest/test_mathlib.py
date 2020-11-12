import mathlib


def test_sum():
    total = mathlib.sum(4, 5)
    assert total == 9

def test_subtract():
    sub_total = mathlib.subtract(11, 5)
    assert sub_total == 6


def def_multiply():
    res = mathlib.multiply(3, 4)
    assert res == 12
