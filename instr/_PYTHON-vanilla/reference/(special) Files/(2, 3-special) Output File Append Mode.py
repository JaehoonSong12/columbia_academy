## Output File (Append Mode, a)
def main():
    # open Function
    outfile = open('sample.txt', 'a')   # returns file object for data on the disk. (arg1: str, arg2: str, return: object)
                                        # (file exists) -> (contents appended)
                                        # (file doesn't exist) -> (create a file)
    
    # write Function (Method)
    outfile.write('Hello there' + '\n') # writes data to a file. (arg: str)
    
    # close Function (Method)
    outfile.close()                     # forces any unsaved data in buffer to be written to the file.

main()
