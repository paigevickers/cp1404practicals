"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
score = float(input("Enter score: "))
if score < 0 or score > 100:
    classification = "Invalid"
elif score < 50:
    classification = "Bad"
elif score <= 90:
    classification = "Pass"
else:
    classification = "Excellent"
print(classification)