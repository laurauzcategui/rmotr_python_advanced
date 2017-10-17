class Distance(object):
    def __init__(self, meters=None, feet=None):
        # Please don't change this method
        if not any((meters, feet)):
            raise ValueError("Provide at least one measure of distance")

        self.meters = meters
        self.feet = feet

    @property
    def distance_in_meters(self):
        if self.feet is not None:
            return self.feet * 0.3048
        return self.meters
    @property
    def distance_in_kilometers(self):
        if self.meters is None:
            return self.feet * 0.0003048
        return self.meters / 1000
    @property
    def distance_in_miles(self):
        if self.meters is None:
            return self.feet * 0.0001893939394
        return round(self.meters * 0.000621371)
    @property
    def distance_in_feet(self):
        if self.feet is None:
            return self.meters / 0.3048
        return self.feet
