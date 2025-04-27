def countYZ(s: str) -> int:
    """
    Description:
        Given a string, count the number of words ending in 'y' or 'z'.
        The character must appear at the end of a word — that is, it must not be
        immediately followed by another alphabetic letter. The comparison is
        case-insensitive.

    Examples:
        countYZ("fez day") → 2
        countYZ("day fez") → 2
        countYZ("day fyyyz") → 2

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-ap/q28.py`

    Args:
        s (str): The input string.

    Returns:
        int: The number of words ending in 'y' or 'z'.
    """
    ### [Your Implementation Here]
    
    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.

    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.


# Unit tests for countYZ function
import unittest

class TestCountYZ(unittest.TestCase):
    def test_countYZ(self):
        self.assertEqual(countYZ("fez day"), 2)
        self.assertEqual(countYZ("day fez"), 2)
        self.assertEqual(countYZ("day fyyyz"), 2)
        self.assertEqual(countYZ("day yak"), 1)
        self.assertEqual(countYZ("day:yak"), 1)
        self.assertEqual(countYZ("!!day--yaz!!"), 2)
        self.assertEqual(countYZ("yak zak"), 0)
        self.assertEqual(countYZ("DAY abc XYZ"), 2)
        self.assertEqual(countYZ("aaz yyz my"), 3)
        self.assertEqual(countYZ("y2bz"), 2)
        self.assertEqual(countYZ("zxyx"), 0)

if __name__ == "__main__":
    unittest.main()
