def hasOne(n: int) -> bool:
    """
    Description:
        Given a positive integer n, return true if it contains a digit '1'. 
        Note: Use % to get the rightmost digit, and / to discard the rightmost digit.

    Examples:
        hasOne(10) → True
        hasOne(22) → False
        hasOne(220) → False

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-iteration+recursion/q08.py`

    Args:
        n (int): A positive integer.

    Returns:
        bool: True if the number contains at least one digit '1', False otherwise.
    """
    while n > 0:
        if n % 10 == 1:
            return True
        n //= 10
    return False


# Unit tests for hasOne function
import unittest

class TestHasOne(unittest.TestCase):
    def test_hasOne(self):
        self.assertTrue(hasOne(10))
        self.assertFalse(hasOne(22))
        self.assertFalse(hasOne(220))
        self.assertTrue(hasOne(212))
        self.assertTrue(hasOne(1))
        self.assertFalse(hasOne(9))
        self.assertTrue(hasOne(211112))
        self.assertTrue(hasOne(121121))
        self.assertFalse(hasOne(222222))
        self.assertTrue(hasOne(56156))
        self.assertFalse(hasOne(56556))

if __name__ == "__main__":
    unittest.main()
