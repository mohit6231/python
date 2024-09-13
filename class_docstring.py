class Calculator:
    """
    A simple calculator class to perform basic arithmetic operations.

    Methods:
    add(a, b) -> Adds two numbers.
    subtract(a, b) -> Subtracts the second number from the first.
    """

    def add(self, a, b):
        """Add two numbers."""
        return a + b


c = Calculator()
print(c.add(2, 3))
