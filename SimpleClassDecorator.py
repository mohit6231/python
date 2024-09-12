def my_decorator(cls):
    cls.decorated = True  # Add a new attribute to the class
    return cls


@my_decorator
class SimpleClassDecorator:
    pass


# Example usage
print(SimpleClassDecorator.decorated)  # Outputs: True
