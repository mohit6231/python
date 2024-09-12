# Using set comprehension
unique_squares = {x ** 2 for x in range(10)}
print(unique_squares)

# Using generator expression
gen = (x ** 2 for x in range(10))

for num in gen:
    print(num)  # Prints squares one by one
