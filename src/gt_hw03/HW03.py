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
    
    ## Middle abstraction, stage #2, important function: range(<int>)
    cleaned_caption = ""
    for index in range(len(caption)):
        if not caption[index].isdigit(): cleaned_caption += caption[index]
    
    # Lostest abstraction, stage #1, important function: len(<array>)
    cleaned_caption = ""
    index = 0
    while (index < len(caption)):
        if not caption[index].isdigit(): cleaned_caption += caption[index]
        index += 1

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
def iceCream(flavor, min_vowels):
    """
    Function Name: iceCream()
    Parameters: 
    - flavor (str): The name of the ice cream flavor.
    - min_vowels (int): The number of vowels to compare against.
    Returns: 
    - str: A sentence indicating whether the ice cream flavor has more vowels than the specified number.

    Description:
    This function determines whether an ice cream flavor contains more vowels than a given number and 
    returns a formatted sentence based on the result.

    Steps:
    1. Convert the `flavor` string to lowercase to ensure consistent vowel counting.
    2. Count the vowels ('a', 'e', 'i', 'o', 'u') in the `flavor` string.
    3. Compare the vowel count to the given `number`.
    - If the vowel count is greater, return: 
        'Yes, {flavor} ice cream has more than {number} vowels!'
    - Otherwise, return:
        'No, {flavor} ice cream doesn't have more than {number} vowels!'

    Assumptions:
    - The `flavor` is a valid non-empty string.
    - The `number` is a non-negative integer.
    - Outputs must exactly match the specified format.
    """

    def isVowel(character): ## strings are case-senstive
        character = character.lower()
        if character == 'a': return True
        if character == 'o': return True
        if character == 'i': return True
        if character == 'e': return True
        if character == 'u': return True
        return False

    total_number_of_vowels = 0 # for logic
    for i in range(len(flavor)): # [1][2][3]: range gives you an array [0,1,2,3,4,....,len(flavor) - 1]
        if (isVowel(flavor[i])): total_number_of_vowels += 1

    if total_number_of_vowels > min_vowels:
        return f"Yes, {flavor.lower()} ice cream has more than {min_vowels} vowels!"
    return f"No, {flavor.lower()} ice cream doesn't have more than {min_vowels} vowels!"


################# < Sample Runs >

# >>> iceCream("ChoCoLaTe", 3)
# 'Yes, chocolate ice cream has more than 3 vowels!'

# >>> iceCream("strawBERRY", 2)
# 'No, strawberry ice cream doesn't have more than 2 vowels!'

#########################################

"""
Function Name: dreamCar()
Parameters: car price (float), bank balance(float), interest rate (float)
Returns: number of years (int)
Description: While you're eating your ice cream, you start thinking about your dream car.
You want to figure out how long it will take for you to save up and buy that car. Luckily,
you've got some money in the bank that's growing every year with compound interest. Given
the price of your dream car ( float ), the money you currently have in the bank ( float ), and
the interest rate of your bank account ( float ) given as a percent, return how many years it
will take for you to have enough money for your dream car.
"""
def dreamCar(price, balance, rate):
    """
    Function Name: dreamCar()
    Parameters: 
    - car_price (float): The price of your dream car.
    - bank_balance (float): The initial amount of money in your bank account.
    - interest_rate (float): The annual interest rate (in percentage) applied to the bank balance.

    Returns: 
    - int: The number of years it will take to save enough money to buy the car.

    Description:
    This function calculates how many years it will take to save up enough money for your dream car, given an initial bank balance and a compound interest rate. Each year, the bank balance grows by the interest rate, and the function iterates year by year until the balance meets or exceeds the car's price.

    Steps:
    1. Initialize a counter for the number of years (`years = 0`).
    2. While the `bank_balance` is less than the `car_price`:
    - Increment the `bank_balance` by the compound interest (using the formula: `bank_balance += bank_balance * (interest_rate / 100)`).
    - Increment the `years` counter.
    3. Once the `bank_balance` is sufficient, return the `years` counter.

    Assumptions:
    - All input values are positive numbers.
    - Interest compounds annually.
    - Outputs must be integers representing whole years.
    """
    
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
