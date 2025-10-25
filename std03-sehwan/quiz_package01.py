#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Instructions to run the tests via the CLI:
    1. Open your terminal or command prompt.
    2. Run the tests by executing: `python std03-sehwan/quiz_package01.py`

It contains two functions:
1.  wordsFront: Returns the first 'n' strings from a list.
2.  wordsWithoutList: Returns a list with strings of a specific length removed.

"""
# Import the unittest module, needed for creating test cases.
# We only need to import it once at the top of the file.
import unittest

# Import List from the typing module for type hinting (e.g., List[str])
# This is preferred for compatibility with Python versions < 3.10
from typing import List



















# -----------------------------------------------------------------
# Question 5: wordsCount
# -----------------------------------------------------------------
def wordsCount(words: list[str], length: int) -> int:
    """
    Description:
        Given an array of strings, return the count of the 
        number of strings that have the given length.

    Examples:
        wordsCount(["a", "bb", "b", "ccc"], 1) → 2
        wordsCount(["a", "bb", "b", "ccc"], 3) → 1
        wordsCount(["a", "bb", "b", "ccc"], 4) → 0

    Args:
        words (list[str]): A list of words (strings).
        length (int): The length of the strings to count.

    Returns:
        int: The number of strings that have the given length.
    """
    ### [Your Implementation Here]
    count = 0
    for word in words:
        if len(word) == length: 
            count = count + 1
    return count

    # https://www.w3schools.com/python/python_strings.asp



    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.
    return 0
    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.




# -----------------------------------------------------------------
# Question 6: wordsFront
# -----------------------------------------------------------------

def wordsFront(words: List[str], n: int) -> List[str]:
    """
    Description:
        Given an array of strings, return a new array containing the first N strings.
        N will be in the range 1..length of the input array.

    Examples:
        wordsFront(["a", "b", "c", "d"], 1) -> ["a"]
        wordsFront(["a", "b", "c", "d"], 2) -> ["a", "b"]
        wordsFront(["a", "b", "c", "d"], 3) -> ["a", "b", "c"]

    Args:
        words (List[str]): A list of strings.
        n (int): The number of strings to return from the start of the list.

    Returns:
        List[str]: A list containing the first N strings from the input array.
    """
    
    ### [Your Implementation Here]
    selectedlist=[]
    count = 0
    for word in words:
        selectedlist.append(word)
        count = count + 1
        if(count == n): break
    return selectedlist

    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.
    return None
    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.


# -----------------------------------------------------------------
# Question 7: wordsWithoutList
# -----------------------------------------------------------------
def wordsWithoutList(words: List[str], length: int) -> List[str]:
    """
    Description:
        Given an array of strings, return a new list where all the 
        strings of the given length are omitted.

    Examples:
        wordsWithoutList(["a", "bb", "b", "ccc"], 1) -> ["bb", "ccc"]
        wordsWithoutList(["a", "bb", "b", "ccc"], 3) -> ["a", "bb", "b"]
        wordsWithoutList(["a", "bb", "b", "ccc"], 4) -> ["a", "bb", "b", "ccc"]

    Args:
        words (List[str]): A list of strings.
        length (int): The length of the strings to omit from the list.

    Returns:
        List[str]: A new list with all strings of the given length omitted.
    """
    ### [Your Implementation Here]
    
    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.
    return None
    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.




# -----------------------------------------------------------------
# Question 8: hasOne
# -----------------------------------------------------------------
def hasOne(n: int) -> bool:
    """
    Description:
        Given a positive integer n, return true if it contains a digit '1'. 
        Note: Use % to get the rightmost digit, and / to discard the rightmost digit.

    Examples:
        hasOne(10) → True
        hasOne(22) → False
        hasOne(220) → False

    Args:
        n (int): A positive integer.

    Returns:
        bool: True if the number contains at least one digit '1', False otherwise.
    """
    ### [Your Implementation Here]
    
    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.
    return False
    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.






































# -----------------------------------------------------------------
# Unit Tests
# -----------------------------------------------------------------
class TestWordsCount(unittest.TestCase):
    def test_wordsCount(self):
        self.assertEqual(wordsCount(["a", "bb", "b", "ccc"], 1), 2)
        self.assertEqual(wordsCount(["a", "bb", "b", "ccc"], 3), 1)
        self.assertEqual(wordsCount(["a", "bb", "b", "ccc"], 4), 0)
        self.assertEqual(wordsCount(["xx", "yyy", "x", "yy", "z"], 1), 2)
        self.assertEqual(wordsCount(["xx", "yyy", "x", "yy", "z"], 2), 2)
        self.assertEqual(wordsCount(["xx", "yyy", "x", "yy", "z"], 3), 1)

class TestWordsFront(unittest.TestCase):
    """
    Unit tests for the wordsFront function.
    """
    def test_wordsFront(self):
        # This single test method runs multiple assertions for wordsFront
        self.assertEqual(wordsFront(["a", "b", "c", "d"], 1), ["a"])
        self.assertEqual(wordsFront(["a", "b", "c", "d"], 2), ["a", "b"])
        self.assertEqual(wordsFront(["a", "b", "c", "d"], 3), ["a", "b", "c"])
        self.assertEqual(wordsFront(["a", "b", "c", "d"], 4), ["a", "b", "c", "d"])
        self.assertEqual(wordsFront(["Hi", "There"], 1), ["Hi"])
        self.assertEqual(wordsFront(["Hi", "There"], 2), ["Hi", "There"])

class TestWordsWithoutList(unittest.TestCase):
    """
    Unit tests for the wordsWithoutList function.
    """
    def test_wordsWithoutList(self):
        # This single test method runs multiple assertions for wordsWithoutList
        self.assertEqual(wordsWithoutList(["a", "bb", "b", "ccc"], 1), ["bb", "ccc"])
        self.assertEqual(wordsWithoutList(["a", "bb", "b", "ccc"], 3), ["a", "bb", "b"])
        self.assertEqual(wordsWithoutList(["a", "bb", "b", "ccc"], 4), ["a", "bb", "b", "ccc"])
        self.assertEqual(wordsWithoutList(["xx", "yyy", "x", "yy", "z"], 1), ["xx", "yyy", "yy"])
        self.assertEqual(wordsWithoutList(["xx", "yyy", "x", "yy", "z"], 2), ["yyy", "x", "z"])


class TestHasOne(unittest.TestCase):
    def test_hasOne(self):
        self.assertTrue(hasOne(10))
        self.assertFalse(hasOne(22))
        self.assertFalse(hasOne(220))
        self.assertTrue(hasOne(212))
        self.assertTrue(hasOne(1))
        self.assertFalse(hasOne(9))
        self.assertTrue(hasOne(211112))
        self.assertTrue(hasOne(121121))
        self.assertFalse(hasOne(222222))
        self.assertTrue(hasOne(56156))
        self.assertFalse(hasOne(56556))


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