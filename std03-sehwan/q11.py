def copyEndy(nums: list[int], count: int) -> list[int]:
    """
    Description:
        Given an array of positive integers, return a new list containing the first `count` endy numbers from the original array.
        An integer is endy if it is in the range 0..10 or 90..100 (inclusive).

    Examples:
        copyEndy([9, 11, 90, 22, 6], 2) → [9, 90]
        copyEndy([9, 11, 90, 22, 6], 3) → [9, 90, 6]
        copyEndy([12, 1, 1, 13, 0, 20], 2) → [1, 1]

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python q11.py`
        
    Args:
        nums (list[int]): The list of positive integers to check.
        count (int): The number of endy integers to return.
        
    Returns:
        list[int]: A list containing the first `count` endy integers.
    """
    ### [Your Implementation Here]
    return None
    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.

    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.


# Unit tests for copyEndy function
import unittest

class TestCopyEndy(unittest.TestCase):
    def test_copyEndy(self):
        self.assertEqual(copyEndy([9, 11, 90, 22, 6], 2), [9, 90])
        self.assertEqual(copyEndy([9, 11, 90, 22, 6], 3), [9, 90, 6])
        self.assertEqual(copyEndy([12, 1, 1, 13, 0, 20], 2), [1, 1])
        self.assertEqual(copyEndy([12, 1, 1, 13, 0, 20], 3), [1, 1, 0])
        self.assertEqual(copyEndy([0], 1), [0])
        self.assertEqual(copyEndy([10, 11, 90], 2), [10, 90])
        self.assertEqual(copyEndy([90, 22, 100], 2), [90, 100])
        self.assertEqual(copyEndy([12, 11, 10, 89, 101, 4], 1), [10])
        self.assertEqual(copyEndy([13, 2, 2, 0], 2), [2, 2])
        self.assertEqual(copyEndy([13, 2, 2, 0], 3), [2, 2, 0])
        self.assertEqual(copyEndy([13, 2, 13, 2, 0, 30], 2), [2, 2])
        self.assertEqual(copyEndy([13, 2, 13, 2, 0, 30], 3), [2, 2, 0])

if __name__ == "__main__":
    unittest.main()
