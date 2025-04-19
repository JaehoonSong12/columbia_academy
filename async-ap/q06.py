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
        2. Run the tests by executing: `python async-ap/q06.py`

    Args:
        words (list[str]): A list of strings.
        n (int): The number of strings to return from the start of the list.

    Returns:
        list[str]: A list containing the first N strings from the input array.
    """
    ### [Your Implementation Here]
    
    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.
    i = 0
    new_list = []
    while i < n:
        new_list.append(words[i])
        i += 1
    return new_list
    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.


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
