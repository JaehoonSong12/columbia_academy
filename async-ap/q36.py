def fix34(nums: list[int]) -> list[int]:
    """
    Description:
        Return a list containing exactly the same numbers as the given list, 
        but rearranged so that every 3 
        is immediately followed by a 4. Do not move the 3's themselves, but 
        every other number may move (specifically, may be swaped).
        You may assume:
          - The list contains the same number of 3's and 4's.
          - Every 3 has a non-3 immediately after it.
          - No 4 appears before the first 3.

    Examples:
        fix34([1, 3, 1, 4]) → [1, 3, 4, 1]
        fix34([1, 3, 1, 4, 4, 3, 1]) → [1, 3, 4, 1, 1, 3, 4]
        fix34([3, 2, 2, 4]) → [3, 4, 2, 2]
        fix34([3, 2, 3, 2, 4, 4]) → [3, 4, 3, 4, 2, 2]

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-ap/q36.py`

    Args:
        nums (list[int]): The input list of integers containing matching numbers of 3's and 4's.

    Returns:
        list[int]: A new list where each 3 is immediately followed by a 4.
    """
    ### [Your Implementation Here]
    
    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.

    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.


# Unit tests for fix34 function
import unittest

class TestFix34(unittest.TestCase):
    def test_fix34(self):
        self.assertEqual(fix34([1, 3, 1, 4]), [1, 3, 4, 1])
        self.assertEqual(fix34([1, 3, 1, 4, 4, 3, 1]), [1, 3, 4, 1, 1, 3, 4])
        self.assertEqual(fix34([3, 2, 2, 4]), [3, 4, 2, 2])
        self.assertEqual(fix34([3, 2, 3, 2, 4, 4]), [3, 4, 3, 4, 2, 2])
        self.assertEqual(fix34([2, 3, 2, 3, 2, 4, 4]), [2, 3, 4, 3, 4, 2, 2])
        self.assertEqual(fix34([5, 3, 5, 4, 5, 4, 5, 4, 3, 5, 3, 5]), 
                         [5, 3, 4, 5, 5, 5, 5, 5, 3, 4, 3, 4])
        self.assertEqual(fix34([3, 1, 4]), [3, 4, 1])
        self.assertEqual(fix34([3, 4, 1]), [3, 4, 1])
        self.assertEqual(fix34([1, 1, 1]), [1, 1, 1])
        self.assertEqual(fix34([1]), [1])
        self.assertEqual(fix34([]), [])
        self.assertEqual(fix34([7, 3, 7, 7, 4]), [7, 3, 4, 7, 7])
        self.assertEqual(fix34([3, 1, 4, 3, 1, 4]), [3, 4, 1, 3, 4, 1])
        self.assertEqual(fix34([3, 1, 1, 3, 4, 4]), [3, 4, 1, 3, 4, 1])

if __name__ == "__main__":
    unittest.main()
