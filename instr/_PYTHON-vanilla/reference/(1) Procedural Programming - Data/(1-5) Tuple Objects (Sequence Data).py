## Tuples (immutable)
print((2, 'Kelly', 5.2))
print((2,))
print(((2, 3),
       (3, 4)))     # Tuples can be nested

# Advantages of tuple
# 1. faster than list
# 2. tuples are safe because it is immutable


## Index
my_tuple = (10, 20, 30)
print(my_tuple[-3])      # specify the first element
print(my_tuple[-2])      # specify the second element
print(my_tuple[-1])      # specify the third element
print(my_tuple[0])       # specify the first element
print(my_tuple[1])       # specify the second element
print(my_tuple[2])       # specify the third element

# Negative Index Rule:
# 1. Python interpreter adds negative indexes to the length of the tuple to determine the position
# 2. IndexError exception will be raised when an invalid index is used


## List Slicing
tuple_1 = ('1st', '2nd', '3rd', '4th')
print(tuple_1[2:4])         # returns a new tuple of a sliced tuple, index on [2, 4)
print(tuple_1[0:4:2])       # returns a new tuple of a sliced tuple, index on [0, 4) with a step value, 2
print(tuple_1[:3])          # (!) default starting index is 0
print(tuple_1[1:])          # (!) default ending index is len(tuple_1)
print(tuple_1[-5:6])        # (!) no IndexError exceptions raised due to default values


## List Expressions with Operators (concatenation, repetition, in, not in)
print((1, 2) + (3, 4))      # returns a new joined tuple of two tuples (return: list)
print((0,) * 5)             # returns a new tuple of multipe copies (return: list)
print(2 in (1, 2, 3))       # determines if an item is contained in a tuple (return: bool)
print(2 not in (1, 2, 3))   # determines if an item is contained in a tuple (return: bool)


## Member Functions
x = ('item', 'item')

# search - index Function (Method)
print(x.index('item'))      # returns the index of the first corresponding element
                            # (!) ValueError exceptions raised if no item found
