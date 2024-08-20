try:
    age = int(input("Age: "))
except ValueError as ex:
    print("You didn't enter valid age")
    print(ex)
    print(type(ex))
else:
    print('Process complete')


try:
    with open("datastructures.py") as file:
        print('File Opened')
        file.close()
    age = int(input("Age: "))
    age = 10/age
except (ValueError, ZeroDivisionError):
    print('Invalid')
