def has22(nums: list[int]) -> bool:
    """
    Description:
        Given a list of integers, return True if the list contains a 2 next to a 2 somewhere.

    Examples:
        has22([1, 2, 2]) → True
        has22([1, 2, 1, 2]) → False
        has22([2, 1, 2]) → False

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-ap/q33.py`

    Args:
        nums (list[int]): The list of integers to check.

    Returns:
        bool: True if there is at least one occurrence of two consecutive 2's, False otherwise.
    """
    ### [Your Implementation Here]
    i = 0
    while i < len(nums) - 1:
        if nums[i] == 2:
            if nums[i + 1] == 2:
                return True
        i += 1
    return False
    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.

    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.


# Unit tests for has22 function
import unittest

class TestHas22(unittest.TestCase):
    def test_has22(self):
        self.assertTrue(has22([1, 2, 2]))
        self.assertFalse(has22([1, 2, 1, 2]))
        self.assertFalse(has22([2, 1, 2]))
        self.assertTrue(has22([2, 2, 1, 2]))
        self.assertFalse(has22([1, 3, 2]))
        self.assertTrue(has22([1, 3, 2, 2]))
        self.assertTrue(has22([2, 3, 2, 2]))
        self.assertTrue(has22([4, 2, 4, 2, 2, 5]))
        self.assertFalse(has22([1, 2]))
        self.assertTrue(has22([2, 2]))
        self.assertFalse(has22([2]))
        self.assertFalse(has22([]))
        self.assertTrue(has22([3, 3, 2, 2]))
        self.assertFalse(has22([5, 2, 5, 2]))

if __name__ == "__main__":
    unittest.main()