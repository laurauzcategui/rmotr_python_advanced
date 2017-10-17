class PrimeNumbersIterator(object):
    def __iter__(self):
        self.number = 1

    def _is_prime(self, number):
        if number > 1:
            for i in range(2,number):
             if (number % i) == 0:
                 return False
            else:
                 return True
        else:
            return False

    def __next__(self):
        is_prime = self.number if self._is_prime(self.number) else None
        if is_prime is Not None:
            return self.number 

    def __iter__(self):
        return self

    next = __next__

obj = PrimeNumbersIterator()


#iterator = iter(PrimeNumbersIterator())
#
#next(iterator)  # 2
#next(iterator)  # 3
#next(iterator)  # 5
#next(iterator)  # 11
#next(iterator)  # 13
## ... fast forward ...
#next(iterator)  # 163
#next(iterator)  # 167
#next(iterator)  # 173
