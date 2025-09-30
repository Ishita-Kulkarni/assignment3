# Command-Line Calculator

A Python-based command-line calculator with a REPL interface that supports addition, subtraction, multiplication, and division.  
The application handles invalid input, division by zero, and supports scientific notation.

---

## **Features**

- **REPL Interface:** Continuously prompts users until they choose to quit.
- **Arithmetic Operations:** Addition (+), Subtraction (-), Multiplication (*), Division (/).
- **Input Validation:** Ensures numeric input; supports floats, integers, and scientific notation.
- **Error Handling:** Graceful messages for invalid input or division by zero.
- **Extensible & Maintainable:** Uses DRY principle; easy to add new operations.

---

## **Project Structure**

assignment3/
│
├── src/
│ ├── init.py
│ └── calculator.py # Core calculator logic
├── tests/
│ ├── init.py
│ └── test_operations.py # Unit tests
├── main.py # CLI entry point
├── README.md
└── requirements.txt

---

## **Setup Instructions**

1. Clone the Repository
```bash
git clone git@github.com:your-username/my_project.git
cd my_project

2. Create and Activate Virtual Environment
# Linux / Mac
python3 -m venv .venv
source .venv/bin/activate

# Windows (PowerShell)
python -m venv .venv
.venv\Scripts\Activate.ps1

3. Install Dependencies
pip install -r requirements.txt

Usage

Run the calculator CLI:

python main.py

Example session:

Welcome to the Command-Line Calculator!

Select operation:
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Quit
Enter choice (1-5): 1
Enter the first number: 3
Enter the second number: 4
Result: 7

Testing

Run all unit tests using pytest:

pytest


Check test coverage:

pytest --cov=src --cov-report=term-missing