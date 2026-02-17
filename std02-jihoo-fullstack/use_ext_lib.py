import math
import numpy
import pandas as pd
from rich import print

# import matplotlib.pyplot as plt # as == alias definition



def main():
    print(f"The value of pi is:     {math.pi}")
    print(f"The value of e is:      {math.e}")




    values = [10, 20, 30, 40, 50]
    average = numpy.mean(values)
    print(f"1. Numpy (Math Mean):     {average}")

    

    values = [10, 20, 30, 40, 50]
    series = pd.Series(values)
    print("2. Pandas Mean:", series.mean())


    

    print("3. [bold blue]Fancy font[/bold blue] styling!")
    print("[italic]기울임 글씨[/italic]")
    print("[underline]밑줄 글씨[/underline]")
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
    3. pip install rich

    import subprocess
    subprocess.check_call(["python", "-m", "pip", "install", "numpy"])
    subprocess.check_call(["python", "-m", "pip", "install", "pandas"])
    subprocess.check_call(["python", "-m", "pip", "install", "rich"])



"""