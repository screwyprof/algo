def cake(n):
    if n == 1:
        return 0
    elif n % 2 != 0:
        return n
    elif n % 2 == 0:
        return n / 2