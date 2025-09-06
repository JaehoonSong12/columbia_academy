def copyEvens(nums: list[int], count: int) -> list[int]:
    """
    Description:
        Given an array of positive integers, return a new list containing 
        the first `count` even numbers from the original array.
        The original array will contain at least `count` even numbers.

    Examples:
        copyEvens([3, 2, 4, 5, 8], 2) → [2, 4]
        copyEvens([3, 2, 4, 5, 8], 3) → [2, 4, 8]
        copyEvens([6, 1, 2, 4, 5, 8], 3) → [6, 2, 4]

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python q10.py`

    Args:
        nums (list[int]): A list of positive integers.
        count (int): The number of even integers to return.

    Returns:
        list[int]: A list of the first `count` even integers from the original array.
    """
    ### [Your Implementation Here]
    
    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.
    return None

    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.


# Unit tests for copyEvens function
import unittest

class TestCopyEvens(unittest.TestCase):
    def test_copyEvens(self):
        self.assertEqual(copyEvens([3, 2, 4, 5, 8], 2), [2, 4])
        self.assertEqual(copyEvens([3, 2, 4, 5, 8], 3), [2, 4, 8])
        self.assertEqual(copyEvens([6, 1, 2, 4, 5, 8], 3), [6, 2, 4])
        self.assertEqual(copyEvens([6, 1, 2, 4, 5, 8], 4), [6, 2, 4, 8])
        self.assertEqual(copyEvens([3, 1, 4, 1, 5], 1), [4])
        self.assertEqual(copyEvens([2], 1), [2])
        self.assertEqual(copyEvens([6, 2, 4, 8], 2), [6, 2])
        self.assertEqual(copyEvens([6, 2, 4, 8], 3), [6, 2, 4])
        self.assertEqual(copyEvens([6, 2, 4, 8], 4), [6, 2, 4, 8])
        self.assertEqual(copyEvens([1, 8, 4], 1), [8])
        self.assertEqual(copyEvens([1, 8, 4], 2), [8, 4])
        self.assertEqual(copyEvens([2, 8, 4], 2), [2, 8])

if __name__ == "__main__":
    unittest.main()
