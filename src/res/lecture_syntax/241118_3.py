print("========================================= python operations")


print("========================================= integer division")
print(5.0 / 2)


## `//` integer division 
# expected to get integer quotient without the remainder
print(5 // 2) # operands are 2 int -> 1 int
# 5 / 2 = 2 R 1
print(5.0 // 2.0) # operands are 2 float -> 1 float
print(5.0 // 2) # operands are 1 float, 1 int -> 1 float

## `%` remainder operation
print(100 % 2)
print(99 % 2)



print(5**2)



# exception of reading code. When you have `operations` you 
# are not always following the code from left-top to the bottom-right
print(5 + 2 * 4) # smilar order of operations in math

# c lang, everything looks like function call.
# recursive calling <- technically enable you to read something from right to left.
# print((5).plus((2).times(4)))


print((5 + 2) * 4)





print('One', end='End of your String!') # change end of line character
print('Two', end='End of your String!') # change end of line character
print('Three', end='End of your String!') # change end of line character


print('I\'m gangstar')



# This program demonstrates how a floating-point
# number can be rounded.
amount_due = 5000.0
monthly_payment = amount_due / 12.0
print(f'The monthly payment is {monthly_payment:.2f}.')
