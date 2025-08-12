import os
import sys
import types
import pytest

# Ensure project root is on sys.path for imports when running pytest from various CWDs
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from task_2_flat_generator import flat_generator


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
            [['a', ['b']], ['c']],  # вложенный список как элемент не должен разворачиваться в задаче №2
            ['a', ['b'], 'c'],
        ),
    ],
)
def test_flat_generator_returns_expected_flat_sequence(list_of_lists, expected):
    assert list(flat_generator(list_of_lists)) == expected


@pytest.mark.parametrize(
    "list_of_lists, expected_first_two",
    [
        ([['x', 'y']], ['x', 'y']),
        ([['a'], [1]], ['a', 1]),
    ],
)
def test_flat_generator_yields_in_order_with_next(list_of_lists, expected_first_two):
    gen = flat_generator(list_of_lists)
    for expected in expected_first_two:
        assert next(gen) == expected


def test_flat_generator_type_is_generator():
    gen = flat_generator([['a']])
    assert isinstance(gen, types.GeneratorType)


