z = input().split()
a = int(z[0]) - 1
b = z[1]

print(b[: a] + b[a + 1:])