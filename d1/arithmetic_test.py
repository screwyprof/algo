import pytest

from arithmetic import arithmetic


@pytest.mark.parametrize("a, b, c, expected_d", [
    (2, 2, '+', 4),
    (2, 2, '-', 0),
    (2, 3, '*', 6),
    (4, 2, '/', 2)
])
def test_arithmetic(a: float, b: float, c: str, expected_d: float):
    d = arithmetic(a, b, c)
    assert d == expected_d
