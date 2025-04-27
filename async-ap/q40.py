def sum28(nums: list[int]) -> bool:
    """
    Description:
        Given a list of integers, return True if the sum of all the 2's in the list is exactly 8.

    Examples:
        sum28([2, 3, 2, 2, 4, 2]) → True
        sum28([2, 3, 2, 2, 4, 2, 2]) → False
        sum28([1, 2, 3, 4]) → False
        sum28([2, 2, 2, 2]) → True
        sum28([1, 2, 2, 2, 2, 4]) → True

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-ap/q40.py`

    Args:
        nums (list[int]): The list of integers to examine.

    Returns:
        bool: True if the sum of all 2's is exactly 8, otherwise False.
    """
    ### [Your Implementation Here]
    
    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.

    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.


# Unit tests for sum28 function
import unittest

class TestSum28(unittest.TestCase):
    def test_sum28(self):
        self.assertTrue(sum28([2, 3, 2, 2, 4, 2]))
        self.assertFalse(sum28([2, 3, 2, 2, 4, 2, 2]))
        self.assertFalse(sum28([1, 2, 3, 4]))
        self.assertTrue(sum28([2, 2, 2, 2]))
        self.assertTrue(sum28([1, 2, 2, 2, 2, 4]))
        self.assertFalse(sum28([]))
        self.assertFalse(sum28([2]))
        self.assertFalse(sum28([8]))
        self.assertFalse(sum28([2, 2, 2]))
        self.assertFalse(sum28([2, 2, 2, 2, 2]))
        self.assertTrue(sum28([1, 2, 2, 1, 2, 2]))
        self.assertTrue(sum28([5, 2, 2, 2, 4, 2]))

if __name__ == "__main__":
    unittest.main()
