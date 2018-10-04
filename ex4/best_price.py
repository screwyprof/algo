def best_price(a1: int, a2: int, a3: int, b1: int, b2: int, b3: int) -> int:
    a = [a1, a2, a3]
    b = [b1, b2, b3]

    a.sort(reverse=True)
    b.sort(reverse=True)

    price = 0
    for i in range(3):
        price += a[i] * b[i]

    return price
