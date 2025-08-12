class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self._stack = None

    def __iter__(self):
        self._stack = [iter(self.list_of_list)]
        return self

    def __next__(self):
        # Lazy initialization to allow calling next() without iter()
        if self._stack is None:
            self._stack = [iter(self.list_of_list)]
        while self._stack:
            try:
                next_item = next(self._stack[-1])
            except StopIteration:
                self._stack.pop()
                continue

            if isinstance(next_item, list):
                self._stack.append(iter(next_item))
                continue

            return next_item

        raise StopIteration


def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()


