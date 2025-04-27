def catDog(s: str) -> bool:
    """
    Description:
        Return True if the strings "cat" and "dog" appear the 
        same number of times in the given string.
        The comparison is case-sensitive and counts non-overlapping 
        occurrences.

    Examples:
        catDog("catdog") → True
        catDog("catcat") → False
        catDog("1cat1cadodog") → True

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-ap/q30.py`

    Args:
        s (str): The input string to examine.

    Returns:
        bool: True if "cat" and "dog" occur the same number of times, False otherwise.
    """
    ### [Your Implementation Here]
    
    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.

    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.


# Unit tests for catDog function
import unittest

class TestCatDog(unittest.TestCase):
    def test_catDog(self):
        self.assertTrue(catDog("catdog"))
        self.assertFalse(catDog("catcat"))
        self.assertTrue(catDog("1cat1cadodog"))
        self.assertFalse(catDog("catxxdogxxxdog"))
        self.assertTrue(catDog("catxdogxdogxcat"))
        self.assertFalse(catDog("catxdogxdogxca"))
        self.assertFalse(catDog("dogdogcat"))
        self.assertTrue(catDog("dogogcat"))
        self.assertFalse(catDog("dog"))
        self.assertFalse(catDog("cat"))
        self.assertTrue(catDog("ca"))
        self.assertTrue(catDog("c"))
        self.assertTrue(catDog(""))

if __name__ == "__main__":
    unittest.main()
