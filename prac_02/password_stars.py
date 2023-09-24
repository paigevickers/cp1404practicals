password = input("Password: ")
while len(password) < 5:
    print("Invalid password")
for letter in password:
    print("*", end="")