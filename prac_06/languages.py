"""
CP1404/CP5632 Practical
Intermediate Exercise - Using ProgramingLanguage class in a program
Estimate:
Actual:
"""
from programming_language import ProgrammingLanguage


def main():
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)


main()
