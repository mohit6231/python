import sys
x = [1, 2, 3]

# Increment reference count
y = x

# Decrement reference count
y = None


# Example 2: Reference Counting with Cyclic Reference
# Create two objects that refer to each other
x = [1, 2, 3]
y = [4, 5, 6]
x.append(y)
y.append(x)


# Create an object
x = [1, 2, 3]

# Get reference count
ref_count = sys.getrefcount(x)

print("Reference count of x:", ref_count)
