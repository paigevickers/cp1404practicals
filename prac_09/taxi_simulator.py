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

        elif menu_choice == "D":
            # if current_taxi is None:
            #     print("You need to choose a taxi before you can drive")
            distance = float(input("Drive how far? "))
            current_taxi.drive(distance)
            print(f"Your {current_taxi.name} cost you ${current_taxi.get_fare():.2f}")
            total_fare += current_taxi.get_fare()

        print(f"Bill to date: ${total_fare:.2f}")
        print(MENU)
        menu_choice = get_valid_choice()

    print(f"Total trip cost: ${total_fare}")
    print("Taxi's now:")
    for i, taxi in enumerate(taxis):
        print(f"{i} {taxi}")


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


main()
