def scoresClump(scores: list[int]) -> bool:
    """
    Description:
        Given an array of scores sorted in increasing order, 
        return True if the array contains 
        3 adjacent scores that differ from each other by at 
        most 2. In other words, if any 
        consecutive triplet of scores has a maximum difference 
        (between the highest and lowest) 
        of 2 or less, the function returns True.

    Examples:
        scoresClump([3, 4, 5]) → True
        scoresClump([3, 4, 6]) → False
        scoresClump([1, 3, 5, 5]) → True

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-ap/q03.py`

    Args:
        scores (list[int]): A list of integer scores, sorted in increasing order.

    Returns:
        bool: True if there exists a triplet of adjacent scores with a max difference of 2 or less,
              otherwise False.
    """
    ### [Your Implementation Here]
    i = 0
    while i < len(scores) - 2:
        if scores[i] - scores[i + 2] <= 2 and scores[i] - scores[i + 2] >= -2:
            return True
        i += 1
    return False
    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.

    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.


# Unit tests for the scoresClump function
import unittest

class TestScoresClump(unittest.TestCase):
    def test_scoresClump(self):
        self.assertTrue(scoresClump([3, 4, 5]))           # → True
        self.assertFalse(scoresClump([3, 4, 6]))          # → False
        self.assertTrue(scoresClump([1, 3, 5, 5]))         # → True
        self.assertTrue(scoresClump([2, 4, 5, 6]))         # → True
        self.assertFalse(scoresClump([2, 4, 5, 7]))         # → False
        self.assertTrue(scoresClump([2, 4, 4, 7]))         # → True
        self.assertFalse(scoresClump([3, 3, 6, 7, 9]))      # → False
        self.assertTrue(scoresClump([3, 3, 7, 7, 9]))       # → True
        self.assertFalse(scoresClump([4, 5, 8]))            # → False

if __name__ == "__main__":
    unittest.main()
