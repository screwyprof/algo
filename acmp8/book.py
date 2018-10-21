z = input().split()
k = int(z[0])
n = int(z[1])

a = (n - 1) // k
b = (n - 1) % k
print(a + 1, b + 1)