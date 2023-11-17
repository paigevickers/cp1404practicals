"""
CP1404 Practical 09
Test the UnreliableCar class
"""
from unreliable_car import UnreliableCar

my_car = UnreliableCar(name="Honda", fuel=100, reliability=43)
my_car.drive(80)
print(my_car)
