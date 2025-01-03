

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
    """
    This function determines whether the group should walk or take an 
    Uber to the restaurant based on the distance and hunger level provided.

    Decision Table:
    | distance | hungerLevel     | decision |
    |----------|-----------------|----------|
    | <= 7     | Not Hungry      | Walk     |
    | <= 5     | Slightly Hungry | Walk     |
    | <= 3     | Hungry          | Walk     |
    | <= 1     | Very Hungry     | Walk     |
    | > 7      | Not Hungry      | Uber     |
    | > 5      | Slightly Hungry | Uber     |
    | > 3      | Hungry          | Uber     |
    | > 1      | Very Hungry     | Uber     |

    Steps:
    1. Check the `hungerLevel` and apply the corresponding distance threshold.
    2. Return "Walk" if the distance is within the threshold, otherwise 
    return "Uber".

    Assumptions:
    - The input `distance` is a non-negative integer.
    - The input `hungerLevel` is a valid string from the given set of hunger levels.
    - Outputs are case-sensitive and must match exactly "Walk" or "Uber".
    """
    if distance < 0: return "Runtime Error: Your `distance` is not valid (cannot be negative)."
    # Error Handling with Decision Structure, "early return technique", not try-catch block!
    if hungerLevel == "Not Hungry": 
        if distance <= 7: return "Walk"
        else: return "Uber"
    if hungerLevel == "Slightly Hungry":
        if distance <= 5: return "Walk"
        else: return "Uber"
    if hungerLevel == "Hungry":
        if distance <= 3: return "Walk"
        else: return "Uber"
    if hungerLevel == "Very Hungry":
        if distance <= 1: return "Walk"
        else: return "Uber"
    return "Runtime Error: Your `hungerLevel` is not valid." # Error Handling with Decision Structure, not try-catch block!
     # in python, `and` vs in other lang, `&&`

################# < Sample Runs >

# >>> dinnerPlans(4, "Slightly Hungry")
# 'Walk'

# >>> dinnerPlans(6, "Very Hungry")
# 'Uber'

# >>> dinnerPlans(6, "Starving")
# 'Runtime Error: Your `hungerLevel` is not valid.'

# >>> dinnerPlans(-1, "Very Hungry")
# 'Runtime Error: Your `distance` is not valid (cannot be negative).'



#########################################

"""
Function Name: weekendTrip()
Parameters: distance (float), speed (float), freeTime (float)
Returns: transportMode (str)
"""
def weekendTrip(distance, speed, freeTime):
    """
    This function determines the best mode of transportation to 
    visit a destination based on the distance, speed, and available 
    free time. If the travel time exceeds 20% of the free time, it returns a message indicating that the trip would take too much time. Otherwise, the function uses the following speed thresholds to determine the mode of transportation:

    Decision Table:
    | speed                 | transportMode |
    |-----------------------|---------------|
    | 2.5 <= speed <= 15    | walking       |
    | 15 < speed <= 20      | biking        |
    | speed > 20            | driving       |

    Steps:
    1. Calculate the travel time as `distance / speed`.
    2. Determine if the travel time is less than or equal to 20% of `freeTime`.
    3. If true, decide the mode of transportation based on the speed:
        - 2.5 <= speed <= 15: "walking"
        - 15 < speed <= 20: "biking"
        - speed > 20: "driving"
    4. If false, return: "Going to this destination would take too much time."

    Assumptions:
    - `distance` and `freeTime` are positive.
    - `speed` is always 2.5 mph or greater.
    - Outputs are case-sensitive and must match exactly.
    """
    PERCENT_OF = 0.2
    travelTime = distance / speed
    if speed < 2.5 and distance < 0 and freeTime < 0: 
        return "Runtime Error: Your `speed,` 'distance,' and 'freeTime' is not valid ('speed' must not be less than 2.5 and 'distance' and 'freeTime' cannot be negative)."
    if speed < 2.5 and distance < 0:
        return "Runtime Error: Your `speed` and 'distance' is not valid ('speed' must not be less than 2.5 and 'distance' cannot be negative)."
    if speed < 2.5:
        return "Runtime Error: Your `speed` is not valid (must not be less than 2.5)."
    if distance < 0 and freeTime < 0:
        return "Runtime Error: Your `distance` and 'freeTime' is not valid ('distance' and 'freeTime' cannot be negative)."
    if distance < 0: 
        return "Runtime Error: Your `distance` is not valid (cannot be negative)."
    if freeTime < 0: 
        return "Runtime Error: Your `freeTime` is not valid (cannot be negative)."
    # body
    if travelTime > (PERCENT_OF * freeTime): return "Going to this destination would take too much time."
    if speed > 20: return "driving"
    if speed >= 15: return "biking"
    return "walking"

################# < Sample Runs >

# >>> weekendTrip(7.0, 46.66, 1.0)
# 'driving'

# >>> weekendTrip(10.0, 5.0, 8.0)
# 'Runtime Error: Going to this destination would take too much time.'

# >>> weekendTrip(7.0, 46.66, -1.0)
# 'Runtime Error: Your `freeTime` is not valid (cannot be negative).'

# >>> weekendTrip(7.0, -46.66, -1.0)
# 'Runtime Error: Your `speed` is not valid (must not be less than 2.5).'

# >>> weekendTrip(0.06, 1.2, 1.0)
# 'Runtime Error: Your `speed` is not valid (must not be less than 2.5).'

# >>> weekendTrip(-7.0, -46.66, 1.0)
# 'Runtime Error: Your `distance` is not valid (cannot be negative).'


#########################################

"""
Function Name: textFriends()
Parameters: distance (float), speed (float), freeTime (float), numSnacks (int), numFriends (int)
Returns: textMsg (str)
"""
def textFriends(distance, speed, freeTime, numSnacks, numFriends):
    """
    This function determines whether a trip is feasible by calling `weekendTrip()`. 
    If the trip is feasible (travel time is ≤ 20% of free time), the function 
    calculates how snacks will be divided among friends and includes the transport 
    mode in the message. Otherwise, it returns: "Going to this destination would 
    take too much time."

    Steps:
    1. Call `weekendTrip()` to check if the trip is feasible and get the transport mode.
    2. If the trip takes too much time, return: "Going to this destination would take too much time."
    3. Calculate snacks per person as `numSnacks // numFriends`.
    4. Calculate leftover snacks as `numSnacks % numFriends`.
    5. Return a formatted text message using the transport mode.

    Assumptions:
    - All input values are valid and positive.
    - `numFriends` includes the user.
    - Outputs are case-sensitive and must match the required format.
    """
    return

################# < Sample Runs >

# >>> textFriends(25.0, 65.0, 2.5, 17, 3)
# 'If each of us gets 5 snack(s), there will be 2 left. I will be driving, who else is doing the same?'

# >>> textFriends(1.5, 2.5, 3.0, 13, 7)
# 'If each of us gets 1 snack(s), there will be 6 left. I will be walking, who else is doing the same?'