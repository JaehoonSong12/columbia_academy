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
        2. Run the tests by executing: `python async-iteration+recursion/q05.py`

    Args:
        words (list[str]): A list of words (strings).
        length (int): The length of the strings to count.

    Returns:
        int: The number of strings that have the given length.
    """
    return sum(1 for word in words if len(word) == length)


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
