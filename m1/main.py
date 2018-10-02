from m1.quadratic_equation import quadratic_equation


def exit_with_msg(code: int):
    print("Нажмите любую клавишу для выхода")
    input()
    exit(code)


print("Программа для решения квадратного уравнения вида ax^2+bx+c=0\n")
print("Введите значения:")

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

d, x1, x2 = quadratic_equation(a, b, c)

if a == 0:
    if b == 0 and c == 0:
        print("a = 0, b = 0, c = 0: Программа не имеет решения.")
        exit_with_msg(0)
    elif b == 0 and c != 0:
        print("a = 0, b = 0: Программа не имеет решения.")
        exit_with_msg(0)
    else:
        print("x = " + str(x1))
        exit_with_msg(0)

if d < 1:
    print("D < 0: Программа не имеет решения.")
    exit_with_msg(0)

if d == 0:
    print("D = 0: x = " + str(x1))
    exit_with_msg(0)

print("D > 0: x1 = " + str(x1) + " x2 = " + str(x2))
exit_with_msg(0)
