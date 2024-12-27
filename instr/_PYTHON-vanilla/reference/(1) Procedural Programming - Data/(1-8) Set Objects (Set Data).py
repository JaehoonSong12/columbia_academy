## Sets (by set Function, mutable)
print(set())                # returns an empty set (return: set)
print(set([1, 2, 3]))       # returns a set containg all the elements of the argument (arg: list, return: set)
print(set(('ab', 2, 3)))    # returns a set containg all the elements of the argument (arg: tuple, return: set)
print(set('string'))        # returns a set containg all the elements of the argument (arg: string, return: set)

# (!) Sets cannot contain duplicate elements


## Set Expressions with Operators (in, not in, union, intersection, difference, symmetric difference, subset, superset)
print(1 in set([1, 2, 3]))                # determines if an element exists in a set (return: bool)
print(1 not in set([1, 2, 3]))            # determines if an element does not exist in a set (return: bool)

print(set([1, 2, 3]) | set([3, 4, 5]))    # returns the union of two sets (return: set)
print(set([1, 2, 3]).union(set([3, 4, 5])))

print(set([1, 2, 3]) & set([3, 4, 5]))    # returns the intersection of two sets (return: set)
print(set([1, 2, 3]).intersection(set([3, 4, 5])))

print(set([1, 2, 3]) - set([3, 4, 5]))    # returns the difference of two sets (return: set)
print(set([1, 2, 3]).difference(set([3, 4, 5])))

print(set([1, 2, 3]) ^ set([3, 4, 5]))    # returns the symmetric difference of two sets (return: set)
print(set([1, 2, 3]).symmetric_difference(set([3, 4, 5])))

print(set([3]) <= set([3, 4, 5]))         # determines if the first set is subset of the second (return: bool)
print(set([3]).issubset(set([3, 4, 5])))

print(set([1, 2, 3]) >= set([3]))         # determines if the first set is superset of the second (return: bool)
print(set([1, 2, 3]).issuperset(set([3])))


## Member Functions
myset = set()

# add Function (Method)
myset.add(1)                # add an element to a set (arg: data, void)

# update Function (Method)
myset.update([2, 3, 4])     # add a group of elements to a set (arg: sequence, void)

# discard Function (Method)
myset.discard(1)            # remove an item from a set (arg: data, void)
                            # (!) No KeyError exception

# remove Function (Method)
myset.remove(1)             # remove an item from a set (arg: data, void)
                            # (!) KeyError exception if if the item is not in the set

# clear Function (Method)
myset.clear()               # clear all the elements of a set (void)