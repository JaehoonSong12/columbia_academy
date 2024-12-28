

"""
Georgia Institute of Technology - CS1301
HW02 - Conditionals
"""

#########################################

"""
Function Name: skillLevel()
Parameters: passRate (int)
Returns: "Beginner" or "Moderate" or "Advanced" (str)
"""
def skillLevel(passRate):
    """
    This function assesses the skill level of a class based on the percentage of students who passed a diagnostic exam.

    Steps:
    1. Ask the user for the percentage of students who passed the exam (positive number between 0 and 100).
    2. Determine the skill level based on the following conditions:
       - If 25% or less pass, the skill level is "Beginner".
       - If more than 25% and 75% or less pass, the skill level is "Moderate".
       - If more than 75% pass, the skill level is "Advanced".
    3. Print the skill level.

    Assumptions:
    - The input is a valid percentage (0 to 100 inclusive).
    - The skill level is determined by exact boundary conditions as stated.
    """
    if (passRate <= 25): return "Beginner" # <- at this point, we already sorted everyone who has <= 25%
    elif (passRate <= 75): return "Moderate" # <- at this point, we already sorted everyone who has <= 75%
    else: return "Advanced"
    return # end point (termination)

#########################################

"""
Function Name: bookStore()
Parameters: item (str), walletAmount (float), quantity (int)
Returns: moneyLeftOver (float)
Description: While you wait for your exam results, you decide to head over to the Barnes and
Noble Bookstore to pick up some Georgia Tech swag for you and your close friends. A Shirt
costs $15.50, a Lanyard costs $4.25, a Sweatshirt costs $25.00, and a Mug costs $10.50.
Write a function that takes a bookstore item and checks if you can buy that item based on
the amount of money in your wallet and the quantity you want to purchase. If you can buy
the items requested, return a float that represents how much money is left in your wallet. If
you cannot buy the items, return “Not enough money!”. Round your answer to 2 decimal
places.
"""
def bookStore(item, walletAmount, quantity): # parameters: accepting values from the stack
    # [YOUR_IMPLEMENTATION]
    """
        bookStore("Shirt", 350.48, 8) 
    226.48
        bookStore("Lanyard", 200.0, 70) 
    'Not enough money!'
    """
    # conditionals to decide item prices!
    if item == "Shirt": item_price = 15.50
    if item == "Lanyard": item_price = 4.25
    if item == "Sweatshirt": item_price = 25.00
    if item == "Mug": item_price = 10.50
    # main logic
    total_price = item_price * quantity
    amount_left = float(walletAmount - (total_price))
    if walletAmount >= total_price: return round(amount_left, 2)
    else: return "'Not enough money!'"

#########################################

"""
Function Name: dinnerPlans()
Parameters: distance (int), hungerLevel (str)
Returns: transportMode (str)
"""
def dinnerPlans(distance, hungerLevel):
    # [YOUR_IMPLEMENTATION]
    return

#########################################

"""
Function Name: weekendTrip()
Parameters: distance (float), speed (float), freeTime (float)
Returns: transportMode (str)
"""
def weekendTrip(distance, speed, freeTime):
    # [YOUR_IMPLEMENTATION]
    return

#########################################

"""
Function Name: textFriends()
Parameters: distance (float), speed (float), freeTime (float), numSnacks (int), numFriends (int)
Returns: textMsg (str)
"""
def textFriends(distance, speed, freeTime, numSnacks, numFriends):
    # [YOUR_IMPLEMENTATION]
    return