# hw01.py
"""
Homework01: Python Data-type and Functions for Input and Output Abstraction
- Understanding data-types while working with variables
- Understanding usage of abstraction for input (keyboard) and output (monitor)
- Understanding expressions and operator precedence
- Mastering string operations and print function formatting
- Exploring input abstraction and named constants
"""






# Part 1: Concepts, MCQ & FRQ
""" Q1
Question:
    Is Python a case-sensitive programming language? 
    Say, are "temperature" and "Temperature" the same variables 
    (case-insensitive)? or two different variables (case-sensitive)?
    (a) Yes
    (b) No

Answer:
    [YOUR_ANSWER]
"""



""" Q2
Question:
    Which of the following are illegal variable names in Python, and why?
    - x
    - 99bottles
    - july2009
    - theSalesFigureForFiscalYear
    - r&d
    - grade_report

Answer:
    [YOUR_ANSWER]
"""



""" Q3
Question:
    Is the variable name Sales the same as sales? Why or why not?

Answer:
    [YOUR_ANSWER]
"""



""" Q4
Question:
    Is the following assignment statement valid or invalid? If it is invalid, why?

    72 = amount

Answer:
    [YOUR_ANSWER]
"""




""" Q5
Question:
    What will the following code display?

    val = 99
    print('The value is', 'val')

Answer:
    [YOUR_ANSWER]
"""




""" Q6
Question:
    2.15 Look at the following assignment statements:

    value1 = 99
    value2 = 45.9
    value3 = 7.0
    value4 = 7
    value5 = 'abc'

    After these statements execute, what is the Python data type of the values referenced by each variable?

Answer:
    [YOUR_ANSWER]
"""



""" Q7
Question:
    What will be displayed by the following program?

    my_value = 99
    my_value = 0
    print(my_value)

Answer:
    [YOUR_ANSWER]
"""




""" Q8
Question:
    Complete the following table by writing the value of each expression in the Value column:

    | Expression          | Value |
    |---------------------|-------|
    | 6 + 3 * 5           | [  ] |
    | 12 / 2 - 4          | [  ] |
    | 9 + 14 * 2 - 6      | [  ] |
    | (6 + 2) * 3         | [  ] |
    | 14 / (11 - 4)       | [  ] |
    | 9 + 12 * (8 - 3)    | [  ] |

Answer:
    [YOUR_ANSWER]
"""




""" Q9
Question:
    What value will be assigned to `result` after the following statement executes?

    result = 9 // 2

Answer:
    [YOUR_ANSWER]
"""




""" Q10
Question:
    What value will be assigned to `result` after the following statement executes?

    result = 9 % 2

Answer:
    [YOUR_ANSWER]
"""




""" Q11
Question:
    What is string concatenation?

Answer:
    [YOUR_ANSWER]
"""




""" Q12
Question:
    After the following statement executes, what value will be assigned to the `result` variable?

    result = '1' + '2'

Answer:
    [YOUR_ANSWER]
"""




""" Q13
Question:
    After the following statement executes, what value will be assigned to the `result` variable?

    result = 'h' 'e' 'l' 'l' 'o'

Answer:
    [YOUR_ANSWER]
"""





""" Q14
Question:
    How do you suppress the print function's ending newline?

Answer:
    [YOUR_ANSWER]
"""




""" Q15
Question:
    How can you change the character that is automatically displayed between multiple items that are passed to the print function?

Answer:
    [YOUR_ANSWER]
"""




""" Q16
Question:
    What is the '\n' escape character?

Answer:
    [YOUR_ANSWER]
"""




""" Q17
Question:
    You need the user of a program to enter a customer's last name. Write a statement that prompts the user to enter this data and assigns the input to a variable.

Answer:
    [YOUR_CODE]
"""



""" Q18
Question:
    You need the user of a program to enter the amount of sales for the week. Write a statement that prompts the user to enter this data and assigns the input to a variable.

Answer:
    [YOUR_CODE]
"""



""" Q19
Question:
    What will the following code display?

    name = 'Karlie'
    print('Hello {name}')

Answer:
    [YOUR_ANSWER]
"""




""" Q20
Question:
    What will the following code display?

    name = 'Karlie'
    print(f'Hello {name}')

Answer:
    [YOUR_ANSWER]
"""





""" Q21
Question:
    What will the following code display?

    value = 99
    print(f'The value is {value + 1}')

Answer:
    [YOUR_ANSWER]
"""






""" Q22
Question:
    What will the following code display?

    value = 65.4321
    print(f'The value is {value:.2f}')

Answer:
    [YOUR_ANSWER]
"""




""" Q23
Question:
    What will the following code display?

    value = 987654.129
    print(f'The value is {value:,.2f}')

Answer:
    [YOUR_ANSWER]
"""





