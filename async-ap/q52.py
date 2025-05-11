def canBalance(nums: list[int]) -> bool:
    """
    Description:
        Given a non-empty list of integers, return True if there is a place to split the list
        so that the sum of the numbers on one side is equal to the sum of the numbers on the other side.

    Examples:
        canBalance([1, 1, 1, 2, 1]) → True   # split after third 1: sum([1,1,1]) == sum([2,1])
        canBalance([2, 1, 1, 2, 1]) → False
        canBalance([10, 10]) → True
        canBalance([10, 0, 1, -1, 10]) → True
        canBalance([1, 1, 1, 1, 4]) → True
        canBalance([2, 1, 1, 1, 4]) → False
        canBalance([2, 3, 4, 1, 2]) → False
        canBalance([1, 2, 3, 1, 0, 2, 3]) → True
        canBalance([1, 2, 3, 1, 0, 1, 3]) → False
        canBalance([1]) → False

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-ap/q52.py`

    Args:
        nums (list[int]): A non-empty list of integers.

    Returns:
        bool: True if there exists an index where the sum of the elements to the left
              equals the sum of the elements to the right.
    """
    ### [Your Implementation Here]
    
    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.

    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.


# Unit tests for canBalance function
import unittest

class TestCanBalance(unittest.TestCase):
    def test_canBalance(self):
        self.assertTrue(canBalance([1, 1, 1, 2, 1]))
        self.assertFalse(canBalance([2, 1, 1, 2, 1]))
        self.assertTrue(canBalance([10, 10]))
        self.assertTrue(canBalance([10, 0, 1, -1, 10]))
        self.assertTrue(canBalance([1, 1, 1, 1, 4]))
        self.assertFalse(canBalance([2, 1, 1, 1, 4]))
        self.assertFalse(canBalance([2, 3, 4, 1, 2]))
        self.assertTrue(canBalance([1, 2, 3, 1, 0, 2, 3]))
        self.assertFalse(canBalance([1, 2, 3, 1, 0, 1, 3]))
        self.assertFalse(canBalance([1]))

if __name__ == "__main__":
    unittest.main()
