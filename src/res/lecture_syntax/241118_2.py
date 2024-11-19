# `Literal` means every `hard-coded values`
# you type-in in your code directly, not by the user input.
hardcoded_var = "Hey, I'm hard-coded!"
print(hardcoded_var)

# resolution #1: not to hard-code (prompt)
print("========================================= avoid of hardcode by user prompt")
prompted_var = input("Hey user, type-in your own comment, I don't want to hard-code.")
print("This is what you just type-in, not hardcoded: " + hardcoded_var)

# resolution #2: not to hard-code (file)
print("========================================= avoid of hardcode by files")
with open('./res/customData.txt', 'r') as file:
    content_var = file.read()
print(content_var)




"""
This can be just your comment
because if you don't store it, it will
destory by itself.!
"""



print("========================================= python exclusive way to store multi-line string")
triple_quoted_string_example = """
This is how to store
multi-line input
in python only
You can't do this in other programming languages.
"""
print(triple_quoted_string_example)





"""
Program 2-8 from textbook
<Question> 
What did they do in this code?
<Answer>
`top_speed` and `distance` variables were set by `assignment` 
operation with hard-coded values (literals) that are `160` and `300`
"""
# Create two variables: top_speed and distance.
top_speed = 160 
# in python lang, top_speed <- snake_case convention
# in c lang, topSpeed <- camelCase convention
distance = 300
# Display the values referenced by the variables.
print('The top speed is')
print(top_speed)
print('The distance traveled is')
print(distance)



print("========================================= why hard-code is bad example")
# hard-coded
print('The radius of a circle: ', 7)
print('The area of a circle: ', 49, 'pi')

# constant oriented (`constant` means the portion of values that will never change and dependent to the other values.)
RADIUS = 7 # in python, constants are expected to be UPPER_SNAKE_CASE convention
print('The radius of a circle: ', RADIUS)
print('The area of a circle: ', RADIUS * RADIUS, 'pi')