a = input().split()
w = int(a[0])
h = int(a[1])
r = int(a[2])
c = 0

if w < h:
    c = w
elif h < w:
    c = h

if (r * 2) <= c:
    print('YES')
elif (r * 2) > c:
    print('NO')
