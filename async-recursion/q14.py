def noX(s: str) -> str:
    """
    Description:
        Given a string, compute recursively a new string where all 
        the 'x' chars have been removed.

    Examples:
        noX("xaxb") -> "ab"
        noX("abc") -> "abc"
        noX("xx") -> ""

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-recursion/q14.py`

    Args:
        s (str): The input string.

    Returns:
        str: The modified string with all 'x' characters removed.
    """
    # Base case: your implementation and comment here.

    # Recursive case: your implementation and comment here.


# Unit tests for the noX function
import unittest

class TestNoXFunction(unittest.TestCase):
    def test_noX(self):
        self.assertEqual(noX("xaxb"), "ab")        # noX("xaxb") → "ab"
        self.assertEqual(noX("abc"), "abc")        # noX("abc") → "abc"
        self.assertEqual(noX("xx"), "")           # noX("xx") → ""
        self.assertEqual(noX(""), "")             # noX("") → ""
        self.assertEqual(noX("axxbxx"), "ab")     # noX("axxbxx") → "ab"
        self.assertEqual(noX("Hellox"), "Hello")  # noX("Hellox") → "Hello"

if __name__ == '__main__':
    unittest.main()
