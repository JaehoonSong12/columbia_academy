def userCompare(aName: str, aId: int, bName: str, bId: int) -> int:
    """
    Description:
        We have data for two users, A and B, each with a string 
        `name` and an integer `id`.
        The goal is to order the users for sorting. Return:
          - -1 if A comes before B
          -  1 if A comes after B
          -  0 if they are the same.
        Order first by name (lexicographically), and if the names 
        are equal, order by id.

    Examples:
        userCompare("bb", 1, "zz", 2) → -1
        userCompare("bb", 1, "aa", 2) → 1
        userCompare("bb", 1, "bb", 1) → 0
        userCompare("bb", 5, "bb", 1) → 1
        userCompare("bb", 5, "bb", 10) → -1
        userCompare("adam", 1, "bob", 2) → -1
        userCompare("bob", 1, "bob", 2) → -1
        userCompare("bzb", 1, "bob", 2) → 1

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-ap/q19.py`

    Args:
        aName (str): Name of user A.
        aId   (int): ID of user A.
        bName (str): Name of user B.
        bId   (int): ID of user B.

    Returns:
        int: -1 if A < B, 1 if A > B, 0 if they are equal.
    """
    ### [Your Implementation Here]
    
    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.

    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.


# Unit tests for userCompare function
import unittest

class TestUserCompare(unittest.TestCase):
    def test_userCompare(self):
        self.assertEqual(userCompare("bb", 1, "zz", 2), -1)
        self.assertEqual(userCompare("bb", 1, "aa", 2), 1)
        self.assertEqual(userCompare("bb", 1, "bb", 1), 0)
        self.assertEqual(userCompare("bb", 5, "bb", 1), 1)
        self.assertEqual(userCompare("bb", 5, "bb", 10), -1)
        self.assertEqual(userCompare("adam", 1, "bob", 2), -1)
        self.assertEqual(userCompare("bob", 1, "bob", 2), -1)
        self.assertEqual(userCompare("bzb", 1, "bob", 2), 1)

if __name__ == "__main__":
    unittest.main()
