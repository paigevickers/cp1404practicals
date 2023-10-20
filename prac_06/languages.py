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
    programming_languages = [python, ruby, visual_basic]
    dynamic_languages = [language.name for language in programming_languages if language.is_dynamic()]
    print(f"The dynamically typed languages are:\n"
          f"{dynamic_languages[0]}\n"
          f"{dynamic_languages[1]}")

    # dynamic_languages = [language for language in programming_languages if language.is_dynamic() == "True"]
    # print(dynamic_languages)


main()
