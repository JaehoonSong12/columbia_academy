

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

#########################################

"""
Function Name: bookStore()
Parameters: item (str), walletAmount (float), quantity (int)
Returns: moneyLeftOver (float)
"""
def bookStore(item, walletAmount, quantity):
    # [YOUR_IMPLEMENTATION]
    return

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