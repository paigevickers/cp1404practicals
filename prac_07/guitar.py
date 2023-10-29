"""
CP1404/CP5632 Practical
Do-from-scratch Exercises - Create Guitar class
Estimate: 15 minutes
Actual: 10 minutes
"""


class Guitar:
    """Represent a Guitar object"""
    def __init__(self, name="".title(), year=0, cost=0.0):
        """Initialise a Guitar instance"""
        self.name = name
        self.year = year
        self.cost = cost
        self.age = 0

    def __str__(self):
        """Return string of Guitar object"""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        self.age += 2023 - self.year
        return self.age

    def is_vintage(self):
        """Determine if the Guitar object is vintage"""
        if (2023 - self.year) >= 50:
            return True
        else:
            return False

    def __lt__(self, other):
        return self.year < other.year


# def run_test():
#     guitar = Guitar("Fender", 1966, 200)
#     print(guitar)
#
#
# run_test()
