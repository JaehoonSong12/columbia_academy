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