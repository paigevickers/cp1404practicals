"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    user_score = float(input("Enter score: "))
    classification = determine_result(user_score)
    print(classification)
    random_score = random.randint(0, 100)
    classification = determine_result(random_score)
    print(classification)


def determine_result(score):
    if score < 0 or score > 100:
        classification = "Invalid"
    elif score < 50:
        classification = "Bad"
    elif score <= 90:
        classification = "Pass"
    else:
        classification = "Excellent"
    return classification


main()
