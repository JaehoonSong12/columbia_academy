def sumHeights2(heights: list[int], start: int, end: int) -> int:
    """
    Description:
        A variation on the sumHeights problem. We have an array of heights representing
        the altitude along a walking trail. Given start/end indexes into the array,
        return the sum of the changes for a walk beginning at the start index and ending
        at the end index, however increases in height count double.

    Examples:
        sumHeights2([5, 3, 6, 7, 2], 2, 4) → 7
        sumHeights2([5, 3, 6, 7, 2], 0, 1) → 2
        sumHeights2([5, 3, 6, 7, 2], 0, 4) → 15

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-ap/q17.py`

    Args:
        heights (list[int]): List of integer altitudes along the trail.
        start (int): Starting index of the walk.
        end (int): Ending index of the walk.

    Returns:
        int: The total sum of height changes, counting each upward change twice.
    """
    ### [Your Implementation Here]
    i = start
    abs_height_sum = 0
    while i < end:
        if heights[i + 1] - heights[i] > 0:
            abs_height_sum += 2 * (heights[i + 1] - heights[i])
        else:
            abs_height_sum += abs(heights[i] - heights[i + 1])
        i += 1
    return abs_height_sum
    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.

    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.


# Unit tests for sumHeights2 function
import unittest

class TestSumHeights2(unittest.TestCase):
    def test_sumHeights2(self):
        self.assertEqual(sumHeights2([5, 3, 6, 7, 2], 2, 4), 7)
        self.assertEqual(sumHeights2([5, 3, 6, 7, 2], 0, 1), 2)
        self.assertEqual(sumHeights2([5, 3, 6, 7, 2], 0, 4), 15)
        self.assertEqual(sumHeights2([5, 3, 6, 7, 2], 1, 1), 0)
        self.assertEqual(sumHeights2([1, 2, 3, 4, 5, 4, 3, 2, 10], 0, 3), 6)
        self.assertEqual(sumHeights2([1, 2, 3, 4, 5, 4, 3, 2, 10], 4, 8), 19)
        self.assertEqual(sumHeights2([1, 2, 3, 4, 5, 4, 3, 2, 10], 7, 8), 16)
        self.assertEqual(sumHeights2([1, 2, 3, 4, 5, 4, 3, 2, 10], 8, 8), 0)
        self.assertEqual(sumHeights2([1, 2, 3, 4, 5, 4, 3, 2, 10], 2, 2), 0)
        self.assertEqual(sumHeights2([1, 2, 3, 4, 5, 4, 3, 2, 10], 3, 6), 4)
        self.assertEqual(sumHeights2([10, 8, 7, 7, 7, 6, 7], 1, 4), 1)
        self.assertEqual(sumHeights2([10, 8, 7, 7, 7, 6, 7], 1, 5), 2)

if __name__ == "__main__":
    unittest.main()
