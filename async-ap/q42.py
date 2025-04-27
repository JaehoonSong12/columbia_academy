def luckySum(a: int, b: int, c: int) -> int:
    """
    Description:
        Given 3 integer values, a, b, c, return their sum. However, if one of the values
        is 13 then it does not count toward the sum and values to its right do not count.
        So for example, if b is 13, then both b and c do not count.

    Examples:
        luckySum(1, 2, 3) → 6
        luckySum(1, 2, 13) → 3
        luckySum(1, 13, 3) → 1

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-ap/q42.py`

    Args:
        a (int): First integer.
        b (int): Second integer.
        c (int): Third integer.

    Returns:
        int: The sum as described, skipping 13 and any values to its right.
    """
    ### [Your Implementation Here]
    
    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.

    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.


# Unit tests for luckySum function
import unittest

class TestLuckySum(unittest.TestCase):
    def test_luckySum(self):
        self.assertEqual(luckySum(1, 2, 3), 6)
        self.assertEqual(luckySum(1, 2, 13), 3)
        self.assertEqual(luckySum(1, 13, 3), 1)
        self.assertEqual(luckySum(1, 13, 13), 1)
        self.assertEqual(luckySum(6, 5, 2), 13)
        self.assertEqual(luckySum(13, 2, 3), 0)
        self.assertEqual(luckySum(13, 2, 13), 0)
        self.assertEqual(luckySum(13, 13, 2), 0)
        self.assertEqual(luckySum(9, 4, 13), 13)
        self.assertEqual(luckySum(8, 13, 2), 8)
        self.assertEqual(luckySum(7, 2, 1), 10)
        self.assertEqual(luckySum(3, 3, 13), 6)

if __name__ == "__main__":
    unittest.main()
