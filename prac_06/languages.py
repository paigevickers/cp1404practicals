"""
CP1404/CP5632 Practical
Intermediate Exercise - Using ProgramingLanguage class in a program
Estimate: 20 minutes
Actual: 20 minutes
"""
from programming_language import ProgrammingLanguage


def main():
    """Creating lists from class objects"""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    programming_languages = get_list(python, ruby, visual_basic)
    dynamic_languages = get_dynamic_languages(programming_languages)
    print(f"The dynamically typed languages are:\n"
          f"{dynamic_languages[0]}\n"
          f"{dynamic_languages[1]}")


def get_dynamic_languages(programming_languages):
    """List comprehension of languages with dynamic typing"""
    dynamic_languages = [language.name for language in programming_languages if language.is_dynamic()]
    return dynamic_languages


def get_list(python, ruby, visual_basic):
    """Create list of objects"""
    programming_languages = [python, ruby, visual_basic]
    return programming_languages


main()
