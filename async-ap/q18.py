def bigHeights(heights: list[int], start: int, end: int) -> int:
    """
    Description:
        A variation on the sumHeights problem. We have an array of heights representing
        the altitude along a walking trail. Given start/end indexes into the array,
        return the number of "big" steps for a walk beginning at the start index and
        ending at the end index. A step is "big" if the change is 5 or more up or down.

    Examples:
        bigHeights([5, 3, 6, 7, 2], 2, 4) → 1
        bigHeights([5, 3, 6, 7, 2], 0, 1) → 0
        bigHeights([5, 3, 6, 7, 2], 0, 4) → 1
        bigHeights([5, 3, 6, 7, 3], 0, 4) → 0

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-ap/q18.py`

    Args:
        heights (list[int]): The list of integer altitudes along the trail.
        start (int): The starting index of the walk (inclusive).
        end (int): The ending index of the walk (inclusive).

    Returns:
        int: The count of "big" steps (difference ≥ 5) between start and end.
    """
    ### [Your Implementation Here]
    i = start
    count = 0
    while i < end:
        if abs(heights[i] - heights[i + 1]) >= 5:
            count += 1
        i += 1
    return count
    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.

    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.


# Unit tests for bigHeights function
import unittest

class TestBigHeights(unittest.TestCase):
    def test_bigHeights(self):
        self.assertEqual(bigHeights([5, 3, 6, 7, 2], 2, 4), 1)
        self.assertEqual(bigHeights([5, 3, 6, 7, 2], 0, 1), 0)
        self.assertEqual(bigHeights([5, 3, 6, 7, 2], 0, 4), 1)
        self.assertEqual(bigHeights([5, 3, 6, 7, 3], 0, 4), 0)
        self.assertEqual(bigHeights([5, 3, 6, 7, 2], 1, 1), 0)
        self.assertEqual(bigHeights([5, 13, 6, 7, 2], 1, 2), 1)
        self.assertEqual(bigHeights([5, 13, 6, 7, 2], 0, 2), 2)
        self.assertEqual(bigHeights([5, 13, 6, 7, 2], 1, 4), 2)
        self.assertEqual(bigHeights([5, 13, 6, 7, 2], 0, 4), 3)
        self.assertEqual(bigHeights([5, 13, 6, 7, 2], 0, 3), 2)
        self.assertEqual(bigHeights([1, 2, 3, 4, 5, 4, 3, 2, 10], 0, 3), 0)
        self.assertEqual(bigHeights([1, 2, 3, 4, 5, 4, 3, 2, 10], 4, 8), 1)
        self.assertEqual(bigHeights([1, 2, 3, 14, 5, 4, 3, 2, 10], 0, 3), 1)
        self.assertEqual(bigHeights([1, 2, 3, 14, 5, 4, 3, 2, 10], 7, 8), 1)
        self.assertEqual(bigHeights([1, 2, 3, 14, 5, 4, 3, 2, 10], 3, 8), 2)
        self.assertEqual(bigHeights([1, 2, 3, 14, 5, 4, 3, 2, 10], 2, 8), 3)

if __name__ == "__main__":
    unittest.main()
