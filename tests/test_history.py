"""History owns its collection and rejects invalid removal requests."""

import pytest

from calculator.calculation import Add, Subtract
from calculator.history import History


def test_empty_history():
    assert History().get_history() == []


def test_mixed_history():
    history = History()
    first = Add(10, 5)
    second = Subtract(20, 7)
    history.add(first)
    history.add(second)
    assert history.get_history() == [first, second]


def test_returned_list_is_a_copy():
    history = History()
    calculation = Add(10, 5)
    history.add(calculation)
    returned_list = history.get_history()
    returned_list.clear()
    # Editing the copy should not erase the owned collection.
    assert history.get_history() == [calculation]


def test_remove():
    history = History()
    calculation = Add(10, 5)
    history.add(calculation)
    assert history.remove(0) is calculation
    assert history.get_history() == []


def test_invalid_removal():
    history = History()
    calculation = Add(10, 5)
    history.add(calculation)
    with pytest.raises(IndexError):
        history.remove(-1)
    assert history.get_history() == [calculation]
