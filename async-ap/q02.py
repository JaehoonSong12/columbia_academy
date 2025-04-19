def scores100(scores: list[int]) -> bool:
    """
    Description:
        Given an array of scores, return True if there are scores 
        of 100 next to each other
        in the array. The array length will be at least 2.
    
    Examples:
        scores100([1, 100, 100]) → True
        scores100([1, 100, 99, 100]) → False
        scores100([100, 1, 100, 100]) → True

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-ap/q02.py`

    Args:
        scores (list[int]): A list of integer scores.

    Returns:
        bool: True if there is at least one occurrence of consecutive 100's, else False.
    """
    ### [Your Implementation Here]

    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.
    i = 0
    while i < len(scores) - 1:
        if scores[i] == 100:
            if scores[i + 1] == 100:
                return True
        i += 1
    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.


# Unit tests for the scores100 function
import unittest

class TestScores100(unittest.TestCase):
    def test_scores100(self):
        self.assertTrue(scores100([1, 100, 100]))           # → True
        self.assertFalse(scores100([1, 100, 99, 100]))        # → False
        self.assertTrue(scores100([100, 1, 100, 100]))        # → True
        self.assertFalse(scores100([100, 1, 100, 1]))         # → False
        self.assertFalse(scores100([1, 2, 3, 4, 5]))          # → False
        self.assertFalse(scores100([1, 2, 100, 4, 5]))        # → False

if __name__ == "__main__":
    unittest.main()
