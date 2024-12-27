## Lists (mutable)
print([2, 'Kelly', 5.2])
print([[2, 3],
       [3, 4]])     # Lists can be nested


## Index
my_list = [10, 20, 30]
print(my_list[-3])      # specify the first element
print(my_list[-2])      # specify the second element
print(my_list[-1])      # specify the third element
print(my_list[0])       # specify the first element
print(my_list[1])       # specify the second element
print(my_list[2])       # specify the third element

# Negative Index Rule:
# 1. Python interpreter adds negative indexes to the length of the list to determine the position
# 2. IndexError exception will be raised when an invalid index is used


## List Slicing
list_1 = ['1st', '2nd', '3rd', '4th']
print(list_1[2:4])          # returns a new list of a sliced list, index on [2, 4)
print(list_1[0:4:2])        # returns a new list of a sliced list, index on [0, 4) with a step value, 2
print(list_1[:3])           # (!) default starting index is 0
print(list_1[1:])           # (!) default ending index is len(list_1)
print(list_1[-5:6])         # (!) no IndexError exceptions raised due to default values


## List Expressions with Operators (concatenation, repetition, in, not in)
print([1, 2] + [3, 4])      # returns a new joined list of two lists (return: list)
print([0] * 5)              # returns a new list of multipe copies (return: list)
print(2 in [1, 2, 3])       # determines if an item is contained in a list (return: bool)
print(2 not in [1, 2, 3])   # determines if an item is contained in a list (return: bool)


## Member Functions
x = ['item', 'item']

# search - index Function (Method)
print(x.index('item'))      # returns the index of the first corresponding element
                            # (!) ValueError exceptions raised if no item found

# sort - sort Function (Method)
x.sort()                    # sorts the items in a list (void)
print(x)

# sort - reverse Function (Method)
x.reverse()                 # reverses the order of a list (void)
print(x)

# modification - append Function (Method)
x.append('appended item')   # adds an item to the end of the list (void)
print(x)

# modification - insert Function (Method)
x.insert(1, 'new item')     # inserts an item into a list (void)
print(x)                    # (!) no IndexError exceptions raised

# modification - del Statement
del x[1]                    # removes an item from the list based on the index
print(x)

# modification - remove Function (Method)
x.remove('item')            # removes an item from the list (void)
print(x)                    # (!) ValueError exceptions raised if no item found
