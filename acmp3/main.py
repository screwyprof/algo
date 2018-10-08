n = input()
if int(n) == 5:
    print(25)
    exit(0)
b = int(str(n[: -1]))

if int(n[-1]) == 5:
    print(str(b * (b + 1)) + '25')


