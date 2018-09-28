def estimate_uniqueness(n: int, m: int) -> int:
    if n < 0 or n > 1000:
        return -1

    if m < 0 or m > 26 * n ** 2:
        return -1

    return int(19 * m + (n + 239) * (n + 366) / 2)
