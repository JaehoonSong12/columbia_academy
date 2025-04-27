def repeatFront(s: str, n: int) -> str:
    """
    Description:
        Given a string `s` and an integer `n`, return a string made of the first `n` characters
        of `s`, followed by the first `n-1` characters, and so on down to 1. You may assume
        0 ≤ n ≤ len(s).

    Examples:
        repeatFront("Chocolate", 4) → "ChocChoChC"
        repeatFront("Chocolate", 3) → "ChoChC"
        repeatFront("Ice Cream", 2) → "IcI"

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-ap/q46.py`

    Args:
        s (str): The input string.
        n (int): Number of characters to start with (0 ≤ n ≤ len(s)).

    Returns:
        str: The concatenated prefix sequence.
    """
    ### [Your Implementation Here]
    
    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.

    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.


# Unit tests for repeatFront function
import unittest

class TestRepeatFront(unittest.TestCase):
    def test_repeatFront(self):
        self.assertEqual(repeatFront("Chocolate", 4), "ChocChoChC")
        self.assertEqual(repeatFront("Chocolate", 3), "ChoChC")
        self.assertEqual(repeatFront("Ice Cream", 2), "IcI")
        self.assertEqual(repeatFront("Ice Cream", 1), "I")
        self.assertEqual(repeatFront("Ice Cream", 0), "")
        self.assertEqual(repeatFront("xyz", 3), "xyzxyx")
        self.assertEqual(repeatFront("", 0), "")
        self.assertEqual(repeatFront("Java", 4), "JavaJavJaJ")
        self.assertEqual(repeatFront("Java", 1), "J")

if __name__ == "__main__":
    unittest.main()
