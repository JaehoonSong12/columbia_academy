# hw00.py
"""
Homework: Python Variables, Functions, and Abstraction
- Working with variables
- Creating functions (APIs)
- Understanding abstraction
- Differentiating between syntax and semantics
"""










# Part 0: Good Practices
"""
Task 0.1: Avoid Hardcoding Values.
Define a function `calculate_square_root(number)` that returns the square root of the given number.
Do not hardcode the value inside the function. Call the function with different values.

Task 0.2: Use Meaningful Variable Names.
Ensure that all your variables in previous tasks use meaningful names.
Review your previous functions and rename variables if necessary.
"""
import math

def calculate_square_root(number):
    """
    Returns the square root of the given number.

    Arguments:
    number -- The number to calculate the square root of.

    Returns:
    The square root of `number`.
    """
    return math.sqrt(number)

print(calculate_square_root(16))  # Should print 4.0
print(calculate_square_root(25))  # Should print 5.0
















# Part 1: Working with Variables
"""
Task 1.1: Define a variable `myMessage` with the value 'Good coding practice!' and print it.
"""

"""
Task 1.2: Define two variables, `x = 10` and `y = 5`. 
Create a third variable `z` which is the sum of `x` and `y`, and print `z`.
"""

"""
Task 1.3: Define two variables `greeting = "Hello, "` and `name = "John"`.
Concatenate them and print the result: 'Hello, John'.
"""










# Part 2: Functions (APIs)
"""
Task 2.1: Writing a Novel: Use functions to avoid repetitive print statements.
Imagine you are writing a novel where a character keeps saying the same line over and over. 
Instead of repeatedly writing the same line in the code, we can use a function to simplify and 
abstract away the repetition. This is what API is.
"""
def repeat_line():
    """
    Prints a repetitive line to simulate the repetition in a novel.
    This function abstracts away the repetitive task of printing the same line multiple times.
    """

# Calling the function multiple times, simulating a repetitive part of a novel
repeat_line()  # Character says the same line once
repeat_line()  # Character repeats the line again
repeat_line()  # Character repeats the line one more time




"""
Task 2.2: Define a function `calculate_area(radius)` that calculates the area of a circle.
Use the formula `area = pi * radius^2` and return the result.
Use `math.pi` for the value of π. Call the function with a radius of 7 and print the result.
"""
import math

def calculate_area(radius):
    """
    Calculates the area of a circle given a radius.

    Arguments:
    radius -- The radius of the circle.

    Returns:
    The area of the circle.
    """

print(calculate_area(7))  # Print the area with radius 7