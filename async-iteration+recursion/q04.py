def scoresAverage(scores: list[int]) -> int:
    """
    Description:
        Given an array of scores, compute the integer average 
        of the first half and the second half,
        and return whichever is larger. The second half begins 
        at index len(scores)//2.
        You must use a helper function that computes the average 
        of the values between two indices.

    Examples:
        scoresAverage([2, 2, 4, 4]) → 4
        scoresAverage([4, 4, 4, 2, 2, 2]) → 4
        scoresAverage([3, 4, 5, 1, 2, 3]) → 4

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-iteration+recursion/q04.py`

    Args:
        scores (list[int]): A list of scores (at least 2 elements long).

    Returns:
        int: The higher integer average between the first and second half of the list.
    """
    mid = len(scores) // 2
    return max(
        average(scores, 0, mid),
        average(scores, mid, len(scores))
    )


def average(scores: list[int], start: int, end: int) -> int:
    """
    Helper function to compute the average of elements in scores[start:end].
    
    Args:
        scores (list[int]): The list of scores.
        start (int): The start index (inclusive).
        end (int): The end index (exclusive).

    Returns:
        int: The integer average of the elements in the specified range.
    """
    return sum(scores[start:end]) // (end - start)


# Unit tests for scoresAverage function
import unittest

class TestScoresAverage(unittest.TestCase):
    def test_scoresAverage(self):
        self.assertEqual(scoresAverage([2, 2, 4, 4]), 4)
        self.assertEqual(scoresAverage([4, 4, 4, 2, 2, 2]), 4)
        self.assertEqual(scoresAverage([3, 4, 5, 1, 2, 3]), 4)
        self.assertEqual(scoresAverage([5, 6]), 6)
        self.assertEqual(scoresAverage([5, 4]), 5)
        self.assertEqual(scoresAverage([5, 4, 5, 6, 2, 1, 2, 3]), 5)

if __name__ == "__main__":
    unittest.main()
