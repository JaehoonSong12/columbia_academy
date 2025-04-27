def fizzArray(n: int) -> list[int]:
    """
    Description:
        Given a number n, create and return a new list of length n containing the numbers
        0, 1, 2, ... n-1. If n is 0, return an empty list.

    Examples:
        fizzArray(4) → [0, 1, 2, 3]
        fizzArray(1) → [0]
        fizzArray(10) → [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-ap/q47.py`

    Args:
        n (int): Non-negative length of the array to generate.

    Returns:
        list[int]: A list of integers from 0 up to n-1.
    """
    ### [Your Implementation Here]
    
    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.

    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.


# Unit tests for fizzArray function
import unittest

class TestFizzArray(unittest.TestCase):
    def test_fizzArray(self):
        self.assertEqual(fizzArray(4), [0, 1, 2, 3])
        self.assertEqual(fizzArray(1), [0])
        self.assertEqual(fizzArray(10), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(fizzArray(0), [])
        self.assertEqual(fizzArray(2), [0, 1])
        self.assertEqual(fizzArray(7), [0, 1, 2, 3, 4, 5, 6])

if __name__ == "__main__":
    unittest.main()
