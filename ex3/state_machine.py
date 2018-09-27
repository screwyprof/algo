k = int(input())
if k < 1 or k > 10000:
    exit(1)

i = 0
while i < k:
    a = input().split()
    n = int(a[0])
    m = int(a[1])

    if n < 0 or n > 1000:
        exit(1)
    if m < 0 or m > 26 * n ** 2:
        exit(1)

    d = int(19 * m + (n + 239) * (n + 366) / 2)
    print(d)

    i += 1

