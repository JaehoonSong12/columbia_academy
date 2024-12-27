## Variable (created by assignment statements)
var_name = 3             # references any type of data or value (int)
print(var_name)

var_name = 4             # reassigned, and references a new type of data or value (int)
print(var_name)          # the previous data, 3, is removed (Garbage Collection)

var_name = 3.24          # reassigned, and references a new type of data or value (float)
print(var_name)          # the previous data, 4, is removed (Garbage Collection)

var_name = 'Hi, there'   # reassigned, and references a new type of data or value (str)
print(var_name)          # the previous data, 3.24, is removed (Garbage Collection)

var_name = True          # reassigned, and references a new type of data or value again (bool)
print(var_name)          # the previous data, 'Hi, there', is removed (Garbage Collection)

# Variable Naming Rule:
# 1. keywords cannot be used for variable naming
# 2. Spaces cannot be used for variable naming
# 3. A digit cannot be used in the first letter of variable
# 4. Variables are case-sensitive
