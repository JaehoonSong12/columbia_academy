## Input File (Read Mode, r)
def main():
    # open Function
    infile = open('sample.txt', 'r')    # returns file object for data on the disk. (arg1: str, arg2: str, return: object)
                                        # (file exists) -> (contents read)
    
    # readline Function (Method)
    line1 = infile.readline()           # returns a line of content up to '\n' (return: str)
    line2 = infile.readline()           # (at the end of the file) -> ('\n' don't have to be included)
    line3 = infile.readline()           # (After the end of the file) -> (returns empty string)

    # rstrip Function (Method)
    line1 = line1.rstrip('\n')          # removes all duplicated strings from the right side of a string (arg: str)
    line2 = line2.rstrip('\n')
    line3 = line3.rstrip('\n')
    
    print(line1)
    print(line2)
    print(line3)
    
    # close Function (Method)
    infile.close()


def main_loop_ver1():
    # open Function
    infile = open('sample.txt', 'r')
    
    # while Loop (not prefered, prefered for records)
    line = infile.readline()    # priming read
    while (line != ''):         # special condition
        line = line.rstrip('\n')
        print(line)
        line = infile.readline()
    
    # close Function (Method)
    infile.close()


def main_loop_ver2():
    # open Function
    infile = open('sample.txt', 'r')
    
    # for Loop (prefered, not preferd for records)
    for line in infile:
        line = line.rstrip('\n')
        print(line)
    
    # close Function (Method)
    infile.close()


main()
main_loop_ver1()
main_loop_ver2()

# < Additional Information >
# readlines Function
# infile.readlines()
# 1. retuns a list of data (return: list)
#   (!) the list must be a set of string data
# 2. it does not automatically strip a newline at the end of each item
