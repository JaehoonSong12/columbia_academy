## random Module
import random       # load the math module into memory


## Library Functions (Black Boxes)
# seed Function (default argument: current time)
random.seed(10)                 # specify the seed value for pseudorandom number set 

# randint Function
print(random.randint(1, 10))    # returns random integer on [1, 10] (argument1: int, argument2: int, return: int)

# randrange Function
print(random.randrange(10))     # returns random integer on [0, 10) (argument: int, return: int)
print(random.randrange(5, 10))  # returns random integer on [5, 10) (argument1: int, argument2: int, return: int)
print(random.randrange(5, 9, 2))# returns random integer on [5, 9) with a step value, 2 (argument1: int, argument2: int, argument3: int, return: int)

# randrange Function in Sequence Formula:
# randrange(a): n (n < a)
# randrange(a, b): n + a (n + a < b)
# randrange(a, b, c): c * n + a (c * n + a < b)
# randrange(a, b, -c): -c * n + a (-c * n + a > b)


# random Function
print(random.random())          # returns random floating number on [0, 1) (return: float)

# uniform Function
print(random.uniform(1.2, 2.3)) # returns random floating number on [1.2, 2.3) (argument1: float, argument2: float, return: float)
