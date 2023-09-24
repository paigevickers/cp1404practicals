def main():
    password = get_password()
    print_stars(password)


def print_stars(password):
    for letter in password:
        print("*", end="")


def get_password():
    password = input("Password: ")
    while len(password) < 5:
        print("Invalid password")
    return password


main()