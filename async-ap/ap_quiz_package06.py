#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Instructions to run the tests via the CLI:
    1. Open your terminal or command prompt.
    2. Run the tests by executing: `python async-ap/ap_quiz_package05.py`

This is a list of quiz questions for practice, including:
1.  more14: Check if the array contains more 1's than 4's.
"""

# Import the unittest module, needed for creating test cases.
# We only need to import it once at the top of the file.
import unittest

# Import List from the typing module for type hinting (e.g., List[str])
# This is preferred for compatibility with Python versions < 3.10
from typing import List

































# -----------------------------------------------------------------
# Question 1: countCode
# -----------------------------------------------------------------
def gHappy(s: str) -> bool:
    """
    Description:
        We'll say that a lowercase 'g' in a string is "happy" if there is another 'g'
        immediately to its left or right. Return True if all the 'g's in the given string
        are happy.

    Examples:
        gHappy("xxggxx") → True
        gHappy("xxgxx") → False
        gHappy("xxggyygxx") → False

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-ap/q51.py`

    Args:
        s (str): The input string.

    Returns:
        bool: True if every 'g' in the string is happy, False otherwise.
    """
    ### [Your Implementation Here]
    
    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.

    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.



def canBalance(nums: list[int]) -> bool:
    """
    Description:
        Given a non-empty list of integers, return True if there is a place to split the list
        so that the sum of the numbers on one side is equal to the sum of the numbers on the other side.

    Examples:
        canBalance([1, 1, 1, 2, 1]) → True   # split after third 1: sum([1,1,1]) == sum([2,1])
        canBalance([2, 1, 1, 2, 1]) → False
        canBalance([10, 10]) → True
        canBalance([10, 0, 1, -1, 10]) → True
        canBalance([1, 1, 1, 1, 4]) → True
        canBalance([2, 1, 1, 1, 4]) → False
        canBalance([2, 3, 4, 1, 2]) → False
        canBalance([1, 2, 3, 1, 0, 2, 3]) → True
        canBalance([1, 2, 3, 1, 0, 1, 3]) → False
        canBalance([1]) → False

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-ap/q52.py`

    Args:
        nums (list[int]): A non-empty list of integers.

    Returns:
        bool: True if there exists an index where the sum of the elements to the left
              equals the sum of the elements to the right.
    """
    ### [Your Implementation Here]
    
    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.

    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.





















# -----------------------------------------------------------------
# Unit Tests
# -----------------------------------------------------------------
class TestGHappy(unittest.TestCase):
    def test_gHappy(self):
        self.assertTrue(gHappy("xxggxx"))
        self.assertFalse(gHappy("xxgxx"))
        self.assertFalse(gHappy("xxggyygxx"))
        self.assertFalse(gHappy("g"))
        self.assertTrue(gHappy("gg"))
        self.assertTrue(gHappy(""))
        self.assertTrue(gHappy("xxgggxyz"))
        self.assertFalse(gHappy("xxgggxyg"))
        self.assertTrue(gHappy("xxgggxygg"))
        self.assertFalse(gHappy("mgm"))
        self.assertTrue(gHappy("mggm"))
        self.assertTrue(gHappy("yyygggxyy"))

class TestCanBalance(unittest.TestCase):
    def test_canBalance(self):
        self.assertTrue(canBalance([1, 1, 1, 2, 1]))
        self.assertFalse(canBalance([2, 1, 1, 2, 1]))
        self.assertTrue(canBalance([10, 10]))
        self.assertTrue(canBalance([10, 0, 1, -1, 10]))
        self.assertTrue(canBalance([1, 1, 1, 1, 4]))
        self.assertFalse(canBalance([2, 1, 1, 1, 4]))
        self.assertFalse(canBalance([2, 3, 4, 1, 2]))
        self.assertTrue(canBalance([1, 2, 3, 1, 0, 2, 3]))
        self.assertFalse(canBalance([1, 2, 3, 1, 0, 1, 3]))
        self.assertFalse(canBalance([1]))




# -----------------------------------------------------------------
# Main execution block
# -----------------------------------------------------------------

if __name__ == "__main__":
    """
    This conditional block checks if the script is being run directly.
    If it is, it calls `unittest.main()`.
    
    `unittest.main()` discovers all test cases (TestWordsFront
    and TestWordsWithoutList) and runs them.
    
    `verbosity=2` is added to provide a more detailed output,
    showing the result of each test method individually, which
    satisfies the requirement for clear results for each function.
    """
    unittest.main(verbosity=2)