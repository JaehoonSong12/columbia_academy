def fizzArray2(n: int) -> list[str]:
    """
    Description:
        Given a non-negative integer n, create and return a new list of length n
        containing the string representations of the numbers 0, 1, 2, ... n-1.
        If n is 0, return an empty list.

    Examples:
        fizzArray2(4)  → ["0", "1", "2", "3"]
        fizzArray2(10) → ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        fizzArray2(2)  → ["0", "1"]

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-ap/q49.py`

    Args:
        n (int): The length of the array to generate (n ≥ 0).

    Returns:
        list[str]: A list of strings "0" through str(n-1).
    """
    ### [Your Implementation Here]
    
    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.

    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.


# Unit tests for fizzArray2 function
import unittest

class TestFizzArray2(unittest.TestCase):
    def test_fizzArray2(self):
        self.assertEqual(fizzArray2(4),  ["0", "1", "2", "3"])
        self.assertEqual(fizzArray2(10), ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
        self.assertEqual(fizzArray2(2),  ["0", "1"])
        self.assertEqual(fizzArray2(1),  ["0"])
        self.assertEqual(fizzArray2(0),  [])
        self.assertEqual(fizzArray2(7),  ["0","1","2","3","4","5","6"])
        self.assertEqual(fizzArray2(9),  ["0","1","2","3","4","5","6","7","8"])
        self.assertEqual(fizzArray2(11), ["0","1","2","3","4","5","6","7","8","9","10"])

if __name__ == "__main__":
    unittest.main()
