def my_generator():
    yield 1
    yield 2
    yield 3


gen = my_generator()

for val in gen:
    print(val)


try:
    print(next(gen))  # Raises StopIteration
except StopIteration:
    print("No more values")


def infinite_counter(start=0):
    while True:
        yield start
        start += 1


counter = infinite_counter()
print(next(counter))  # Output: 0
print(next(counter))  # Output: 1
print(next(counter))  # Output: 2

gen = (x**2 for x in range(5))
print(next(gen))  # Output: 0
print(next(gen))  # Output: 1
print(next(gen))  # Output: 4

for val in gen:
    print(val)


def accumulator():
    total = 0
    while True:
        value = yield total
        if value is None:
            break
        total += value


gen = accumulator()
print(next(gen))  # Output: 0
print(gen.send(5))  # Output: 5
print(gen.send(10))  # Output: 15
gen.close()  # To stop the generator


def countdown(n):
    while n > 0:
        yield n
        n -= 1


gen = countdown(5)
print(next(gen))  # Output: 5
gen.close()  # Stops the generator


def generator1():
    yield from range(3)


def generator2():
    yield from generator1()
    yield "done"


for val in generator2():
    print(val)

# Output:
# 0
# 1
# 2
# done
