from array import array
from collections import deque
letters = ['a', 'b', 'c', 'd']
matrix = [[0, 1], [1, 2]]
zeroes = [0] * 5
combined = zeroes + letters
print(matrix)
print(combined)
print(list(range(20)))
print(letters[:3])
print(letters[0:])
print(letters[::2])  # skip the 2nd element and returns 2 elements total
numbers = list(range(20))
print(numbers[::2])  # display even numbers

numbers = [1, 2, 3]
# This only works when we define all vars, if we skip one, error too many values to unpack
first, second, third = numbers
print(first)
first, *other = numbers
print(other)

letters = ['a', 'b', 'c', 'd']
for letter in letters:
    print(letter)

for letter in enumerate(letters):  # returns tuple
    print(letter)
    print(letter[0])

for index, letter in enumerate(letters):  # returns tuple
    print(index, letter)

letters.append('e')
letters.insert(0, 'alpha')
print(letters)

letters.pop()
letters.pop(0)
print(letters)
del letters[1]
print(letters)
letters.clear()
print(letters)

letters = ['a']
print(letters.index('a'))

nums = [20, 10, 2, 1, 44]
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)
print(sorted(nums, reverse=True))

items = [
    ("P1", 10),
    ("P2", 9),
    ("P3", 12)
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)

# lambda function
items.sort(key=lambda item: item[1])
print(items)

prices = []
for item in items:
    prices.append(item[1])

print(prices)

# map function
x = map(lambda item: item[1], items)
print(x)
for item in x:
    print(item)

prices = list(map(lambda item: item[1], items))
print(prices)

y = list(filter(lambda item: item[1] > 10, items))
filter = [item for item in items if item[1] > 10]  # list comprehension
print(y)
print(filter)

price = [item[1] for item in items]  # list comprehension
print(price)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list(zip(list1, list2)))
print(list(zip("abc", list1, list2)))

stacks = []
stacks.append(1)
stacks.append(2)
stacks.pop()
print(stacks)

queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)
if not queue:
    print('not empty')

x = 10
y = 11
x, y = y, x  # tuple method, tuple cannot be modified
print(x)
print(y)

numbers = array('i', [1, 2, 3])
print(numbers)
# numbers[0] = 1.2
numbers[0] = 12
print(numbers)

numbers = [1, 1, 2, 3, 4]
uniques = set(numbers)
print(uniques)

second = {1, 4}
second.add(5)
second.remove(5)
print(second)
print(len(second))

print(uniques | second)
print(uniques & second)
print(uniques - second)
print(uniques ^ second)

point = {'x': 1, 'y': 2}
point = dict(x=1, y=2)

print(point.get('a', 0))

for key, value in point.items():
    print(key, value)
