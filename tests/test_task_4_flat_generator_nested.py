import os
import sys
import types
import pytest

# Ensure project root is on sys.path for imports when running pytest from various CWDs
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from task_4_flat_generator_nested import flat_generator


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
def test_flat_generator_nested_returns_expected_sequence(nested, expected):
    assert list(flat_generator(nested)) == expected


def test_flat_generator_nested_type_is_generator():
    gen = flat_generator([[1, [2]]])
    assert isinstance(gen, types.GeneratorType)


