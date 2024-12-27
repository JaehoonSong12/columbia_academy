## pyplot Module
import matplotlib.pyplot as plt     # load the pyplot module as plt into memory
                                    # alias help us to shorten the prefix

## Library Functions (Black Boxes)
# plot Function
plt.plot([1, 2, 3, 4],[2, 5, 1, 8],
         marker='s')                        # creates data sets for x-axis and y-axis of a line graph (arg1: list, arg2: list, arg3: str, void)

# marker arguments
# 1. 'o' - dot
# 2. 's' - square
# 3. '*' - star
# 4. 'D' - diamond
# 5. '^' - upward triangle
# 6. 'v' - downward triangle
# 7. '>' - right pointing triangle
# 8. '<' - left pointing triangle


# xlim Function
plt.xlim(xmin=0, xmax=5)                    # change the lower and upper bound of the range of x values (keywrod arguments, void)

# ylim Function
plt.ylim(ymin=0, ymax=10)                   # change the lower and upper bound of the range of y values (keywrod arguments, void)

# xticks Function
plt.xticks([1, 2, 3, 4],
           ['one', 'two', 'three', 'four']) # customize each tick mark's label on the x-axis (arg1: list, arg2: list, void)

# yticks Function
plt.yticks([1, 2, 5, 8],
           ['one', 'two', 'five', 'eight']) # customize each tick mark's label on the y-axis (arg1: list, arg2: list, void)

# title Function
plt.title('Title of Data')                  # title to the graph (arg: str, void)

# xlabel Function
plt.xlabel('x-axis')                        # title to the x-axis (arg: str, void)

# ylabel Function
plt.ylabel('y-axis')                        # title to the y-axis (arg: str, void)

# grid Function
plt.grid(True)                              # determine if grid the graph or not (arg: bool, void)

# show Function
plt.show()                                  # displays the graph (void)
