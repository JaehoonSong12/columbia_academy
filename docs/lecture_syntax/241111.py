# Open the file in write mode and write some strings
f = open('myfile.txt', 'w')
f.write("Hello, this is the first line.\n")
f.write("This is the second line.\n")
f.write("And this is the third line.\n")
f.close()  # Close the file after writing

# Open the file in read mode and print its contents
f = open('myfile.txt', 'r')
content = f.read()  # Read the entire file
print(content)
f.close()  # Close the file after reading



# variable define (syntax)
myVar = "Hello World World"

# API define (syntax)
def myAPI(mycomment):
    print("You are calling me, but you don't need to know anything (abstraction)")
    print(mycomment)





# API is the core concept for abstraction
# abstraction means hiding all the actions (semantics 
# by just calling the API, offers simpler syntax.)

# (1) manual coding
print("You are calling me, but you don't need to know anything (abstraction)")
print("Hello World World")

# (2) API call (syntax)
myAPI(myVar) # version 1: using variable, you can bring up data on your RAM
myAPI("my data I'm directly writing") # version 2: not using varible, temproray use (hard-code)
# "Don't do hardcode!"

# API - general term for programming.
# function - a special name indicating "API" role in python programming language





# syntax for python: <target>(<arguments>)        
# syntax for bash: <target> <arguments>        
#                                       <- very like English or Korean ... grammer
#                                       <- a text rules you have to write for running something 
### target == print
### arguments == ["Hello World"]
### 

# semantics: how your memory is going to work based on your given syntax

## Syntax -> command, semantics -> behavior (is the one that is abstracted out.)






#########################################

"""
Function Name: listen()
Parameters: N/A
Returns: None
"""
def listen():
    songs = int(input("How many songs did you listen to? "))
    podcasts = int(input("How many podcasts did you listen to? "))
    totalMinutes = songs * 3 + podcasts * 25
    print("By listening to " + str(songs) + " songs and " + str(podcasts) + " podcasts, you have spent " + str(totalMinutes // 60) + " hours and " + str(totalMinutes % 60) + " minutes on Spotify.")

#########################################