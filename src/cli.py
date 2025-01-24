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
    

    # from gt_hw02.HW02 import textFriends
    # print(textFriends(25.0, 65.0, 2.5, 17, 3))
    # print(textFriends(1.5, 2.5, 3.0, 13, 7))
    # print(textFriends(10.0, 5.0, 8.0, 13, 7))
    # print(textFriends(7.0, -46.66, -1.0, 13, 7))

    

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


    # from gt_hw03.HW03 import movieNight
    # caption = "Mr. and M4rs. Dursley of nu28mber four, Privet Drive, wer903e proud to say th6at they we6re perfectly norm3al, tha894nk you ve89ry much." 
    # print(movieNight(caption))




    # from gt_hw03.HW03 import dreamCar
    # print(dreamCar(50000.0, 10000.0, 5.0))
    # print(dreamCar(100000.0, 112.15, 2.1))



    
    # from gt_hw03.HW03 import battleship
    # battleship(3)
    # battleship(6)

    # from gt_hw03.HW03 import tennisMatch
    # tennisMatch("Arvin", "Arushi", "11221-222-1111-11121-22111-")
    # tennisMatch("Anthony", "Caitlin", "1122-22211-11122-1212-")

    from gt_hw04.HW04 import findMax
    print(findMax([1, 8, 3, 2, -4], 2, 4))
    print(findMax([3, 0, 7, 3, 2], 0, 4))




    

    # Custom Question! 
    """
    You have a string, that is given.
    Now, you are going to sort (in ascedning order, a->b->c->d->...) all the characters, 
    you can count the occurence of each letter!
    (Note: Ignore any whitespaces)
    For example, 
    "hi my name is jaehoon" -> {your implementation} -> "aaeehhiijmmnnoosy" << this is the sorted string!
    
    Article Refereces (Algorithm)
    1. https://www.geeksforgeeks.org/sorting-algorithms-in-python/
    2. https://www.programiz.com/dsa/sorting-algorithm

    dcba
        d <- d should go the last
       c <- c should go the second last

    """
    


    def sort(input): # unsorted*
        if len(input) == 0: # no empty string
            return output
        output = "" # sorted string / sorted array
        input = input.strip().lower()
        # For loop to iterate, 97 <= english_letter_ascii < 123


        # https://www.probabilitycourse.com/chapter1/1_2_2_set_operations.php
        # A={1, 2, 3, 4, 2} = {1, 2, 3, 4} = range(97, 123)
        # B={33}
        # A \union B 
        for english_letter_ascii in sorted({33, 36} | set(range(97, 123))): # you are assuming, the valid range of letter is constant.
            i = 0
            while (i < len(input)): 
                ## sort ????????????? <- more than 13 knwon solutions, each has their own benefit
                if ord(input[i]) == "32":
                    print()
                elif ord(input[i]) == english_letter_ascii: ## <- must be repreted for every character
                    output = output + input[i]
                i += 1
            
            
            # elif ord(input[i]) <= ord(input[i - 1]):
            #     output = input[i] + output
            # elif ord(input[i]) > ord(input[i - 1]):
            #     output = output + input[i]
            
            # print(ord(input[i])) # tells you ASCII value (`ord`inal value) so you can sort it by comparing
            

        # for char in input:
        #     ## original string! restore
        #     # output = output + char # [1] -> [1][2] -> [1][2][3]
        #     ## reverse
        #     output = char + output # [1] -> [2][1] -> [3][2][1]
            
        return output
    

    # string_given = "hi my name is $jaehoon, $taiyon, $jack, and $alysia, everyone is here!"
    # print(string_given)
    # print(sort(string_given))



    # print(ord(" "))

    # greeting = "     Hello!  "
    # stripped_greeting = greeting.strip()
    # print(stripped_greeting,"How are you?")








    # ## Array (Ordered Collection of Values, n-tuples, vectors in math)
    # vect1 = [1, 2, 3]
    # vect2 = [2, 2, 2]

    # vect3 = vect1 + vect2

    # ## Set (Unordered Collection of Values, number set in math)
    # set1 = {1,2,3}
    # set2 = {2,2,2}

    # for x in vect3:
    #     print(x)
    



    # game_record_string = "11221-222-1111-11121-22111-"

    # rounds_of_the_game = game_record_string.split('-')

    # for round in rounds_of_the_game:
    #     print(round)






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