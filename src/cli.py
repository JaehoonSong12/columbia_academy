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

    # from gt_hw04.HW04 import findMax
    # print(findMax([1, 8, 3, 2, -4], 2, 4))
    # print(findMax([3, 0, 7, 3, 2], 0, 4))




    

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






    def print_game_board(board: list, width_of_board: int):
        """
        Prints the 1D game board in a 2D format for better visualization.
        
        Parameters:
        board (list): The game board stored as a 1D list.
        width_of_board (int): The number of columns in the board.
        
        Example:
        >>> board = create_game_board(3, 3)
        >>> print_game_board(board, 3)
        X O O
        X O O
        X O O
        """
        for i in range(len(board)):
            cell = board[i]
            # print("\n")
            if ((i % width_of_board) == 2): 
                print(cell, end="\n")
            else: 
                print(cell, end=" ")
        return
    
    def is_row_bingo(board: list, width_of_board: int):
        for row_index in range(len(board) // width_of_board):
            is_row_bingo_detected = True # flag to identify if there is at least one row bingo
            first_cell = board[((row_index * width_of_board))] # the very first character that is supposed to be in the entire row
            for col_index in range(width_of_board): # process each row
                cell = board[((row_index * width_of_board) + col_index)]
                if (first_cell != cell): 
                    is_row_bingo_detected = False 
            if (is_row_bingo_detected): 
                return True # logic for each row, even if you don't find it, you need to give me another chance
                # print(f"You are at row: {row_index}")
                # print(f"You are at col: {col_index}") 
                # print(f"You are at i based on row {row_index} & col {col_index}: {board[((row_index * width_of_board) + col_index) ]}")
        return False
        #      0    1    2
        #  0 ['X', 'O', 'O', 
        #  1 'X', 'X', 'X', 
        #  2 'X', 'O', 'O'] 9
        
        # "X", "O", "O",
        # "X", "X", "X",
        # "X", "O", "O"
        
        # [0,    1 ,  2,     3,  4,  5,     6,   7,  8 ] 
        # ['X', 'O', 'O',  'X', 'O', 'O',  'X', 'O', 'O'] 

        
        return True
    
    def is_col_bingo(board: list, width_of_board: int):
        return False
        return True
    
    def is_diagonal_bingo(board: list, width_of_board: int):
        return False
        return True






    def create_game_board(width: int, height: int) -> list:
        """
        Creates a 2D game board represented as a 1D list.
        
        The board is filled with "X" and "O" based on the following rule:
        - If the position index (computed as row * width + col) is divisible by 3, place "X".
        - Otherwise, place "O".
        
        Parameters:
        width (int): The number of columns in the board.
        height (int): The number of rows in the board.
        
        Returns:
        list: A 1D list representing the game board.
        
        Example:
        >>> create_game_board(3, 3)
        ['X', 'O', 'O', 'X', 'O', 'O', 'X', 'O', 'O']
        """
        return None
    

    # Example usage
    COLS = 3
    ROWS = 3
    board = create_game_board(COLS, ROWS)



    board = [ "X", "O", "O", "X", "O", "O", "X", "O", "O"]

    board = [
        "X", "B", "X",
        "A", "A", "B",
        "X", "O", "O"
    ]

    # print_game_board(board, ROWS)

    # if (is_col_bingo(board, ROWS)): print("You got a column bingo!")
    # else: print("You dont' get any column bingo!")
    # if (is_row_bingo(board, ROWS)): print("You got a row bingo!")
    # else: print("You dont' get any row bingo!")
    # if (is_diagonal_bingo(board, ROWS)): print("You got a diagonal bingo!")
    # else: print("You dont' get any diagonal bingo!")


    # print(True) # boolean data type
    # fdsgfsdgfdgfd = 12
    # print(fdsgfsdgfdgfd)
    # print(12)
    # print(False)

    # print(2 > 1)    # 2 > 1 --> True (boolean data)

    # print("Ture? False? anything that is non-zero are true, anything that is zero are false")
    # print(bool(50)) # True
    # print(bool(0))  # False
    # print(bool(-1)) # True
    # print(bool(5))  # True


    # print(2 == 1)

    # if (2 > 1): print("hi")
    # if (True): print("hi")

    # if (boolean data type)


    # from gt_hw04.HW04 import fruitPie
    # print(fruitPie(["apple", 2, "cherry", 10, "watermelon", 5], 4))

    # from gt_hw04.HW04 import replaceWord
    # print(replaceWord("I used to rule the world","seas"))

    # from gt_hw04.HW04 import highestSum
    # myList = ["3lf", "bg_73e", "001!0", "gg9./"] 
    # print(highestSum(myList))
    # myList = ["py1h0n", "1s", "v3ry", "fun!!11!!!111"]
    # print(highestSum(myList))


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



    from gt_hw07.HW07 import findCuisine
    print(findCuisine('./gt_hw07/restaurants.txt', 'American'))
  
    from gt_hw04.HW04 import sublist
    alist = ['a', 'b', 'd', 'e', 't'] 
    blist = ['b', 'd', 'e']
    print(sublist(alist, blist))

    alist = [6, 2, 3, 4, 5] 
    blist = [6, 3] 
    print(sublist(alist, blist))

    alist = ["The", "Houston", "Astros", "are", "cheaters"] 
    blist = ["The", "Houston", "Astros", "are", "cheaters"] 
    print(sublist(alist,blist))

    # #### file I/O API!!!!!
    # import os
    
    # try:
    #     os.mkdir("new_directory")
    #     print("Directory created successfully.")
    # except FileExistsError:
    #     print("Directory already exists.")
    # except OSError as e:
    #     print(f"Error creating directory: {e}")


    # filename = "./new_directory/example.txt"

    # file = open(filename, "w") # w: writing mode (inputting values as file)
    # # print(type(23))
    # # print(type(file))
    # file.write("Hello, World!\n")
    # file.write("dsafdafdafaf, World!\n")
    # file.write("Hello, dsafdafdafaf!\n")
    # file.close()

    # file = open(filename, "r")
    # output = file.read()
    # print(type(output))
    # print(output)



    # ############### < Procedure Programming (PP) Paradigm >
    # animal_types = ["Dog", "Cat", "Mouse"]
    # animal_sounds = ["Bark", "Meow", "Squeak"]

    # def report(types, sounds):
    #     print(f"This animal is {types}, it makes its sound, {sounds}.")
    #     return
    # for i in range(len(animal_types)):
    #     report(animal_types[i], animal_sounds[i])
    





    # ############### Object Oriented Programming (OOP) Paradigm - step#1 encapsulation
    # # self var <- system setup variable used to store the memory 
    # #               address of objects in `heap`.
    # class Animal:
    #     def __init__(self, type, sound): # __init__: is called to initalize your class object 
    #         self.type = type             # self.type (in `heap`, OOP): self (class object's) value, type
    #         self.sound = sound           # type (in `stack`, PP): parameter accepting arguments outside
    #     def report(self):
    #         print(f"This animal is a {self.type}, it makes its sound, {self.sound}.")
    
    # # Animal("Human", "Hi") # === Animal.__init__(self, "Human", "Hi")


    # animals = [
    #     Animal("Dog", "Bark"),  # <- these data are in heap, not stack
    #     Animal("Mouse", "Squeak"),
    #     Animal("Cat", "Meow")   # <- these data are in heap, not stack
    # ]

    # for animal in animals:
    #     animal.report()




    
    # ############### Object Oriented Programming (OOP) Paradigm - step#2 inheritance/polymorphism
    # class Animal:
    #     def __init__(self, type, sound): # __init__: is called to initalize your class object 
    #         self.type = type             # self.type (in `heap`, OOP): self (class object's) value, type
    #         self.sound = sound           # type (in `stack`, PP): parameter accepting arguments outside
    #     def report(self):
    #         print(f"This animal is a {self.type}, it makes its sound, {self.sound}.")
    # class Dog(Animal):
    #     def __init__(self):
    #         super().__init__("Dog", "Bark")
    # class Cat(Animal):
    #     def __init__(self):
    #         super().__init__("Cat", "Meow")
    #     # @override
    #     def report(self):
    #         print(f"Cats are unique, this generation gave up on making sound.")
    # class Mouse(Animal):
    #     def __init__(self):
    #         super().__init__("Mouse", "Squeak")

    # animals = [
    #     Dog(),  # <- these data are in heap, not stack
    #     Mouse(),
    #     Cat()   # <- these data are in heap, not stack
    # ]

    # for animal in animals:
    #     animal.report()
    #     print(type(animal))





    # ###### HW07
    # from gt_hw07.HW07 import restaurantFilter
    # print(restaurantFilter('./gt_hw07/restaurants.txt'))

    # from gt_hw07.HW07 import createDirectory
    # createDirectory('./gt_hw07/restaurants.txt', './gt_hw07/directory.txt')


    # from gt_hw07.HW07 import infectedPercentage
    # print(infectedPercentage(["Belgium", "Belarus", "Bermuda"], './gt_hw07/covid.csv'))
    # print(infectedPercentage(["Sweden", "Turkey", "Ukraine"], './gt_hw07/covid.csv'))




    from gt_hw07.HW07 import countryStatus
    print(
        countryStatus(["United States", "Tonga", "Poland", "New Zealand", "Norway"], './gt_hw07/covid.csv')
    )
    print(
        countryStatus(["Belgium", "Bangladesh", "Belarus", "Bermuda"], './gt_hw07/covid.csv')
    )
    


    from gt_hw07.HW07 import compareRisk
    print(
        compareRisk("Tunisia", ["Belgium", "Bangladesh", "Belarus", "Bermuda"], './gt_hw07/covid.csv')
    )
    print(
        compareRisk("Tuvalu", ["Turkmenistan", "Norway", "Netherlands", "Philippines"], './gt_hw07/covid.csv')
    )
    


    # slicing notation
    text = "hello"
    print(text[1:])  # "ello"

    # Recursion Example
    def reverse_string(s):
        if s == "":
            return s
        return reverse_string(s[1:]) + s[0]
    
    print(reverse_string("abc"))  # "cba"






    from gt_hw08.HW08 import meetNewPeople
    meetNewPeople("Slytherin")










    from gt_hw10.HW10 import Room, Task, Crewmate, Impostor, AmongUs
    """
    Detailed usage of AmongUs, Crewmate, Impostor, Room, and Task classes.
    """

    # Create room and task objects.
    room1 = Room("Medbay")
    task1 = Task("Scan")

    # Create crewmate players.
    crew1 = Crewmate("Alice", "Red", ("Hat", "Gloves"))
    crew2 = Crewmate("Amanda", "Blue", ("Cap",))

    # Create impostor players.
    imp1 = Impostor("Bob", "Green", ("Knife",))
    imp2 = Impostor("Brenda", "Yellow", ("Sunglasses",))

    # Create an AmongUs game with a maximum of 4 players.
    game = AmongUs(4)

    # Register all players to the game.
    # If the lobby is full or a player with the same name already exists,
    # the method returns an error message. Otherwise, players are added to the game.
    print(game.registerPlayer(crew1))   # Registers a crewmate.
    print(game.registerPlayer(crew2))   # Registers another crewmate.
    print(game.registerPlayer(imp1))    # Registers an impostor.
    print(game.registerPlayer(imp2))    # Registers another impostor.

    # Print the current state of the game.
    print("\nCurrent Players:")
    print("Crewmates:", game.crewmates)
    print("Impostors:", game.impostors)

    # Register a task to a room.
    # If the task already exists in any room, the method will return a message.
    game.registerTask(task1, room1)
    print("\nRooms after task registration:")
    print(game.rooms)

    # A crewmate does a task.
    # The task's isCompleted attribute is updated, and the crewmate's tasksDone counter increases.
    print("\nBefore performing task:", task1)
    crew1.doTask(task1)
    print("After performing task:", task1)
    print("Crewmate {} has completed {} task(s).".format(crew1.name, crew1.tasksDone))

    # If another crewmate tries to perform the same task, they receive a message.
    result = crew2.doTask(task1)
    print("Attempt by {}: {}".format(crew2.name, result))

    # An impostor eliminates a crewmate.
    print("\nBefore elimination, is {} alive? {}".format(crew2.name, crew2.isAlive))
    imp1.eliminate(crew2)
    print("After elimination, is {} alive? {}".format(crew2.name, crew2.isAlive))
    print("Impostor {} has eliminated {} player(s).".format(imp1.name, imp1.eliminateCount))

    # A crewmate calls a meeting.
    # In the meeting, each player votes based on the first letter of their names.
    # The player with the most votes is ejected, and the method returns a message indicating the result.
    meeting_result = crew1.callMeeting(game)
    print("\nMeeting result:", meeting_result)

    # Check if the game is over.
    # The game is over if all crewmates or all impostors have been eliminated.
    game_state = game.gameOver()
    print("Game over state:", game_state)







    
if __name__ == "__main__":
    main()