# main.py
from src.calculator import add, subtract, multiply, divide, parse_number

def print_menu():
    print("\nSelect operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Quit")

def get_input(prompt):
    """Get a number from the user, handle invalid inputs."""
    while True:
        try:
            return parse_number(input(prompt).strip())
        except ValueError as e:
            print(e)

def perform_operation(func, a, b):
    """Execute an arithmetic operation with error handling."""
    try:
        result = func(a, b)
        print(f"Result: {result}")
    except ValueError as e:
        print(e)

def main():
    print("Welcome to the Command-Line Calculator!")

    operation_map = {
        '1': (add, '+'),
        '2': (subtract, '-'),
        '3': (multiply, '*'),
        '4': (divide, '/')
    }

    while True:
        print_menu()
        choice = input("Enter choice (1-5): ").strip()

        if choice == '5':
            print("Goodbye!")
            break

        if choice not in operation_map:
            print("Invalid choice. Please select 1-5.")
            continue

        a = get_input("Enter the first number: ")
        b = get_input("Enter the second number: ")

        func, symbol = operation_map[choice]
        perform_operation(func, a, b)

if __name__ == "__main__":
    main()
