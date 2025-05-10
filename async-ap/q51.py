def gHappy(s: str) -> bool:
    """
    Description:
        We'll say that a lowercase 'g' in a string is "happy" if there is another 'g'
        immediately to its left or right. Return True if all the 'g's in the given string
        are happy.

    Examples:
        gHappy("xxggxx") → True
        gHappy("xxgxx") → False
        gHappy("xxggyygxx") → False

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-ap/q51.py`

    Args:
        s (str): The input string.

    Returns:
        bool: True if every 'g' in the string is happy, False otherwise.
    """
    ### [Your Implementation Here]
    
    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.

    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.



# Unit tests for gHappy function
import unittest

class TestGHappy(unittest.TestCase):
    def test_gHappy(self):
        self.assertTrue(gHappy("xxggxx"))
        self.assertFalse(gHappy("xxgxx"))
        self.assertFalse(gHappy("xxggyygxx"))
        self.assertFalse(gHappy("g"))
        self.assertTrue(gHappy("gg"))
        self.assertTrue(gHappy(""))
        self.assertTrue(gHappy("xxgggxyz"))
        self.assertFalse(gHappy("xxgggxyg"))
        self.assertTrue(gHappy("xxgggxygg"))
        self.assertFalse(gHappy("mgm"))
        self.assertTrue(gHappy("mggm"))
        self.assertTrue(gHappy("yyygggxyy"))

if __name__ == "__main__":
    unittest.main()
