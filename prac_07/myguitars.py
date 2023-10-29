"""
CP1404/CP5632 Practical
Intermediate Exercises - Guitar Program
Estimate: 15 minutes
Actual: 10 minutes
"""
import csv
from guitar import Guitar
from operator import itemgetter


def main():
    guitars = []
    with open("guitars.csv", "r") as in_file:
        reader = csv.reader(in_file)
        for row in reader:
            guitar = Guitar(row[0], row[1], row[2])
            guitars.append(guitar)
    guitars.sort()
    print(guitars)
    for guitar in guitars:
        print(guitar)


main()
