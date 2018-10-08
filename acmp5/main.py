a = input().split()
a1 = int(a[0])
a2 = int(a[1])
a3 = int(a[2])

if (a1 + a2 == a3) or (a1 + a3 == a2) or (a2 + a3 == a1):
    print('YES')
else:
    print('NO')