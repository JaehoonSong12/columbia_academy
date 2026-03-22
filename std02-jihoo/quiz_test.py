# python std02-jihoo/quiz_test.py`



# -----------------------------------------------------------------
# Question 1: scores_increasing
# -----------------------------------------------------------------
def scores_increasing(scores: list[int]) -> bool:
    """
    Description:
        Given a list of scores (integers), return True if the scores are 
        in non-decreasing order - that is, each score is equal to or 
        greater than the one before.

    Examples:
        scores_increasing([1, 3, 4]) -> True
        scores_increasing([1, 3, 2]) -> False
        scores_increasing([1, 1, 4]) -> True

    Args:
        scores (list[int]): A list of integers, length 2 or more.

    Returns:
        bool: True if each score is equal or greater than the previous one.
    """
    ### [Your Implementation Here]
    for i in range(len(scores) - 1):
        if scores[i+1] < scores[i]: 
            return False
    return True


    # Case-1. If the question can be solved with 'iteration (for/while)', 
    # design the most efficient algorithm.
    
    # Case-2. If the question can be solved with 'recursion', design a 
    # correct algorithm. Since the recursion can be inefficient, use 
    # either 'tabulation' or 'memorization' to break it down into 'iteration'.
    return False



scores_increasing([1, 3, 4, 10, 2, 5])   