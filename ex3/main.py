from ex3.state_machine import estimate_uniqueness

k = int(input())
if k < 1 or k > 10000:
    exit(1)

for _ in range(k):
    n, m = [int(x) for x in input().split()]
    if estimate_uniqueness(n, m) < 0:
        exit(1)

