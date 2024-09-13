class Descriptor:
    def __get__(self, instance, owner):
        print("Getting value")
        return instance.__dict__.get(self.name, None)

    def __set__(self, instance, value):
        print("Setting value")
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name

    def __delete__(self, instance):
        print("Deleting value")
        del instance.__dict__[self.name]


class MyClass:
    attr = Descriptor()


# Example usage
obj = MyClass()
obj.attr = 42  # Triggers __set__
print(obj.attr)  # Triggers __get__
del obj.attr  # Triggers __delete__
