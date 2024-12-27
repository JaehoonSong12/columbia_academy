## Strings (immutable)
print('String')


## Index
my_string = 'ABC'
print(my_string[-3])    # specify the first character
print(my_string[-2])    # specify the second character
print(my_string[-1])    # specify the third character
print(my_string[0])     # specify the first character
print(my_string[1])     # specify the second character
print(my_string[2])     # specify the third character

# Negative Index Rule:
# 1. Python interpreter adds negative indexes to the length of the string to determine the position
# 2. IndexError exception will be raised when an invalid index is used


## String Slicing (Substrings)
string_1 = 'abcdefghij'
print(string_1[2:4])        # returns a substring, index on [2, 4)
print(string_1[0:4:2])      # returns a substring, index on [0, 4) with a step value, 2
print(string_1[:3])         # (!) default starting index is 0
print(string_1[1:])         # (!) default ending index is len(string_1)
print(string_1[-5:100])     # (!) no IndexError exceptions raised due to default values


## String Expressions with Operators (concatenation, repetition, in, not in)
print('Hello ' + 'World')           # returns an appended string (return: str)
print('w' * 5)                      # returns a new string of multipe copies (return: list)
print('seven' in 'seven years')     # determines if one string is contained in another string (return: bool)
print('seven' not in 'seven years') # determines if one string is contained in another string (return: bool)


## Member Functions

# conversion - split Function (Method)
print('1 2 3'.split())              # returns a list separated by spaces (return: list)
print('4/5/6'.split('/'))           # returns a list separated by the argument (arg: str, return: list)

# test - isalpha Function (Method)
print('abc'.isalpha())              # returns True if the string only has alphabetic letters (return: bool)

# test - isdigit Function (Method)
print('23'.isdigit())               # returns True if the string only has numeric digits (return: bool)

# test - isspace Function (Method)
print(' '.isspace())                # returns True if the string only has whitespace characters (return: bool)

# test - isalnum Function (Method)
print('2a'.isalnum())               # returns True if the string only has alphabetic letters or numeric digits (return: bool)

# test - islower Function (Method)
print('ab'.islower())               # returns True if the string only has alphabetic letters in lowercase (return: bool)

# test - isupper Function (Method)
print('AB'.isupper())               # returns True if the string only has alphabetic letters in uppercase (return: bool)

# modification - lower Function (Method)
print('ABC'.lower())                # returns a copy of the string in lowercase (return: str)

# modification - upper Function (Method)
print('abc'.upper())                    # returns a copy of the string in uppercase (return: str)

# modification - lstrip Function (Method)
print('\n  white spaces'.lstrip())      # returns a copy of the string without all leading whitespaces (return: str)
print('\n\n white spaces'.lstrip('\n')) # returns a copy of the string without all the argument at the beginning (arg: str, return: str)

# modification - rstrip Function (Method)
print('\tHello World\t'.rstrip())                   # returns a copy of the string without all trailing whitespaces (return: str)
print('\tHello World\t'.rstrip(' World\t'))         # returns a copy of the string without all the argument at the end (arg: str, return: str)

# modification - strip Function (Method)
print('\tHello World\t'.strip())                    # returns a copy of the string without all leading and trailing whitespaces (return: str)
print('\tHello World\t'.strip('H'))                 # returns a copy of the string without all the argument at the beginning and at the end (arg: str, return: str)

# search - startswith Function (Method)
print('Here is a string'.startswith('Here'))     # returns True if the string starts with the argument (arg: str, return: bool)

# search - endswith Function (Method)
print('Here is a string'.endswith('string'))     # returns True if the string ends with the argument (arg: str, return: bool)

# search - find Function (Method)
print('Here is a string'.find('is'))             # returns the lowest index of the argument found in the string (arg: str, return: int)

# replace - replace Function (Method)
print('Here is a string'.replace('is','is not')) # returns a copy of the string with all the instances of 'is' replaced by 'is not' (arg1: str, arg2: str, return: str)