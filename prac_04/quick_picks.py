"""
CP1404/CP5632 Practical
"Quick Pick" Lottery Ticket Generator
"""
import random


def main():
    number_of_picks = int(input("Number of quick picks? "))
    NUMBER = 6
    get_picks(number_of_picks, NUMBER)
    print('\n'.join(' '.join(row) for row in get_picks(NUMBER, number_of_picks)))


def get_picks(number_of_picks, NUMBER):
    return [[str(random.randint(1, 46)) for count in range(number_of_picks)] for pick in range(NUMBER)]


main()
