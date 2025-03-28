def array11(nums: list, index: int) -> int:
    """
    Description:
        Given an array of ints, compute recursively the number of times that the value 11 appears in the array.
        The function considers only the part of the array that begins at the given index.
        A recursive call moves forward by passing index+1.

    Examples:
        array11([1, 2, 11], 0) → 1
        array11([11, 11], 0) → 2
        array11([1, 2, 3, 4], 0) → 0

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-recursion/q16.py`

    Args:
        nums (list): The input list of integers.
        index (int): The current index to check.

    Returns:
        int: The number of times 11 appears in the array.
    """
    # Base case: your implementation and comment here.

    # Recursive case: your implementation and comment here.


# Unit tests for the array11 function
import unittest

class TestArray11Function(unittest.TestCase):
    def test_array11(self):
        self.assertEqual(array11([1, 2, 11], 0), 1)    # array11([1,2,11], 0) → 1
        self.assertEqual(array11([11, 11], 0), 2)      # array11([11,11], 0) → 2
        self.assertEqual(array11([1, 2, 3, 4], 0), 0)  # array11([1,2,3,4], 0) → 0
        self.assertEqual(array11([1, 11, 3, 11, 11], 0), 3)  # array11([1,11,3,11,11], 0) → 3
        self.assertEqual(array11([11], 0), 1)          # array11([11], 0) → 1
        self.assertEqual(array11([1], 0), 0)          # array11([1], 0) → 0
        self.assertEqual(array11([], 0), 0)          # array11([], 0) → 0
        self.assertEqual(array11([11, 2, 3, 4, 11, 5], 0), 2)  # array11([11,2,3,4,11,5], 0) → 2
        self.assertEqual(array11([11, 5, 11], 0), 2)  # array11([11,5,11], 0) → 2

if __name__ == '__main__':
    unittest.main()
