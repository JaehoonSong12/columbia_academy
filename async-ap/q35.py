def withoutString(base: str, remove: str) -> str:
    """
    Description:
        Given two strings, `base` and `remove`, return a version of the `base` string where all
        non-overlapping instances of the `remove` string have been removed. Removal is not case
        sensitive (e.g. removing "is" will remove "IS", "Is", etc.), but the remaining characters
        keep their original case. You may assume `remove` has length 1 or more.

    Examples:
        withoutString("Hello there", "llo") → "He there"
        withoutString("Hello there", "e")   → "Hllo thr"
        withoutString("Hello there", "x")   → "Hello there"

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-ap/q35.py`

    Args:
        base (str):    The original string.
        remove (str):  The substring to remove (case-insensitive).

    Returns:
        str: The resulting string after all instances of `remove` have been removed.
    """
    ### [Your Implementation Here]
    
    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.

    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.


# Unit tests for withoutString function
import unittest

class TestWithoutString(unittest.TestCase):
    def test_withoutString(self):
        self.assertEqual(withoutString("Hello there", "llo"), "He there")
        self.assertEqual(withoutString("Hello there", "e"), "Hllo thr")
        self.assertEqual(withoutString("Hello there", "x"), "Hello there")
        self.assertEqual(withoutString("This is a FISH", "IS"), "Th a FH")
        self.assertEqual(withoutString("THIS is a FISH", "is"), "TH a FH")
        self.assertEqual(withoutString("abxxxxab", "xx"), "abab")
        self.assertEqual(withoutString("abxxxab", "xx"), "abxab")
        self.assertEqual(withoutString("abxxxab", "x"), "abab")
        self.assertEqual(withoutString("xxx", "x"), "")
        self.assertEqual(withoutString("xxx", "xx"), "x")
        self.assertEqual(withoutString("xyzzy", "Y"), "xzz")
        self.assertEqual(withoutString("", "x"), "")
        self.assertEqual(withoutString("abcabc", "b"), "acac")
        self.assertEqual(withoutString("AA22bb", "2"), "AAbb")
        self.assertEqual(withoutString("1111", "1"), "")
        self.assertEqual(withoutString("1111", "11"), "")
        self.assertEqual(withoutString("MkjtMkx", "Mk"), "jtx")
        self.assertEqual(withoutString("Hi HoHo", "Ho"), "Hi ")

if __name__ == "__main__":
    unittest.main()
