"""
CP1404 Practical 09
SilverServiceTaxi class
"""
from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    new_fare_cost = 4.50

    def __init__(self, name, fuel, fanciness):
        Taxi.__init__(self, name, fuel)
        self.fanciness = fanciness
        self.price_per_km = super().price_per_km * fanciness

    def __str__(self):
        return f"{super().__str__()} plus flagfall of $4.50"

    def get_fare(self):
        """Return the price for the taxi trip."""
        return (self.price_per_km * self.current_fare_distance) + self.new_fare_cost