""" Q24
Question:
    What will the following code display?

    value = 9876543210
    print(f'The value is {value:,d}')

Answer:
    [YOUR_ANSWER]
"""



""" Q25
Question:
    What is the advantage of using named constants?

Answer:
    [YOUR_ANSWER]
"""





""" Q26
Question:
    Write a Python statement that defines a named constant for a 10 percent discount.

Answer:
    [YOUR_CODE]
"""






""" Q27
Question:
    A ________ error does not prevent the program from running, but causes it to produce incorrect results.
    a. syntax
    b. hardware
    c. logic
    d. fatal

Answer:
    [YOUR_ANSWER]
"""





""" Q28
Question:
    A ________ is a single function that the program must perform in order to satisfy the customer.
    a. task
    b. software requirement
    c. prerequisite
    d. predicate

Answer:
    [YOUR_ANSWER]
"""





""" Q29
Question:
    A(n) ________ is a set of well-defined logical steps that must be taken to perform a task.
    a. logarithm
    b. plan of action
    c. logic schedule
    d. algorithm

Answer:
    [YOUR_ANSWER]
"""



""" Q30
Question:
    A ________ is a sequence of characters.
    a. char sequence
    b. character collection
    c. string
    d. text block

Answer:
    [YOUR_ANSWER]
"""

""" Q31
Question:
    A ________ is a name that references a value in the computer's memory.
    a. variable
    b. register
    c. RAM slot
    d. byte

Answer:
    [YOUR_ANSWER]
"""

""" Q32
Question:
    A string literal in Python must be enclosed in ________.
    a. parentheses
    b. single-quotes
    c. double-quotes
    d. either single-quotes or double-quotes

Answer:
    [YOUR_ANSWER]
"""

""" Q33
Question:
    Short notes placed in different parts of a program explaining how those parts of the program work are called ________.
    a. comments
    b. reference manuals
    c. tutorials
    d. external documentation

Answer:
    [YOUR_ANSWER]
"""

""" Q34
Question:
    A(n) ________ makes a variable reference a value in the computer's memory.
    a. variable declaration
    b. assignment statement
    c. math expression
    d. string literal

Answer:
    [YOUR_ANSWER]
"""

""" Q35
Question:
    This symbol marks the beginning of a comment in Python.
    a. &
    b. *
    c. **
    d. #

Answer:
    d hi
"""

""" Q36
Question:
    Which of the following statements will cause an error?
    a. x = 17
    b. 17 = x
    c. x = 99999
    d. x = '17'

Answer:
    [YOUR_ANSWER]
"""

""" Q37
Question:
    In the expression 12 + 7, the values on the right and left of the + symbol are called ________.
    a. operands
    b. operators
    c. arguments
    d. math expressions

Answer:
    [YOUR_ANSWER]
"""

""" Q38
Question:
    This operator performs integer division.
    a. //
    b. %
    c. **
    d. /

Answer:
    [YOUR_ANSWER]
"""

""" Q39
Question:
    This is an operator that raises a number to a power.
    a. %
    b. *
    c. **
    d. /

Answer:
    [YOUR_ANSWER]
"""

""" Q40
Question:
    This operator performs division, but instead of returning the quotient it returns the remainder.
    a. %
    b. *
    c. **
    d. /

Answer:
    [YOUR_ANSWER]
"""

""" Q41
Question:
    Suppose the following statement is in a program: price = 99.0. After this statement executes, the price variable will reference a value of which data type?
    a. int
    b. float
    c. currency
    d. str

Answer:
    [YOUR_ANSWER]
"""

""" Q42
Question:
    Which built-in function can be used to read input that has been typed on the keyboard?
    a. input()
    b. get_input()
    c. read_input()
    d. keyboard()

Answer:
    [YOUR_ANSWER]
"""

""" Q43
Question:
    Which built-in function can be used to convert an int value to a float?
    a. int_to_float()
    b. float()
    c. convert()
    d. int()

Answer:
    [YOUR_ANSWER]
"""

""" Q44
Question:
    A magic number is ________.
    a. a number that is mathematically undefined
    b. an unexplained value that appears in a program's code
    c. a number that cannot be divided by 1
    d. a number that causes computers to crash

Answer:
    [YOUR_ANSWER]
"""

""" Q45
Question:
    A ________ is a name that represents a value that does not change during the program's execution.
    a. named literal
    b. named constant
    c. variable signature
    d. key term

Answer:
    [YOUR_ANSWER]
"""









# Part 2: Abstraction of Computer's IO System: Input (Keyboard), Output (Monitor)
def input_favorite_color():
    """
    Prompts the user to enter their favorite color and returns it.
    :return: The favorite color entered by the user.
    """
    # [YOUR_IMPLEMENTATION]
    return

