"""
Georgia Institute of Technology - CS1301
HW01 - Functions and Expressions

Usage:
    python HW01.py
"""


# INPUT / OUPUT
# python code, syntax (grammer)
# 1. input(message)
# 2. print(message)    ** optional: print(f"message") format string 


"""
Function Name: dominosTime()
Parameters: N/A
Returns: None
"""
def dominosTime():
    pizzas = int(input("How many pizzas do you want? "))
    pasta = int(input("How many orders of pasta do you want? "))
    wings = int(input("How many orders of chicken wings do you want? "))

    print(f"You ordered {pizzas} pizzas")
    # print(f"By ordering {pizzas} pizzas, {pasta} orders of pasta, "
    #       f"and {wings} orders of chicken wings, your "
    #       f"order total is ${12*pizzas + 6*pasta + 8*wings}.")
    return

# Test
dominosTime()






"""
Function Name: tipAndSplit()
Parameters: N/A
Returns: None
"""
def tipAndSplit():
    """
    This function calculates the tip for a food delivery and splits the 
    total cost (including the tip) among friends.

    Steps:
    1. Ask the user for the order total (positive integer).
    2. Ask the user for the tip percentage they want to give the driver (positive integer).
    3. Ask the user for the number of friends splitting the total (positive integer).
    4. Calculate the tip using the formula:
       Tip = (Order Total x Tip Percentage) / 100.
    5. Calculate the total cost by adding the tip to the order total.
    6. Divide the total cost by the number of friends to get the amount each friend must pay.
    7. Round the tip and each friend's share to 2 decimal places.
    8. Print the tip and the amount each friend must pay.

    Assumptions:
    - All inputs are positive integers.
    - Outputs are rounded to 2 decimal places for clarity.
    """


    return

# # Test
# tipAndSplit()
