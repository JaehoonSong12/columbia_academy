def changeXY(s: str) -> str:
    """
    Description:
        Given a string, compute recursively (no loops) a new string where all 
        the lowercase 'x' chars have been changed to 'y' chars.

    Examples:
        changeXY("codex") -> "codey"
        changeXY("xxhixx") -> "yyhiyy"
        changeXY("xhixhix") -> "yhiyhiy"

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-recursion/q12.py`

    Args:
        s (str): The input string.

    Returns:
        str: The modified string with 'x' replaced by 'y'.
    """
    # Base case: your implementation and comment here.

    # Recursive case: your implementation and comment here.


# Unit tests for the changeXY function
import unittest

class TestChangeXYFunction(unittest.TestCase):
    def test_changeXY(self):
        self.assertEqual(changeXY("codex"), "codey")        # changeXY("codex") → "codey"
        self.assertEqual(changeXY("xxhixx"), "yyhiyy")      # changeXY("xxhixx") → "yyhiyy"
        self.assertEqual(changeXY("xhixhix"), "yhiyhiy")    # changeXY("xhixhix") → "yhiyhiy"
        self.assertEqual(changeXY("hiy"), "hiy")            # changeXY("hiy") → "hiy"
        self.assertEqual(changeXY("h"), "h")                # changeXY("h") → "h"
        self.assertEqual(changeXY("x"), "y")                # changeXY("x") → "y"
        self.assertEqual(changeXY(""), "")                  # changeXY("") → ""
        self.assertEqual(changeXY("xxx"), "yyy")            # changeXY("xxx") → "yyy"
        self.assertEqual(changeXY("yyhxyi"), "yyhyyi")      # changeXY("yyhxyi") → "yyhyyi"
        self.assertEqual(changeXY("hihi"), "hihi")          # changeXY("hihi") → "hihi"

if __name__ == '__main__':
    unittest.main()