def display_personal_info():
    """
    Prompts the user to enter their personal information and displays it.
    """
    # [YOUR_IMPLEMENTATION]
    return






# Part 3: Data Types and Operations
def assign_sum():
    """
    Assigns the sum of 10 and 14 to a variable named `total` and returns it.
    :return: The sum of 10 and 14.
    """
    # [YOUR_IMPLEMENTATION]
    return

def assign_sum_with_input():
    """
    Assigns the sum of two numbers to a variable named `total` and returns it.
    :return: The sum of two inputted numbers.
    """
    # [YOUR_IMPLEMENTATION]
    return

def calculate_due(total, down_payment):
    """
    Calculates the amount due by subtracting the down payment from the total.
    :param total: Total amount (float).
    :param down_payment: Down payment (float).
    :return: The due amount after subtraction.
    """
    # [YOUR_IMPLEMENTATION]
    return

def calculate_total_with_tax(subtotal):
    """
    Multiplies the subtotal by 0.15 (tax) and returns the total.
    :param subtotal: Subtotal amount (float).
    :return: Total amount after adding tax.
    """
    # [YOUR_IMPLEMENTATION]
    return


def convert_celsius_to_fahrenheit(celsius):
    """
    Converts a Celsius temperature to Fahrenheit.
    :param celsius: Temperature in Celsius (float).
    :return: Temperature in Fahrenheit.
    """
    # [YOUR_IMPLEMENTATION]
    return

def calculate_gender_percentages(males, females):
    """
    Calculates the percentage of males and females in a class.
    :param males: Number of males (int).
    :param females: Number of females (int).
    :return: A tuple containing percentages of males and females.
    """
    # [YOUR_IMPLEMENTATION]
    return

def calculate_grapevines(row_length, end_post_space, vine_space):
    """
    Calculates the number of grapevines that fit in a row.
    :param row_length: Length of the row in feet (float).
    :param end_post_space: Space used by an end-post assembly in feet (float).
    :param vine_space: Space between vines in feet (float).
    :return: Number of grapevines that fit in the row.
    """
    # [YOUR_IMPLEMENTATION]
    return

def calculate_compound_interest(principal, annual_rate, times_compounded, years):
    """
    Calculates the account balance after a specified number of years with compound interest.
    :param principal: Principal amount deposited (float).
    :param annual_rate: Annual interest rate as a decimal (float).
    :param times_compounded: Times interest is compounded per year (int).
    :param years: Number of years the interest is earned (float).
    :return: Total account balance after the specified years.
    """
    # [YOUR_IMPLEMENTATION]
    return

# Entry Point of Execution
def main():
    """
    Runs test cases (expected output with given input) for the homework functions.
    """
    print("Running Tests...")

    ############################################################################
    ################################## Part 2 ##################################
    ############################################################################
    # Part 2.1: Favorite Color Input
    color = input_favorite_color()
    print(f"Favorite Color: {color}")
    # Part 2.2: Display Personal Information
    display_personal_info()

    ############################################################################
    ################################## Part 3 ##################################
    ############################################################################
    # Part 3.1: Assign Sum
    total = assign_sum()
    print(f"Sum of 10 and 14: {total}")
    # Part 3.2: Assign Sum with User Prompt
    total = assign_sum_with_input()
    print(f"Sum of the two numbers you just input: {total}")
    # Part 3.3: Calculate Due
    due = calculate_due(total=24, down_payment=10)
    print(f"Amount Due: {due}")
    # Part 3.3: Calculate Total with Tax
    total_with_tax = calculate_total_with_tax(subtotal=100)
    print(f"Total with Tax: {total_with_tax}")
    # Part 3.4: Celsius to Fahrenheit
    fahrenheit = convert_celsius_to_fahrenheit(celsius=25)
    print(f"25°C in Fahrenheit: {fahrenheit}")
    # Part 3.5: Male and Female Percentages
    male_percentage, female_percentage = calculate_gender_percentages(males=8, females=12)
    print(f"Male Percentage: {male_percentage}%, Female Percentage: {female_percentage}%")
    # Part 3.6: Calculate Grapevines
    vines = calculate_grapevines(row_length=50, end_post_space=3, vine_space=2)
    print(f"Grapevines that fit in the row: {vines}")
    # Part 3.7: Compound Interest
    compound_amount = calculate_compound_interest(principal=1000, annual_rate=0.05, times_compounded=4, years=10)
    print(f"Compound Interest Total: {compound_amount}")

# Direct Execution
if __name__ == "__main__": # __name__: module name, __main__: executed module name
    main()