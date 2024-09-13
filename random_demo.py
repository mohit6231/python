import random


def roll_dice():
    return random.randint(1, 6)


# Roll the dice
dice_roll = roll_dice()
print(f"The dice roll result is: {dice_roll}")

print(random.random())  # Output: Random float between 0.0 and 1.0

print(random.randint(1, 10))  # Output: Random integer between 1 and 10

print(random.uniform(1, 10))  # Output: Random float between 1 and 10

# Output: Random number between 0 and 100 that is divisible by 10
print(random.randrange(0, 100, 10))

choices = ['apple', 'banana', 'cherry']
print(random.choice(choices))  # Output: Randomly chosen element from the list

choices = ['apple', 'banana', 'cherry']
# Output: A list of 2 randomly chosen elements
print(random.choices(choices, k=2))

# With weights
# 'apple' has a higher chance of being chosen
print(random.choices(choices, weights=[10, 1, 1], k=2))

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)  # Output: Randomly shuffled list

numbers = [1, 2, 3, 4, 5]
# Output: A list of 3 randomly chosen unique elements
print(random.sample(numbers, 3))

random.seed(42)  # Set the seed
print(random.random())  # Output: Always the same random number when seed is set
