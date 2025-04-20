def dividesSelf(n: int) -> bool:
    """
    Description:
        A positive integer divides itself if every digit in the number 
        divides into the number evenly.
        For example, 128 divides itself since 1, 2, and 8 all divide 
        into 128 evenly.
        A number with a 0 digit does not divide itself, as 0 does not 
        divide into any number.

    Examples:
        dividesSelf(128) → True
        dividesSelf(12) → True
        dividesSelf(120) → False

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-ap/q09.py`

    Args:
        n (int): A positive integer.

    Returns:
        bool: True if the number divides itself, False otherwise.
    """
    ### [Your Implementation Here]
    
    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.
    i = 0
    n = str(n)
    while i < len(n):
        if int(n[i]) == 0:
            return False
        if not int(n) % int(n[i]) == 0:
            return False
        i += 1
    return True

    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.


# Unit tests for dividesSelf function
import unittest

class TestDividesSelf(unittest.TestCase):
    def test_dividesSelf(self):
        self.assertTrue(dividesSelf(128))
        self.assertTrue(dividesSelf(12))
        self.assertFalse(dividesSelf(120))
        self.assertTrue(dividesSelf(122))
        self.assertFalse(dividesSelf(13))
        self.assertFalse(dividesSelf(32))
        self.assertTrue(dividesSelf(22))
        self.assertFalse(dividesSelf(42))
        self.assertTrue(dividesSelf(212))
        self.assertFalse(dividesSelf(213))
        self.assertTrue(dividesSelf(162))

if __name__ == "__main__":
    unittest.main()
