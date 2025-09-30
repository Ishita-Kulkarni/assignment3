def calculate(operator, num1, num2):
    """Performs the requested arithmetic operation."""
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            # Explicitly raise an error for division by zero
            raise ZeroDivisionError("Error: Division by zero is not allowed.")
        return num1 / num2
    else:
        # Should be caught by the main loop, but included for completeness
        raise ValueError("Error: Invalid operation.")

def get_validated_input(prompt):
    """
    Prompts the user for input and validates that it is a number (float).
    Continues prompting until valid input is received.
    """
    while True:
        user_input = input(prompt).strip()
        if user_input.lower() == 'quit':
            return 'quit'
        try:
            # Attempt to convert the input to a float
            return float(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid number or 'quit'.")

def get_validated_operator():
    """
    Prompts the user for an operator and validates that it is one of the supported
    operations (+, -, *, /).
    """
    valid_operators = ['+', '-', '*', '/']
    while True:
        operator = input("Enter operator (+, -, *, /) or 'quit': ").strip()
        if operator.lower() == 'quit':
            return 'quit'
        if operator in valid_operators:
            return operator
        else:
            print("Invalid operator. Please enter one of +, -, *, / or 'quit'.")

def repl_calculator():
    """
    Main Read-Eval-Print Loop (REPL) for the command-line calculator.
    """
    print("Welcome to the CLI Calculator!")
    print("Enter 'quit' at any prompt to exit the application.")
    print("-" * 30)

    while True:
        # --- 1. Read (Get Operator) ---
        operator = get_validated_operator()
        if operator == 'quit':
            break

        # --- 2. Read (Get Numbers) ---
        num1 = get_validated_input("Enter first number: ")
        if num1 == 'quit':
            break

        num2 = get_validated_input("Enter second number: ")
        if num2 == 'quit':
            break

        # --- 3. Eval & Error Handling ---
        try:
            # Ensure numbers are floats before passing to calculation
            result = calculate(operator, float(num1), float(num2))

            # --- 4. Print ---
            print(f"\nResult: {num1} {operator} {num2} = {result}")

        except ZeroDivisionError as e:
            # Handle division by zero specifically
            print(e)
        except Exception as e:
            # Handle any other unexpected errors
            print(f"An unexpected error occurred: {e}")

        print("-" * 30)

    print("Thank you for using the calculator. Goodbye!")

if __name__ == "__main__":
    repl_calculator()