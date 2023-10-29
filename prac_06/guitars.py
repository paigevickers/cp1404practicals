"""
CP1404/CP5632 Practical
Do-from-scratch Exercises - Use the Guitar class in a program
Estimate: 45 minutes
Actual: 1 hour
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
        guitar = get_guitar(name)  # create Guitar object
        guitars = get_list(guitars, guitar)  # get list of guitars
        print_added_guitar(guitar) # added guitar message
        name = input("Name: ")
        for guitar in guitars:
            longest_name = get_longest_name(guitar, longest_name)  # determine longest guitar name in list
            largest_cost = get_longest_cost(guitar, largest_cost)  # determine largest cost of guitar in list
    print_loading_message()  # loading message
    print_guitar_list(guitars, longest_name, largest_cost)  # display of all guitars inputted


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
              f"worth ${guitar.cost:{len(str(longest_cost))},.2f} {vintage_string}")


def print_loading_message():
    """Print message user will see when done inputting guitars"""
    print("\n... snip ...\n"  # add blank line before and after message
          "\n"  # add blank line
          "These are my guitars:")


def print_added_guitar(guitar):
    """Print guitar's information when added"""
    print(f"{guitar.name} ({guitar.year}) : ${guitar.cost} added.")


def get_guitar(name):
    """Create Guitar object"""
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    guitar = Guitar(name, year, cost)
    return guitar


def get_list(guitars, guitar):
    """Append guitar to list to get list of guitars"""
    guitars.append(guitar)
    return guitars


def determine_vintage_string(guitar):
    """Determine if a guitar is vintage"""
    if guitar.is_vintage():
        vintage_string = "(vintage)"
    else:
        vintage_string = ""
    return vintage_string


main()
