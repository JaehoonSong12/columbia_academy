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
        2. Run the tests by executing: `python async-ap/q04.py`

    Args:
        scores (list[int]): A list of scores (at least 2 elements long).

    Returns:
        int: The higher integer average between the first and second half of the list.
    """
    ### [Your Implementation Here]
    
    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.
    first_half = []
    second_half = []
    i = 0
    while i < len(scores)//2:
        first_half.append(scores[i])
        i += 1
    while i in range(len(scores)//2, len(scores)):
        second_half.append(scores[i])
        i += 1
    first_sum = 0
    first_amount = len(first_half)
    for n in first_half:
        first_sum += n
    second_sum = 0
    second_amount = len(second_half)
    for n in second_half:
        second_sum += n
    first_average = first_sum / first_amount
    second_average = second_sum / second_amount
    if first_average > second_average:
        return int(first_average)
    return int(second_average)
    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.


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
    ### [Your Implementation Here]
    
    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.

    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.


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
