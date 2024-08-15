import math
print("Hello World")
x = 1
print(x)

students_count = 1000
rating = 4.9
is_published = False
course_name = "Python course"
course_length = len(course_name)
print(course_name[0:3])
print(course_name[-1])
print(course_name[1: -1])

course = "Python \"course"
print(course)
course = "Python \ncourse"
print(course)

fname = 'mohit'
lname = 'bansal'
fullname = f"{fname} {lname}"  # formatted strings
print(fullname)

name = "   mohit bansal"
print(name.upper())
print(name.lower())
print(name.title())
print(name.strip())  # trim whitespaces
print(name.lstrip())  # trim left whitespaces
print(name.find("ban"))  # returns index
print("ban" in name)

print(10 + 3)
print(10 / 3)
print(10 // 3)
print(10 ** 2)

print(math.ceil(2.2))

x = input("x: ")
y = int(x) + 1
print(y)

print(bool("Falsy"))  # returns TRUE

temp = 35
if temp > 30:
    print("Warm")  # autoprep8 reformat code and uses 4 whitespaces
    print("Drink water")
elif temp < 30:
    print("Cold")
else:
    print("it is neutral")
print("Done")

age = 20
message = 'Eligible' if age >= 18 else 'Not Eligible'
print(message)

student = False
if not student:
    print('Eligible')

if 18 < age < 65:  # Chaining comparison operators
    print("Eligible")

if 10 == '10':
    print("a")
elif "bag" > "apple" and "bag" > "cat":
    print("b")
else:
    print("c")

for num in range(3):
   # print("attempt", num)
    print("attempt", num + 1, (num + 1) * ".")

for num in range(1, 10, 2):
   # print("attempt", num)
    print("attempt", num, num * ".")

# for else
success = False
for num in range(3):
    print("attempt", num)
    if success:
        print("break")
        break
else:
    print("failed")

for num in "Python":
    print("String", num)

for num in [1, 2, 3, 4]:
    print("String", num)

count = 0
for num in range(1, 10):
    if num % 2 == 0:
        count += 1
        print(num)
print(f"We have {count} even numbers")
