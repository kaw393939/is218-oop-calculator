"""Start with direct examples before learning parametrization."""

import pytest

from calculator.calculation import Add, Calculation, Subtract


def test_add():
    calculation = Add(10, 5)            # Arrange an object with its own inputs.
    result = calculation.get_result()  # Act through its public method.
    assert result == 15                # Assert an expected answer.


def test_subtract():
    assert Subtract(20, 7).get_result() == 13


def test_abstract_calculation():
    # The abstract contract cannot be used as a concrete operation.
    with pytest.raises(TypeError):
        Calculation(10, 5)


def test_polymorphism():
    calculations = [Add(10, 5), Subtract(10, 5)]
    results = []
    for calculation in calculations:
        # We do not ask which subclass this object belongs to.
        results.append(calculation.get_result())
    assert results == [15, 5]
