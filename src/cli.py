# cli.py: this is an execution point, where Python (PVM) recognize all the python codes.

import sys



# python -c 'import sys; print("\n".join(sys.path))'


im_global_var = 10
# import hw00
# import gt_hw01.HW01
# import hw01

## Pygame project
# import december_escapes.app
# from december_escapes.app import main





# import oop_explained.sample




def encapsulation():
    print("dsadsadsad")

def main():
    # set_modules(os.path.dirname(os.path.abspath(__file__)))
    print("Updated Python path:")
    print("\n".join(sys.path))
    print("App is running...")


    # # importing syntax #1            <- is more common, but can cause naming conflict
    # from oop_explained.sample import encapsulation
    # encapsulation()
    # encapsulation()

    
    # # importing syntax style #2         <- is more wordy, but resolves any issues with vague naming
    # import oop_explained.sample
    # oop_explained.sample.encapsulation()
    # encapsulation()


    
    # help(tipAndSplit)
    # print(bookStore("Shirt", 350.48, 8)) # arguments: actual values you want to pass it to the parameters from the stack where you are at

    # print(bookStore("Lanyard", 200.0, 70) )


    # from gt_hw02.HW02 import dinnerPlans
    # print(dinnerPlans(4, "Slightly Hungry"))
    # print(dinnerPlans(6, "Very Hungry"))
    # print(dinnerPlans(6, "Starving"))
    # print(dinnerPlans(-1, "Very Hungry"))
    

    

    # cars = ["Ford", "Volvo", "BMW"]


    # # array, the start of Abstract Data Type (ADT)
    # integers = [1, 2, 3, 5]
    
    # characters = ['H', 'e', 'l', 'l', 'o']

    # # lv1 of ADT, string
    # my_string = "Hello"

    # result = "" # null
    # for x in characters:
    #     result += x # result = result + char
    # print(result)

    # result = ""
    # for x in my_string: # ['H', 'e', 'l', 'l', 'o']
    #     result = result + x
    # print(result)


    # result = ""
    # x = 0
    #  # ['H', 'e', 'l', 'l', 'o']
    # #  'H' == index 0            my_string[0]
    # #  'e' == index 1            my_string[1]
    # #  'l' == index 2            my_string[2]
    # #  'l' == index 3            my_string[3]
    # #  'o' == index 4            my_string[4]
    # while (x < len(my_string)): # x < 5
    #     result = result + my_string[x]
    #     x = x + 1
    # print(result)


    # real_numbers = [2.4, 1.5, 2.3]
    # example = "Hie" # = ['H','i','e']
    # sum = 0.0
    # for y in real_numbers:
    #     sum += y
    # print(sum)

    # print("--------------Testing!---------------")
    # print(example[0])
    # print(example[1])
    # print(example[2])


    from gt_hw03.HW03 import movieNight
    caption = "Mr. and M4rs. Dursley of nu28mber four, Privet Drive, wer903e proud to say th6at they we6re perfectly norm3al, tha894nk you ve89ry much." 
    print(movieNight(caption))


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


    #########################
    # Programming Paradignms!
    # oop_explained.sample.oo_paradigm()

if __name__ == "__main__":
    main()