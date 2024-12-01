# cli.py

import sys
import os

def set_modules(base_dir):
    """
    Recursively adds base_dir and all subdirectories of base_dir to the Python path.
    """
    sys.path.append(base_dir)
    for root, dirs, _ in os.walk(base_dir):
        for directory in dirs:
            full_path = os.path.join(root, directory)
            if full_path not in sys.path: sys.path.append(full_path)






im_global_var = 10
# import hw00
# import gt_hw01.HW01
# import hw01
import december_escapes.app

def main():
    print("Updated Python path:")
    print("\n".join(sys.path))
    set_modules(os.path.dirname(os.path.abspath(__file__)))
    print("Updated Python path:")
    print("\n".join(sys.path))
    print("App is running...")
    # hw01.main()  # Test HW01
    # hw01.main()  # Test HW02
    # hw03.main()  # Test HW03
    # hw04.main()  # Test HW04
    # hw05.main()  # Test HW05
    # hw06.main()  # Test HW06
    # hw07.main()  # Test HW07
    # hw08.main()  # Test HW08
    # hw09.main()  # Test HW09
    # hw10.main()  # Test HW10
    # hw11.main()  # Test HW11
    # hw12.main()  # Test HW12
    
    # ########################################
    # ############### GT_HW01
    # ########################################
    # gt_hw01.HW01.dominosTime()  # Test GT_HW01
    # gt_hw01.HW01.tipAndSplit()  # Test GT_HW01
    # gt_hw01.HW01.youtuber()  # Test GT_HW01
    # gt_hw01.HW01.bathBomb()  # Test GT_HW01


    # ########################################
    # ############### December Escapes
    # ########################################
    # december_escapes.app.main()


    # hw02.main()  # Test GT_HW02
    # hw03.main()  # Test GT_HW03
    # hw04.main()  # Test GT_HW04
    # hw05.main()  # Test GT_HW05
    # hw06.main()  # Test GT_HW06
    # hw07.main()  # Test GT_HW07
    # hw08.main()  # Test GT_HW08
    # hw09.main()  # Test GT_HW09
    # hw10.main()  # Test GT_HW10
    # hw11.main()  # Test GT_HW11
    # hw12.main()  # Test GT_HW12


if __name__ == "__main__":
    main()