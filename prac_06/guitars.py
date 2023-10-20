"""
CP1404/CP5632 Practical
Do-from-scratch Exercises - Use the Guitar class in a program
Estimate: 15 minutes
Actual: 10 minutes
"""
from guitar import Guitar


def main():
    """Get guitars from user and display at the end."""
    print("My guitars!")
    name = input("Name: ")
    guitars = []
    longest_name = ""
    largest_cost = 0.0
    while name != "":
        guitar = get_guitar(name)
        guitars = get_list(guitars, guitar)
        print_added_guitar(guitar)
        name = input("Name: ")
        for guitar in guitars:
            longest_name = get_longest_name(guitar, longest_name)
            largest_cost = get_longest_cost(guitar, largest_cost)
    print_loading_message()
    print_guitar_list(guitars, longest_name, largest_cost)


def get_longest_cost(guitar, largest_cost):
    """Determine the largest cost of a guitar in a list"""
    if guitar.cost > largest_cost:
        largest_cost = guitar.cost
    return largest_cost


def get_longest_name(guitar, longest_name):
    """Determine the longest name of a guitar in a list"""
    if len(guitar.name) > len(longest_name):
        longest_name = guitar.name
    return longest_name


def print_guitar_list(guitars, longest_name, longest_cost):
    """Print the list of guitars in proper formatting"""
    for guitar in guitars:
        vintage_string = determine_vintage_string(guitar)  # determine if guitar is vintage
        print(f"Guitar {1 + guitars.index(guitar)}: {guitar.name:>{len(longest_name)}}, "
              f"worth ${guitar.cost:{len(str(longest_cost))},.2f} {vintage_string}")  #


def print_loading_message():
    print("\n... snip ...\n"
          "\n"
          "These are my guitars:")


def print_added_guitar(guitar):
    print(f"{guitar.name} ({guitar.year}) : ${guitar.cost} added.")


def get_guitar(name):
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    guitar = Guitar(name, year, cost)
    return guitar


def get_list(guitars, guitar):
    guitars.append(guitar)
    return guitars


def determine_vintage_string(guitar):
    if guitar.is_vintage():
        vintage_string = "(vintage)"
    else:
        vintage_string = ""
    return vintage_string


main()
