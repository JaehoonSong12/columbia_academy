def commonTwo(a: list[str], b: list[str]) -> int:
    """
    Description:
        Start with two arrays of strings, `a` and `b`, each in 
        alphabetical order, possibly with duplicates.
        Return the count of the number of unique strings which 
        appear in both arrays. Use a single-pass
        linear solution taking advantage of the sorted order.

    Examples:
        commonTwo(["a", "c", "x"], ["b", "c", "d", "x"]) → 2
        commonTwo(["a", "c", "x"], ["a", "b", "c", "x", "z"]) → 3
        commonTwo(["a", "b", "c"], ["a", "b", "c"]) → 3

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-ap/q21.py`

    Args:
        a (list[str]): First sorted list of strings, may contain duplicates.
        b (list[str]): Second sorted list of strings, may contain duplicates.

    Returns:
        int: The count of unique strings that appear in both `a` and `b`.
    """
    ### [Your Implementation Here]
    
    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.

    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.


# Unit tests for commonTwo function
import unittest

class TestCommonTwo(unittest.TestCase):
    def test_commonTwo(self):
        self.assertEqual(commonTwo(["a", "c", "x"], ["b", "c", "d", "x"]), 2)
        self.assertEqual(commonTwo(["a", "c", "x"], ["a", "b", "c", "x", "z"]), 3)
        self.assertEqual(commonTwo(["a", "b", "c"], ["a", "b", "c"]), 3)
        self.assertEqual(commonTwo(["a", "a", "b", "b", "c"], ["a", "b", "c"]), 3)
        self.assertEqual(commonTwo(["a", "a", "b", "b", "c"], ["a", "b", "b", "b", "c"]), 3)
        self.assertEqual(commonTwo(["a", "a", "b", "b", "c"], ["a", "b", "b", "c", "c"]), 3)
        self.assertEqual(commonTwo(["b", "b", "b", "b", "c"], ["a", "b", "b", "b", "c"]), 2)
        self.assertEqual(commonTwo(["a", "b", "c", "c", "d"], ["a", "b", "b", "c", "d", "d"]), 4)
        self.assertEqual(commonTwo(["a", "a", "b", "b", "c"], ["b", "b", "b"]), 1)
        self.assertEqual(commonTwo(["a", "a", "b", "b", "c"], ["c", "c"]), 1)
        self.assertEqual(commonTwo(["a", "a", "b", "b", "c"], ["b", "b", "b", "x"]), 1)
        self.assertEqual(commonTwo(["a", "a", "b", "b", "c"], ["b", "b"]), 1)
        self.assertEqual(commonTwo(["a"], ["a", "b"]), 1)
        self.assertEqual(commonTwo(["a"], ["b"]), 0)
        self.assertEqual(commonTwo(["a", "a"], ["b", "b"]), 0)
        self.assertEqual(commonTwo(["a", "b"], ["a", "b"]), 2)

if __name__ == "__main__":
    unittest.main()
