import os
import sys
import pytest

# Ensure project root is on sys.path for imports when running pytest from various CWDs
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from task_1_flat_iterator import FlatIterator


@pytest.mark.parametrize(
    "list_of_lists, expected",
    [
        (
            [
                ['a', 'b', 'c'],
                ['d', 'e', 'f', 'h', False],
                [1, 2, None],
            ],
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None],
        ),
        (
            [
                ['a'],
                [],
                [1, 2],
            ],
            ['a', 1, 2],
        ),
        (
            [],
            [],
        ),
        (
            [[], [], []],
            [],
        ),
        (
            [[0, '', None, False, True], [3.14]],
            [0, '', None, False, True, 3.14],
        ),
        (
            [['a', ['b']], ['c']],  # вложенный список как элемент не должен разворачиваться в задаче №1
            ['a', ['b'], 'c'],
        ),
    ],
)
def test_flat_iterator_returns_expected_flat_sequence(list_of_lists, expected):
    assert list(FlatIterator(list_of_lists)) == expected


@pytest.mark.parametrize(
    "list_of_lists, expected_length",
    [
        ([['x', 'y']], 2),
        ([['a'], [], [1, 2, 3]], 4),
        ([], 0),
    ],
)
def test_stop_iteration_after_exhaustion(list_of_lists, expected_length):
    iterator = FlatIterator(list_of_lists)
    consumed = 0
    try:
        while True:
            next(iterator)
            consumed += 1
    except StopIteration:
        pass
    assert consumed == expected_length
    with pytest.raises(StopIteration):
        next(iterator)


def test_multiple_independent_iterators_do_not_interfere():
    source = [[1, 2], [3]]
    it1 = FlatIterator(source)
    it2 = FlatIterator(source)

    assert next(it1) == 1
    assert next(it2) == 1
    assert next(it1) == 2
    assert next(it2) == 2
    assert next(it1) == 3
    assert next(it2) == 3
    with pytest.raises(StopIteration):
        next(it1)
    with pytest.raises(StopIteration):
        next(it2)


