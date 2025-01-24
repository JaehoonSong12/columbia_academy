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
    - Increment the `years` counter (by 1).
    3. Once the `bank_balance` is sufficient, return the `years` counter.

    Assumptions:
    - All input values are positive numbers.
    - Interest compounds annually. (n = 1) Note**: technically, reference `./docs/math/compound_interest.md`
    - Outputs must be integers representing whole years.
    """
    years = 0
    while balance < price:
        balance += balance * (rate / 100)
        years += 1
    return years

#########################################

"""
Function Name: battleship()
Parameters: board size (int)
Returns: None (NoneType)
Description: After realizing how long it will take you to buy your dream car, you decide to
play a game of Battleship to pass the time. In Battleship, each space on the board is a coor-
dinate, marked with a letter and a number. The letter starts from 'a', and the number starts
from '1'. When given a board size, generate a Battleship board for you and your friends to
play on. You should only print the board. You will not be given a board size greater than 26.
"""
def battleship(size):
    row = None
    col = None
    for x in range(size): # [0,1,2,3,4,5]
        # [x=0] -> [x=1] -> [x=2] -> [x=3] -> [x=4] -> [x=5]
        row = chr(97 + x) # converts an integer to its corresponding character based on `ASCII code` 
        # reference: https://www.ascii-code.com/
        for y in range(size): # [0,1,2,3,4,5]
            col = y + 1
            print(f"{row}{col}", end=' ') # escape character, newline for ending of `print` function
            # [y=0] -> [y=1] -> [y=2] -> [y=3] -> [y=4] -> [y=5]
        print(end='\n')
    
    #       [y=0] -> [y=1] -> [y=2]
    # [x=0]   a1       a2      a3 '\n'
    # [x=1]   b1       b2      b3
    # [x=2]   c1       c2      c3
    return

#########################################

"""
Function: tennisMatch()
Parameters: player 1 (str), player 2 (str), match record (str)
Returns: winner (str)
"""
def tennisMatch(p1, p2, record):
    """
    Description:
    This function determines the winner of a tennis match based on the game records provided 
    in the match_record string. Each game contributes points to a player, and the player with 
    the most points in a game wins that game. The function calculates the total games won by 
    each player and determines the winner of the match.
    If both players win the same number of games, the match is declared a tie.

    Steps:
    1. Split the match_record string into individual games using '-' as a delimiter.
    2. Initialize counters for games won by p1 (player1) and p2 (player2).
    3. For each game:
        a. Count the number of '1's (points scored by p1 (player1)) and '2's (points scored by 
           p2 (player2)).
        b. Compare the counts and update the game counters for the respective player.
        c. Ignore games where the counts are equal (tie games).
    4. Compare the total games won by both players:
        a. If one player has more wins, format and return the winner string.
        b. If both players have the same number of wins, return "It's a tie!".

    Assumptions:
    - p1 (player1) and p2 (player2) are non-empty strings representing player names.
    - match_record is a valid string formatted as described, with each game separated by 
      '-' and containing only '1's and '2's.
    - Games with equal points for both players are ignored.

    Notes:
    - The function assumes there are no leading or trailing '-' in the match_record.
    """
    # [YOUR_IMPLEMENTATION]
    rounds_of_the_game = record.split('-')
    p1_game_points = 0
    p2_game_points = 0
    for round in rounds_of_the_game:
        p1_round_points = 0
        p2_round_points = 0
        for point in round:
            if ord(point) == 49: # if point == "1":
                p1_round_points += 1
            else: p2_round_points +=1
        if p1_round_points > p2_round_points:
            p1_game_points += 1
        elif p2_round_points > p1_round_points:
            p2_game_points += 1
    if p1_game_points > p2_game_points:
        winner = p1
        winner_game_points = p1_game_points
        loser_game_points = p2_game_points
    elif p2_game_points > p1_game_points:
        winner = p2
        winner_game_points = p2_game_points
        loser_game_points = p1_game_points
    if p1_game_points == p2_game_points:
        print("It's a tie!")
    else: print(f"{winner} won! The score was {winner_game_points}-{loser_game_points}.")
    return

################# < Sample Runs >

# >>> tennisMatch("Arvin", "Arushi", "11221-222-1111-11121-22111-")
# 'Arvin won! The score was 4-1.'

# >>> tennisMatch("Anthony", "Caitlin", "1122-22211-11122-1212-")
# 'It's a tie!'