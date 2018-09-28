import pytest

from ex3.state_machine import estimate_uniqueness


@pytest.mark.parametrize("m,n,expected", [
    (2, 0, 44344),
    (13, 20, 48134),
    (5, 23, 45699),
    (18, 6, 49458),
    (15, 20, 48767),
    (1000, 26000, 1340237),
    (-1, 5, -1),
    (1001, 7, -1),
    (5, -1, -1),
    (1, 27, -1)
])
def test_estimate_uniqueness(m: int, n: int, expected: int):
    u = estimate_uniqueness(m, n)
    assert u == expected
