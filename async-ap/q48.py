def only14(nums: list[int]) -> bool:
    """
    Description:
        Given a list of integers, return True if every element is either a 1 or a 4.
        An empty list counts as True since there are no disallowed elements.

    Examples:
        only14([1, 4, 1, 4]) → True
        only14([1, 4, 2, 4]) → False
        only14([1, 1]) → True

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-ap/q48.py`

    Args:
        nums (list[int]): The list of integers to check.

    Returns:
        bool: True if every element is 1 or 4, False otherwise.
    """
    ### [Your Implementation Here]
    
    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.

    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.


# Unit tests for only14 function
import unittest

class TestOnly14(unittest.TestCase):
    def test_only14(self):
        self.assertTrue(only14([1, 4, 1, 4]))
        self.assertFalse(only14([1, 4, 2, 4]))
        self.assertTrue(only14([1, 1]))
        self.assertTrue(only14([4, 1]))
        self.assertFalse(only14([2]))
        self.assertTrue(only14([]))
        self.assertFalse(only14([1, 4, 1, 3]))
        self.assertFalse(only14([3, 1, 3]))
        self.assertTrue(only14([1]))
        self.assertTrue(only14([4]))
        self.assertFalse(only14([3, 4]))
        self.assertFalse(only14([1, 3, 4]))
        self.assertTrue(only14([1, 1, 1]))
        self.assertFalse(only14([1, 1, 1, 5]))
        self.assertTrue(only14([4, 1, 4, 1]))

if __name__ == "__main__":
    unittest.main()
