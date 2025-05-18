def loneSum(a: int, b: int, c: int) -> int:
    """
    Description:
        Given 3 integer values, a, b, and c, return their sum. However, if one of the values
        is the same as another value, that value does not count toward the sum.

    Examples:
        loneSum(1, 2, 3) → 6
        loneSum(3, 2, 3) → 2
        loneSum(3, 3, 3) → 0

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-ap/q34.py`

    Args:
        a (int): First integer.
        b (int): Second integer.
        c (int): Third integer.

    Returns:
        int: The sum of the values that are not duplicated.
    """
    ### [Your Implementation Here]
    total = 0
    if a != b and a != c:
        total += a
    if b != a and b != c:
        total += b
    if c != a and c != b:
        total += c
    return total
    
    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.

    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.


# Unit tests for loneSum function
import unittest

class TestLoneSum(unittest.TestCase):
    def test_loneSum(self):
        self.assertEqual(loneSum(1, 2, 3), 6)
        self.assertEqual(loneSum(3, 2, 3), 2)
        self.assertEqual(loneSum(3, 3, 3), 0)
        self.assertEqual(loneSum(9, 2, 2), 9)
        self.assertEqual(loneSum(2, 2, 9), 9)
        self.assertEqual(loneSum(2, 9, 2), 9)
        self.assertEqual(loneSum(2, 9, 3), 14)
        self.assertEqual(loneSum(4, 2, 3), 9)
        self.assertEqual(loneSum(1, 3, 1), 3)

if __name__ == "__main__":
    unittest.main()