def xyzThere(s: str) -> bool:
    """
    Description:
        Return True if the given string contains an appearance of 
        "xyz" where the "xyz"
        is not directly preceded by a period ('.'). For example, 
        "xxyz" counts but "x.xyz" does not.

    Examples:
        xyzThere("abcxyz") → True
        xyzThere("abc.xyz") → False
        xyzThere("xyz.abc") → True

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-ap/q38.py`

    Args:
        s (str): The input string to check.

    Returns:
        bool: True if "xyz" appears not preceded by '.', otherwise False.
    """
    ### [Your Implementation Here]
    
    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.

    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.


# Unit tests for xyzThere function
import unittest

class TestXyzThere(unittest.TestCase):
    def test_xyzThere(self):
        self.assertTrue(xyzThere("abcxyz"))
        self.assertFalse(xyzThere("abc.xyz"))
        self.assertTrue(xyzThere("xyz.abc"))
        self.assertFalse(xyzThere("abcxy"))
        self.assertTrue(xyzThere("xyz"))
        self.assertFalse(xyzThere("xy"))
        self.assertFalse(xyzThere("x"))
        self.assertFalse(xyzThere(""))
        self.assertTrue(xyzThere("abc.xyzxyz"))
        self.assertTrue(xyzThere("abc.xxyz"))
        self.assertFalse(xyzThere(".xyz"))
        self.assertFalse(xyzThere("12.xyz"))
        self.assertTrue(xyzThere("12xyz"))
        self.assertFalse(xyzThere("1.xyz.xyz2.xyz"))

if __name__ == "__main__":
    unittest.main()
