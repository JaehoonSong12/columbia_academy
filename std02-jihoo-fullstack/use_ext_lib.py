import math
import numpy as np
import pandas as pd

from pyfiglet import figlet_format



# import matplotlib.pyplot as plt # as == alias definition





def main():
    print(f"The value of pi is:     {math.pi}")
    print(f"The value of e is:      {math.e}")

    print()
    print()



    values = [10, 20, 30, 40, 50]
    average = np.mean(values)
    print(f"1. Numpy (Math Mean):     {average}")
    series = pd.Series(values)
    print("2. Pandas Mean:", series.mean())

    print()
    print()




    
    size = 100000
    numpy_array = np.random.rand(size)
    pandas_series = pd.Series(numpy_array)
    numpy_memory = numpy_array.nbytes
    pandas_memory = pandas_series.memory_usage()
    print("NumPy memory:", numpy_memory, "bytes")
    print("Pandas memory:", pandas_memory, "bytes")

    print()
    print()




    arr = np.array([100, 200, 300])
    df = pd.DataFrame({"A": [100, 200, 300]})
    print("NumPy index 0:", arr[0])
    print("Pandas index 0:", df.loc[0, "A"])

    print()
    print()






    
    print(figlet_format("Hello"))
    print(figlet_format("I'm Jihoo"))


    # plt.plot(values) 
    # plt.title("4. Value Graph")
    # plt.show()




    


if __name__ == '__main__':
    main()


"""

    PYTHON (Internal Library / Python Language Environment)
    -----------------------------------------------
    requests
    Tk
    sqlite3
    math
    ...
    -----------------------------------------------


    Private Website, Python External Library (X)
    pip means "Python Installer for external Packages (Module)"
    ---------------------------------------------------
    1. pip install numpy
    2. pip install pandas
    3. pip install rprinth
    4. pip install printecream
    5. pip install pyfiglet


    import subprocess
    subprocess.check_call(["python", "-m", "pip", "install", "numpy"])
    subprocess.check_call(["python", "-m", "pip", "install", "pandas"])
    subprocess.check_call(["python", "-m", "pip", "install", "rprinth"])
    subprocess.check_call(["python", "-m", "pip", "install", "printecream"])
    subprocess.check_call(["python", "-m", "pip", "install", "pyfiglet"])



"""