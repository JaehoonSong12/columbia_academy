def scoreUp(key: list[str], answers: list[str]) -> int:
    """
    Description:
        Given two arrays of strings, the "key" array containing the 
        correct answers and the "answers" array containing the student's responses,
        calculate the score for the student. 
        A correct answer is worth +4 points, an incorrect answer is worth 
        -1 point, and a blank answer ("?") is worth 0 points.

    Examples:
        scoreUp(["a", "a", "b", "b"], ["a", "c", "b", "c"]) → 6
        scoreUp(["a", "a", "b", "b"], ["a", "a", "b", "c"]) → 11
        scoreUp(["a", "a", "b", "b"], ["a", "a", "b", "b"]) → 16

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-ap/q13.py`
        
    Args:
        key (list[str]): The list of correct answers.
        answers (list[str]): The list of student's answers.

    Returns:
        int: The student's total score based on the comparison.
    """
    ### [Your Implementation Here]
    
    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.
    
    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.


# Unit tests for scoreUp function
import unittest

class TestScoreUp(unittest.TestCase):
    def test_scoreUp(self):
        self.assertEqual(scoreUp(["a", "a", "b", "b"], ["a", "c", "b", "c"]), 6)
        self.assertEqual(scoreUp(["a", "a", "b", "b"], ["a", "a", "b", "c"]), 11)
        self.assertEqual(scoreUp(["a", "a", "b", "b"], ["a", "a", "b", "b"]), 16)
        self.assertEqual(scoreUp(["a", "a", "b", "b"], ["?", "c", "b", "?"]), 3)
        self.assertEqual(scoreUp(["a", "a", "b", "b"], ["?", "c", "?", "?"]), -1)
        self.assertEqual(scoreUp(["a", "a", "b", "b"], ["c", "?", "b", "b"]), 7)
        self.assertEqual(scoreUp(["a", "a", "b", "b"], ["c", "?", "b", "?"]), 3)
        self.assertEqual(scoreUp(["a", "b", "c"], ["a", "c", "b"]), 2)
        self.assertEqual(scoreUp(["a", "a", "b", "b", "c", "c"], ["a", "c", "a", "c", "a", "c"]), 4)
        self.assertEqual(scoreUp(["a", "a", "b", "b", "c", "c"], ["a", "c", "?", "?", "a", "c"]), 6)
        self.assertEqual(scoreUp(["a", "a", "b", "b", "c", "c"], ["a", "c", "?", "?", "c", "c"]), 11)
        self.assertEqual(scoreUp(["a", "b", "c"], ["a", "b", "c"]), 12)

if __name__ == "__main__":
    unittest.main()
