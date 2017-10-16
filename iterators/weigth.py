class Weight(object):
    def __init__(self, kilograms=None, pounds=None):
        if kilograms is None and pounds is None:
            raise AttributeError("You must pass at least one value for kilograms or pounds")
        self._kilograms = kilograms
        self._pounds = pounds

    @property
    def kilograms(self):
        if self._pounds is None:
            return self._kilograms
        return self._pounds * 0.453

    @property
    def pounds(self):
        if self._kilograms is None:
            return self._pounds
        return self._kilograms * 2.205

    def __add__(self,other):
        if self._kilograms is None:
            return Weight(pounds= (self.pounds + other.pounds))
        else:
            return Weight(kilograms= (self.kilograms + other.kilograms))
