def scoresSpecial(a: list[int], b: list[int]) -> int:
    """
    Description:
        Given two arrays of non-negative integer scores, a "special" 
        score is one which is a multiple of 10
        (e.g., 40 or 90). Return the sum of the largest special score 
        in array `a` plus the largest special
        score in array `b`.

    Examples:
        scoresSpecial([12, 10, 4], [2, 20, 30]) → 40
        scoresSpecial([20, 10, 4], [2, 20, 10]) → 40
        scoresSpecial([12, 11, 4], [2, 20, 31]) → 20
        scoresSpecial([1, 20, 2, 50], [3, 4, 5]) → 50
        scoresSpecial([10, 4, 20, 30], [30, 20, 99]) → 60

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-ap/q15.py`

    Args:
        a (list[int]): First list of non-negative scores.
        b (list[int]): Second list of non-negative scores.

    Returns:
        int: Sum of the largest multiple-of-10 in `a` and the largest multiple-of-10 in `b`.
    """
    def max_special(scores: list[int]) -> int:
        """
        Helper:
            Finds the largest "special" score (a multiple of 10) in the given list.
            Returns 0 if there are no multiples of 10.
        """
        return None
    ### [Your Implementation Here]
    
    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.

    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.
    return None


# Unit tests for scoresSpecial function
import unittest

class TestScoresSpecial(unittest.TestCase):
    def test_scoresSpecial(self):
        self.assertEqual(scoresSpecial([12, 10, 4], [2, 20, 30]), 40)
        self.assertEqual(scoresSpecial([20, 10, 4], [2, 20, 10]), 40)
        self.assertEqual(scoresSpecial([12, 11, 4], [2, 20, 31]), 20)
        self.assertEqual(scoresSpecial([1, 20, 2, 50], [3, 4, 5]), 50)
        self.assertEqual(scoresSpecial([3, 4, 5], [1, 50, 2, 20]), 50)
        self.assertEqual(scoresSpecial([10, 4, 20, 30], [20]), 50)
        self.assertEqual(scoresSpecial([10, 4, 20, 30], [3, 20, 99]), 50)
        self.assertEqual(scoresSpecial([10, 4, 20, 30], [30, 20, 99]), 60)
        self.assertEqual(scoresSpecial([], [2]), 0)
        self.assertEqual(scoresSpecial([], [20]), 20)
        self.assertEqual(scoresSpecial([14, 10, 4], [4, 20, 30]), 40)

if __name__ == "__main__":
    unittest.main()
    # Run the tests when the script is executed directly
    # This allows the tests to be run from the command line or an IDE.