# Traditional way
squares = []
for x in range(10):
    squares.append(x ** 2)

# Using list comprehension
squares = [x ** 2 for x in range(10)]
print(squares)

even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
print(even_squares)  # Output: [0, 4, 16, 36, 64]
