"""
CP1404/CP5632 Practical
Intermediate Exercise - ProgramingLanguage class
Estimate:
Actual:
"""


class ProgrammingLanguage:
    """Represent a programming language object"""

    def __init__(self, language="", typing="", reflection="", year=0):
        """Initialise a ProgrammingLanguage instance"""
        self.language = language
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determine if the language is dynamic"""
        if self.typing == "Dynamic":
            return True
        else:
            return False
