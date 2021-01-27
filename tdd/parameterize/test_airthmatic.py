from . import airthmatic
import pytest


@pytest.mark.parametrize("test_input, expected_output",
                         [
                             (5, 25),
                             (7, 49),
                             (9, 81),
                             (10, 100)
                         ]
                         )
def test_calc_square(test_input, expected_output):
    result = airthmatic.calc_square(test_input)
    assert result == expected_output
