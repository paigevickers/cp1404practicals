"""
CP1404/CP5632 Practical
Do-from-scratch - Project Management Program
Estimate: minutes
Actual: minutes
"""
from project import Project


def main():
    projects = []
    print_menu()
    choice = input(">>> ").upper()
    while choice != "Q":
        # if choice == "L":
        # in_filename = input("Data file to load from: ")
        projects = load_data("projects.txt", projects)
        # print("Data loaded.")
        if choice == "S":
            out_filename = input("Data file to save to: ")
            write_data(out_filename, projects)
            print("Data saved.")
        if choice == "D":
            display_projects(projects)
        if choice == "U":
            for project in projects:
                print(f"{projects.index(project)} {project}")
            project_choice = input("Project Choice: ")
            print(projects[project_choice])
            new_percentage = int(input("New Percentage: "))
        print_menu()
        choice = input(">>> ").upper()


def display_projects(projects):
    print("Incomplete projects:")
    incomplete_projects = get_incomplete_projects(projects)
    print_projects(incomplete_projects)
    print("Complete projects:")
    complete_projects = [project for project in projects if project.completion_percentage == "100"]
    print_projects(complete_projects)


def print_projects(incomplete_projects):
    for project in incomplete_projects:
        print(f"\t{project}")


def get_incomplete_projects(projects):
    complete_projects = [project for project in projects if project.completion_percentage != "100"]
    return complete_projects


def get(projects):
    incomplete_projects = [project for project in projects if project.completion_percentage != "100"]
    for project in incomplete_projects:
        print(f"\t{project}")


def write_data(out_filename, projects):
    with open(out_filename, "w") as out_file:
        for project in projects:
            out_file.write(project)


def load_data(filename, projects):
    with open(filename, "r") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            project = Project(parts[0], parts[1], parts[2], parts[3], parts[4])
            projects.append(project)
    projects.sort()
    return projects


def print_menu():
    print("- (L)oad projects\n"
          "- (S)ave projects\n"
          "- (D)isplay projects\n"
          "- (F)ilter projects by date\n"
          "- (A)dd new project\n"
          "- (U)pdate project\n"
          "- (Q)uit")


main()
