## Numeric Literals
print(2)        # data type: int
print(4.3)      # data type: float


## Numeric Expressions with Operators
print(2.4 + 4)  # Addition returns the sum
print(8.2 - 5)  # Subtraction returns the difference
print(8 * 5)    # Multiplication returns the product
print(100 / 4)  # Division returns the quotient (return: float)
print(-8 // 5)  # Division returns the integer part (return: int)
print(9.4 % 5)  # Remainder returns the remainder
print(2**4)     # Exponent returns the power

# Operator Precedence:
# (!) Parentheses are the first
# 1. Exponent
# 2. Multiplication, Division, and Remainder
# 3. Addition and Subtraction


## Mixed-Type Expressions
print(-8 // 5)      # Two int values, the result will be an int
print(-8.6 // 5.0)  # Two float values, the result will be an float
print(-8.2 // 5)    # int and float values, the int will be considered as a float, the result will be an float