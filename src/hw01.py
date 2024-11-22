# hw01.py
"""
Homework01: Python Data-type and Functions for Input and Output Abstraction
- Understanding data-types while working with variables
- Understanding usage of abstraction for input (keyboard) and output (monitor)
- Understanding expressions and operator precedence
- Mastering string operations and print function formatting
- Exploring input abstraction and named constants
"""






# Part 1: Concetps, MCQ & FRQ
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














# Part 2: Output (Monitor)
def display_cat_message():
    """
    [IMPLEMENT_YOUR_ANSWER] Displays the text: The cat said "meow."

    Question:
        This function prints the phrase 'The cat said "meow."' to the console.

    Answer:
        
    """

# Part 3: Input (Keyboard)

# Part 4: Data Types

def main():
    """
    Runs test cases for the homework functions.
    """
    print("Running Tests...")

    # Part 3: Test cases
    print("\nDisplay Cat Message Test:")
    display_cat_message()  # Expected: The cat said "meow."

if __name__ == "__main__":
    main()