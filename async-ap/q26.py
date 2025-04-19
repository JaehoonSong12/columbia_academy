def centeredAverage(nums: list[int]) -> int:
    """
    Description:
        Return the "centered" average of a list of integers.
        The centered average is the mean of the values, excluding the smallest
        and largest values (ignoring only one copy of each).
        Use integer division for the result.
        The input list is guaranteed to have a length of 3 or more.

    Examples:
        centeredAverage([1, 2, 3, 4, 100]) → 3
        centeredAverage([1, 1, 5, 5, 10, 8, 7]) → 5
        centeredAverage([-10, -4, -2, -4, -2, 0]) → -3

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-ap/q26.py`

    Args:
        nums (list[int]): A list of integers with length 3 or more.

    Returns:
        int: The centered average of the list using integer division.
    """
    ### [Your Implementation Here]
    
    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.

    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.


# Unit tests for centeredAverage function
import unittest

class TestCenteredAverage(unittest.TestCase):
    def test_centeredAverage(self):
        self.assertEqual(centeredAverage([1, 2, 3, 4, 100]), 3)
        self.assertEqual(centeredAverage([1, 1, 5, 5, 10, 8, 7]), 5)
        self.assertEqual(centeredAverage([-10, -4, -2, -4, -2, 0]), -3)
        self.assertEqual(centeredAverage([5, 3, 4, 6, 2]), 4)
        self.assertEqual(centeredAverage([5, 3, 4, 0, 100]), 4)
        self.assertEqual(centeredAverage([100, 0, 5, 3, 4]), 4)
        self.assertEqual(centeredAverage([4, 0, 100]), 4)
        self.assertEqual(centeredAverage([0, 2, 3, 4, 100]), 3)
        self.assertEqual(centeredAverage([1, 1, 100]), 1)
        self.assertEqual(centeredAverage([7, 7, 7]), 7)
        self.assertEqual(centeredAverage([1, 7, 8]), 7)
        self.assertEqual(centeredAverage([1, 1, 99, 99]), 50)
        self.assertEqual(centeredAverage([1000, 0, 1, 99]), 50)
        self.assertEqual(centeredAverage([4, 4, 4, 4, 5]), 4)
        self.assertEqual(centeredAverage([4, 4, 4, 1, 5]), 4)
        self.assertEqual(centeredAverage([6, 4, 8, 12, 3]), 6)

if __name__ == "__main__":
    unittest.main()
