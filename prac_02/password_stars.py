"""
CP1404 Practical 2
"""


def main():
    password = get_password()
    print_stars(password)


def print_stars(password):
    """Print star for every letter in password"""
    for letter in password:
        print("*", end="")


def get_password():
    """Get valid password from user"""
    password = input("Password: ")
    while len(password) < 5:
        print("Invalid password")
    return password


main()
