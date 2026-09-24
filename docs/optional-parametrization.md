# Optional: parametrize a test after its behavior is clear

[Course home](https://github.com/kaw393939/is218-oop-calculator) · [Stage 5](https://github.com/kaw393939/is218-oop-calculator/blob/learn/05-reliability/docs/lessons/05-reliability.md)

Complete the required Stage 5 suite first. It uses ordinary functions and loops. Parametrization changes how examples are supplied to a test; it does not add application behavior or replace assertions.

For a separate practice experiment, create `tests/test_parameter_practice.py` in your solution with this familiar loop:

```python
from calculator.calculation import Add


def test_add_examples():
    for a, b, expected in [(2, 3, 5), (-2, 3, 1), (0, 0, 0)]:
        assert Add(a, b).get_result() == expected
```

Run just this practice file with `python -m pytest tests/test_parameter_practice.py --cov-fail-under=0`. The temporary override is needed because running a single practice file does not cover the whole application. Predict its result, then replace its contents with:

```python
import pytest

from calculator.calculation import Add


@pytest.mark.parametrize("a,b,expected", [(2, 3, 5), (-2, 3, 1), (0, 0, 0)])
def test_add_examples(a, b, expected):
    assert Add(a, b).get_result() == expected
```

Rerun the same practice-file command. The decorator asks pytest to call the function once per row. Three cases are now reported instead of one test containing a loop. The examples and the assertion remain equivalent. This can improve failure reporting when there are many cases.

Do not replace unrelated tests such as the independent-instance check with this arithmetic table: they protect different behavior. Run the whole suite after any refactoring. Delete this temporary practice file afterward, or keep it clearly identified as your own experiment; never delete established regressions to restore an expected count.
