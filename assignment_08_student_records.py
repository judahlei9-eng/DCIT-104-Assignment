# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
#
# Build a console-based program that stores and manages student information.
# Each student record must contain:
#
#   - Name   : the student's full name (text)
#   - ID     : a unique student ID number (e.g. 20240001)
#   - Scores : a list of scores from multiple assessments (e.g. [75, 88, 90])
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Student
#      - Ask the user to enter the student's name and ID.
#      - Ask how many scores to enter, then collect each score one by one.
#      - Save the student record and confirm it was added.
#
#   2. Display All Students
#      - Print a formatted table showing every student's:
#          Name, ID, individual scores, and their average score.
#      - If no students have been added yet, print a message saying so.
#
#   3. Calculate Average Score for a Specific Student
#      - Ask the user to enter a student ID.
#      - Find the student and calculate the average of their scores.
#      - Display the result. If the ID is not found, print an error message.
#
#   4. Quit
#      - End the program.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ================================
#      STUDENT RECORD SYSTEM MENU
#   ================================
#   1. Add student
#   2. Display all students
#   3. Calculate average score
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Student name: Alice Mensah
#   Student ID: 20240001
#   How many scores? 3
#   Enter score 1: 78
#   Enter score 2: 85
#   Enter score 3: 90
#   Student "Alice Mensah" added successfully.
#
#   Enter your choice (1-4): 2
#   --------------------------------------------------
#   Name           ID          Scores         Average
#   --------------------------------------------------
#   Alice Mensah   20240001    78, 85, 90     84.33
#   --------------------------------------------------
#
#   Enter your choice (1-4): 3
#   Enter student ID: 20240001
#   Alice Mensah's average score: 84.33
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store all student records in a list of dictionaries.
#   Example structure:
#       student = {
#           "name": "Alice Mensah",
#           "id": 20240001,
#           "scores": [78, 85, 90]
#       }
# - Average scores should be rounded to 2 decimal places.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices and missing student IDs gracefully.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================

def display_menu():
    """Prints the main menu options."""
    print("================================")
    print("   STUDENT RECORD SYSTEM MENU   ")
    print("================================")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")


def add_student(students):
    """Prompts the user for student details and appends a new dictionary record."""
    name = input("Student name: ").strip()
    student_id = input("Student ID: ").strip()

    try:
        num_scores = int(input("How many scores? "))
        scores = []
        for i in range(1, num_scores + 1):
            score = float(input(f"Enter score {i}: "))
            scores.append(score)

        # Store as a dictionary record
        student = {
            "name": name,
            "id": student_id,
            "scores": scores
        }

        students.append(student)
        print(f'Student "{name}" added successfully.')

    except ValueError:
        print("Error: Invalid numeric input. Student creation cancelled.")


def display_all_students(students):
    """Prints a formatted table displaying all registered students and their stats."""
    if not students:
        print("No student records available.")
        return

    print("-" * 50)
    print(f"{'Name':<15} {'ID':<11} {'Scores':<14} {'Average':<7}")
    print("-" * 50)

    for student in students:
        scores_str = ", ".join(
            str(int(s)) if s.is_integer() else f"{s:.1f}" for s in student["scores"]
        )
        avg_score = sum(student["scores"]) / len(student["scores"]) if student["scores"] else 0.0

        print(f"{student['name']:<15} {student['id']:<11} {scores_str:<14} {avg_score:<7.2f}")

    print("-" * 50)


def calculate_student_average(students):
    """Finds a student by ID and prints their calculated average score."""
    search_id = input("Enter student ID: ").strip()

    for student in students:
        if student["id"] == search_id:
            if student["scores"]:
                avg = sum(student["scores"]) / len(student["scores"])
                print(f"{student['name']}'s average score: {avg:.2f}")
            else:
                print(f"{student['name']} has no recorded scores.")
            return

    print("Error: Student ID not found.")


def main():
    """Main execution loop for managing student records."""
    students = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            add_student(students)
        elif choice == '2':
            display_all_students(students)
        elif choice == '3':
            calculate_student_average(students)
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a number between 1 and 4.")

        print()  # Spacer line between actions


if __name__ == "__main__":
    main()
# =============================================================================

