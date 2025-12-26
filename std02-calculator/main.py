import os
import sys

import ctypes # C library binding module


def load_c_library(lib_name):
    """
    Load the C shared library using ctypes.
    This function performs the following steps:
    1. Locate the shared library (.so) file.
    2. Load the library using ctypes.
    3. return the loaded library object.
    """
    # --------------------------------------------------------------------------
    # 1. Locate the Shared Library
    # --------------------------------------------------------------------------
    script_dir = os.path.dirname(os.path.abspath(__file__))
    lib_path = os.path.join(script_dir, lib_name)
    if not os.path.exists(lib_path):
        print(f"Error: Could not find {lib_name} at {lib_path}")
        print("Did you run 'make' to build the C library first?")
        sys.exit(1)
    # --------------------------------------------------------------------------
    # 2. Load the Library
    # --------------------------------------------------------------------------
    try:
        # ctypes.CDLL loads the shared object file
        c_lib = ctypes.CDLL(lib_path)
    except OSError as e:
        print(f"Error loading library: {e}")
        sys.exit(1)
    print(f"Successfully loaded {lib_name}")
    return c_lib






def main():
    
    c_lib = load_c_library("libmain.so")



    c_lib.quiz_time()
    
    
    # c_function_name = "quiz_time"
    # if hasattr(c_lib, c_function_name): c_lib.quiz_time()
    # else: print(f"Function '{c_function_name}' not found. Ensure you have a specific function to call in your C code.")




    # # EXAMPLE 2: Calling a function with arguments and return values
    # # Let's assume cs50.c has a function: int add(int a, int b)
    # if hasattr(c_lib, 'add'):
    #     print("\n--- Calling C function 'add' ---")
        
    #     # Explicitly define argument types (good practice for safety)
    #     # c_int corresponds to C's int type
    #     c_lib.add.argtypes = [ctypes.c_int, ctypes.c_int]
        
    #     # Explicitly define return type
    #     c_lib.add.restype = ctypes.c_int
        
    #     # Call the function
    #     result = c_lib.add(10, 20)
    #     print(f"Result from C 'add(10, 20)': {result}")

if __name__ == "__main__":
    main()