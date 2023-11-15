"""
CP1404 Practical 09
Test SilverServiceTaxi class
"""
from prac_09.silver_service_taxi import SilverServiceTaxi

my_hummer = SilverServiceTaxi("Hummer", 200, 4)  # create SilverServiceTaxi object
print(my_hummer)
my_hummer.drive(40)  # drive the taxi 40 km
print(my_hummer)  # print the taxi's details
print(my_hummer.get_fare())  # print the taxi's current fair
my_hummer.start_fare()  # restart meter by starting new fare
my_hummer.drive(100)  # drive 100km
print(my_hummer.get_fare())  # print the taxi's new fair

my_rover = SilverServiceTaxi("Range Rover", 100, 2)  # create a SilverServiceTax object
print(my_rover)
my_rover.drive(18)
print(my_rover.get_fare())