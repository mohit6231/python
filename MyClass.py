def add_method(cls):
    def new_method(self):
        return "This is a new method!"
    cls.new_method = new_method  # Add the new method to the class
    return cls

@add_method
class MyClass:
    def existing_method(self):
        return "This is an existing method."

# Example usage
obj = MyClass()
print(obj.existing_method())  # Outputs: This is an existing method.
print(obj.new_method())       # Outputs: This is a new method!
