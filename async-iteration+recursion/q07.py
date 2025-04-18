def wordsWithoutList(words: list[str], length: int) -> list[str]:
    """
    Description:
        Given an array of strings, return a new list where all the 
        strings of the given length are omitted.

    Examples:
        wordsWithoutList(["a", "bb", "b", "ccc"], 1) → ["bb", "ccc"]
        wordsWithoutList(["a", "bb", "b", "ccc"], 3) → ["a", "bb", "b"]
        wordsWithoutList(["a", "bb", "b", "ccc"], 4) → ["a", "bb", "b", "ccc"]

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-iteration+recursion/q07.py`

    Args:
        words (list[str]): A list of strings.
        length (int): The length of the strings to omit from the list.

    Returns:
        list[str]: A new list with all strings of the given length omitted.
    """
    return [word for word in words if len(word) != length]


# Unit tests for wordsWithoutList function
import unittest

class TestWordsWithoutList(unittest.TestCase):
    def test_wordsWithoutList(self):
        self.assertEqual(wordsWithoutList(["a", "bb", "b", "ccc"], 1), ["bb", "ccc"])
        self.assertEqual(wordsWithoutList(["a", "bb", "b", "ccc"], 3), ["a", "bb", "b"])
        self.assertEqual(wordsWithoutList(["a", "bb", "b", "ccc"], 4), ["a", "bb", "b", "ccc"])
        self.assertEqual(wordsWithoutList(["xx", "yyy", "x", "yy", "z"], 1), ["xx", "yyy", "yy"])
        self.assertEqual(wordsWithoutList(["xx", "yyy", "x", "yy", "z"], 2), ["yyy", "x", "z"])

if __name__ == "__main__":
    unittest.main()
