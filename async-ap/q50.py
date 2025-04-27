def noTeenSum(a: int, b: int, c: int) -> int:
    """
    Description:
        Given three integer values a, b, and c, return their sum.
        However, if any of the values is a 'teen' (in the range 13..19 inclusive),
        that value counts as 0, except 15 and 16 are not considered teens.
        Use a helper function fixTeen(n) to handle teen adjustment,
        avoiding repeating code.

    Examples:
        noTeenSum(1, 2, 3)   → 6
        noTeenSum(2, 13, 1)  → 3
        noTeenSum(2, 1, 14)  → 3

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-ap/q50.py`

    Args:
        a (int): First integer value.
        b (int): Second integer value.
        c (int): Third integer value.

    Returns:
        int: The sum after applying the teen rules.
    """
    ### [Your Implementation Here]
    
    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.

    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.


# Unit tests for noTeenSum function
import unittest

class TestNoTeenSum(unittest.TestCase):
    def test_noTeenSum(self):
        self.assertEqual(noTeenSum(1, 2, 3), 6)
        self.assertEqual(noTeenSum(2, 13, 1), 3)
        self.assertEqual(noTeenSum(2, 1, 14), 3)
        self.assertEqual(noTeenSum(2, 1, 15), 18)
        self.assertEqual(noTeenSum(2, 1, 16), 19)
        self.assertEqual(noTeenSum(2, 1, 17), 3)
        self.assertEqual(noTeenSum(17, 1, 2), 3)
        self.assertEqual(noTeenSum(2, 15, 2), 19)
        self.assertEqual(noTeenSum(16, 17, 18), 16)
        self.assertEqual(noTeenSum(17, 18, 19), 0)
        self.assertEqual(noTeenSum(15, 16, 1), 32)
        self.assertEqual(noTeenSum(15, 15, 19), 30)
        self.assertEqual(noTeenSum(15, 19, 16), 31)
        self.assertEqual(noTeenSum(5, 17, 18), 5)
        self.assertEqual(noTeenSum(17, 18, 16), 16)
        self.assertEqual(noTeenSum(17, 19, 18), 0)

if __name__ == "__main__":
    unittest.main()
