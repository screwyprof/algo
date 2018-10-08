a = int(input())
c1 = 0
c2 = 0
for i in range(a):
    b = int(input())
    if b == 1:
        c1 += 1
    elif b == 0:
        c2 += 1
if c1 > c2:
    print(c2)
elif c1 == c2:
    print(c1)
elif c1 < c2:
    print(c1)