def mixString(a: str, b: str) -> str:
    """
    Description:
        Given two strings, `a` and `b`, create a new string by alternating characters:
        take the first char of `a`, then the first char of `b`, then the second char of `a`,
        then the second char of `b`, and so on. Any leftover characters from the longer string
        go at the end of the result.

    Examples:
        mixString("abc", "xyz") → "axbycz"
        mixString("Hi", "There") → "HTihere"
        mixString("xxxx", "There") → "xTxhxexre"

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-ap/q56.py`

    Args:
        a (str): First input string.
        b (str): Second input string.

    Returns:
        str: The merged string with alternating characters.
    """
    ### [Your Implementation Here]
    
    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.

    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.


# Unit tests for mixString function
import unittest

class TestMixString(unittest.TestCase):
    def test_mixString(self):
        self.assertEqual(mixString("abc", "xyz"), "axbycz")
        self.assertEqual(mixString("Hi", "There"), "HTihere")
        self.assertEqual(mixString("xxxx", "There"), "xTxhxexre")
        self.assertEqual(mixString("xxx", "X"), "xXxx")
        self.assertEqual(mixString("2/", "27 around"), "22/7 around")
        self.assertEqual(mixString("", "Hello"), "Hello")
        self.assertEqual(mixString("Abc", ""), "Abc")
        self.assertEqual(mixString("", ""), "")
        self.assertEqual(mixString("a", "b"), "ab")
        self.assertEqual(mixString("ax", "b"), "abx")
        self.assertEqual(mixString("a", "bx"), "abx")
        self.assertEqual(mixString("So", "Long"), "SLoong")
        self.assertEqual(mixString("Long", "So"), "LSoong")

if __name__ == "__main__":
    unittest.main()
