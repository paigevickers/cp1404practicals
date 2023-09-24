"""
CP1404/CP5632 - Practical
"""


def main():
    """Get choice from user to operate menu"""
    choice = input("Choice: ")
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = determine_result(score)
            print(result)
        elif choice == "S":
            for i in range(score):
                print("*", end="")
        else:
            print("Invalid choice")
        choice = input("Choice: ")
    print("Farewell")


def determine_result(score):
    """Determine result of score"""
    if score < 50:
        result = "Bad"
    elif score <= 90:
        result = "Pass"
    else:
        result = "Excellent"
    return result


def get_valid_score():
    """Get a valid score"""
    score = int(input("Score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Score: "))
    return score


main()
