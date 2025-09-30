import pytest
from src.calculator import add, subtract, multiply, divide, parse_number

# -----------------------------
# Addition Tests
# -----------------------------
@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (-1, 1, 0),
    (0, 0, 0),
    (1.5, 2.5, 4.0)
])
def test_add(a, b, expected):
    assert add(a, b) == expected

# -----------------------------
# Subtraction Tests
# -----------------------------
@pytest.mark.parametrize("a,b,expected", [
    (5, 2, 3),
    (0, 3, -3),
    (-2, -2, 0),
    (2.5, 1.0, 1.5)
])
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected

# -----------------------------
# Multiplication Tests
# -----------------------------
@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 6),
    (0, 5, 0),
    (-2, 3, -6),
    (1.5, 2, 3.0)
])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected

# -----------------------------
# Division Tests
# -----------------------------
@pytest.mark.parametrize("a,b,expected", [
    (6, 3, 2),
    (-6, 3, -2),
    (5.0, 2.0, 2.5)
])
def test_divide(a, b, expected):
    assert divide(a, b) == expected

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        divide(5, 0)

# -----------------------------
# Number Parsing Tests
# -----------------------------
@pytest.mark.parametrize("value,expected", [
    ("42", 42),
    ("3.14", 3.14),
    ("0", 0),
    ("-7", -7),
    ("1e-3", 0.001)
])
def test_parse_number_valid(value, expected):
    assert parse_number(value) == expected

@pytest.mark.parametrize("value", ["abc", "", "1,2", " "])
def test_parse_number_invalid(value):
    with pytest.raises(ValueError):
        parse_number(value)
