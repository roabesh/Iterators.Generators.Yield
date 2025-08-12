class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self._outer_index = 0
        self._inner_index = 0

    def __iter__(self):
        self._outer_index = 0
        self._inner_index = 0
        return self

    def __next__(self):
        while self._outer_index < len(self.list_of_list):
            current_list = self.list_of_list[self._outer_index]

            if self._inner_index < len(current_list):
                item = current_list[self._inner_index]
                self._inner_index += 1
                return item

            self._outer_index += 1
            self._inner_index = 0

        raise StopIteration


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()


