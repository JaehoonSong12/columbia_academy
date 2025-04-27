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
    def quicksort(arr: list[str]) -> list[str]:
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)
    ### [Your Implementation Here]
    c = a + b
    c = quicksort(c) # n log n
    unique_c = [c[0]] # O(1)
    for i in range(1, len(c) - 1): # O(n)
        if (len(unique_c) == n): 
            break
        if (c[i] != unique_c[-1]): 
            unique_c.append(c[i])
    return unique_c

    # i = 0
    # j = 0
    # curr_ord = -1
    # while len(c) < n:
    #     if ord(a[i]) < ord(b[j]):
    #         c.append(a[i])
    #         curr_ord = ord(a[i])
    #         i += 1
    #     elif ord(b[j]) < ord(a[i]):
    #         c.append(b[i])
    #         curr_ord = ord(b[j])
    #         j += 1
    #     elif ord(a[i]) == ord(b[j]):
    #         if ord(a[i]) != curr_ord: 
    #             c.append(a[i])
    #             curr_ord = ord(a[i])
    #             i += 1
    #         j += 1
    # return c

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
