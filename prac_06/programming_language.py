"""
CP1404/CP5632 Practical
Intermediate Exercise - ProgramingLanguage class
Estimate:
Actual:
"""


class ProgrammingLanguage:
    """Represent a programming language object"""

    def __init__(self, name="", typing="", reflection="", year=0):
        """Initialise a ProgrammingLanguage instance"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determine if the language is dynamic"""
        if self.typing == "Dynamic":
            return True
        else:
            return False

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, " \
               f"First appeared in {self.year}"
