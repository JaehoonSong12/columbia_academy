def endOther(a: str, b: str) -> bool:
    """
    Description:
        Given two strings, return True if either of the strings appears at the very end
        of the other string, ignoring upper/lower case differences.

    Examples:
        endOther("Hiabc", "abc") → True
        endOther("AbC", "HiaBc") → True
        endOther("abc", "abXabc") → True

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-ap/q37.py`

    Args:
        a (str): First input string.
        b (str): Second input string.

    Returns:
    
        bool: True if one string appears at the end of the other (case-insensitive), else False.
    """
    ### [Your Implementation Here]
    
    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.

    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.


# Unit tests for endOther function
import unittest

class TestEndOther(unittest.TestCase):
    def test_endOther(self):
        self.assertTrue(endOther("Hiabc", "abc"))
        self.assertTrue(endOther("AbC", "HiaBc"))
        self.assertTrue(endOther("abc", "abXabc"))
        self.assertFalse(endOther("Hiabc", "abcd"))
        self.assertTrue(endOther("Hiabc", "bc"))
        self.assertFalse(endOther("Hiabcx", "bc"))
        self.assertTrue(endOther("abc", "abc"))
        self.assertTrue(endOther("xyz", "12xyz"))
        self.assertFalse(endOther("yz", "12xz"))
        self.assertTrue(endOther("Z", "12xz"))
        self.assertTrue(endOther("12", "12"))
        self.assertFalse(endOther("abcXYZ", "abcDEF"))
        self.assertFalse(endOther("ab", "ab12"))
        self.assertTrue(endOther("ab", "12ab"))

if __name__ == "__main__":
    unittest.main()
