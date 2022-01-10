from car import Car
from random import randint


class UnreliableCar(Car):
    """An unreliable version of cars"""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car if that number is less than the car's reliability"""
        random_num = randint(0, 100)
        if random_num >= self.reliability:
            distance = 0
        drive_distance = super().drive(distance)
        return drive_distance
