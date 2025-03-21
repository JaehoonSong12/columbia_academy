def countX(s: str) -> int:
    """
    Description:
        Given a string, compute recursively (no loops) the number of lowercase 'x' chars in the string.

    Examples:
        countX("xxhixx") -> 4
        countX("xhixhix") -> 3
        countX("hi") -> 0

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-recursion/q10.py`

    Args:
        s (str): The input string.

    Returns:
        int: The count of 'x' characters in the string.
    """
    # Base case: your implementation and comment here.

    # Recursive case: your implementation and comment here.


# Unit tests for the countX function
import unittest

class TestCountXFunction(unittest.TestCase):
    def test_countX(self):
        self.assertEqual(countX("xxhixx"), 4)   # countX("xxhixx") → 4
        self.assertEqual(countX("xhixhix"), 3)  # countX("xhixhix") → 3
        self.assertEqual(countX("hi"), 0)       # countX("hi") → 0
        self.assertEqual(countX("h"), 0)        # countX("h") → 0
        self.assertEqual(countX("x"), 1)        # countX("x") → 1
        self.assertEqual(countX(""), 0)         # countX("") → 0
        self.assertEqual(countX("hihi"), 0)     # countX("hihi") → 0
        self.assertEqual(countX("hiAAhi12hi"), 0)  # countX("hiAAhi12hi") → 0

if __name__ == '__main__':
    unittest.main()
