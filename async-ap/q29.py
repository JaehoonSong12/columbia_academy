def maxSpan(nums: list[int]) -> int:
    """
    Description:
        Consider the leftmost and rightmost appearances of some value in an array.
        We'll say that the "span" is the number of elements between the two, inclusive.
        A single occurrence of a value has a span of 1.
        Return the largest span found in the given array.
        Note: Efficiency is not a priority.

    Examples:
        maxSpan([1, 2, 1, 1, 3]) → 4
        maxSpan([1, 4, 2, 1, 4, 1, 4]) → 6
        maxSpan([1, 4, 2, 1, 4, 4, 4]) → 6

    Instructions to run the tests via the CLI:
        1. Open your terminal or command prompt.
        2. Run the tests by executing: `python async-ap/q29.py`

    Args:
        nums (list[int]): The input list of integers.

    Returns:
        int: The largest span found in the array.
    """
    ### [Your Implementation Here]
    
    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.

    if len(nums) == 0:
        return 0
    
    if len(nums) == len(list(set(nums))):
        return 1


    i = 0
    current_span = 0
    while i < len(nums):
        j = i + 1
        new_span = 0
        start_span_ind = i
        end_span_ind = j
        while j < len(nums):
            if nums[j] == nums[i]:
                if j != end_span_ind:
                    end_span_ind = j
            j += 1
        new_span = end_span_ind - start_span_ind + 1
        if current_span < new_span:
            current_span = new_span
        i += 1
    return current_span
    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.


# Unit tests for maxSpan function
import unittest

class TestMaxSpan(unittest.TestCase):
    def test_maxSpan(self):
        self.assertEqual(maxSpan([1, 2, 1, 1, 3]), 4)
        self.assertEqual(maxSpan([1, 4, 2, 1, 4, 1, 4]), 6)
        self.assertEqual(maxSpan([1, 4, 2, 1, 4, 4, 4]), 6)
        self.assertEqual(maxSpan([3, 3, 3]), 3)
        self.assertEqual(maxSpan([3, 9, 3]), 3)
        self.assertEqual(maxSpan([3, 9, 9]), 2)
        self.assertEqual(maxSpan([3, 9]), 1)
        self.assertEqual(maxSpan([3, 3]), 2)
        self.assertEqual(maxSpan([]), 0)
        self.assertEqual(maxSpan([1]), 1)

if __name__ == "__main__":
    unittest.main()
