"""
Student Result Management System
A simple console-based Python application to calculate student results.
"""

def get_mark(subject):
    """Read and validate a mark between 0 and 100."""
    while True:
        try:
            mark = float(input(f"Enter marks for {subject} (0-100): "))
            if 0 <= mark <= 100:
                return mark
            print("Please enter a mark between 0 and 100.")
        except ValueError:
            print("Invalid input. Enter a number, such as 78 or 84.5.")


def calculate_grade(percentage):
    """Return a grade based on the student's percentage."""
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    elif percentage >= 40:
        return "E"
    return "F"


def create_result():
    """Collect student details and print a result summary."""
    print("\n--- Enter Student Details ---")
    name = input("Student name: ").strip()
    while not name:
        print("Name cannot be empty.")
        name = input("Student name: ").strip()

    roll_number = input("Roll number: ").strip()
    while not roll_number:
        print("Roll number cannot be empty.")
        roll_number = input("Roll number: ").strip()

    subjects = ["Python", "Mathematics", "Computer Networks", "Database Systems", "English"]
    marks = {subject: get_mark(subject) for subject in subjects}

    total = sum(marks.values())
    maximum = len(subjects) * 100
    percentage = total / maximum * 100
    grade = calculate_grade(percentage)
    status = "PASS" if all(mark >= 35 for mark in marks.values()) else "FAIL"

    print("\n" + "=" * 42)
    print("             STUDENT RESULT")
    print("=" * 42)
    print(f"Name       : {name}")
    print(f"Roll number: {roll_number}")
    print("-" * 42)
    for subject, mark in marks.items():
        print(f"{subject:<24} {mark:>6.1f}/100")
    print("-" * 42)
    print(f"Total      : {total:.1f}/{maximum}")
    print(f"Percentage : {percentage:.2f}%")
    print(f"Grade      : {grade}")
    print(f"Result     : {status}")
    print("=" * 42)


def main():
    """Display the menu and allow repeated result calculations."""
    print("Welcome to Student Result Management System")
    while True:
        print("\n1. Calculate student result")
        print("2. Exit")
        choice = input("Choose an option (1/2): ").strip()

        if choice == "1":
            create_result()
        elif choice == "2":
            print("Thank you for using the application.")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
