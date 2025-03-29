def countAbc(s: str) -> int:
    """
    Description:
        Recursively counts the total number of "abc" and "aba" substrings 
        that appear in the given string.

    Examples:
        countAbc("abc") → 1
        countAbc("abcxxabc") → 2
        countAbc("abaxxaba") → 2

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-recursion/q22.py`

    Args:
        s (str): The input string.

    Returns:
        int: The count of occurrences of "abc" or "aba" substrings.
    """
    # Base case: your implementation and comment here.

    # Recursive case: your implementation and comment here.


# Unit tests for the countAbc function
import unittest

class TestCountAbcFunction(unittest.TestCase):
    def test_countAbc(self):
        self.assertEqual(countAbc("abc"), 1)  # countAbc("abc") → 1
        self.assertEqual(countAbc("abcxxabc"), 2)  # countAbc("abcxxabc") → 2
        self.assertEqual(countAbc("abaxxaba"), 2)  # countAbc("abaxxaba") → 2
        self.assertEqual(countAbc("ababc"), 2)  # countAbc("ababc") → 2
        self.assertEqual(countAbc("abxbc"), 0)  # countAbc("abxbc") → 0
        self.assertEqual(countAbc("aaabc"), 1)  # countAbc("aaabc") → 1
        self.assertEqual(countAbc("hello"), 0)  # countAbc("hello") → 0
        self.assertEqual(countAbc(""), 0)  # countAbc("") → 0
        self.assertEqual(countAbc("ab"), 0)  # countAbc("ab") → 0
        self.assertEqual(countAbc("aba"), 1)  # countAbc("aba") → 1
        self.assertEqual(countAbc("aca"), 0)  # countAbc("aca") → 0
        self.assertEqual(countAbc("aaa"), 0)  # countAbc("aaa") → 0

if __name__ == '__main__':
    unittest.main()
