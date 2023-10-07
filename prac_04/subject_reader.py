"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    display_subject_details(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    records = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        records.append(parts)
    input_file.close()
    return records


def display_subject_details(records):
    """Print the fata like: subject is taught by lecturer and has this number of students"""
    for record in records:
        print(f"{record[0]} is taught by {record[1]} and has {record[2]} students")


main()
