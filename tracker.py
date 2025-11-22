"""
GradeBook Analyzer
Author: <Sambhav Agarawal>
Date: <22-11-2025>

Description:
A CLI tool that reads student marks (manual or CSV),
calculates statistics, assigns grades, and prints a formatted table.
"""
print("\n===============================")
print ("Welcome to GradeBook Analyzer")
print("===============================\n")


import csv
import statistics

# ---------------------------------------------
# Task 3 – Statistical Functions
# ---------------------------------------------
def calculate_average(marks_dict):
    return sum(marks_dict.values()) / len(marks_dict)

def calculate_median(marks_dict):
    return statistics.median(marks_dict.values())

def find_max_score(marks_dict):
    max_name = max(marks_dict, key=marks_dict.get)
    return max_name, marks_dict[max_name]

def find_min_score(marks_dict):
    min_name = min(marks_dict, key=marks_dict.get)
    return min_name, marks_dict[min_name]


# ---------------------------------------------
# Task 4 – Grade Assignment
# ---------------------------------------------
def assign_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


# ---------------------------------------------
# Task 2 – Manual Input or CSV Import
# ---------------------------------------------
def manual_input():
    marks = {}
    n = int(input("Enter number of students: "))

    for _ in range(n):
        name = input("Enter student name: ")
        score = int(input(f"Enter marks for {name}: "))
        marks[name] = score

    return marks


def load_csv():
    marks = {}
    file = input("Enter CSV filename (with .csv extension): ")

    try:
        with open(file, "r") as f:
            reader = csv.reader(f)
            next(reader)  # skip header

            for row in reader:
                name = row[0]
                score = int(row[1])
                marks[name] = score

        print("CSV loaded successfully!")

    except FileNotFoundError:
        print("File not found! Please try again.")

    return marks


# ---------------------------------------------
# Task 6 – Print Final Results Table
# ---------------------------------------------
def print_table(marks_dict, grades_dict):
    print("\nName\t\tMarks\tGrade")
    print("-----------------------------------------")
    for name, marks in marks_dict.items():
        print(f"{name:10}\t{marks:5}\t{grades_dict[name]}")


# ---------------------------------------------
# MAIN PROGRAM LOOP
# ---------------------------------------------
def main():
    print("\n===== WELCOME TO GRADEBOOK ANALYZER =====")
    print("Choose an option:")
    print("1. Manual Input")
    print("2. Load from CSV")
    print("3. Exit")

    while True:
        choice = input("\nEnter your choice (1-3): ")

        if choice == "1":
            marks = manual_input()

        elif choice == "2":
            marks = load_csv()

        elif choice == "3":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice! Try again.")
            continue

        if not marks:
            print("No data found. Try again.")
            continue

        # ---------------------------------------------
        # Task 4 – Create grades dictionary
        # ---------------------------------------------
        grades = {name: assign_grade(score) for name, score in marks.items()}

        # Grade distribution
        grade_counts = {
            "A": list(grades.values()).count("A"),
            "B": list(grades.values()).count("B"),
            "C": list(grades.values()).count("C"),
            "D": list(grades.values()).count("D"),
            "F": list(grades.values()).count("F"),
        }

        # ---------------------------------------------
        # Task 5 – Pass / Fail using list comprehension
        # ---------------------------------------------
        passed_students = [name for name, score in marks.items() if score >= 40]
        failed_students = [name for name, score in marks.items() if score < 40]

        # ---------------------------------------------
        # Task 3 – Statistics
        # ---------------------------------------------
        avg = calculate_average(marks)
        med = calculate_median(marks)
        max_name, max_score = find_max_score(marks)
        min_name, min_score = find_min_score(marks)

        # Print Statistics
        print("\n===== ANALYSIS SUMMARY =====")
        print(f"Average Score: {avg:.2f}")
        print(f"Median Score: {med}")
        print(f"Highest Score: {max_name} – {max_score}")
        print(f"Lowest Score: {min_name} – {min_score}")

        # Print Grade Distribution
        print("\nGrade Distribution:")
        for grade, count in grade_counts.items():
            print(f"{grade}: {count}")

        # Print Pass/Fail
        print("\nPassed Students:", ", ".join(passed_students))
        print("Failed Students:", ", ".join(failed_students))

        # ---------------------------------------------
        # Task 6 – Final Table
        # ---------------------------------------------
        print_table(marks, grades)

        # Repeat?
        again = input("\nDo you want to perform another analysis? (y/n): ")
        if again.lower() != "y":
            print("Thank you for using GradeBook Analyzer!")
            break


# Run Program
if __name__ == "__main__":
    main()
