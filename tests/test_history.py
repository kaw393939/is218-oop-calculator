"""Verify collection ownership, ordering, and removal boundaries."""

import pytest

from calculator.calculation import Add, Subtract
from calculator.history import History


def test_empty_history():
    assert History().get_history() == []


def test_mixed_history_and_copy():
    # Verify both the returned contents and protection of the owned collection.
    history = History()
    calculations = [Add(10, 5), Subtract(20, 7)]
    for calculation in calculations:
        history.add(calculation)
    snapshot = history.get_history()
    assert snapshot == calculations
    snapshot.clear()
    assert history.get_history() == calculations


@pytest.mark.parametrize("index", [0, 1, 2])
def test_remove_first_middle_last(index):
    # Identity (is) confirms we received the exact object that was stored.
    history = History()
    calculations = [Add(1, 2), Subtract(3, 4), Add(5, 6)]
    for calculation in calculations:
        history.add(calculation)
    assert history.remove(index) is calculations[index]
    assert history.get_history() == calculations[:index] + calculations[index + 1 :]


@pytest.mark.parametrize("populated", [False, True])
@pytest.mark.parametrize("index", [-1, 1, 99])
def test_invalid_removal_preserves_history(populated, index):
    # Stacked parametrization tests every populated/index combination.
    # Check the exception AND the unchanged state after the rejected request.
    history = History()
    if populated:
        history.add(Add(1, 2))
    before = history.get_history()
    with pytest.raises(IndexError, match="Calculation does not exist"):
        history.remove(index)
    assert history.get_history() == before


def test_remove_only_item():
    history = History()
    calculation = Add(1, 2)
    history.add(calculation)
    assert history.remove(0) is calculation
    assert history.get_history() == []


def test_sessions_are_independent():
    first, second = History(), History()
    first.add(Add(1, 2))
    assert second.get_history() == []


def test_reject_non_calculation():
    history = History()
    with pytest.raises(TypeError, match="Calculation objects only"):
        history.add("not a calculation")
    assert history.get_history() == []
