#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW07 - File I/O & CSV
"""

"""
Function Name: findCuisine()
Parameters: filename (str), cuisine (str)
Returns: list of restaurants (list)
"""

def findCuisine(filename, cuisine):
    # [YOUR_IMPLEMENTATION]
    #### file IO API
    file = open(filename, "r")  # [PP, to generate an object] vs OOP
    data = file.read()          # PP vs [OOP, to operate]
    file.close()                # PP vs [OOP, to operate]
    #### convential procedual coding
    processed_data = data.split("\n\n")
    restaurants_same_cuisine = []
    for record in processed_data:
        fields_arr = record.split("\n")
        # print(fields_arr)
        if fields_arr[1] == cuisine:
            restaurants_same_cuisine.append(fields_arr[0])
            
    return restaurants_same_cuisine
    

"""
Function Name: restaurantFilter()
Parameters: filename (str)
Returns: dictionary that maps cuisine type (str) to a 
list of restaurants of the same cuisine type (list)
"""

def restaurantFilter(filename):
    # [YOUR_IMPLEMENTATION]
    #### file IO API        ("r" = read mode)
    file = open(filename, "r")  # [PP, to generate an object] vs OOP
    data = file.read()          # PP vs [OOP, to operate]
    file.close()                # PP vs [OOP, to operate]
    #### convential procedual coding
    processed_data = data.split("\n\n")
    dict_object = {} # <- empty <dict>
    for row in processed_data:
        columns = row.split("\n")
        key = columns[1]
        value = columns[0]
        if key not in dict_object: dict_object[key] = []
        dict_object[key].append(value)            # <<< f(x) = y
    
    ## Extra Curricular (Serialization)
    import json # json library, API, to convert (or serialize) a dict to a string
    json_string = json.dumps(dict_object, indent=2)
    file = open('./gt_hw07/restaurants.json', 'w') # ("w" = write mode)
    file.write(json_string)
    file.close()

    return dict_object

# {
#     'Mexican': ['Taco Bell', 'La Parilla'], 
#     'American': ['Cookout', "McDonald's", "Wendy's", 'Chickfila'], 
#     'Italian': ['Olive Garden', 'Twisted Kitchen'], 'Greek': ['Gyro Bros'], 
#     'Chinese': ['Panda Express'], 
#     'Japanese': ['Momonoki']
# }

# JSON (JavaScript Object Notation) is a lightweight data 
# interchange format (string) that is easy to read and write for 
# humans and easy to parse for machines. It is commonly 
# used for data storage, APIs, and configuration files.


## computer ((dict)) ---------------- commnuniate (dict) ------------------- computer ((dict))




"""
Function Name: createDirectory()
Parameters: filename (str), output filename (str)
Returns: None (NoneType)
"""

def createDirectory(inputfile, outputfile):
    # [YOUR_IMPLEMENTATION]
    file = open(inputfile, "r")
    data = file.read()
    file.close()
    dict_fast_food = {}
    dict_sit_down = {}
    processed_data = data.split("\n\n")
    for row in processed_data:
        columns = row.split("\n")
        
        food_type = columns[2]
        key = columns[0]
        value = columns[1]
        print(f"key: {key}, value: {value}, food-type: {food_type}")

        if food_type == "Fast Food":
            dict_fast_food[key] = value
        if food_type == "Sit-down":
            dict_sit_down[key] = value
    
    fast_food_array = sorted(dict_fast_food.keys())
    for key in fast_food_array:
        print(f"sorted key: {key}, sorted value: {dict_fast_food[key]}")
    
    print(dict_sit_down)
    sit_down_array = sorted(dict_sit_down.keys())

    string = "Fast Food\n"
    for key in fast_food_array:
        string += f"{key} - {value}\n"


    # file write
    serial_string = "Restaurant Directory\n"
    file = open(outputfile, 'w') # ("w" = write mode)
    file.write(serial_string)
    file.close()
    return



# Restaurant Directory
# Fast Food
# 1. Chickfila - American
# 2. Cookout - American
# 3. Gyro Bros - Greek
# 4. McDonald's - American
# 5. Panda Express - Chinese
# 6. Taco Bell - Mexican
# 7. Wendy's - American
# Sit-down
# 1. La Parilla - Mexican
# 2. Momonoki - Japanese
# 3. Olive Garden - Italian
# 4. Twisted Kitchen - Italian



"""
Function Name: infectedPercentage()
Parameters: country list(list), filename(str)
Returns: country and percentage (tuple)
"""

def infectedPercentage(countryList, filename):
    # [YOUR_IMPLEMENTATION]
    return
"""
Function Name: countryStatus()
Parameters: country list (list), filename(str)
Returns: risk dictionary (dict)
"""

def countryStatus(countryList, filename):
    # [YOUR_IMPLEMENTATION]
    return

"""
Function Name: compareRisk()
Parameters: country to compare (str), country list (list), filename(str)
Returns: compared countries (list)
"""

def compareRisk(country, countryList, filename):
    # [YOUR_IMPLEMENTATION]
    return