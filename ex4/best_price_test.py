import pytest

from ex4.best_price import best_price


@pytest.mark.parametrize("a1, a2, a3, b1, b2, b3, expected_price", [
    (1, 2, 3, 3, 2, 1, 14)
])
def test_best_price(a1: int, a2: int, a3: int, b1: int, b2: int, b3: int, expected_price: int):
    price = best_price(a1, a2, a3, b1, b2, b3)
    assert price == expected_price
