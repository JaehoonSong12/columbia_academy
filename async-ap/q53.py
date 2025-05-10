def no14(nums: list[int]) -> bool:
    """
    Description:
        Given a list of integers, return True if it contains no 1's or it contains no 4's (or both).
        In other words, it fails only if there is at least one 1 and at least one 4.

    Examples:
        no14([1, 2, 3]) → True   # has 1's but no 4's
        no14([1, 2, 3, 4]) → False  # has both 1 and 4
        no14([2, 3, 4]) → True   # has 4's but no 1's

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-ap/q53.py`

    Args:
        nums (list[int]): The list of integers to examine.

    Returns:
        bool: True if the list contains no 1's or no 4's, False otherwise.
    """
    ### [Your Implementation Here]
    
    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.

    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.


# Unit tests for no14 function
import unittest

class TestNo14(unittest.TestCase):
    def test_no14(self):
        self.assertTrue(no14([1, 2, 3]))
        self.assertFalse(no14([1, 2, 3, 4]))
        self.assertTrue(no14([2, 3, 4]))
        self.assertFalse(no14([1, 1, 4, 4]))
        self.assertTrue(no14([2, 2, 4, 4]))
        self.assertFalse(no14([2, 3, 4, 1]))
        self.assertTrue(no14([2,1,1]))
        self.assertFalse(no14([1, 4]))
        self.assertTrue(no14([2]))
        self.assertTrue(no14([2, 1]))
        self.assertTrue(no14([1]))
        self.assertTrue(no14([4]))
        self.assertTrue(no14([]))
        self.assertTrue(no14([1, 1, 1, 1]))
        self.assertFalse(no14([9, 4, 4, 1]))
        self.assertFalse(no14([4, 2, 3, 1]))
        self.assertTrue(no14([4, 2, 3, 5]))
        self.assertTrue(no14([4, 4, 2]))
        self.assertFalse(no14([1, 4, 4]))

if __name__ == "__main__":
    unittest.main()
