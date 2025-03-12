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

    ############ Seralizing 
    #### (object data (structured) in a given language env, python)
    #### to
    #### serialized string (non-structured)

    # string operation (algorithm)
    serial_string = "Restaurant Directory\n"
    serial_string += "Fast Food\n"
    fast_food_number = 0
    sit_down_number = 0
    for key in fast_food_array:
        fast_food_number += 1
        value = dict_fast_food[key]
        serial_string += f"{fast_food_number}. {key} - {value}\n"
                                            #  x - f(x), not x - y bc y is not dynamically updated
    serial_string += "Sit-Down\n"
    for key in sit_down_array:
        sit_down_number += 1
        value = dict_sit_down[key]
        serial_string += f"{sit_down_number}. {key} - {value}\n"
    
    # file write
    file = open(outputfile, 'w') # ("w" = write mode)
    file.write(serial_string)
    file.close()
    return





"""
Function Name: infectedPercentage()
Parameters: country list(list), filename(str)
Returns: country and percentage (tuple)
"""

def infectedPercentage(countryList, filename):
    # [YOUR_IMPLEMENTATION]


    ########## 1. open file (serialized string)
    f = open(filename, "r")
    data = f.read().split('\n')
    f.close()

    ########## 2. normalize/clean serial string
    data_without_colname = []
    is_first = True
    for row in data:
        if is_first: 
            is_first = False
            continue
        data_without_colname.append(row)

    ############ 3. Parsing
    #### serial string (non-structured)
    #### to
    #### object data (structured) in a given language env, python
    dictData = {} # f(x) = y, x: input, y: output, x == "countries", y == "percentage of infected individuals"
    for row in data_without_colname:
        fields = row.split(',')
        country = fields[0]
        case = int(fields[1])
        infected = int(fields[2])
        # print((country, case, infected))
        key = country
        value = round((infected / case) * 100, 2)
        dictData[key] = value
        # print((key, dictData[key]))
    
    ############ 4. Problem Solving!
    greatest_avg_country = countryList[0]
    for country in countryList:
        if dictData[country] > dictData[greatest_avg_country]:
            greatest_avg_country = country
    

    return (greatest_avg_country, dictData[greatest_avg_country]) # tuple is like a vector!




    # # example 1: Indexing (Access elements by index)
    # my_tuple = ("Python", "Java", "C++")
    # print(my_tuple[0])  # Output: Python
    # print(my_tuple[1])  # Output: Java
    # print(my_tuple[-1]) # Output: C++
    # # example 2
    # vec1 = (1,2)
    # vec2 = (3,4)
    # print(vec1 + vec2)
    # # example 3
    # fruits = ("apple", "banana", "cherry")
    # for fruit in fruits:
    #     print(fruit)



"""
Function Name: countryStatus()
Parameters: country list (list), filename(str)
Returns: risk dictionary (dict)
"""

def countryStatus(countryList, filename):
    f = open(filename, "r")
    data = f.read().split('\n')
    f.close()

    data_without_colname = []
    is_first = True
    for row in data:
        if is_first: 
            is_first = False
            continue
        data_without_colname.append(row)
    
    dict_data = {}
    for row in data_without_colname:
        fields = row.split(',')
        country = fields[0]
        case = int(fields[1])
        infected = int(fields[2])
        # print((country, case, infected))
        key = country
        value = round((infected / case) * 100, 2)
        dict_data[key] = value

    risks = ["Low Risk", "Medium Risk", "High Risk"]
    dict_data_risk = {}
    key = risks[0]
    if key not in dict_data_risk: dict_data_risk[key] = [] # defines empty array
    key = risks[1]
    if key not in dict_data_risk: dict_data_risk[key] = [] # defines empty array
    key = risks[2]
    if key not in dict_data_risk: dict_data_risk[key] = [] # defines empty array

    for country in countryList:
        if dict_data[country] <= 25:
            key = risks[0]
            dict_data_risk[key].append(country) # adds new member to the array
        elif dict_data[country] <= 65:
            key = risks[1]
            dict_data_risk[key].append(country)
        else:
            key = risks[2]
            dict_data_risk[key].append(country)

    ###### serialization
    import json # json library, API, to convert (or serialize) a dict to a string
    json_string = json.dumps(dict_data_risk, indent=2)
    return json_string

"""
Function Name: compareRisk()
Parameters: country to compare (str), country list (list), filename(str)
Returns: compared countries (list)
"""

def compareRisk(country, countryList, filename):
    # [YOUR_IMPLEMENTATION]
    return