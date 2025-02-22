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
    #### file IO API
    file = open(filename, "r")  # [PP, to generate an object] vs OOP
    data = file.read()          # PP vs [OOP, to operate]
    file.close()                # PP vs [OOP, to operate]
    #### convential procedual coding
    processed_data = data.split("\n\n")
    print(processed_data)
    dict_object = {}
    for row in processed_data:
        columns = row.split("\n")
        key = columns[1]
        value = columns[0]
        if key in dict_object:
            print(f"the key {key} is already there.")
        else:
            print(f"the key {key} is not there.")
            dict_object[key].append(value)
        print(dict_object)

        # print(columns[0], end=",") # restaurant name
        # print(columns[1], end=",") # cuisine type
        # print(columns[2], end=",") # type of food <- we don't need it
        # for cell in columns:
        #     print(cell, end=",")
        print()
    return

"""
Function Name: createDirectory()
Parameters: filename (str), output filename (str)
Returns: None (NoneType)
"""

def createDirectory(inputfile, outputfile):
    # [YOUR_IMPLEMENTATION]
    return

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