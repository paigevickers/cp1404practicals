"""
CP1404/CP5632 Practical
Do-from-scratch Exercises - Create guitar class
Estimate: 20 minutes
Actual: 20 minutes
"""


class Guitar:
    def __init__(self, name="", year=0, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost}"

    def is_vintage(self):
        if (2023 - self.year) >= 50:
            return True
        else:
            return False
