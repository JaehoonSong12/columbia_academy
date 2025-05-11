def repeatEnd(s: str, n: int) -> str:
    """
    Description:
        Given a string `s` and an integer `n`, return a new string made of `n` repetitions
        of the last `n` characters of `s`. You may assume that 0 ≤ n ≤ len(s).

    Examples:
        repeatEnd("Hello", 3) → "llollollo"
        repeatEnd("Hello", 2) → "lolo"
        repeatEnd("Hello", 1) → "o"

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-ap/q55.py`

    Args:
        s (str): The input string.
        n (int): Number of characters from the end to repeat (0 ≤ n ≤ len(s)).

    Returns:
        str: A string consisting of `n` copies of the last `n` characters of `s`.
    """
    ### [Your Implementation Here]
    
    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.

    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.


# Unit tests for repeatEnd function
import unittest

class TestRepeatEnd(unittest.TestCase):
    def test_repeatEnd(self):
        self.assertEqual(repeatEnd("Hello", 3), "llollollo")
        self.assertEqual(repeatEnd("Hello", 2), "lolo")
        self.assertEqual(repeatEnd("Hello", 1), "o")
        self.assertEqual(repeatEnd("Hello", 0), "")
        self.assertEqual(repeatEnd("abc", 3), "abcabcabc")
        self.assertEqual(repeatEnd("1234", 2), "3434")
        self.assertEqual(repeatEnd("1234", 3), "234234234")
        self.assertEqual(repeatEnd("", 0), "")

if __name__ == "__main__":
    unittest.main()
