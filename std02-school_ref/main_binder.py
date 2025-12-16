import ctypes # C library binding module
import os
import sys

def main():
    """
    Main execution function to demonstrate binding C code with Python.
    
    This script performs the following steps:
    1. Locates the shared library (.so) file.
    2. Loads the library using ctypes.
    3. Configures argument and return types for C functions.
    4. Executes the C functions.
    """

    # --------------------------------------------------------------------------
    # 1. Locate the Shared Library
    # --------------------------------------------------------------------------
    
    # Get the absolute path to the directory where this python script is running
    # This ensures we find the .so file even if we run the script from a different folder
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Define the library filename (must match the TARGET in Makefile)
    lib_name = "libmain.so"
    lib_path = os.path.join(script_dir, lib_name)

    # Check if the library exists before attempting to load
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

    # --------------------------------------------------------------------------
    # 3. Call a C Function
    # --------------------------------------------------------------------------

    # EXAMPLE 1: Calling a simple void function (e.g., if you renamed main to run_app)
    # Assume hello.c has a function: void run_app(void)
    
    # We check if the function exists in the library to avoid crashes
    if hasattr(c_lib, 'runApp'):
        print("\n--- Calling C function 'run_app' ---")
        c_lib.runApp()
    else:
        # If you didn't rename main(), you might just be loading the library logic.
        # Note: You can't easily call 'main' directly because of symbol collisions 
        # and argc/argv complexity. It is highly recommended to expose specific 
        # functions in your C code.
        print("\nFunction 'run_app' not found. "
              "Ensure you have a specific function to call in your C code.")

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