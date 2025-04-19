def mergeTwo(a: list[str], b: list[str], n: int) -> list[str]:
    """
    Description:
        Start with two arrays of strings, `a` and `b`, each sorted 
        alphabetically and without duplicates.
        Return a new list containing the first `n` elements from the 
        two arrays merged together.
        The result list should be in alphabetical order and 
        without duplicates.
        You should make a single pass over `a` and `b`, taking 
        advantage of their sorted order.

    Examples:
        mergeTwo(["a", "c", "z"], ["b", "f", "z"], 3) → ["a", "b", "c"]
        mergeTwo(["a", "c", "z"], ["c", "f", "z"], 3) → ["a", "c", "f"]
        mergeTwo(["f", "g", "z"], ["c", "f", "g"], 3) → ["c", "f", "g"]

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-ap/q20.py`

    Args:
        a (list[str]): First sorted list of unique strings.
        b (list[str]): Second sorted list of unique strings.
        n (int): Number of elements to include in the merged result.

    Returns:
        list[str]: A sorted list of the first `n` unique strings from merging `a` and `b`.
    """
    ### [Your Implementation Here]
    
    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.

    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.


# Unit tests for mergeTwo function
import unittest

class TestMergeTwo(unittest.TestCase):
    def test_mergeTwo(self):
        self.assertEqual(mergeTwo(["a", "c", "z"], ["b", "f", "z"], 3), ["a", "b", "c"])
        self.assertEqual(mergeTwo(["a", "c", "z"], ["c", "f", "z"], 3), ["a", "c", "f"])
        self.assertEqual(mergeTwo(["f", "g", "z"], ["c", "f", "g"], 3), ["c", "f", "g"])
        self.assertEqual(mergeTwo(["a", "c", "z"], ["a", "c", "z"], 3), ["a", "c", "z"])
        self.assertEqual(mergeTwo(["a", "b", "c", "z"], ["a", "c", "z"], 3), ["a", "b", "c"])
        self.assertEqual(mergeTwo(["a", "c", "z"], ["a", "b", "c", "z"], 3), ["a", "b", "c"])
        self.assertEqual(mergeTwo(["a", "c", "z"], ["a", "c", "z"], 2), ["a", "c"])
        self.assertEqual(mergeTwo(["a", "c", "z"], ["a", "c", "y", "z"], 3), ["a", "c", "y"])
        self.assertEqual(mergeTwo(["x", "y", "z"], ["a", "b", "z"], 3), ["a", "b", "x"])

if __name__ == "__main__":
    unittest.main()
