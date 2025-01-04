<!-- 
 @requires
 1. VSCode extension: Markdown Preview Enhanced
 2. Shortcut: 'Ctrl' + 'Shift' + 'V'
 3. Split: Drag to right (->)

 @requires
 1. VSCode extension: Markdown All in One
 2. `File` > `Preferences` > `Keyboard Shortcuts`
 3. toggle code span > `Ctrl + '`
 4. toggle code block > `Ctrl + Shift + '`

 @usage
 1. End of Proof (Q.E.D.): <div style="text-align: right;">&#11035;</div>
 2. End of Each Section: 

     <br /><br /><br />

     ---



     <p align="right">(<a href="#readme-top">back to top</a>)</p>

 3. ![image_title_](images/imagefile.png)
 4. [url_title](URL)
 -->
<!-- Anchor Tag (Object) for "back to top" -->
<a id="readme-top"></a> 

Here is where you are going to note all the homeworks!

Try to use Markdown language using Google search, stackoverflow, and chatGPT, as well!

What to do for the HW!
1. `.\src\gt_hw02\HW02.py`: implement the last function.
2. `.\src\cli.py`: Write a note for the following contents!
   - Abstract Data Type (ADT)
   - Array
   - Array of Primitive Data Types
   - What is "index" of array?
   - String vs Array of Char
   - for loop vs while loop

```python
cars = ["Ford", "Volvo", "BMW"]

# array, the start of Abstract Data Type (ADT)
integers = [1, 2, 3, 5]
real_numbers = [2.4, 1.5, 2.3]
characters = ['H', 'e', 'l', 'l', 'o']

# lv1 of ADT, string
my_string = "Hello"

result = "" # null
for x in characters:
  result += x # result = result + char
print(result)

result = ""
for x in my_string: # ['H', 'e', 'l', 'l', 'o']
  result = result + x
print(result)

result = ""
x = 0
# ['H', 'e', 'l', 'l', 'o']
#  'H' == index 0            my_string[0]
#  'e' == index 1            my_string[1]
#  'l' == index 2            my_string[2]
#  'l' == index 3            my_string[3]
#  'o' == index 4            my_string[4]
while (x < len(my_string)): # x < 5
  result = result + my_string[x]
  x = x + 1
print(result)

sum = 0.0
for y in real_numbers:
  sum += y
print(sum)
```
3. `.\src\gt_hw03\HW03.py`: [optional] try to implement the first function. 

## Your Notes Here (in Markdown Format)