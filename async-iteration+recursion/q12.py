def matchUp(a: list[str], b: list[str]) -> int:
    """
    Description:
        Given two arrays of strings of the same length, compare each 
        string in the first array to the corresponding string in the second array. 
        Count the number of times that the two strings are non-empty 
        and start with the same character.

    Examples:
        matchUp(["aa", "bb", "cc"], ["aaa", "xx", "bb"]) → 1
        matchUp(["aa", "bb", "cc"], ["aaa", "b", "bb"]) → 2
        matchUp(["aa", "bb", "cc"], ["", "", "ccc"]) → 1

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-iteration+recursion/q12.py`
        
    Args:
        a (list[str]): The first list of strings to compare.
        b (list[str]): The second list of strings to compare.

    Returns:
        int: The count of non-empty string pairs that start with the same character.
    """
    count = 0
    for str_a, str_b in zip(a, b):
        if str_a and str_b and str_a[0] == str_b[0]:
            count += 1
    return count


# Unit tests for matchUp function
import unittest

class TestMatchUp(unittest.TestCase):
    def test_matchUp(self):
        self.assertEqual(matchUp(["aa", "bb", "cc"], ["aaa", "xx", "bb"]), 1)
        self.assertEqual(matchUp(["aa", "bb", "cc"], ["aaa", "b", "bb"]), 2)
        self.assertEqual(matchUp(["aa", "bb", "cc"], ["", "", "ccc"]), 1)
        self.assertEqual(matchUp(["", "", "ccc"], ["aa", "bb", "cc"]), 1)
        self.assertEqual(matchUp(["", "", ""], ["", "bb", "cc"]), 0)
        self.assertEqual(matchUp(["aa", "bb", "cc"], ["", "", ""]), 0)
        self.assertEqual(matchUp(["aa", "", "ccc"], ["", "bb", "cc"]), 1)
        self.assertEqual(matchUp(["x", "y", "z"], ["y", "z", "x"]), 0)
        self.assertEqual(matchUp(["", "y", "z"], ["", "y", "x"]), 1)
        self.assertEqual(matchUp(["x", "y", "z"], ["xx", "yyy", "zzz"]), 3)
        self.assertEqual(matchUp(["x", "y", "z"], ["xx", "yyy", ""]), 2)
        self.assertEqual(matchUp(["b", "x", "y", "z"], ["a", "xx", "yyy", "zzz"]), 3)
        self.assertEqual(matchUp(["aaa", "bb", "c"], ["aaa", "xx", "bb"]), 1)

if __name__ == "__main__":
    unittest.main()
