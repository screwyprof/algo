from m2.right_triangle import right_triangle


def exit_with_msg(code: int):
    print("Нажмите любую клавишу для выхода")
    input()
    exit(code)


print('Программа для нахождения гипотенузы, периметра, площади и углов прямоугольного треугольника.')
print('Введите значения катетов в сантиметрах:')

a = float(input("a = "))
b = float(input("b = "))

c, p, s, ga, al, be = right_triangle(a, b)

if a == 0 or b == 0:
    print("a = 0 или b == 0, такого треугольника не существует.")
    exit_with_msg(0)

if a != 0 and b != 0:
    print("Гипотенуза равна: " + str(c) + " см, периметр равен: " + str(p) + " см, площадь равна: " + str(
        s) + " см^2, угол γ равен: " + str(ga) + "°, угол α равен: " + str(al) + "°, угол β равен: " + str(be) + "°.")
    exit_with_msg(0)
