"""Assert arithmetic behavior and the abstract calculation contract."""

import pytest

from calculator.calculation import Add, Calculation, Subtract


@pytest.mark.parametrize(
    "operation,a,b,expected",
    [
        (Add, 10, 5, 15),
        (Add, -10, 5, -5),
        (Add, 0, 0, 0),
        (Add, 0.1, 0.2, 0.3),
        (Subtract, 20, 7, 13),
        (Subtract, 5, 10, -5),
        (Subtract, -10, -5, -5),
        (Subtract, 0, 0, 0),
        (Subtract, 1.5, 0.25, 1.25),
    ],
)
def test_arithmetic(operation, a, b, expected):
    calculation = operation(a, b)
    assert calculation.a == a
    assert calculation.b == b
    assert calculation.get_result() == pytest.approx(expected)


def test_calculation_is_abstract():
    with pytest.raises(TypeError, match="abstract"):
        Calculation(1, 2)


def test_polymorphism():
    calculations = [Add(10, 5), Subtract(10, 5), Add(100, 50)]
    assert all(isinstance(item, Calculation) for item in calculations)
    assert [item.get_result() for item in calculations] == [15, 5, 150]
