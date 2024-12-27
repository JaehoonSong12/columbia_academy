## range Function
for target_var in range(3):         # returns a list of whole number on [0, 3)
    print(target_var)               # (argument: int, return: iterable)

for target_var in range(1, 5):      # returns a list of whole number on [1, 5)
    print(target_var)               # (argument1: int, argument2: int, return: iterable)

for target_var in range(1, 5, 2):   # returns a list of whole number on [1, 5) with a step value, 2
    print(target_var)               # (argument1: int, argument2: int, argument3: int, return: iterable)

for target_var in range(9, 0, -1):  # returns a list of whole number on (0, 9] with a step value, -1
    print(target_var)               # (argument1: int, argument2: int, argument3: int, return: iterable)

# range Function in Sequence Formula:
# range(a): n (n < a)
# range(a, b): n + a (n + a < b)
# range(a, b, c): c * n + a (c * n + a < b)
# range(a, b, -c): -c * n + a (-c * n + a > b)
