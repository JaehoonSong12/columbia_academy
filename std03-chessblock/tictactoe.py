import pygame
from enum import Enum

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Configurations    
WHITE = (255, 255, 255)
RED = (255, 0, 0)               # color for X
BLUE = (0, 0, 255)              # color for O
LIGHT_GREEN = (144, 238, 144)   # background color
BORDER_COLOR = (0, 0, 0)        # border color for buttons
BORDER_THICKNESS = 3



# State of buttons define enum (0 = empty, 1 = O, 2 = X)
class State(Enum):
    EMPTY = 0
    FILLO = 1
    FILLX = 2

# 9 transparent square buttons
button_hit_size = 200
button_ui_size = 180
padding_size = (button_hit_size - button_ui_size) // 2
buttons = []
for row in range(3):
    for col in range(3):
        rect = pygame.Rect(
            col * button_hit_size + padding_size, row * button_hit_size + padding_size, 
            button_ui_size, button_ui_size
        )
        buttons.append((rect, State.EMPTY))

# load X.png and O.png images from assets folder
x_image = pygame.image.load("assets/X.png")
o_image = pygame.image.load("assets/O.png")
# scale images to fit button_ui_size
x_image = pygame.transform.scale(x_image, (button_ui_size, button_ui_size))
o_image = pygame.transform.scale(o_image, (button_ui_size, button_ui_size))










# Game loop
running = True
turn = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Exit condition
            running = False
    
    # Fill background
    screen.fill(LIGHT_GREEN)
    
    # black border for visibility
    for button in buttons:
        rect = button[0]
        state = button[1]
        pygame.draw.rect(screen, BORDER_COLOR, rect, BORDER_THICKNESS)
        if state == State.FILLO:
            screen.blit(o_image, rect.topleft)
        if state == State.FILLX:
            screen.blit(x_image, rect.topleft)


    # mouse click event
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        mouse_pos = event.pos
        index = 0
        for button in buttons:
            rect = button[0]
            state = button[1]
            if rect.collidepoint(mouse_pos):
                if state == State.EMPTY and turn % 2 == 0:
                    buttons[index] = (rect, State.FILLO)
                    turn += 1
                elif state == State.EMPTY and turn % 2 == 1:
                    buttons[index] = (rect, State.FILLX)
                    turn += 1
            index += 1
    
    # winning logic
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # columns
        [0, 4, 8], [2, 4, 6]             # diagonals
    ]
    o_combinations = []
    x_combinations = []
    index = 0
    for button in buttons:
        state = button[1]
        if state == State.FILLO:
            o_combinations.append(index)
        if state == State.FILLX:
            x_combinations.append(index)
        index += 1
    for win_combo in winning_combinations:
        if # sehwan HW: algorithm
            print("O wins!")
            running = False
        if # sehwan HW: algorithm
            print("X wins!")
            running = False


    

    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()