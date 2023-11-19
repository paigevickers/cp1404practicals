"""
CP1404 Practical 09
Test SilverServiceTaxi class
"""
from prac_09.silver_service_taxi import SilverServiceTaxi

my_taxi = SilverServiceTaxi(name="Hummer", fuel=200, fanciness=2)  # create silver service taxi object
my_taxi.drive(70)  # drive the taxi 40 km
print(my_taxi)  # print the taxi's details
print(my_taxi.get_fare())  # print the taxi's current fair
my_taxi.start_fare()  # restart meter by starting new fare
my_taxi.drive(100)  # drive 100km
print(my_taxi)
print(my_taxi.get_fare())

my_rover = SilverServiceTaxi(name="Range Rover", fuel=100, fanciness=2)  # create a SilverServiceTax object
my_rover.drive(18)
print(my_rover)
print(my_rover.get_fare())
