import random

from prac_09.car import Car


class UnreliableCar(Car):
    def __init__(self, reliability=0.0, **kwargs):
        """Initialise an Unreliable Car instance, based on parent class Car."""
        super().__init__(**kwargs)
        self.reliability = reliability

    def drive(self, distance):
        if random.randint(0, 100) < self.reliability:
            super().drive(distance)
            return distance
        else:
            return 0
