import pytest

from m1.quadratic_equation import quadratic_equation


@pytest.mark.parametrize("a, b, c, expected_d, expected_x1, expected_x2", [
    (5, 3, 7, -131, 0, 0),  # D < 0
    (1, -8, 12, 16, 6, 2),  # D > 0
    (1, -6, 9, 0, 3, 3),  # D = 0
    (0, 1, 1, -1, 0, 0),  # a = 0

])
def test_quadratic_equation(a: float, b: float, c: float, expected_d: float, expected_x1: float, expected_x2):
    d, x1, x2 = quadratic_equation(a, b, c)
    assert d == expected_d
    assert x1 == expected_x1
    assert x2 == expected_x2
