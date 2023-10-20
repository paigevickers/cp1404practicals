"""
CP1404/CP5632 Practical
Do-from-scratch Exercises - Create program to test Guitar class
Estimate: 10 minutes
Actual: 1 minutes
"""
from guitar import Guitar


def main():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 7289.99)
    print(gibson)  # test class object is correct with correct formatting
    print(another_guitar)
    print(f"{gibson.name} get_age() - Expected 101. Got {gibson.get_age()}")  # test get_age() works correctly
    print(f"{another_guitar.name} get_age() - Expected 10. Got {another_guitar.get_age()}")
    print(f"{gibson.name} is_vintage - Expected True. Got {gibson.is_vintage()}")  # test is_vintage work correctly
    print(f"{another_guitar.name} is_vintage - Expected False. Got {another_guitar.is_vintage()}")


main()
