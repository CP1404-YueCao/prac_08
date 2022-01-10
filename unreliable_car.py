from car import Car


class UnreliableCar(Car):
    """An unreliable version of cars"""


def __init__(self, name, fuel, reliability):
    """Initialise an UnreliableCar"""
    super().__init__(name, fuel)
    self.reliability = reliability
   