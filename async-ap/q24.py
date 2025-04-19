def countEvens(nums: list[int]) -> int:
    """
    Description:
        Return the number of even integers in the given array.
        An integer is even if it has no remainder when divided by 2 (i.e., num % 2 == 0).

    Examples:
        countEvens([2, 1, 2, 3, 4]) → 3
        countEvens([2, 2, 0]) → 3
        countEvens([1, 3, 5]) → 0

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-ap/q24.py`

    Args:
        nums (list[int]): A list of integers.

    Returns:
        int: Count of even integers in the list.
    """
    ### [Your Implementation Here]
    
    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.

    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.


# Unit tests for countEvens function
import unittest

class TestCountEvens(unittest.TestCase):
    def test_countEvens(self):
        self.assertEqual(countEvens([2, 1, 2, 3, 4]), 3)
        self.assertEqual(countEvens([2, 2, 0]), 3)
        self.assertEqual(countEvens([1, 3, 5]), 0)
        self.assertEqual(countEvens([]), 0)
        self.assertEqual(countEvens([11, 9, 0, 1]), 1)
        self.assertEqual(countEvens([2, 11, 9, 0]), 2)
        self.assertEqual(countEvens([2]), 1)
        self.assertEqual(countEvens([2, 5, 12]), 2)

if __name__ == "__main__":
    unittest.main()
