"""
CP1404 Practical 09
Test the Taxi class
"""
from taxi import Taxi

my_taxi = Taxi(name="Prius 1", fuel=100)  # create taxi object
my_taxi.drive(40)  # drive the taxi 40 km
print(my_taxi)  # print the taxi's details
print(my_taxi.get_fare())  # print the taxi's current fair
my_taxi.start_fare()  # restart meter by starting new fare
my_taxi.drive(100)  # drive 100km
print(my_taxi)
print(my_taxi.get_fare())
