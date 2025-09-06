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

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python q14.py`
        
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


# Unit tests for wordsWithout function
import unittest

class TestWordsWithout(unittest.TestCase):
    def test_wordsWithout(self):
        self.assertEqual(wordsWithout(["a", "b", "c", "a"], "a"), ["b", "c"])
        self.assertEqual(wordsWithout(["a", "b", "c", "a"], "b"), ["a", "c", "a"])
        self.assertEqual(wordsWithout(["a", "b", "c", "a"], "c"), ["a", "b", "a"])
        self.assertEqual(wordsWithout(["b", "c", "a", "a"], "b"), ["c", "a", "a"])
        self.assertEqual(wordsWithout(["xx", "yyy", "x", "yy", "x"], "x"), ["xx", "yyy", "yy"])
        self.assertEqual(wordsWithout(["xx", "yyy", "x", "yy", "x"], "yy"), ["xx", "yyy", "x", "x"])
        self.assertEqual(wordsWithout(["aa", "ab", "ac", "aa"], "aa"), ["ab", "ac"])

if __name__ == "__main__":
    unittest.main()
