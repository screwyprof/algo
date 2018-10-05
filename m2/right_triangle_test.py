import pytest

from m2.right_triangle import right_triangle


@pytest.mark.parametrize("a, b, expected_c, expected_p, expected_s, expected_ga, expected_al, expected_be", [
    (3, 4, 5, 12, 6, 90, 36.87, 53.13),  # simple right-triangle
    (0, 1, 0, 0, 0, 0, 0.0, 0.0),  # a = 0
    (1, 0, 0, 0, 0, 0, 0, 0),  # b = 0
    (0, 0, 0, 0, 0, 0, 0, 0)  # a = 0, b = 0
])
def test_right_triangle(a: float, b: float, expected_c, expected_p, expected_s, expected_ga, expected_al, expected_be):
    c, p, s, ga, al, be = right_triangle(a, b)
    assert c == expected_c
    assert p == expected_p
    assert s == expected_s
    assert ga == expected_ga
    assert al == expected_al
    assert be == expected_be
