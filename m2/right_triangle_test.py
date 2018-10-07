import pytest

from m2.right_triangle import *


def test_calc_c_side():
    c = calc_c_side(3, 4)
    assert c == 5


@pytest.mark.parametrize("a, b, expected_s", [
    (3, 4, 6),
    (0, 1, 0),
    (1, 0, 0)
])
def test_calc_square(a, b, expected_s):
    s = calc_square(a, b)
    assert s == expected_s


def test_calc_perimeter():
    p = calc_perimeter(3, 4, 5)
    assert p == 12


@pytest.mark.parametrize("a, b, expected_alpha", [
    (3, 4, 36.87),
    (0, 2, 0)
])
def test_calc_alpha_via_tangent(a, b, expected_alpha):
    alpha = calc_alpha_via_tangent(a, b)
    assert alpha == expected_alpha


@pytest.mark.parametrize("a, b, expected_beta", [
    (3, 4, 53.13),
    (2, 0, 0)
])
def test_calc_beta_via_tangent(a, b, expected_beta):
    beta = calc_beta_via_tangent(a, b)
    assert beta == expected_beta


def test_valid_angles():
    assert valid_angles(90, 45, 45)


def test_valid_angles():
    assert not valid_angles(100, 50, 80)


def test_valid_sides():
    assert valid_sides(3, 4, 5)


def test_valid_sides():
    assert not valid_sides(3, 1, 5)


def test_valid_right_triangle():
    assert valid_right_triangle(3, 4, 5)

def test_valid_right_triangle():
    assert not valid_right_triangle(3, 4, 7)