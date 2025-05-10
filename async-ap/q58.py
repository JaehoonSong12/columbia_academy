def bobThere(s: str) -> bool:
    """
    Description:
        Return True if the given string contains a "bob" pattern—i.e. a 'b', then any character, then another 'b'.
        The middle character can be any char. Overlapping patterns count.

    Examples:
        bobThere("abcbob") → True    # "bob" at positions 3-5
        bobThere("b9b") → True       # "b9b"
        bobThere("bbb") → True       # first and third 'b'

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-ap/q58.py`

    Args:
        s (str): The input string to search.

    Returns:
        bool: True if any substring of the form 'b?b' appears, False otherwise.
    """
    ### [Your Implementation Here]
    
    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.

    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.


# Unit tests for bobThere function
import unittest

class TestBobThere(unittest.TestCase):
    def test_bobThere(self):
        self.assertTrue(bobThere("abcbob"))
        self.assertTrue(bobThere("b9b"))
        self.assertFalse(bobThere("bac"))
        self.assertTrue(bobThere("bbb"))
        self.assertFalse(bobThere("abcdefb"))
        self.assertTrue(bobThere("123abcbcdbabxyz"))
        self.assertFalse(bobThere("b12"))
        self.assertTrue(bobThere("b1b"))
        self.assertTrue(bobThere("b12b1b"))
        self.assertFalse(bobThere("bbc"))
        self.assertFalse(bobThere("bb"))
        self.assertFalse(bobThere("b"))

if __name__ == "__main__":
    unittest.main()
