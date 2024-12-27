## Exceptions (Runtime Error)
print(4/0)                  # ZeroDivisionError
float('forty')              # ValueError
file = open('bad_file.txt') # FileNotFoundError

# How to know more on exceptions:
# 1. Run a program and look at the traceback error messages
# 2. Consult the Python documentation, record the exceptions


## Exception Handler
try:                                    # try/except statement (single exeption)
    # try suite                         # (exception predicted) -> (handler executes) -> (go on)
    print(4/0)                          # (no exception) -> (handler does not execute)-> (go on)
except ZeroDivisionError:               # (exception unpredicted) -> (program halts)
    # handler
    print('Error: ZeroDivisionError')


try:                                    # try/except statement (multiple exeptions)
    float('forty')                      # (exception) -> (handler executes) -> (go on)
    print(4/0)                          # (no exception) -> (handler does not execute)-> (go on)
    file = open('bad_file.txt') 
except ZeroDivisionError:
    print('Error: ZeroDivisionError')
except ValueError:
    print('Error: ValueError')
except FileNotFoundError:
    print('Error: FileNotFoundError')
except:  # except AllErrors
    print('Some Error has been occured!')


try:                                    # try/except/else statement
    print(2 + 4)                        # (exception) -> (handler executes) -> (go on)
except:                                 # (no exception) -> (else suite executes)-> (go on)
    print('Error has been occured!')    
else:
    # else suite
    print('No exceptions!')


try:                                    # try/except/finally statement        
    float('forty')                      # (exception) -> (handler executes) -> (final suite executes) -> (go on)
except:                                 # (no exception) -> (final suite executes) -> (go on)
    print('Error has been occured!')    
finally:
    # finally suite
    print('Ending Comment')


## Default Error Message
try:
    print(4/0)
except ZeroDivisionError as exception_obj:
    print(exception_obj) 
except Exception as exception_obj:
    print(exception_obj)

# exception object displays the default error message
