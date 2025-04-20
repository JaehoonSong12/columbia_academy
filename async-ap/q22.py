def doubleChar(s: str) -> str:
    """
    Description:
        Given a string, return a new string where for every character in the original,
        there are two characters in the result.

    Examples:
        doubleChar("The") → "TThhee"
        doubleChar("AAbb") → "AAAAbbbb"
        doubleChar("Hi-There") → "HHii--TThheerree"

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-ap/q22.py`

    Args:
        s (str): The input string.

    Returns:
        str: A string where each character from `s` is repeated twice.
    """
    ### [Your Implementation Here]
    
    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.

    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.


# Unit tests for doubleChar function
import unittest

class TestDoubleChar(unittest.TestCase):
    def test_doubleChar(self):
        self.assertEqual(doubleChar("The"), "TThhee")
        self.assertEqual(doubleChar("AAbb"), "AAAAbbbb")
        self.assertEqual(doubleChar("Hi-There"), "HHii--TThheerree")
        self.assertEqual(doubleChar("Word!"), "WWoorrdd!!")
        self.assertEqual(doubleChar("!!"), "!!!!")
        self.assertEqual(doubleChar(")"), "))")
        self.assertEqual(doubleChar("a"), "aa")
        self.assertEqual(doubleChar("."), "..")
        self.assertEqual(doubleChar("aa"), "aaaa")

if __name__ == "__main__":
    unittest.main()
