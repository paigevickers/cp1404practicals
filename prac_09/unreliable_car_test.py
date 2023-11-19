"""
CP1404 Practical 09
Test the UnreliableCar class
"""
from unreliable_car import UnreliableCar

my_first_car = UnreliableCar(name="Honda", fuel=100, reliability=43)  # create UnreliableCar object
my_first_car.drive(80)  # drive the car 80km
print(my_first_car)  # print car details
my_first_car.add_fuel(80)  # add fuel
print(my_first_car)

my_second_car = UnreliableCar(name="Kia", fuel=45, reliability=78)
my_second_car.drive(30)
print(my_second_car)
my_second_car.add_fuel(50)
print(my_second_car)
