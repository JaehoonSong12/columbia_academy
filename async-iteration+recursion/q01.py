def scores_increasing(scores: list[int]) -> bool:
    """
    Description:
    Given a list of scores (integers), return True if the scores are 
    in non-decreasing order — that is, each score is equal to or 
    greater than the one before.

    Examples:
        scores_increasing([1, 3, 4]) → True
        scores_increasing([1, 3, 2]) → False
        scores_increasing([1, 1, 4]) → True

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-iteration+recursion/q02.py`

    Args:
        scores (list[int]): A list of integers, length 2 or more.

    Returns:
        bool: True if each score is equal or greater than the previous one.
    """
    ### [Your Implementation Here]

    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.

    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.
    return False


# Unit Tests
import unittest

class TestScoresIncreasing(unittest.TestCase):
    def test_examples(self):
        self.assertTrue(scores_increasing([1, 3, 4]))            # → True
        self.assertFalse(scores_increasing([1, 3, 2]))           # → False
        self.assertTrue(scores_increasing([1, 1, 4]))            # → True
        self.assertTrue(scores_increasing([1, 1, 2, 4, 4, 7]))   # → True
        self.assertFalse(scores_increasing([1, 1, 2, 4, 3, 7]))  # → False
        self.assertTrue(scores_increasing([-5, 4, 11]))          # → True


if __name__ == "__main__":
    unittest.main()
