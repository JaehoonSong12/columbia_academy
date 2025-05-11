def roundSum(a: int, b: int, c: int) -> int:
    """
    Description:
        Given three integers a, b, c, round each to the nearest multiple of 10
        (rounding up if the rightmost digit is 5 or more, otherwise down),
        then return the sum of the rounded values.
        Use a helper function round10(num) to perform the rounding for each value.

    Examples:
        roundSum(16, 17, 18) → 60   # 20 + 20 + 20
        roundSum(12, 13, 14) → 30   # 10 + 10 + 10
        roundSum(6, 4, 4)   → 10    # 10 + 0 + 0

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-ap/q59.py`

    Args:
        a (int): First integer.
        b (int): Second integer.
        c (int): Third integer.

    Returns:
        int: Sum of the three values after rounding each to nearest ten.
    """
    ### [Your Implementation Here]
    
    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.

    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.


# Unit tests for roundSum function
import unittest

class TestRoundSum(unittest.TestCase):
    def test_roundSum(self):
        self.assertEqual(roundSum(16, 17, 18), 60)
        self.assertEqual(roundSum(12, 13, 14), 30)
        self.assertEqual(roundSum(6, 4, 4), 10)
        self.assertEqual(roundSum(4, 6, 5), 20)
        self.assertEqual(roundSum(4, 4, 6), 10)
        self.assertEqual(roundSum(9, 4, 4), 10)
        self.assertEqual(roundSum(0, 0, 1), 0)
        self.assertEqual(roundSum(0, 9, 0), 10)
        self.assertEqual(roundSum(10, 10, 19), 40)
        self.assertEqual(roundSum(20, 30, 40), 90)
        self.assertEqual(roundSum(45, 21, 30), 100)
        self.assertEqual(roundSum(23, 11, 26), 60)
        self.assertEqual(roundSum(23, 24, 25), 70)
        self.assertEqual(roundSum(25, 24, 25), 80)
        self.assertEqual(roundSum(23, 24, 29), 70)
        self.assertEqual(roundSum(11, 24, 36), 70)
        self.assertEqual(roundSum(24, 36, 32), 90)
        self.assertEqual(roundSum(14, 12, 26), 50)
        self.assertEqual(roundSum(12, 10, 24), 40)

if __name__ == "__main__":
    unittest.main()
