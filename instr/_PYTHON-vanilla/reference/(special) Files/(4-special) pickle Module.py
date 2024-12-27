## pickle Module
import pickle       # load the pickle module into memory


def main():
    write()
    my_dictionary = read()
    print(my_dictionary)


## Output File (Writing Binary Mode, wb)
def write():
    # open Function
    outfile = open('sample_binary.txt', 'wb')

    # dump Function (Method)
    pickle.dump({'key1': 112, 'key2': 132}, outfile)

    # close Function
    outfile.close()


## Input File (Reading Binary Mode, rb)
def read():
    # open Function
    infile = open('sample_binary.txt', 'rb')

    # load Function (Method)
    x = pickle.load(infile)     # (!) EOFError exception if the user try to read the end of file

    # close Function
    infile.close()

    return x
    
main()
