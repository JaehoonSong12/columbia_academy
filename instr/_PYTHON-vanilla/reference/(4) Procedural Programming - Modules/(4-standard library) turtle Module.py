## turtle Module
import turtle           # loads the turtle module into memory


## Library Functions (Black Boxes)

# basic settings
turtle.pencolor('red')  # change the turtle's drawing color (void, default argument: 'black')
print(turtle.pencolor())        # returns the turtle's drawing color (return: str)

turtle.bgcolor('green') # change the background color (void, default argument: 'white')
print(turtle.bgcolor())         # returns the turtle's background color (return: str)

turtle.setup(640, 480)  # specify a size for the graphics window (void)

turtle.speed(1)         # change the speed of the animation (void, argument is rounded to an integer 0 - 10)
print(turtle.speed())           # returns the turtle's current speed (return: int)

turtle.pensize(2)       # changes the width of the pen (void, default argument: 1)
print(turtle.pensize())         # returns the pen's current size (return: numeric)

turtle.hideturtle()     # hides the turtle in its window (void)
turtle.showturtle()     # displays the turtle in its window (void, default)
print(turtle.isvisible())       # returns True/False if the turtle is visible (return: bool)

# pen controlling
turtle.penup()          # raise the pen (void)
turtle.pendown()        # lower the pen (void, default)
print(turtle.isdown())          # returns True/False if the pen is down (return: bool)

# movement
turtle.forward(50)      # moves the turtle forward 100 pixels (void)

turtle.left(90)         # turns the turtle left by 90 degrees (void)

turtle.right(90)        # turns the turtle right by 90 degrees (void)

turtle.setheading(150)  # sets the turtle's heading to a specific angle (default argument: 0)
print(turtle.heading())         # returns the turtle's current heading (return: float)

turtle.goto(-100, -100) # move and draw the turtle to a specific position
print(turtle.pos())             # returns the turtle's current position (return: str)
print(turtle.xcor())            # returns the turtle's current x-coordinate (return: numeric)
print(turtle.ycor())            # returns the turtle's current y-coordinate (return: numeric)

# resetting the screen
turtle.clear()          # erases all drawings
turtle.reset()          # erases all drawings and resets color / position
turtle.clearscreen()    # erases all drawings and resets color / position / bgcolor

# drawing technique
turtle.circle(20)       # draws a circle with radius 10 pixels
turtle.dot()            # darws a simple dot
turtle.write('Hi guys') # displays the text in the graphics window

turtle.fillcolor('red') # fill color with red (default argument: 'black')
print(turtle.fillcolor())       # returns the turtle's current fill color (return: str)
turtle.begin_fill()     # fills a shape with a color (begin)
turtle.goto(100, -100)
turtle.goto(-100, -100)
turtle.goto(0, 0)
turtle.end_fill()       # fills a shape with a color (end) (!) shape does not need to be enclosed

# End of Drawing
turtle.done()           # keeps the graphics window to remain open (IDLE does not need)
