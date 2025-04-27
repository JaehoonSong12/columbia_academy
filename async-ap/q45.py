def repeatSeparator(word: str, sep: str, count: int) -> str:
    """
    Description:
        Return a big string made of `count` occurrences of the given `word`, 
        separated by the given separator string `sep`.

    Examples:
        repeatSeparator("Word", "X", 3) → "WordXWordXWord"
        repeatSeparator("This", "And", 2) → "ThisAndThis"
        repeatSeparator("This", "And", 1) → "This"

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-ap/q45.py`

    Args:
        word (str): The word to repeat.
        sep   (str): The separator to place between words.
        count (int): The number of times to repeat `word`.

    Returns:
        str: The resulting string of repeated words separated by `sep`.
    """
    ### [Your Implementation Here]
    
    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.

    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.


# Unit tests for repeatSeparator function
import unittest

class TestRepeatSeparator(unittest.TestCase):
    def test_repeatSeparator(self):
        self.assertEqual(repeatSeparator("Word", "X", 3), "WordXWordXWord")
        self.assertEqual(repeatSeparator("This", "And", 2), "ThisAndThis")
        self.assertEqual(repeatSeparator("This", "And", 1), "This")
        self.assertEqual(repeatSeparator("Hi", "-n-", 2), "Hi-n-Hi")
        self.assertEqual(repeatSeparator("AAA", "", 1), "AAA")
        self.assertEqual(repeatSeparator("AAA", "", 0), "")
        self.assertEqual(repeatSeparator("A", "B", 5), "ABABABABA")
        self.assertEqual(repeatSeparator("abc", "XX", 3), "abcXXabcXXabc")
        self.assertEqual(repeatSeparator("abc", "XX", 2), "abcXXabc")
        self.assertEqual(repeatSeparator("abc", "XX", 1), "abc")
        self.assertEqual(repeatSeparator("XYZ", "a", 2), "XYZaXYZ")

if __name__ == "__main__":
    unittest.main()
