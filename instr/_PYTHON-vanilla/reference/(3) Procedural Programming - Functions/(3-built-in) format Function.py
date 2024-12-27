## format Function (float)
x = 230000 / 12
print(format(x, 'f'))       # up to 6 decimal points are available to display
print(format(x, '.2f'))     # returns a formatted number as a string
                            # (argument1: float, argument2: str, return: str)
print(format(x, ',.2f'))
print(format(x, '12,.2f'))

# format specifier Rule:
# 1. field width designator (digit)
# 2. comma separator (,)
# 3. precision designator (.digit)
# 4. type designator (f: float)


## format Function (percentage)
x = 5 / 12
print(format(x, '%'))       # up to 6 decimal points are available to display
print(format(x, '.0%'))     # returns a formatted number as a string
                            # (argument1: float, argument2: str, return: str)
print(format(x, '5.0%'))

# format specifier Rule:
# 1. field width designator (digit)
# 2. precision designator (.digit)
# 3. type designator (%: percentage)


## format Function (scientific)
x = 230 / 12
print(format(x, 'e'))       # up to 6 decimal points are available to display
print(format(x, '.2e'))     # returns a formatted number as a string
                            # (argument1: float, argument2: str, return: str)
print(format(x, '12.2e'))

# format specifier Rule:
# 1. field width designator (digit)
# 2. precision designator (.digit)
# 3. type designator (e: scientific)


## format Function (int)
x = 123456
print(format(x, 'd'))       # returns a formatted number as a string
                            # (argument1: int, argument2: str, return: str)
print(format(x, ',d'))
print(format(x, '10,d'))

# format specifier Rule:
# 1. field width designator (digit)
# 2. comma separator (,)
# 3. type designator (d: decimal integer)
