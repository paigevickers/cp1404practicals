"""
CP1404 Practical 09
Taxi Simulator
Estimate:
Actual:
"""
from prac_09.silver_service_taxi import SilverServiceTaxi
from prac_09.taxi import Taxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    current_taxi = None
    total_fare = 0
    print("Let's drive")
    taxis = [Taxi(name="Prius", fuel=100), SilverServiceTaxi(name="Limo", fuel=100, fanciness=2),
             SilverServiceTaxi(name="Hummer", fuel=200, fanciness=4)]
    print(MENU)
    menu_choice = get_valid_choice()
    while menu_choice != "Q":
        if menu_choice == "C":
            print("Taxi's available:")
            for i, taxi in enumerate(taxis):
                print(f"{i} {taxi}")
            current_taxi = get_current_taxi(taxis)

        if menu_choice == "D":
            distance = float(input("Drive how far? "))
            current_taxi.drive(distance)
            print(f"Your {current_taxi.name} cost you {current_taxi.get_fare()}")
            total_fare = update_cost(current_taxi.get_fare())
        print(MENU)
        menu_choice = get_valid_choice()
        print(f"Bill to date: ${total_fare}")


def get_valid_choice():
    valid_choice = ["Q", "C", "D"]
    menu_choice = input(">>> ").upper()
    if menu_choice not in valid_choice:
        print(f"Invalid option.")
    else:
        return menu_choice


def get_current_taxi(taxis):
    taxi_index = int(input("Choose taxi: "))
    try:
        current_taxi = taxis[taxi_index]
        return current_taxi
    except IndexError:
        print("Invalid taxi choice")


def update_cost(new_fare):
    total_fare += new_fare
    return total_fare

main()
