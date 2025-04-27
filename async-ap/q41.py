def more14(nums: list[int]) -> bool:
    """
    Description:
        Given a list of integers, return True if the number of 1's in the list is greater than
        the number of 4's.

    Examples:
        more14([1, 4, 1]) → True
        more14([1, 4, 1, 4]) → False
        more14([1, 1]) → True
        more14([1, 6, 6]) → True

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-ap/q41.py`

    Args:
        nums (list[int]): The list of integers to examine.

    Returns:
        bool: True if count of 1's is greater than count of 4's, otherwise False.
    """
    ### [Your Implementation Here]
    
    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.

    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.


# Unit tests for more14 function
import unittest

class TestMore14(unittest.TestCase):
    def test_more14(self):
        self.assertTrue(more14([1, 4, 1]))
        self.assertFalse(more14([1, 4, 1, 4]))
        self.assertTrue(more14([1, 1]))
        self.assertTrue(more14([1, 6, 6]))
        self.assertTrue(more14([1]))
        self.assertFalse(more14([1, 4]))
        self.assertTrue(more14([6, 1, 1]))
        self.assertFalse(more14([1, 6, 4]))
        self.assertTrue(more14([1, 1, 4, 4, 1]))
        self.assertTrue(more14([1, 1, 6, 4, 4, 1]))
        self.assertFalse(more14([]))
        self.assertFalse(more14([4, 1, 4, 6]))
        self.assertFalse(more14([4, 1, 4, 6, 1]))
        self.assertTrue(more14([1, 4, 1, 4, 1, 6]))

if __name__ == "__main__":
    unittest.main()
