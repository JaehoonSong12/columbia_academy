import random
from enum import Enum

class PigState(Enum):
    SIDE_NO_DOT = 0
    SIDE_DOT    = 1
    RAZORBACK   = 2
    TROTTER     = 3
    SNOUTER     = 4
    JOWLER      = 5
    OINKER      = 6

    def __str__(self):
        return self.name.replace("_", " ").title()

pig_points = {
    PigState.SIDE_NO_DOT:   5,
    PigState.SIDE_DOT:      5,
    PigState.RAZORBACK:     5,
    PigState.TROTTER:       5,
    PigState.SNOUTER:       10,
    PigState.JOWLER:        15,
}


def get_roll():
    cdf_value = random.random()
    # Cumulative distribution function values for each pig state
    cdf_ybounds = [0.349, 0.651, 0.875, 0.963, 0.993, 0.999, 1.000]
    for i in range(len(cdf_ybounds)):
        if cdf_value < cdf_ybounds[i]:
            return PigState(i)

def get_two_pigs():
    return (get_roll(), get_roll())

def get_state(pigs):
    pig1, pig2 = pigs
    if pig1 == PigState.SIDE_NO_DOT and pig2 == PigState.SIDE_NO_DOT:
        return (1,  "Sider",    True)
    if pig1 == PigState.SIDE_DOT and pig2 == PigState.SIDE_DOT:
        return (1,  "Sider",    True)
    if (pig1 == PigState.SIDE_NO_DOT and pig2 == PigState.SIDE_DOT):
        return (0,  "Pig Out",  False)
    if (pig1 == PigState.SIDE_DOT and pig2 == PigState.SIDE_NO_DOT):
        return (0,  "Pig Out",  False)
    if (pig1 == PigState.OINKER or pig2 == PigState.OINKER):
        return (0,  "Oinker",   False)        
    if pig1 == PigState.RAZORBACK and pig2 == PigState.RAZORBACK:
        return (pig_points[PigState.RAZORBACK] * 4, "Double Razorback", True)
    if pig1 == PigState.TROTTER and pig2 == PigState.TROTTER:
        return (pig_points[PigState.TROTTER] * 4, "Double Trotter", True)
    if pig1 == PigState.SNOUTER and pig2 == PigState.SNOUTER:
        return (pig_points[PigState.SNOUTER] * 4, "Double Snouter", True)
    if pig1 == PigState.JOWLER and pig2 == PigState.JOWLER:
        return (pig_points[PigState.JOWLER] * 4, "Duble Jowler", True)
    return (pig_points[pig1] + pig_points[pig2], "Normal", True)

def play_turn(is_continuable=True):
    round_point = 0
    while (is_continuable):
        pigs = get_two_pigs()
        pig1, pig2 = pigs
        points, state_desc, is_continuable = get_state(pigs)
        print(f"Player rolled: {pig1} and {pig2} - {state_desc}, Points: {points}")
        round_point += points
        if is_continuable:
            choice = input("Do you want to roll again? (y/n): ").strip().lower()
            if choice[0] == 'n': break
    if (state_desc == "Pig Out"): round_point = 0
    if (state_desc == "Oinker"): return (round_point, True) # true, means the whole point reset
    return (round_point, False)




def print_score_table(score_table):
    print("Score Table:")
    for entry in score_table:
        print(entry)
    print("\n")



def main():
    player1_points = 0
    player2_points = 0
    round = 1
    score_table = []
    while (True):
        if (round % 2 == 1):
            print(f"--- Round {round}: Player 1's Turn ---")
            round_point, is_reset = play_turn()
            player1_points += round_point
            if is_reset:
                player1_points = 0
                print("Player 1's total points reset to 0 due to Oinker!")
        else:
            print(f"--- Round {round}: Player 2's Turn ---")
            round_point, is_reset = play_turn()
            player2_points += round_point
            if is_reset:
                player2_points = 0
                print("Player 2's total points reset to 0 due to Oinker!")
        print(f"--- End of Round {round} ---")
        score_table.append(f"After Round {round}: Player 1 = {player1_points}, Player 2 = {player2_points}")
        print_score_table(score_table)
        if (player1_points >= 100):
            print("Player 1 wins!")
            break
        if (player2_points >= 100):
            print("Player 2 wins!")
            break
        round += 1

        
    


if __name__ == "__main__":
    main()


# pip install pyinstaller
# pyinstaller --onefile passthepig.py