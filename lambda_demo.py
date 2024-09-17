def calc(num): return "Even number" if num % 2 == 0 else "Odd number"


print(calc(20))

string = 'GeeksforGeeks'

# lambda returns a function object
print(lambda string: string)


def filter_nums(s): return ''.join([ch for ch in s if not ch.isdigit()])


print("filter_nums():", filter_nums("Geeks101"))


def do_exclaim(s): return s + '!'


print("do_exclaim():", do_exclaim("I am tired"))


def find_sum(n): return sum([int(x) for x in str(n)])


print("find_sum():", find_sum(101))
