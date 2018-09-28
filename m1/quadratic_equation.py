# Program to solve quadratic equation ax^2+bx+c=0, where a != 0.
# Program has no decision for complex roots in case when D < 0.

import math


def quadratic_equation(a: float, b: float, c: float) -> [float, float, float]:
    if a == 0:
        return -1, 0, 0

    d = b ** 2 - (4 * a * c)
    if d < 0:
        return d, 0, 0

    if d == 0:
        x = -b / (2 * a)
        return 0, x, x

    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    return d, x1, x2
