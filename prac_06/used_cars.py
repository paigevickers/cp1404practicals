"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180)
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)

    limo = Car(100)  # create car object (no name field in Car class)
    limo = Car("limo", 100)  # create car object (including name field in Car class)
    limo.add_fuel(20)  # add 20 units of fuel
    print(f"Car has fuel: {limo.fuel}") # print amount of fuel in car
    limo.drive(115)  # drive car 115km
    print(limo)  # print car object in proper formatting


main()
