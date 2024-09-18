# Importing gc module
import gc

# Returns the number of
# objects it has collected
# and deallocated
collected = gc.collect()

# Prints Garbage collector
# as 0 object
print("Garbage collector: collected",
      "%d objects." % collected)


i = 0

# create a cycle and on each iteration x as a dictionary
# assigned to 1


def create_cycle():
    x = {}
    x[i+1] = x
    print(x)


# lists are cleared whenever a full collection or
# collection of the highest generation (2) is run
collected = gc.collect()  # or gc.collect(2)
print("Garbage collector: collected %d objects." % (collected))

print("Creating cycles...")
for i in range(10):
    create_cycle()

collected = gc.collect()

print("Garbage collector: collected %d objects." % (collected))


# Create some objects
obj1 = [1, 2, 3]
obj2 = {"a": 1, "b": 2}
obj3 = "Hello, world!"

# Delete references to objects
del obj1
del obj2
del obj3

# Force a garbage collection
gc.collect()


# Disable the garbage collector
gc.disable()

# Create some objects
obj1 = [1, 2, 3]
obj2 = {"a": 1, "b": 2}
obj3 = "Hello, world!"

# Delete references to objects
del obj1
del obj2
del obj3

# The garbage collector is disabled, so it will not run


# Disable the garbage collector
gc.disable()

# Enable the garbage collector
gc.enable()


# Trigger a garbage collection
gc.collect()

# Get the current garbage collector thresholds
thresholds = gc.get_threshold()
print(thresholds)


gc.set_threshold(500, 5, 5)
print("Garbage collector thresholds set")

# Get the current garbage collector thresholds
thresholds = gc.get_threshold()
print("Current thresholds:", thresholds)
