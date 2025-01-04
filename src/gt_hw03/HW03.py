import math

"""
Georgia Institute of Technology - CS1301
HW03 - Iteration
"""

#########################################

"""
Function Name: movieNight()
Parameters: a caption (str)
Returns: the fixed caption (str)
"""
def movieNight(caption):
    """
    This function processes a movie caption and removes all numeric characters. 
    It returns the fixed caption as a string without altering the order of other characters.

    Steps:
    1. Use a string method or regular expression to remove all numeric characters from the caption.
    2. Return the cleaned caption.

    Assumptions:
    - The input `caption` is a non-empty string.
    - The function preserves spaces, punctuation, and letter case.
    """
    # Highest abstraction, stage #3, important function: in <array>
    cleaned_caption = ""
    # each time, 
    for each_character in caption: 
        if not each_character.isdigit(): cleaned_caption += each_character
        # result = result + each_character # original way
        # result = each_character + result  # reversed way
        # result = each_character + result + each_character # palindrome way
    
    # Lostest abstraction, stage #1, important function: len(<array>)
    cleaned_caption = ""
    index = 0
    while (index < len(caption)):
        if not caption[index].isdigit(): cleaned_caption += caption[index]
        index += 1
    
    ## Middle abstraction, stage #2, important function: range(<int>)
    cleaned_caption = ""
    for index in range(len(caption)):
        if not caption[index].isdigit(): cleaned_caption += caption[index]

    # result = ""
    # for each_character in string_a_set_of_charactors:
    #     if not f"{each_character}".isdigit(): print(each_character)  # Process each character here
    
    return cleaned_caption

################# < Sample Runs >

# >>> caption = "Mr. and M4rs. Dursley of nu28mber four, Privet Drive, wer903e 
# proud to say th6at they we6re perfectly norm3al, tha894nk you ve89ry much." 

# >>> movieNight(caption)
# 'Mr. and Mrs. Dursley of number four, Privet Drive, were proud to say that they 
# were perfectly normal, thank you very much.'


#########################################

"""
Function Name: iceCream()
Parameters: flavor (str), number of vowels (int)
Returns: a sentence (str)
"""
def iceCream(flavor, vowels):
    # [YOUR_IMPLEMENTATION]
    return

#########################################

"""
Function Name: dreamCar()
Parameters: car price (float), bank balance(float), interest rate (float)
Returns: number of years (int)
"""
def dreamCar(price, balance, rate):
    # [YOUR_IMPLEMENTATION]
    return

#########################################

"""
Function Name: battleship()
Parameters: board size (int)
Returns: None (NoneType)
"""
def battleship(size):
    # [YOUR_IMPLEMENTATION]
    return

#########################################

"""
Function: tennisMatch()
Parameters: player 1 (str), player 2 (str), match record (str)
Returns: winner (str)
"""
def tennisMatch(p1, p2, record):
    # [YOUR_IMPLEMENTATION]
    return
