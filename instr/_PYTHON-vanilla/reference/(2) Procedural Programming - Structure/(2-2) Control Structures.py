## Sequence Structure
print('sentence 1')
print('sentence 2')
print('sentence 3')


## Decision Structure
if (True):                          # if statement (single alternative)
    print('Condition is true.')


if (False):                         # if-else statement (dual alternative)
    print('Condition is true.')
else:
    print('Condition is false.')


if (False):                         # if-elif-else statement (multiple alternative)
    print('option A')
elif (False):
    print('option B')
else:
    print('option C')


## Repetition Structure (loop)
var = 'y' # initialization
while (var == 'y'):                 # while Loop (condition-controlled, pretest)
    print ('repeat!')
    var = input('Enter "y" to repeat: ') # terminator


for target_var in [4, 2, 3]:        # for loop (count-controlled)
    print(target_var)


# Control Structures Rule:
# 1. Every control structures can be nested
# 2. Python interpreter uses the indentation for places the block begins and ends
