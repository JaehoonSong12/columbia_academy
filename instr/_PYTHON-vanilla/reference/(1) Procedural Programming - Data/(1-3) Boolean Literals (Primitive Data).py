## Boolean Literals
print(True)
print(False)


## Boolean Expressions with Relational Operators (numeric arguments)
print(2 > 3)        # Greater than              (retrun: bool)
print(2 < 3)        # Less than                 (retrun: bool)
print(2 >= 3)       # Greater than or equal to  (retrun: bool)
print(2 <= 3)       # Less than or equal to     (retrun: bool)
print(2 == 3)       # Equal to                  (retrun: bool)
print(2 != 3)       # Not equal to              (retrun: bool)


## Boolean Expressions with Relational Operators (string arguments)
print('Mary' > 'Mark')      # Greater than              (retrun: bool)
print('Mary' < 'Mark')      # Less than                 (retrun: bool)
print('Mary' >= 'Mark')     # Greater than or equal to  (retrun: bool)
print('Marker' <= 'Mark')   # Less than or equal to     (retrun: bool)
print('Marky' == 'Mark')    # Equal to                  (retrun: bool)
print('Mary' != 'Mark')     # Not equal to              (retrun: bool)

# String Comparisons Rule:
# 1. strings are compared character by character
# 2. compares the ASCII codes for the characters
# 3. if one is shorter, fill it with NULL characters so the length can be same


## Complex Boolean Expressions with Logical Operators (boolean arguments)
print(2 > 3 and 10 < 11)    # and   (return: bool)
print(2 > 3 or 10 < 11)     # or    (return: bool)
print(not (4 > 3))            # not   (return: bool)

# Short-Circuit Evaluation:
# 1. If the left side of and operator is false, the right side isn't checked
# 2. If the left side of or operator is true, the right side isn't checked
