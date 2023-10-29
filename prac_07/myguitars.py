"""
CP1404/CP5632 Practical
Intermediate Exercises - Guitar Program
Estimate: 15 minutes
Actual: 10 minutes
"""
import csv
from guitar import Guitar


def main():
    guitars = []  # set guitars to the empty list
    open_file(guitars)
    name = input("New guitar name: ")
    get_new_guitar(guitars, name)  # create Guitar object
    guitars.sort()
    print_guitars(guitars)
    write_file(guitars)


def write_file(guitars):
    """Write list of files to csv"""
    with open("guitars.csv", "w") as out_file:
        writer = csv.writer(out_file)
        for guitar in guitars:
            writer.writerow(guitar)


def print_guitars(guitars):
    """Print every guitar in list"""
    for guitar in guitars:
        print(guitar)


def get_new_guitar(guitars, name):
    """Create new Guitar object"""
    while name != "":
        guitar = get_guitar(name)  # create Guitar object
        guitars.append(guitar)  # add to existing list of guitars
        print_added_guitar(guitar)  # added guitar message
        name = input("Name: ")


def open_file(guitars):
    """Open csv for reading, append every row to list in Guitar object format"""
    with open("guitars.csv", "r") as in_file:
        reader = csv.reader(in_file)
        for row in reader:
            guitar = Guitar(row[0], row[1], row[2])
            guitars.append(guitar)


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
    year = input("Year: ")
    cost = input("Cost: ")
    guitar = Guitar(name, year, cost)
    return guitar


main()
