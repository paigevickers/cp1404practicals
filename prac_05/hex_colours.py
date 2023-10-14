"""
CP1404/CP5632 Practical
Intermediate Exercise
Hex Colours
"""


def main():
    COLOUR_TO_CODE = {"Acid Green": "b0bf1a", "Banana Mania": "fae7b5",
                      "Cosmic Cobalt": "2e2d88", "Dogwood Rose": "d71868",
                      "Electric Lime": "ccff00", "Fuzzy Wuzzy": "87421f",
                      "Glossy Grape": "ab92b3", "Mango Tango": "ff8243",
                      "Twilight Lavender": "8a496b", "Vegas Gold": "c5b358"}
    colour_name = input("Colour name: ").title()
    while colour_name != "":
        get_valid_colour(COLOUR_TO_CODE, colour_name)
        colour_name = input("Colour name: ").title()


def get_valid_colour(COLOUR_TO_CODE, colour_name):
    """Get valid colour name and either code or invalid message"""
    if colour_name in COLOUR_TO_CODE:
        print(f"{colour_name} is #{COLOUR_TO_CODE[colour_name]}")
    else:
        print("Invalid colour name")


main()
