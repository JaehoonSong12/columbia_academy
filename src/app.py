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
