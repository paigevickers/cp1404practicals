"""
CP1404/CP5632 Practical
Basic list operations and security checker
"""


def main():
    numbers = get_list()
    print(f"The first number is {numbers[0]}\n"
          f"The last number is {numbers[-1]}\n"
          f"The smallest number is {min(numbers)}\n"
          f"The largest number is {max(numbers)}\n"
          f"The average of the numbers is {sum(numbers)/len(numbers)}")


def get_list():
    """Get 5 numbers from user input and add to list"""
    numbers = []
    for i in range(0, 5):
        number = int(input("Number: "))
        numbers.append(number)
    return numbers


main()


usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
name = input("Name: ")
if name in usernames:
    print("Access granted")
else:
    print("Access denied")