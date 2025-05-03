def countHi(s: str) -> int:
    """
    Description:
        Return the number of times the string "hi" appears anywhere in the given string.
        The match is case-sensitive, so only lowercase "hi" counts.

    Examples:
        countHi("abc hi ho") → 1
        countHi("ABChi hi") → 2
        countHi("hihi") → 2

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-ap/q23.py`

    Args:
        s (str): Input string to search within.

    Returns:
        int: Number of times "hi" appears.
    """
    ### [Your Implementation Here]
    
    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.
    i = 0
    count = 0
    while i < len(s) - 1:
        if s[i] == "h":
            if s[i + 1] == "i":
                count += 1
        i += 1
    return count

    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.


# Unit tests for countHi function
import unittest

class TestCountHi(unittest.TestCase):
    def test_countHi(self):
        self.assertEqual(countHi("abc hi ho"), 1)
        self.assertEqual(countHi("ABChi hi"), 2)
        self.assertEqual(countHi("hihi"), 2)
        self.assertEqual(countHi("hiHIhi"), 2)
        self.assertEqual(countHi(""), 0)
        self.assertEqual(countHi("h"), 0)
        self.assertEqual(countHi("hi"), 1)
        self.assertEqual(countHi("Hi is no HI on ahI"), 0)
        self.assertEqual(countHi("hiho not HOHIhi"), 2)

if __name__ == "__main__":
    unittest.main()
