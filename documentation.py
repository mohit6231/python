# This is a single-line comment
x = 10  # You can also add comments after code

"""
This is a multi-line comment or docstring.
It can span multiple lines.
"""
# Docstrings


def add(a, b):
    """Add two numbers and return the result."""
    return a + b


def multiply(a, b):
    """
    Multiply two numbers.

    This function takes two numbers and returns their product.
    It works for both integers and floating-point numbers.
    """
    return a * b


print(add.__doc__)  # Output: Add two numbers and return the result.
