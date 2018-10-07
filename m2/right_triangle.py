import math


def calc_c_side(a: float, b: float) -> float:
    return math.sqrt(a ** 2 + b ** 2)


def calc_perimeter(a: float, b: float, c: float) -> float:
    return a + b + c


def calc_square(a: float, b: float) -> float:
    return (a * b) / 2


def calc_alpha_via_tangent(a: float, b: float) -> float:
    return round(math.degrees(math.atan(a / b)), 2)


def calc_beta_via_tangent(a: float, b: float) -> float:
    return round(math.degrees(math.atan(b / a)), 2)


def valid_angles(alpha: float, beta: float, gamma: float) -> bool:
    return alpha + beta + gamma == 180


def valid_sides(a: float, b: float, c: float) -> bool:
    return (a + b) > c and (a + c) > b and (b + c) > a


def valid_right_triangle(a: float, b: float, c: float) -> bool:
    return a ** 2 + b ** 2 == c ** 2
