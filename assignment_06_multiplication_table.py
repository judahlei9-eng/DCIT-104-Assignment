# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# Write a Python program that generates multiplication tables using loops
# and functions.
#
# -----------------------------------------------------------------------------
# PART A — Single Table
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Print the multiplication table for that number from 1 to 12.
#
# Expected output (if user enters 5):
#
#   Multiplication Table for 5:
#   5  x  1  =  5
#   5  x  2  =  10
#   5  x  3  =  15
#   ...
#   5  x  12 =  60
#
# -----------------------------------------------------------------------------
# PART B — Bonus: Tables from 1 to N
# -----------------------------------------------------------------------------
# - Ask the user to enter a number N.
# - Print the full multiplication table for every number from 1 to N.
# - Add a separator line (e.g. "---") between each table.
#
# Expected output (if user enters 3):
#
#   Multiplication Table for 1:
#   1  x  1  =  1
#   ...
#   1  x  12 =  12
#   ---------------------------
#   Multiplication Table for 2:
#   2  x  1  =  2
#   ...
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - N must be a positive integer. If the user enters an invalid value,
#   print an error message and stop.
# - Each part must be in its own function (see scaffold below).
# - Complete Part A before attempting Part B.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================

def print_single_table(number):
    """Prints the multiplication table for a given number from 1 to 12."""
    print(f"Multiplication Table for {number}:")
    for i in range(1, 13):
        # Using format formatting to ensure double-digit alignment like the expected output
        if i < 10:
            print(f"{number}  x  {i}  =  {number * i}")
        else:
            print(f"{number}  x  {i} =  {number * i}")


def print_tables_up_to_n(n):
    """Prints multiplication tables for numbers from 1 to N with separators."""
    for current_number in range(1, n + 1):
        print_single_table(current_number)
        # Add a separator line after each table except the last one
        if current_number < n:
            print("-" * 27)


if __name__ == "__main__":
    # ---------------- PART A — Single Table ----------------
    try:
        user_input = int(input("Enter a number: "))
        print_single_table(user_input)
    except ValueError:
        print("Error: Please enter a valid integer.")

    print()  # Blank line between Part A and Part B

    # ---------------- PART B — Bonus: Tables from 1 to N ----------------
    try:
        n_input = int(input("Enter N (tables from 1 to N): "))

        # Input validation for positive integer N
        if n_input <= 0:
            print("Error: N must be a positive integer.")
        else:
            print_tables_up_to_n(n_input)
    except ValueError:
        print("Error: Please enter a valid integer.")
# =============================================================================

