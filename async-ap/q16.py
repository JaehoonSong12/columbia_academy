def sumHeights(heights: list[int], start: int, end: int) -> int:
    """
    Description:
        We have an array of heights, representing the altitude along a walking trail.
        Given start/end indexes into the array, return the sum of the changes for a walk
        beginning at the start index and ending at the end index. For example, with the
        heights [5, 3, 6, 7, 2] and start=2, end=4 yields a sum of 1 + 5 = 6.
        The start and end indices will both be valid with start <= end.

    Examples:
        sumHeights([5, 3, 6, 7, 2], 2, 4) → 6
        sumHeights([5, 3, 6, 7, 2], 0, 1) → 2
        sumHeights([5, 3, 6, 7, 2], 0, 4) → 11

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-ap/q16.py`

    Args:
        heights (list[int]): List of integer altitudes along the trail.
        start (int): Starting index of the walk.
        end (int): Ending index of the walk.

    Returns:
        int: The total sum of absolute height changes from start to end.
    """
    ### [Your Implementation Here]
    
    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.

    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.


# Unit tests for sumHeights function
import unittest

class TestSumHeights(unittest.TestCase):
    def test_sumHeights(self):
        self.assertEqual(sumHeights([5, 3, 6, 7, 2], 2, 4), 6)
        self.assertEqual(sumHeights([5, 3, 6, 7, 2], 0, 1), 2)
        self.assertEqual(sumHeights([5, 3, 6, 7, 2], 0, 4), 11)
        self.assertEqual(sumHeights([5, 3, 6, 7, 2], 1, 1), 0)
        self.assertEqual(sumHeights([1, 2, 3, 4, 5, 4, 3, 2, 10], 0, 3), 3)

if __name__ == "__main__":
    unittest.main()
