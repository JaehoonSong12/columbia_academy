def wordsFront(words: list[str], n: int) -> list[str]:
    """
    Description:
        Given an array of strings, return a new array containing the first N strings.
        N will be in the range 1..length of the input array.

    Examples:
        wordsFront(["a", "b", "c", "d"], 1) → ["a"]
        wordsFront(["a", "b", "c", "d"], 2) → ["a", "b"]
        wordsFront(["a", "b", "c", "d"], 3) → ["a", "b", "c"]

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-iteration+recursion/q06.py`

    Args:
        words (list[str]): A list of strings.
        n (int): The number of strings to return from the start of the list.

    Returns:
        list[str]: A list containing the first N strings from the input array.
    """
    return words[:n]


# Unit tests for wordsFront function
import unittest

class TestWordsFront(unittest.TestCase):
    def test_wordsFront(self):
        self.assertEqual(wordsFront(["a", "b", "c", "d"], 1), ["a"])
        self.assertEqual(wordsFront(["a", "b", "c", "d"], 2), ["a", "b"])
        self.assertEqual(wordsFront(["a", "b", "c", "d"], 3), ["a", "b", "c"])
        self.assertEqual(wordsFront(["a", "b", "c", "d"], 4), ["a", "b", "c", "d"])
        self.assertEqual(wordsFront(["Hi", "There"], 1), ["Hi"])
        self.assertEqual(wordsFront(["Hi", "There"], 2), ["Hi", "There"])

if __name__ == "__main__":
    unittest.main()
