## Modules
import sample   # load a module into memory
# (!) Python interpreter will look for the module file based on the current and default location


def main():
    sample.function_1()          # functions in module can be called (dot notation)
    print(sample.function_2())

main()
