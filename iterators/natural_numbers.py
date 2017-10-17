class NumbersIterator(object):
    def __init__(self):
        self.next_number = 1

    def __iter__(self):
        return self

    def __next__(self):
        prev_value = self.next_number
        self.next_number += 1
        return prev_value

    next = __next__

iterator = iter(NumbersIterator())

assert next(iterator) == 1
assert next(iterator) == 2
assert next(iterator) == 3
assert next(iterator) == 4
