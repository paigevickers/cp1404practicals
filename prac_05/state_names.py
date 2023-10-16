"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

state_code = input("Enter short state: ").upper()  # make input upper case
while state_code != "":
    try:
        print(state_code, "is", CODE_TO_NAME[state_code])
    except KeyError:  # except KeyError when input is not in CODE_TO_NAME
        print("Invalid short state")
    state_code = input("Enter short state: ").upper() # make input upper case

for code, name in CODE_TO_NAME.items():
    print(f"{code:3} is {name}")
