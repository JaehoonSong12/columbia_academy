### Extra curiculurr
# runtime complexity: time you consume with certain # of inputs.





    # 1. sequential actions



"""
Function Name: dominosTime()
Parameters: N/A
Returns: None
"""
def dominosTime():
    # flag, Boolean (True / False), 1-bit
    flag = input("Do you really wanna do this? ('no' if you don't want)")
    flag = (flag.lower() == "no") # relational operator, tells us if an equation is true or false (solutions)
    # early return: it decides if the user wants to really do the following actions.
    if (flag): return


    pizza_amount = input("How many pizzas do you want?") # '23'
    pasta_amount = input("How many orders of pasta do you want?") # '3'
    chicken_wings_amount = input("How many orders of chicken wings do you want?") # '10'
    pizza_pay = int(pizza_amount) * 12
    pasta_pay = int(pasta_amount) * 6
    chicken_wings_pay = int(chicken_wings_amount) * 8
    total_price = int(pizza_pay) + int(pasta_pay) + int(chicken_wings_pay)
    print(f"By ordering {pizza_amount} pizzas, {pasta_amount} orders of pasta, and {chicken_wings_amount} orders of chicken wings, your order total comes to {total_price}.")
    return


def getSquareRoot(number_to_square_root): # parameter (local variable, initialized by function calls outside.)
    # flag like operation, false validation.
    flag = number_to_square_root < 0 # relational operator (comparision-purposed operators return T/F)
    # early return (if statement)
    if (flag == True): return -1 # negative input, not great
    import math
    return math.sqrt(number_to_square_root)


def getSquareRoot2(number_to_square_root): # parameter (local variable, initialized by function calls outside.)
    # flag like operation, true validation.
    flag = number_to_square_root >= 0 # relational operator (comparision-purposed operators return T/F)
    # if-else statement
    if (flag == True): 
        import math
        return math.sqrt(number_to_square_root)
    else:
        return -1 # negative input, not great

number = getSquareRoot(-3)
print(number)
number = getSquareRoot(5)
print(number)


epsilon = 0.001
if (abs(2.2340 - getSquareRoot(5)) < epsilon): print("the number is acceptable")
else: print("the number is not acceptable")
# if statement syntax
# if (<bool>): 
#     noremal statement 1
#     noremal statement 2
#     noremal statement 3
#     ....


name1 = 'Mary'
name2 = 'Mark'
if name1 == name2:
    print('The names are the same.') # skipped
else:
    print('The names are NOT the same.') # executed


# dominosTime()


    # 2. conditional actions
        # if it is late, you sleep.
        # else you don't sleep.
        # if you don't like eating soup, you skip (break)


# Input: Student's percentage score
score = float(input("Enter the student's score: "))

# Decide the grade using if-else statements
if score >= 90: grade = 'A'
if score >= 80: grade = 'B'
if score >= 70: grade = 'C'
if score >= 60: grade = 'D'
else: grade = 'F'

# Output: Display the grade
print(f"The student's grade is: {grade}")


## boolean operation
# truth table
# Short-Circuit Evaluation: if you don't need to read the rest of the part,
# you quit what you are doing now, decide the result immediately.
# this will help runtime improvement.

# False and True

# 3. iteration, repetitional actions.
# for each table
#     1. get the order
#     2. bring dishes to table
#     3. ask anything else to do
#     4. get tipped