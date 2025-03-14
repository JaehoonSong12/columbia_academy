#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW08 - APIs
"""

import requests

"""
Function Name: meetNewPeople()
Parameters: house (str)
Returns: list of people (list)
"""

def meetNewPeople(house):
    ### by instructor (Jaehoon)
    apiKey = "$2a$10$4B95LnHHtY4Rwoe2Ah34IO1urSSipQYyIhfwVvOYFAoqHaAEnOg7K"
    baseUrl = "https://www.potterapi.com/v1/"
    url = baseUrl + "characters" + "?key=" + apiKey
    r = requests.get(url)

    theData = r.json()
    outputData = []
    for x in theData:
        if "house" in x and x["house"] == house:
            if "bloodStatus" in x and x["bloodStatus"] == "pure-blood":
                if "deathEater" in x and x["deathEater"] == False:
                    outputData.append(x["name"])
    return outputData

    # [YOUR_IMPLEMENTATION]
    return None

"""
Function Name: matchingStudents()
Parameters: character name (str)
Returns: list of students (list)
"""

def matchingStudents(charName):
    ### by instructor (Jaehoon)
    apiKey = "$2a$10$4B95LnHHtY4Rwoe2Ah34IO1urSSipQYyIhfwVvOYFAoqHaAEnOg7K"
    baseUrl = "https://www.potterapi.com/v1/"
    url = baseUrl + "characters" + "?key=" + apiKey
    r = requests.get(url)
    
    # [YOUR_IMPLEMENTATION]
    return

"""
Function Name: similarCharacters()
Parameters: movieID1 (str), movieID2 (str)
Returns: number of people (int)
"""

def similarCharacters(movieID1, movieID2):
    # [YOUR_IMPLEMENTATION]
    return

"""
Function Name: spaceDrifting()
Parameters: passengers(int), max price(int)
Returns: list of valid starships (list)
"""

def spaceDrifting(passengers, maxPrice):
    # [YOUR_IMPLEMENTATION]
    return

"""
Function Name: perfectMatch()
Parameters: list of candidates (list)
Returns: list of potential matches (list)
"""

def perfectMatch(candidates):
    # [YOUR_IMPLEMENTATION]
    return