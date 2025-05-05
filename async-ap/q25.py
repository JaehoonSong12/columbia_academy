def bigDiff(nums: list[int]) -> int:
    """
    Description:
        Given a list of integers with length 1 or more, return the difference
        between the largest and smallest values in the list.

    Examples:
        bigDiff([10, 3, 5, 6]) → 7
        bigDiff([7, 2, 10, 9]) → 8
        bigDiff([2, 10, 7, 2]) → 8

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-ap/q25.py`

    Args:
        nums (list[int]): A list of one or more integers.

    Returns:
        int: The difference between the maximum and minimum values in the list.
    """
    ### [Your Implementation Here]
    
    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.
    largest = nums[0]
    smallest = nums[0]
    for num in nums:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
    difference = largest - smallest
    return difference
    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.


# Unit tests for bigDiff function
import unittest

class TestBigDiff(unittest.TestCase):
    def test_bigDiff(self):
        self.assertEqual(bigDiff([10, 3, 5, 6]), 7)
        self.assertEqual(bigDiff([7, 2, 10, 9]), 8)
        self.assertEqual(bigDiff([2, 10, 7, 2]), 8)
        self.assertEqual(bigDiff([2, 10]), 8)
        self.assertEqual(bigDiff([10, 2]), 8)
        self.assertEqual(bigDiff([10, 0]), 10)
        self.assertEqual(bigDiff([2, 3]), 1)
        self.assertEqual(bigDiff([2, 2]), 0)
        self.assertEqual(bigDiff([2]), 0)
        self.assertEqual(bigDiff([5, 1, 6, 1, 9, 9]), 8)
        self.assertEqual(bigDiff([7, 6, 8, 5]), 3)
        self.assertEqual(bigDiff([7, 7, 6, 8, 5, 5, 6]), 3)

if __name__ == "__main__":
    unittest.main()
