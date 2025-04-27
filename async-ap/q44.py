def fix45(nums: list[int]) -> list[int]:
    """
    Description:
        Return a list containing exactly the same numbers as the given list, but rearranged so that every 4
        is immediately followed by a 5. Do not move the 4's themselves, but every other number may move.
        You may assume:
          - The list contains the same number of 4's and 5's.
          - Every 4 has a non-4 immediately after it.
          - 5's may appear anywhere in the original list.

    Examples:
        fix45([5, 4, 9, 4, 9, 5]) → [9, 4, 5, 4, 5, 9]
        fix45([1, 4, 1, 5]) → [1, 4, 5, 1]
        fix45([1, 4, 1, 5, 5, 4, 1]) → [1, 4, 5, 1, 1, 4, 5]
        fix45([4, 2, 2, 5]) → [4, 5, 2, 2]

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-ap/q44.py`

    Args:
        nums (list[int]): The input list of integers containing matching numbers of 4's and 5's.

    Returns:
        list[int]: A new list where each 4 is immediately followed by a 5.
    """
    ### [Your Implementation Here]
    
    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.

    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.


# Unit tests for fix45 function
import unittest

class TestFix45(unittest.TestCase):
    def test_fix45(self):
        self.assertEqual(fix45([5, 4, 9, 4, 9, 5]), [9, 4, 5, 4, 5, 9])
        self.assertEqual(fix45([1, 4, 1, 5]), [1, 4, 5, 1])
        self.assertEqual(fix45([1, 4, 1, 5, 5, 4, 1]), [1, 4, 5, 1, 1, 4, 5])
        self.assertEqual(fix45([4, 9, 4, 9, 5, 5, 4, 9, 5]), [4, 5, 4, 5, 9, 9, 4, 5, 9])
        self.assertEqual(fix45([5, 5, 4, 1, 4, 1]), [1, 1, 4, 5, 4, 5])
        self.assertEqual(fix45([4, 2, 2, 5]), [4, 5, 2, 2])
        self.assertEqual(fix45([4, 2, 4, 2, 5, 5]), [4, 5, 4, 5, 2, 2])
        self.assertEqual(fix45([4, 2, 4, 5, 5]), [4, 5, 4, 5, 2])
        self.assertEqual(fix45([1, 1, 1]), [1, 1, 1])
        self.assertEqual(fix45([4, 5]), [4, 5])
        self.assertEqual(fix45([5, 4, 1]), [1, 4, 5])
        self.assertEqual(fix45([]), [])
        self.assertEqual(fix45([5, 4, 5, 4, 1]), [1, 4, 5, 4, 5])
        self.assertEqual(fix45([4, 5, 4, 1, 5]), [4, 5, 4, 5, 1])
        self.assertEqual(fix45([3, 4, 5]), [3, 4, 5])
        self.assertEqual(fix45([4, 1, 5]), [4, 5, 1])
        self.assertEqual(fix45([5, 4, 1]), [1, 4, 5])
        self.assertEqual(fix45([2, 4, 2, 5]), [2, 4, 5, 2])

if __name__ == "__main__":
    unittest.main()
