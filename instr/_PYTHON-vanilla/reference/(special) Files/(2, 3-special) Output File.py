## Output File (Writing Mode, w)
def main():
    # open Function
    outfile = open('sample.txt', 'w')   # returns file object for data on the disk. (arg1: str, arg2: str, return: object)
                                        # (file exists) -> (contents erased)
                                        # (file doesn't exist) -> (create a file)
    
    # write Function (Method)
    outfile.write('First Data' + '\n')  # writes data to a file. (arg: str)
    outfile.write('Second Data' + '\n') # (!) '\n' is concatenated for reading file
    
    # close Function (Method)
    outfile.close()                     # forces any unsaved data in buffer to be written to the file.

main()

# < Additional Information >
# writelines Function
# outfile.writelines(list)
# 1. writes a list of data to a file (arg: list)
#   (!) the list must be a set of string data
# 2. it does not automatically write a newline at the end of each item
