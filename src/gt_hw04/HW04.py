"""
Georgia Institute of Technology - CS1301
HW04 - Strings, Indexing and Lists (Arrays)
"""

#########################################

"""
Function Name: findMax()
Parameters: a caption list of numbers (list), start index (int), stop index (int)
Returns: highest number (int)
"""
def findMax(theNumbersMason, theStart, theEnd):
    """
    Description:
    This function determines the maximum value within a specified range of a list. 
    The range is defined by the `start` and `stop` indices, both inclusive. 
    The function iterates through the sublist defined by the indices and identifies the highest value.

    Steps:
    1. Initialize a variable, `max_value`, to hold the highest number found so far. 
       Set it to the first element in the range (numbers[start]).
    2. Iterate through the list from the `start` index to the `stop` index (inclusive).
    3. For each number, compare it to `max_value`. If the current number is greater, update `max_value`.
    4. Return the `max_value` after completing the iteration.

    Assumptions:
    - The `numbers` list is non-empty and contains unique integers.
    - The `start` and `stop` indices are valid and within the range of the list.
    - The `start` index is less than or equal to the `stop` index.

    Notes:
    - The function avoids using the built-in `max()` function for educational purposes.
    """
    # theNumbersMason = [1, 8, 3, 2, -4]
    # theStart = 2
    ##### dummy variable
    i = theStart # dummy variable for indexing, use it for processing
    max_value = theNumbersMason[theStart]
    # theEnd = 4

    while i <= theEnd:
        if max_value < theNumbersMason[i]:
            max_value = theNumbersMason[i]
        i += 1
    return max_value

# [100, 1, 2, 3, 100, 1, 2, 3]




################# < Sample Runs >

# >>> findMax([1, 8, 3, 2, -4], 2, 4)
# 3

# >>> findMax([3, 0, 7, 3, 2], 0, 4)
# 7









#########################################





"""
Function Name: fruitPie()
Parameters: list of fruits (list), minimum quantity (int)
Returns: list of fruits (list)
"""
def fruitPie(theFruit, theMin):
    # [YOUR_IMPLEMENTATION]
    COLS = 2
    i = 0
    list_of_fruits = []
    while(i < len(theFruit)):
        if theFruit[i + 1] >= theMin:
            list_of_fruits.append(theFruit[i])
        # print(f"fruit: {theFruit[i]}")
        # print(f"quantity: {theFruit[i + 1]}")
        i += COLS
    return list_of_fruits

#########################################

"""
Function Name: replaceWord()
Parameters: initial sentence (str), replacement word (str)
Returns: corrected sentence (str)
"""
def replaceWord(sentence, word):
    # [YOUR_IMPLEMENTATION]
    split_sentence = sentence.split()
    corrected_sentence_array = []
    for word_in_sentence in split_sentence:
        if len(word_in_sentence) >= 5:
            corrected_sentence_array.append(word)
        else:
            corrected_sentence_array.append(word_in_sentence)
    corrected_sentence = ""
    for corrected_word in corrected_sentence_array:
        corrected_sentence += corrected_word + " "
    return corrected_sentence
    

#########################################

""")
Function Name: highestSum()
Parameters: list of strings (strings)
Returns: index of string with the highest sum (int)
"""
def highestSum(theStrings):
    # [YOUR_IMPLEMENTATION]
    index = 0
    max_value = 0
    max_index = 0
    for string in theStrings:
        sum = 0
        for char in string:
            if char.isdigit():
                sum = sum + int(char)
        if max_value < sum:
            max_value = sum
            max_index = index
        index += 1
    return max_index
    

#########################################

"""
Function: sublist()
Parameters: alist (list), blist (list)
Returns: True or False (`boolean`)
"""
def sublist(aList, bList):
    # [YOUR_IMPLEMENTATION]
    result = False
    if len(aList) < len(bList):
        return False
    
    for i in range(len(aList) - len(bList) + 1):
        if bList[0] == aList[i]:
            result = True
            for j in range(len(bList)):
                if bList[j] != aList[i + j]:
                    result = False
            if (result): return True
    return result