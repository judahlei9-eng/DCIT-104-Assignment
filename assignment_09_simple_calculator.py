# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# Topic: Functions, Control Flow, and Exception Handling
# =============================================================================

def add(num1, num2):
    """Returns the sum of two numbers."""
    return num1 + num2


def subtract(num1, num2):
    """Returns the difference of two numbers."""
    return num1 - num2


def multiply(num1, num2):
    """Returns the product of two numbers."""
    return num1 * num2


def divide(num1, num2):
    """Returns the quotient of two numbers rounded to 2 decimal places."""
    if num2 == 0:
        return "Error: Cannot divide by zero."
    result = num1 / num2
    return round(result, 2)


def modulus(num1, num2):
    """Returns the remainder of division of two numbers."""
    if num2 == 0:
        return "Error: Cannot divide by zero."
    return num1 % num2


def power(num1, num2):
    """Returns num1 raised to the power of num2."""
    return num1 ** num2


def display_menu():
    """Prints the calculator menu options."""
    print("============================")
    print("     SIMPLE CALCULATOR      ")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")


def get_numbers():
    """Helper function to prompt and return two numeric inputs from the user."""
    num1 = float(input("Enter first number : "))
    num2 = float(input("Enter second number: "))
    # Clean up trailing .0 for cleaner display if inputs are whole integers
    num1 = int(num1) if num1.is_integer() else num1
    num2 = int(num2) if num2.is_integer() else num2
    return num1, num2


def main():
    """Main execution loop for the simple calculator."""
    while True:
        display_menu()
        choice = input("Select an operation (1-7): ").strip()

        if choice == '7':
            print("Goodbye!")
            break

        if choice in ('1', '2', '3', '4', '5', '6'):
            try:
                num1, num2 = get_numbers()

                if choice == '1':
                    result = add(num1, num2)
                    print(f"Result: {num1} + {num2} = {result}")

                elif choice == '2':
                    result = subtract(num1, num2)
                    print(f"Result: {num1} - {num2} = {result}")

                elif choice == '3':
                    result = multiply(num1, num2)
                    print(f"Result: {num1} * {num2} = {result}")

                elif choice == '4':
                    result = divide(num1, num2)
                    if isinstance(result, str):
                        print(result)
                    else:
                        print(f"Result: {num1} / {num2} = {result:.2f}" if isinstance(result, float) else f"Result: {num1} / {num2} = {result}")

                elif choice == '5':
                    result = modulus(num1, num2)
                    if isinstance(result, str):
                        print(result)
                    else:
                        print(f"Result: {num1} % {num2} = {result}")

                elif choice == '6':
                    result = power(num1, num2)
                    print(f"Result: {num1} ** {num2} = {result}")

            except ValueError:
                print("Error: Invalid numeric input. Please enter valid numbers.")

        else:
            print("Invalid choice! Please select an operation from 1 to 7.")

        print()  # Extra blank line for visual spacing between calculations


if __name__ == "__main__":
    main()
# =============================================================================

