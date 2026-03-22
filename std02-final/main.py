



# 1. Create a single room of your map in main using your Sq struct.
class Sq:
    def __init__(self, description: str, is_walkable: bool):
        self.description = description
        self.is_walkable = is_walkable
    def __str__(self):
        return self.description


def main():
    
    # Create a simple room layout
    T = True
    F = False
    single_room = [
        [Sq("x", F), Sq("x", F), Sq("x", F), Sq("x", F), Sq("x", F), Sq("x", F), Sq("x", F), Sq("x", F), Sq("x", F), Sq("x", F), Sq("x", F)],
        [Sq("x", F), Sq(" ", T), Sq(" ", T), Sq("x", F), Sq(" ", T), Sq(" ", T), Sq("x", F), Sq(" ", T), Sq(" ", T), Sq(" ", T), Sq("x", F)],
        [Sq("x", F), Sq(" ", T), Sq(" ", T), Sq(" ", T), Sq(" ", T), Sq(" ", T), Sq("x", F), Sq(" ", T), Sq("x", F), Sq(" ", T), Sq("x", F)],
        [Sq("x", F), Sq(" ", T), Sq("x", F), Sq("x", F), Sq("x", F), Sq(" ", T), Sq("x", F), Sq(" ", T), Sq("x", F), Sq(" ", T), Sq("x", F)],
        [Sq("x", F), Sq(" ", T), Sq(" ", T), Sq(" ", T), Sq(" ", T), Sq(" ", T), Sq(" ", T), Sq(" ", T), Sq("x", F), Sq(" ", T), Sq(" ", T)],
        [Sq("x", F), Sq("x", F), Sq("x", F), Sq("x", F), Sq("x", F), Sq("x", F), Sq("x", F), Sq("x", F), Sq("x", F), Sq("x", F), Sq("x", F)],
    ]
    

    
    # 2. Write the game look in C that allows the player 
    # to walk around the room and see your prompts for what is in the room, 
    # and NOT walk through any xs or out of bounds. 
    # Ensure player can walk into any appropriate Sq, 
    # and that they are shown 
    # the prompts for each Sq in the room.
    # command constants
    CMD_UP1 = 'go north'
    CMD_UP2 = 'north'
    CMD_UP3 = 'n'
    UP_CMD = [CMD_UP1, CMD_UP2, CMD_UP3]
    CMD_DOWN1 = 'go south'
    CMD_DOWN2 = 'south'
    CMD_DOWN3 = 's'
    DOWN_CMD = [CMD_DOWN1, CMD_DOWN2, CMD_DOWN3]
    CMD_LEFT1 = 'go west'
    CMD_LEFT2= 'west'
    CMD_LEFT3= 'w'
    LEFT_CMD = [CMD_LEFT1, CMD_LEFT2, CMD_LEFT3]
    CMD_RIGHT1 = 'go east'
    CMD_RIGHT2 = 'east'
    CMD_RIGHT3 = 'e'
    RIGHT_CMD = [CMD_RIGHT1, CMD_RIGHT2, CMD_RIGHT3]


    CMD_QUIT = 'quit'

    ALL_CMD = [
        CMD_UP1, 
        CMD_UP2, 
        CMD_UP3,
        CMD_DOWN1,
        CMD_DOWN2,
        CMD_DOWN3,
        CMD_LEFT1,
        CMD_LEFT2,
        CMD_LEFT3,
        CMD_RIGHT1,
        CMD_RIGHT2,
        CMD_RIGHT3,
        CMD_QUIT,
    ]


    # x x x x x x x x x x x 
    # x p   x     x       x 
    # x           x   x   x
    # x   x x x   x   x   x
    # x               x
    # x x x x x x x x x x x

    print("Welcome to the Adventure Game!")
    print("You are in a room.")
    player_x, player_y = 1, 1  # starting position
    new_x, new_y = player_x, player_y
    single_room[player_y][player_x].description = "p"
    single_room[player_y][player_x].is_walkable = F
    while True:
        for row in single_room:
            for sq in row:
                print(sq, end=" ")
            print()
        # print("Available commands: go north, go south, go west, go east, quit")
        command = input("Enter your command: ").lower().strip()
        if command == CMD_QUIT:
            print("Thanks for playing!")
            print("Goodbye! You were at position ({}, {})".format(player_x, player_y))
            for row in single_room:
                for sq in row:
                    print(sq, end=" ")
                print()
            break
        if command not in ALL_CMD:
            print("Invalid command. Try again.")
            continue
        if (not (0 <= player_y < len(single_room)) and (0 <= player_x < len(single_room[0]))):
            print("You just escaped the room! Congratulations!")
            break


        print(f"player_x = {player_x}, player_y = {player_y}")
        # determine new position
        if   command in UP_CMD:     new_y = player_y-1
        elif command in DOWN_CMD:   new_y = player_y+1
        elif command in LEFT_CMD:   new_x = player_x-1
        elif command in RIGHT_CMD:  new_x = player_x+1
        # check bounds and walkability
        if single_room[new_y][new_x].is_walkable:
            # move player
            single_room[player_y][player_x].description = " "
            single_room[player_y][player_x].is_walkable = T
            player_x, player_y = new_x, new_y
            single_room[player_y][player_x].description = "p"
            single_room[player_y][player_x].is_walkable = F
        else:
            print("You can't go that way! That's a wall")
        


        







# in C, int main(int argc, char** argv) {...}
if __name__ == "__main__": 
    main()