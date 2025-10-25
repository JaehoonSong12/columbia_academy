#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Instructions to run the tests via the CLI:
    1. Open your terminal or command prompt.
    2. Run the tests by executing: `python ap_quiz_package02.py`

This is a list of quiz questions for practice, including:

"""
# Import the unittest module, needed for creating test cases.
# We only need to import it once at the top of the file.
import unittest

# Import List from the typing module for type hinting (e.g., List[str])
# This is preferred for compatibility with Python versions < 3.10
from typing import List

































# -----------------------------------------------------------------
# Question 1: copyEndy
# -----------------------------------------------------------------
def copyEndy(nums: list[int], count: int) -> list[int]:
    """
    Description:
        Given an array of positive integers, return a new list containing 
        the first `count` endy numbers from the original array.
        An integer is endy if it is in the range 0..10 or 90..100 (inclusive).

    Examples:
        copyEndy([9, 11, 90, 22, 6], 2) → [9, 90]
        copyEndy([9, 11, 90, 22, 6], 3) → [9, 90, 6]
        copyEndy([12, 1, 1, 13, 0, 20], 2) → [1, 1]

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python q11.py`
        
    Args:
        nums (list[int]): The list of positive integers to check.
        count (int): The number of endy integers to return.
        
    Returns:
        list[int]: A list containing the first `count` endy integers.
    """
    ### [Your Implementation Here]
    return None
    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.

    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.




# -----------------------------------------------------------------
# Question 2: matchUp
# -----------------------------------------------------------------
def matchUp(a: list[str], b: list[str]) -> int:
    """
    Description:
        Given two arrays of strings of the same length, compare each 
        string in the first array to the corresponding string in the second array. 
        Count the number of times that the two strings are non-empty 
        and start with the same character.

    Examples:
        matchUp(["aa", "bb", "cc"], ["aaa", "xx", "bb"]) → 1
        matchUp(["aa", "bb", "cc"], ["aaa", "b", "bb"]) → 2
        matchUp(["aa", "bb", "cc"], ["", "", "ccc"]) → 1
        
    Args:
        a (list[str]): The first list of strings to compare.
        b (list[str]): The second list of strings to compare.

    Returns:
        int: The count of non-empty string pairs that start with the same character.
    """
    ### [Your Implementation Here]
    return 0
    
    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.
    
    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.



# -----------------------------------------------------------------
# Question 3: scoreUp
# -----------------------------------------------------------------
def scoreUp(key: list[str], answers: list[str]) -> int:
    """
    Description:
        Given two arrays of strings, the "key" array containing the 
        correct answers and the "answers" array containing the student's responses,
        calculate the score for the student. 
        A correct answer is worth +4 points, an incorrect answer is worth 
        -1 point, and a blank answer ("?") is worth 0 points.

    Examples:
        scoreUp(["a", "a", "b", "b"], ["a", "c", "b", "c"]) → 6
        scoreUp(["a", "a", "b", "b"], ["a", "a", "b", "c"]) → 11
        scoreUp(["a", "a", "b", "b"], ["a", "a", "b", "b"]) → 16
        
    Args:
        key (list[str]): The list of correct answers.
        answers (list[str]): The list of student's answers.

    Returns:
        int: The student's total score based on the comparison.
    """
    ### [Your Implementation Here]
    return 0
        


    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.
    
    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.




# -----------------------------------------------------------------
# Question 4: wordsWithout
# -----------------------------------------------------------------
def wordsWithout(words: list[str], target: str) -> list[str]:
    """
    Description:
        Given an array of strings, return a new list without 
        the strings that are equal to the target string.
        The new list should contain all the strings from the 
        original list except the ones that match the target string.

    Examples:
        wordsWithout(["a", "b", "c", "a"], "a") → ["b", "c"]
        wordsWithout(["a", "b", "c", "a"], "b") → ["a", "c", "a"]
        wordsWithout(["a", "b", "c", "a"], "c") → ["a", "b", "a"]

    Args:
        words (list[str]): The list of words to filter.
        target (str): The target word to remove from the list.
        
    Returns:
        list[str]: A new list containing all words except those that are equal to the target string.
    """
    ### [Your Implementation Here]
    return None

    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.

    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.


















# -----------------------------------------------------------------
# Unit Tests
# -----------------------------------------------------------------
class TestCopyEndy(unittest.TestCase):
    def test_copyEndy(self):
        self.assertEqual(copyEndy([9, 11, 90, 22, 6], 2), [9, 90])
        self.assertEqual(copyEndy([9, 11, 90, 22, 6], 3), [9, 90, 6])
        self.assertEqual(copyEndy([12, 1, 1, 13, 0, 20], 2), [1, 1])
        self.assertEqual(copyEndy([12, 1, 1, 13, 0, 20], 3), [1, 1, 0])
        self.assertEqual(copyEndy([0], 1), [0])
        self.assertEqual(copyEndy([10, 11, 90], 2), [10, 90])
        self.assertEqual(copyEndy([90, 22, 100], 2), [90, 100])
        self.assertEqual(copyEndy([12, 11, 10, 89, 101, 4], 1), [10])
        self.assertEqual(copyEndy([13, 2, 2, 0], 2), [2, 2])
        self.assertEqual(copyEndy([13, 2, 2, 0], 3), [2, 2, 0])
        self.assertEqual(copyEndy([13, 2, 13, 2, 0, 30], 2), [2, 2])
        self.assertEqual(copyEndy([13, 2, 13, 2, 0, 30], 3), [2, 2, 0])


class TestMatchUp(unittest.TestCase):
    def test_matchUp(self):
        self.assertEqual(matchUp(["aa", "bb", "cc"], ["aaa", "xx", "bb"]), 1)
        self.assertEqual(matchUp(["aa", "bb", "cc"], ["aaa", "b", "bb"]), 2)
        self.assertEqual(matchUp(["aa", "bb", "cc"], ["", "", "ccc"]), 1)
        self.assertEqual(matchUp(["", "", "ccc"], ["aa", "bb", "cc"]), 1)
        self.assertEqual(matchUp(["", "", ""], ["", "bb", "cc"]), 0)
        self.assertEqual(matchUp(["aa", "bb", "cc"], ["", "", ""]), 0)
        self.assertEqual(matchUp(["aa", "", "ccc"], ["", "bb", "cc"]), 1)
        self.assertEqual(matchUp(["x", "y", "z"], ["y", "z", "x"]), 0)
        self.assertEqual(matchUp(["", "y", "z"], ["", "y", "x"]), 1)
        self.assertEqual(matchUp(["x", "y", "z"], ["xx", "yyy", "zzz"]), 3)
        self.assertEqual(matchUp(["x", "y", "z"], ["xx", "yyy", ""]), 2)
        self.assertEqual(matchUp(["b", "x", "y", "z"], ["a", "xx", "yyy", "zzz"]), 3)
        self.assertEqual(matchUp(["aaa", "bb", "c"], ["aaa", "xx", "bb"]), 1)


class TestScoreUp(unittest.TestCase):
    def test_scoreUp(self):
        self.assertEqual(scoreUp(["a", "a", "b", "b"], ["a", "c", "b", "c"]), 6)
        self.assertEqual(scoreUp(["a", "a", "b", "b"], ["a", "a", "b", "c"]), 11)
        self.assertEqual(scoreUp(["a", "a", "b", "b"], ["a", "a", "b", "b"]), 16)
        self.assertEqual(scoreUp(["a", "a", "b", "b"], ["?", "c", "b", "?"]), 3)
        self.assertEqual(scoreUp(["a", "a", "b", "b"], ["?", "c", "?", "?"]), -1)
        self.assertEqual(scoreUp(["a", "a", "b", "b"], ["c", "?", "b", "b"]), 7)
        self.assertEqual(scoreUp(["a", "a", "b", "b"], ["c", "?", "b", "?"]), 3)
        self.assertEqual(scoreUp(["a", "b", "c"], ["a", "c", "b"]), 2)
        self.assertEqual(scoreUp(["a", "a", "b", "b", "c", "c"], ["a", "c", "a", "c", "a", "c"]), 4)
        self.assertEqual(scoreUp(["a", "a", "b", "b", "c", "c"], ["a", "c", "?", "?", "a", "c"]), 6)
        self.assertEqual(scoreUp(["a", "a", "b", "b", "c", "c"], ["a", "c", "?", "?", "c", "c"]), 11)
        self.assertEqual(scoreUp(["a", "b", "c"], ["a", "b", "c"]), 12)

class TestWordsWithout(unittest.TestCase):
    def test_wordsWithout(self):
        self.assertEqual(wordsWithout(["a", "b", "c", "a"], "a"), ["b", "c"])
        self.assertEqual(wordsWithout(["a", "b", "c", "a"], "b"), ["a", "c", "a"])
        self.assertEqual(wordsWithout(["a", "b", "c", "a"], "c"), ["a", "b", "a"])
        self.assertEqual(wordsWithout(["b", "c", "a", "a"], "b"), ["c", "a", "a"])
        self.assertEqual(wordsWithout(["xx", "yyy", "x", "yy", "x"], "x"), ["xx", "yyy", "yy"])
        self.assertEqual(wordsWithout(["xx", "yyy", "x", "yy", "x"], "yy"), ["xx", "yyy", "x", "x"])
        self.assertEqual(wordsWithout(["aa", "ab", "ac", "aa"], "aa"), ["ab", "ac"])




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