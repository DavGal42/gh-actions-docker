"""
    Description: A simple script which executes some arithmetic operations for 'github actions and docker' task.
    Author: David Galstyan
    Date: 25.11.24
"""

def add(a, b):
    """
        Description: Returns the sum of two numbers.
        Arguments: First number, second number
    """
    return a + b


def subtract(a, b):
    """
        Description: Returns the difference between two numbers.
        Arguments: First number, second number
    """
    return a - b


def multiply(a, b):
    """
        Description: Returns the product of two numbers.
        Arguments: First number, second number
    """
    return a * b


def divide(a, b):
    """
        Description: Returns the division of two numbers. Raises ValueError if the second number is zero.
        Arguments: First number, second number
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b


def floor_divide(a, b):
    """
        Description: Returns the floor division result of two numbers. Raises ValueError if the second number is zero.
        Arguments: First number, second number
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a // b


def modulus(a, b):
    """
        Description: Returns the remainder of the division of two numbers.
        Arguments: First number, second number
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a % b


def main():
    """
        The main function
    """
    print(f"Add: {add(3, 5)}")
    print(f"Subtract: {subtract(10, 4)}")
    print(f"Multiply: {multiply(2, 3)}")
    print(f"Divide: {divide(10, 2)}")
    print(f"Floor Divide: {floor_divide(10, 3)}")
    print(f"Modulus: {modulus(10, 3)}")


if __name__ == "__main__":
    main()