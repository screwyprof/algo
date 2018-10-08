import pytest

from acmp1.cake import *


@pytest.mark.parametrize("n, expected_answer", [
    (1, 0),
    (2, 1),
    (3, 3),
    (4, 2),
    (5, 5)
])
def test_cake(n, expected_answer):
    answer = cake(n)
    assert answer == expected_answer
