for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a
for i in range(0, 100 + 1, 10):
    print(i, end=' ')
print()

# b
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c
number = int(input("Number of stars: "))
for i in range(number):
    print("*", end='')

# d
for i in range(number):
    for j in range(i + 1):
        print("*", end='')
    print("")
