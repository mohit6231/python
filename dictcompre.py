# Traditional way
squares = {}
for x in range(5):
    squares[x] = x ** 2

# Using dictionary comprehension
squares = {x: x ** 2 for x in range(5)}
print(squares)

even_squares = {x: x ** 2 for x in range(10) if x % 2 == 0}
print(even_squares)  # Output: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
