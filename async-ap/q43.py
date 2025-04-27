def equalIsNot(s: str) -> bool:
    """
    Description:
        Given a string, return True if the number of appearances 
        of "is" anywhere in the string
        is equal to the number of appearances of "not" anywhere in 
        the string. The match is case-sensitive.

    Examples:
        equalIsNot("This is not") → False
        equalIsNot("This is notnot") → True
        equalIsNot("noisxxnotyynotxisi") → True

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-ap/q43.py`

    Args:
        s (str): The input string to examine.

    Returns:
        bool: True if count of "is" equals count of "not", otherwise False.
    """
    ### [Your Implementation Here]
    
    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.

    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.


# Unit tests for equalIsNot function
import unittest

class TestEqualIsNot(unittest.TestCase):
    def test_equalIsNot(self):
        self.assertFalse(equalIsNot("This is not"))
        self.assertTrue(equalIsNot("This is notnot"))
        self.assertTrue(equalIsNot("noisxxnotyynotxisi"))
        self.assertFalse(equalIsNot("noisxxnotyynotxsi"))
        self.assertTrue(equalIsNot("xxxyyyzzzintint"))
        self.assertTrue(equalIsNot(""))
        self.assertTrue(equalIsNot("isisnotnot"))
        self.assertFalse(equalIsNot("isisnotno7Not"))
        self.assertFalse(equalIsNot("isnotis"))
        self.assertFalse(equalIsNot("mis3notpotbotis"))

if __name__ == "__main__":
    unittest.main()
