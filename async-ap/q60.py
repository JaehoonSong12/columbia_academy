def countTriple(s: str) -> int:
    """
    Description:
        We'll say that a "triple" in a string is a char appearing three times in a row.
        Return the number of triples in the given string. Triples may overlap.

    Examples:
        countTriple("abcXXXabc") → 1
        countTriple("xxxabyyyycd") → 3
        countTriple("a") → 0

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-ap/q60.py`

    Args:
        s (str): The input string to examine for triples.

    Returns:
        int: The count of positions where a character appears three times in a row.
    """
    ### [Your Implementation Here]
    
    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.

    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.


# Unit tests for countTriple function
import unittest

class TestCountTriple(unittest.TestCase):
    def test_countTriple(self):
        self.assertEqual(countTriple("abcXXXabc"), 1)
        self.assertEqual(countTriple("xxxabyyyycd"), 3)
        self.assertEqual(countTriple("a"), 0)
        self.assertEqual(countTriple(""), 0)
        self.assertEqual(countTriple("XXXabc"), 1)
        self.assertEqual(countTriple("XXXXabc"), 2)
        self.assertEqual(countTriple("XXXXXabc"), 3)
        self.assertEqual(countTriple("222abyyycdXXX"), 3)
        self.assertEqual(countTriple("abYYYabXXXXXab"), 4)
        self.assertEqual(countTriple("abYYXabXXYXXab"), 0)
        self.assertEqual(countTriple("122abhhh2"), 1)

if __name__ == "__main__":
    unittest.main()
