class CountUpToIterator(object):
    def __init__(self,up_to=None):
        if up_to is None:
            raise ValueError("Please set value to up_to you want to count")
        self.up_to = up_to
        self.next_number = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.next_number+1 > self.up_to+1:
            raise StopIteration
        prev_value = self.next_number
        self.next_number += 1
        return prev_value

    next = __next__
