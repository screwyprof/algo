from m2.right_triangle import *


def exit_with_msg(code: int):
    print("Нажмите любую клавишу для выхода")
    input()
    exit(code)


print('Программа для нахождения гипотенузы, периметра, площади и углов прямоугольного треугольника.')
print('Введите значения катетов в сантиметрах:')

a = float(input("a = "))
b = float(input("b = "))
c = calc_c_side(a, b)

if not valid_sides(a, b, c):
    print("Такого треугольника не существует!")
    exit_with_msg(0)

if not valid_right_triangle(a, b, c):
    print("Данный треугольник не прямоугольный!")
    exit_with_msg(0)

p = calc_perimeter(a, b, c)
s = calc_square(a, b)

alpha = calc_alpha_via_tangent(a, b)
beta = calc_beta_via_tangent(a, b)
gamma = 180 - alpha - beta

assert valid_angles(alpha, beta, gamma)

print("a = " + str(a) + " см, b = " + str(b) + " см, c = "+str(c) + " см.")
print("Угол α = " + str(alpha) + "°, угол β = " + str(beta) + "°, угол γ = " + str(gamma) + "°.")
print("S = " + str(s) + " см, P = " + str(p) + " см^2.")
exit_with_msg(0)