import os
import sys
import pytest

# Ensure project root is on sys.path for imports when running pytest from various CWDs
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from task_3_flat_iterator_nested import FlatIterator


@pytest.mark.parametrize(
    "nested, expected",
    [
        (
            [
                [['a'], ['b', 'c']],
                ['d', 'e', [['f'], 'h'], False],
                [1, 2, None, [[[[['!']]]]], []],
            ],
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!'],
        ),
        (
            [[], [[], []], []],
            [],
        ),
        (
            [[1, [2, [3]]]],
            [1, 2, 3],
        ),
        (
            [["x"], ("y",)],  # кортеж не разворачивается, т.к. условие только для list
            ["x", ("y",)],
        ),
    ],
)
def test_flat_iterator_nested_returns_expected_sequence(nested, expected):
    assert list(FlatIterator(nested)) == expected


def test_flat_iterator_nested_stop_iteration():
    it = FlatIterator([[1, [2, [3]]]])
    assert next(it) == 1
    assert next(it) == 2
    assert next(it) == 3
    with pytest.raises(StopIteration):
        next(it)


