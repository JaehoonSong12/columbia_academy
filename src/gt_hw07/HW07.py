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
    file = open(filename, "r")
    data = file.read()
    file.close()
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