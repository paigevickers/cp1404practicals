"""
CP1404/CP5632 Practical
Emails Program
Estimate: 30
Actual: 40
"""


def main():
    email = input("Email: ")
    email_to_name = {}
    while email != "":
        full_name = determine_full_name(email)
        confirm_full_name = input(f"Is your name {full_name}? (Y/n) ").title()
        full_name = determine_correct_name(confirm_full_name, full_name)
        email_to_name[email] = full_name
        email = input("Email: ")
    print_dictionary_items(email_to_name)


def determine_full_name(email):
    """Determines user's full name from given email"""
    names = email.split("@")
    names = names[0].split(".")
    full_name = " ".join(names).title()
    return full_name


def determine_correct_name(confirm_full_name, full_name):
    """Determines correct name if not extracted from email correctly"""
    if confirm_full_name == "No":
        full_name = input("Name: ")
    return full_name


def print_dictionary_items(email_to_name):
    """Prints dictionary items in desired format"""
    for email in email_to_name:
        print(f"{email_to_name[email]} ({email})")


main()
