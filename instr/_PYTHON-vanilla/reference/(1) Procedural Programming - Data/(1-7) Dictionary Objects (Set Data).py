## Dictionaries (by dict Fucntion, mutable)
print(dict())           # returns an empty dictionary (return: dictionary)
print({'Key1': 1101, 'Key2': 2020})

# Structure of Dictionary
# 1. Key: input associated with a value
#       (!) Keys must be primitive data / immutable sequence
# 2. Value: output of input
#       (!) Values can be any type of data


## Key
my_dictionary = {'key1': 1001, 'key2': '2nd', 'key3': [3, 4]}
print(my_dictionary['key1'])    # specify the value of 'key1'
print(my_dictionary['key2'])    # specify the value of 'key2'
print(my_dictionary['key3'])    # specify the value of 'key3'

# (!) KeyError exception will be raised when an invalid key is used


## Dictionary Expressions with Operators (in, not in)
print('key' in {'key': 1010})       # determines if a key exists in a dictionary (return: bool)
print('key' not in {'key': 1010})   # determines if a key does not exist in a dictionary (return: bool)


## Creating Dictionaries, Adding and Deleting Elements
my_dictionary = {}                  # creates an empty dictionary
my_dictionary['Key'] = 40           # adds new key-value pairs
del my_dictionary['Key']            # deletes a key-value pairs (KeyError exception is raised if key does not exist)


## Member Functions
x = {'key1': 1001, 'key2': '2nd', 'key3': [3, 4]}

# clear Function (Method)
x.clear()       # deletes all the elements (void)

# get Function (Method)
print({'key1': 1001, 'key2': '2nd'}.get('key1', 'no key found'))    # returns a value of 'key1' (arg1: key, arg2: value, return: value)

# pop Function (Method)
x = {'key1': 1001, 'key2': '2nd'}
print(x.pop('key1', 'no key found'))    # returns a value of 'key1' (arg1: key, arg2: value, return: value)
                                        # (!) used key-value pair will be removed from the dictionary

# keys Function (Method)
print({'key1': 1001, 'key2': '2nd'}.keys())     # returns a dictionary view of all keys (return: dictionary view)

# values Function (Method)
print({'key1': 1001, 'key2': '2nd'}.values())   # returns a dictionary view of all values (return: dictionary view)

# items Function (Method)
print({'key1': 1001, 'key2': '2nd'}.items())    # returns a dictionary view of a list of tuples contain a key and a value (return: dictionary view)

# popitem Function (Method)
x = {'key1': 1001, 'key2': '2nd'}
print(x.popitem())  # returns the last tuple in the list (return: tuple)
                    # (!) used key-value pair will be removed from the dictionary
                    # (!) KeyError Exception if we call it when it is empty