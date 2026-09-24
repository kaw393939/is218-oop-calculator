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
    # parametrize runs this test once for every row in the table above.
    # Arrange an object, act by calling its method, assert the expected result.
    calculation = operation(a, b)
    assert calculation.a == a
    assert calculation.b == b
    # approx allows tiny floating-point rounding differences for decimals.
    assert calculation.get_result() == pytest.approx(expected)


def test_calculation_is_abstract():
    # An expected exception is a behavior we can test, not a failed test.
    with pytest.raises(TypeError, match="abstract"):
        Calculation(1, 2)


def test_polymorphism():
    # A list comprehension asks every object the same question: get_result().
    calculations = [Add(10, 5), Subtract(10, 5), Add(100, 50)]
    assert all(isinstance(item, Calculation) for item in calculations)
    assert [item.get_result() for item in calculations] == [15, 5, 150]
