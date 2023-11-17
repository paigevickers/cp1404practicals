"""
CP1404 Practical 09
SilverServiceTaxi class
"""
from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Car that includes fare costs and flagfall fee."""
    new_fare_cost = 4.50

    def __init__(self, fanciness, **kwargs):
        """Initialise a SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(**kwargs)
        self.fanciness = fanciness
        self.price_per_km = super().price_per_km * fanciness

    def __str__(self):
        """Return a string like a Taxi but with new fare fee."""
        return f"{super().__str__()} plus flagfall of $4.50"

    def get_fare(self):
        """Return the price for the taxi trip."""
        return super().get_fare() + self.new_fare_cost
