def wordsCount(words: list[str], length: int) -> int:
    """
    Description:
        Given an array of strings, return the count of the number of strings that have the given length.

    Examples:
        wordsCount(["a", "bb", "b", "ccc"], 1) → 2
        wordsCount(["a", "bb", "b", "ccc"], 3) → 1
        wordsCount(["a", "bb", "b", "ccc"], 4) → 0

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-ap/q05.py`

    Args:
        words (list[str]): A list of words (strings).
        length (int): The length of the strings to count.

    Returns:
        int: The number of strings that have the given length.
    """
    ### [Your Implementation Here]
    
    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.
    i = 0
    count = 0
    while i in range(len(words)):
        if len(words[i]) == length:
            count += 1
        i += 1
    return count
    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.


# Unit tests for wordsCount function
import unittest

class TestWordsCount(unittest.TestCase):
    def test_wordsCount(self):
        self.assertEqual(wordsCount(["a", "bb", "b", "ccc"], 1), 2)
        self.assertEqual(wordsCount(["a", "bb", "b", "ccc"], 3), 1)
        self.assertEqual(wordsCount(["a", "bb", "b", "ccc"], 4), 0)
        self.assertEqual(wordsCount(["xx", "yyy", "x", "yy", "z"], 1), 2)
        self.assertEqual(wordsCount(["xx", "yyy", "x", "yy", "z"], 2), 2)
        self.assertEqual(wordsCount(["xx", "yyy", "x", "yy", "z"], 3), 1)

if __name__ == "__main__":
    unittest.main()
