## Functions
# grobal variable
global_var = 'Global'   # global variable (immutable)

# main Function
def main():     # main function starts the program

    print('\nProgram executes: ')
    function1()
    function2()
    function3()

    global global_var   # global keyword to make the global variable mutable
    global_var = 'new'
    print(global_var)
    # (!) Don't use global variable at all, just use it as a global constant

    ex_var = 20             # local variable can be used only within a function
    print('Value of example variable:', ex_var)
    local_var()

    x = function4()
    print(x)
    x, y = function5()  # multiple assignment
    print(x, y)
    
    arg_by_position('A', 'B')           # positional arguments
    arg_by_keyword(var2='B', var1='A')  # keyword arguments
    arg_mixed('A', var3='C', var2='B')  # mixed arguments (positional must be first)


# void Functions
def function1():
    print('This program is')
def function2():
    print('modularized by')
def function3():
    print('divide and conquer!\n')


# Local Variable
def local_var():
    ex_var = 40             # local variable is hidden from other functions (Name Duplication)
    print('Value of example variable:', ex_var)


# Value-Returning Functions
def function4():    # returning a single value
    var = input('Enter your input to return: ')
    return var
def function5():    # returning multiple values
    var1 = input('Enter your fisrt input to return: ')
    var2 = input('Enter your fisrt input to return: ')
    return var1, var2

# Parameters
def arg_by_position(var1, var2):  # parameters are local variables for receiving arguments
    print(var1 + var2)
def arg_by_keyword(var1, var2):
    print(var1 + var2)
def arg_mixed(var1, var2, var3):
    print(var1 + var2 + var3)


## Function Call (after all the function definitions)
main()  # execute the mainline logic


# Function Naming Rule:
# 1. keywords cannot be used for function names
# 2. Spaces cannot be used for function names
# 3. A digit cannot be used in the first letter of function name
# 4. function names are case-sensitive

# Function Structures Rule:
# 1. function header begins with the keyword, def, followed by the funtion name
# 2. Python interpreter uses the indentation for places the block begins and ends
