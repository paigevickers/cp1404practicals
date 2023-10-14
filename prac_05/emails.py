"""
CP1404/CP5632 Practical
Emails Program
Estimate:
Actual:
"""


def main():
    email = input("Email: ")
    # names = email.split("@")
    # names = names[0].split(".")
    # full_name = " ".join(names).title()
    email_to_name = {}
    # confirm_full_name = input(f"Is your name {full_name}? (Y/n) ").upper()
    while email != "":
        names = email.split("@")
        names = names[0].split(".")
        full_name = " ".join(names).title()
        confirm_full_name = input(f"Is your name {full_name}? (Y/n) ").title()
        if confirm_full_name == "No":
            full_name = input("Name: ")
        email_to_name[email] = full_name
        email = input("Email: ")
    for full_name in email_to_name:
        print(f"{email_to_name[email]}  ({full_name})")


main()
