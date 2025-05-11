def isEverywhere(nums: list[int], val: int) -> bool:
    """
    Description:
        We'll say that a value is "everywhere" in a list if for every pair of adjacent elements
        in the list, at least one of the pair is that value. Return True if the given value is
        everywhere in the list. An empty list or a single-element list trivially satisfies this.

    Examples:
        isEverywhere([1, 2, 1, 3], 1) → True
        isEverywhere([1, 2, 1, 3], 2) → False
        isEverywhere([1, 2, 1, 3, 4], 1) → False

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-ap/q54.py`

    Args:
        nums (list[int]): The list of integers to check.
        val (int): The value to verify is "everywhere".

    Returns:
        bool: True if `val` is everywhere in `nums`, False otherwise.
    """
    ### [Your Implementation Here]
    
    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.

    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.


# Unit tests for isEverywhere function
import unittest

class TestIsEverywhere(unittest.TestCase):
    def test_isEverywhere(self):
        self.assertTrue(isEverywhere([1, 2, 1, 3], 1))
        self.assertFalse(isEverywhere([1, 2, 1, 3], 2))
        self.assertFalse(isEverywhere([1, 2, 1, 3, 4], 1))
        self.assertTrue(isEverywhere([2, 1, 2, 1], 1))
        self.assertTrue(isEverywhere([2, 1, 2, 1], 2))
        self.assertFalse(isEverywhere([2, 1, 2, 3, 1], 2))
        self.assertTrue(isEverywhere([3, 1], 3))
        self.assertFalse(isEverywhere([3, 1], 2))
        self.assertTrue(isEverywhere([3], 1))
        self.assertTrue(isEverywhere([], 1))
        self.assertTrue(isEverywhere([1, 2, 1, 2, 3, 2, 5], 2))
        self.assertFalse(isEverywhere([1, 2, 1, 1, 1, 2], 2))
        self.assertFalse(isEverywhere([2, 1, 2, 1, 1, 2], 2))
        self.assertFalse(isEverywhere([2, 1, 2, 2, 2, 1, 1, 2], 2))
        self.assertTrue(isEverywhere([2, 1, 2, 2, 2, 1, 2, 1], 2))
        self.assertTrue(isEverywhere([2, 1, 2, 1, 2], 2))

if __name__ == "__main__":
    unittest.main()
