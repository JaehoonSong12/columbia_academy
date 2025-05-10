def squareUp(n: int) -> list[int]:
    """
    Description:
        Given an integer n >= 0, return a list of length n * n following a specific pattern.
        For each group i from 1 to n, the group consists of (n - i) zeros followed by descending
        integers from i to 1. All such groups are concatenated into a single list.

    Examples:
        squareUp(3) → [0, 0, 1, 0, 2, 1, 3, 2, 1]
        squareUp(2) → [0, 1, 2, 1]
        squareUp(4) → [0, 0, 0, 1, 0, 0, 2, 1, 0, 3, 2, 1, 4, 3, 2, 1]

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-ap/q73.py`

    Args:
        n (int): A non-negative integer representing the square dimension.

    Returns:
        list[int]: The list following the described square-up pattern.
    """
    ### [Your Implementation Here]
    
    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.

    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.


# Unit tests for squareUp function
import unittest

class TestSquareUp(unittest.TestCase):
    def test_squareUp(self):
        self.assertEqual(squareUp(3), [0, 0, 1, 0, 2, 1, 3, 2, 1])
        self.assertEqual(squareUp(2), [0, 1, 2, 1])
        self.assertEqual(squareUp(4), [0, 0, 0, 1, 0, 0, 2, 1, 0, 3, 2, 1, 4, 3, 2, 1])
        self.assertEqual(squareUp(1), [1])
        self.assertEqual(squareUp(0), [])
        self.assertEqual(
            squareUp(6),
            [
                0, 0, 0, 0, 0, 1,
                0, 0, 0, 0, 2, 1,
                0, 0, 0, 3, 2, 1,
                0, 0, 4, 3, 2, 1,
                0, 5, 4, 3, 2, 1,
                6, 5, 4, 3, 2, 1
            ]
        )

if __name__ == "__main__":
    unittest.main()
