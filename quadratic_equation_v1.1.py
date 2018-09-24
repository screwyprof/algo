# Program to solve quadratic equation ax^2+bx+c=0, where a != 0.
# Program has no decision for complex roots in case when D < 0.

import math


def exit_with_msg(code: int):
    print("Нажмите любую клавишу для выхода")
    input()
    exit(code)


print("Программа для решения квадратного уравнения вида ax^2+bx+c=0, где a != 0\n")
print("Введите значения:")

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a == 0:
    print("Это не квадратное уравнение: a = 0")
    exit_with_msg(1)

d = b ** 2 - (4 * a * c)
if d < 0:
    print("D < 0: Программа не имеет решения.")
    exit_with_msg(1)

if d == 0:
    x = -b / (2 * a)

    print("D = 0: x = " + str(x))
    exit_with_msg(0)

x1 = (-b + math.sqrt(d)) / (2 * a)
x2 = (-b - math.sqrt(d)) / (2 * a)

print("D > 0: x1 = " + str(x1) + " x2 = " + str(x2))
exit_with_msg(0)
