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
    """..."""
    while True:
        user_input = input(prompt).strip()
        if user_input.lower() == 'quit':
            return ('quit', None) # Return a status tuple
        try:
            return ('ok', float(user_input)) # Return a status tuple
        except ValueError:
            print("Invalid input. Please enter a valid number or 'quit'.")

def get_validated_operator():
    """..."""
    valid_operators = ['+', '-', '*', '/']
    while True:
        operator = input("Enter operator (+, -, *, /) or 'quit': ").strip()
        if operator.lower() == 'quit':
            return ('quit', None) # Return a status tuple
        if operator in valid_operators:
            return ('ok', operator) # Return a status tuple
        else:
            print("Invalid operator. Please enter one of +, -, *, / or 'quit'.")

def repl_calculator():
    """Main Read-Eval-Print Loop (REPL) for the command-line calculator."""
    print("Welcome to the CLI Calculator!")
    print("Enter 'quit' at any prompt to exit the application.")
    print("-" * 30)

    while True:
        # Helper function to get input and check for quit status immediately
        def get_and_check(getter_func, *args):
            status, value = getter_func(*args)
            if status == 'quit':
                return None, True # Return a flag indicating exit
            return value, False # Return the value and a flag indicating success

        # --- 1. Read (Get Operator) ---
        operator, quit_flag = get_and_check(get_validated_operator)
        if quit_flag:
            break

        # --- 2. Read (Get Numbers) ---
        num1, quit_flag = get_and_check(get_validated_input, "Enter first number: ")
        if quit_flag:
            break

        num2, quit_flag = get_and_check(get_validated_input, "Enter second number: ")
        if quit_flag:
            break

        # --- 3. Eval & Error Handling ---
        try:
            # The values are already guaranteed to be floats (or None if quit)
            result = calculate(operator, num1, num2) 

            # --- 4. Print ---
            print(f"\nResult: {num1} {operator} {num2} = {result}")

        except ZeroDivisionError as e:
            print(e)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        print("-" * 30)

    print("Thank you for using the calculator. Goodbye! 👋")

if __name__ == "__main__":
    repl_calculator()