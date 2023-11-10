"""
CP1404/CP5632 Practical
Do-from-scratch - Project Management Program
Estimate: 40 minutes
Actual: 60 minutes
"""
import datetime

from project import Project


def main():
    projects = []
    print_menu()
    choice = input(">>> ").upper()

    while choice != "Q":
        projects = load_data("projects.txt", projects)
        # print("Data loaded.")
        if choice == "L":
            filename = input("Filename: ")
            # projects = load_data(filename, projects)
            # print("Projects loaded")

        if choice == "S":
            out_filename = input("Data file to save to: ")
            write_data(out_filename, projects)
            print("Projects saved.")

        if choice == "D":
            print("Incomplete projects:")
            incomplete_projects = get_incomplete_projects(projects)
            print_projects(incomplete_projects)
            print("Complete projects:")
            complete_projects = get_complete_projects(projects)
            print_projects(complete_projects)

        if choice == "U":
            for project in projects:
                print(f"{projects.index(project)} {project}")
            project_choice = int(input("Project Choice: "))
            print(projects[project_choice])
            new_percentage = input("New Percentage: ")
            get_new_percentage(new_percentage, project_choice, projects)
            new_priority = input("New Priority: ")
            get_new_priority(new_priority, project_choice, projects)

        if choice == "A":
            print("Let's add a new project")
            name = input("Name: ")
            start_date = input("Start date (dd/mm/yy): ")
            priority = input("Priority: ")
            cost_estimate = input("Cost estimate: ")
            percent_complete = input("Percent complete: ")
            project = Project(name, start_date, priority, cost_estimate, percent_complete)
            projects.append(project)

        if choice == "F":
            date_string = input("Show projects that start after the date (dd/mm/yyyy): ")
            date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            for project in projects:
                if datetime.datetime.strptime(project.start_date, "%d/%m/%Y").date() > date:
                    print(project)

        print_menu()
        choice = input(">>> ").upper()
    print("Thank you for using custom-built project management software.")


def get_new_priority(new_priority, project_choice, projects):
    while new_priority != "":
        new_priority = int(new_priority)
        for project in projects:
            if projects.index(project) == project_choice:
                project.priority = new_priority
        break


def get_new_percentage(new_percentage, project_choice, projects):
    while new_percentage != "":
        new_percentage = int(new_percentage)
        for project in projects:
            if projects.index(project) == project_choice:
                project.completion_percentage = new_percentage
        break


def get_complete_projects(projects):
    complete_projects = [project for project in projects if project.completion_percentage == "100"]
    return complete_projects


def print_projects(projects):
    for project in projects:
        print(f"\t{project}")


def get_incomplete_projects(projects):
    complete_projects = [project for project in projects if project.completion_percentage != "100"]
    return complete_projects


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
