def makeBricks(small: int, big: int, goal: int) -> bool:
    """
    Description:
        Determine if it is possible to reach the desired goal 
        length using a combination
        of small bricks (1 inch each) and big bricks (5 inches each). 
        The function returns True if the goal can be reached 
        exactly, otherwise False.
        No loops are needed for this solution.

    Examples:
        makeBricks(3, 1, 8) → True
        makeBricks(3, 1, 9) → False
        makeBricks(3, 2, 10) → True

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-ap/q27.py`

    Args:
        small (int): Number of small bricks (1 inch each).
        big (int): Number of big bricks (5 inches each).
        goal (int): The target length to achieve.

    Returns:
        bool: True if the goal can be reached using the available bricks, False otherwise.
    """
    ### [Your Implementation Here]
    
    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.

    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.


# Unit tests for makeBricks function
import unittest

class TestMakeBricks(unittest.TestCase):
    def test_makeBricks(self):
        self.assertTrue(makeBricks(3, 1, 8))
        self.assertFalse(makeBricks(3, 1, 9))
        self.assertTrue(makeBricks(3, 2, 10))
        self.assertTrue(makeBricks(3, 2, 8))
        self.assertFalse(makeBricks(3, 2, 9))
        self.assertTrue(makeBricks(6, 1, 11))
        self.assertFalse(makeBricks(6, 0, 11))
        self.assertTrue(makeBricks(1, 4, 11))
        self.assertTrue(makeBricks(0, 3, 10))
        self.assertFalse(makeBricks(1, 4, 12))
        self.assertTrue(makeBricks(3, 1, 7))
        self.assertFalse(makeBricks(1, 1, 7))
        self.assertTrue(makeBricks(2, 1, 7))
        self.assertTrue(makeBricks(7, 1, 11))
        self.assertTrue(makeBricks(7, 1, 8))
        self.assertFalse(makeBricks(7, 1, 13))
        self.assertTrue(makeBricks(43, 1, 46))
        self.assertFalse(makeBricks(40, 1, 46))
        self.assertTrue(makeBricks(40, 2, 47))
        self.assertTrue(makeBricks(40, 2, 50))
        self.assertFalse(makeBricks(40, 2, 52))
        self.assertFalse(makeBricks(22, 2, 33))
        self.assertTrue(makeBricks(0, 2, 10))
        self.assertTrue(makeBricks(1000000, 1000, 1000100))
        self.assertFalse(makeBricks(2, 1000000, 100003))
        self.assertTrue(makeBricks(20, 0, 19))
        self.assertFalse(makeBricks(20, 0, 21))
        self.assertFalse(makeBricks(20, 4, 51))
        self.assertTrue(makeBricks(20, 4, 39))

if __name__ == "__main__":
    unittest.main()
