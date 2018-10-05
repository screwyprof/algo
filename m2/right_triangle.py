import math


def right_triangle(a: float, b: float) -> [float, float]:
    if a == 0 or b == 0:
        return 0, 0, 0, 0, 0, 0

    c = float(round(math.sqrt((a ** 2) + (b ** 2)),2))
    p = float(round(((a + b + c)), 2))
    s = float(round((((a * b) / 2)),2))
    ga = int(90)  # because triangle is right-angled and one angle equals 90°
    al = float(round((math.degrees(math.atan(a / b))), 2))
    be = float(round((90 - al), 2))
    if a != 0 and b != 0:
        return c, p, s, ga, al, be
