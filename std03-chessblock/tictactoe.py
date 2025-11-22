import pygame
from enum import Enum


import sys












# ==============================================================================
# CONFIGURATION AND CONSTANTS
# ==============================================================================
# Colors (R, G, B)
COLOR_WHITE     = (255, 255, 255)
COLOR_BLACK     = (0, 0, 0)
COLOR_GRAY      = (200, 200, 200)
COLOR_DARK_GRAY = (50, 50, 50)
COLOR_BLUE      = (70, 130, 180)
COLOR_GREEN     = (50, 200, 50)
COLOR_RED       = (200, 50, 50)
COLOR_LIGHT_GREEN = (144, 238, 144)   # background color

COLOR_GRAY_HOVER  = (230, 230, 230)
COLOR_BLUE_HOVER  = (100, 160, 210)
COLOR_GREEN_HOVER = (80, 230, 80)
COLOR_RED_HOVER   = (230, 80, 80)

BORDER_THICKNESS = 3





class Screen(Enum):
    MENU = 0
    GAME = 1
    POPUP = 2


# State of buttons define enum (0 = empty, 1 = O, 2 = X)
class State(Enum):
    EMPTY = 0
    FILLO = 1
    FILLX = 2



# ==============================================================================
# UI CLASSES
# ==============================================================================

class Button:
    """
    A UI Button that changes color when hoveCOLOR_RED over.
    """
    def __init__(self, 
                 text, 
                 x, y, 
                 width, height, 
                 base_color, 
                 hover_color, 
                 text_color=COLOR_BLACK,
                 border_size=2):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.base_color = base_color
        self.hover_color = hover_color
        self.text_color = text_color
        self.bolder_size = border_size
        self.font = pygame.font.SysFont("Arial", 24)

    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):   current_color = self.hover_color
        else:                                   current_color = self.base_color
        pygame.draw.rect(surface, current_color, self.rect)
        pygame.draw.rect(surface, COLOR_BLACK, self.rect, self.bolder_size)
        # Render and center the text
        text_surf = self.font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left Click
                if self.rect.collidepoint(event.pos):
                    return True
        return False






# ==============================================================================
# MAIN LOGIC
# ==============================================================================
pygame.init()


# Text Fonts
font_large  = pygame.font.SysFont("Arial", 48, bold=True)
font_med    = pygame.font.SysFont("Arial", 36)
font_small  = pygame.font.SysFont("Arial", 28)


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GAME_SCREEN_WIDTH = 900
GAME_SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
FPS = 60

def set_caption(caption):
    pygame.display.set_caption(caption)

def set_screen_size(width, height):
    global screen
    screen = pygame.display.set_mode((width, height))

def get_screen_size():
    current_w = screen.get_width()
    current_h = screen.get_height()
    return (current_w, current_h)


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

def reset_buttons():
    global buttons
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

def isSubseq(a,b):
    j=0
    for i in range(len(b)):
        if (j == len(a)): return True
        if b[i]==a[j]:
            j=j+1
    if j ==len(a):
        return True
    else:
        return False




def run_game():
    
    
    clock = pygame.time.Clock()

    # ---------------------------------------------------------
    # INITIALIZE UI ELEMENTS
    # ---------------------------------------------------------
    
    # MENU Buttons (Base Color, Hover Color)
    btn_menu_start = Button("START", 
                       SCREEN_WIDTH // 2 - 100, 250, 
                       200, 60, 
                       COLOR_GREEN, COLOR_GREEN_HOVER)
    
    btn_menu_exit = Button("EXIT", 
                      SCREEN_WIDTH // 2 - 100, 350, 
                      200, 60, 
                      COLOR_RED, COLOR_RED_HOVER)

    # GAME Buttons
    btn_game_back = Button("BACK", 
                      GAME_SCREEN_WIDTH-20 - 100, GAME_SCREEN_HEIGHT-20 - 40, 
                      100, 40, 
                      COLOR_GRAY, COLOR_GRAY_HOVER)

    # POPUP
    rect_popup = pygame.Rect(SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 - 100, 
                             400, 200)
    
    # Note: The popup confirm button uses COLOR_BLUE/Lighter COLOR_BLUE
    btn_popup_ok = Button("OK", 
                          SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 + 20, 
                          100, 40, 
                          COLOR_BLUE, 
                          COLOR_BLUE_HOVER, 
                          text_color=COLOR_WHITE)


    # ---------------------------------------------------------
    # GAME LOOP
    # ---------------------------------------------------------
    current_state = Screen.MENU
    running = True
    turn = 0
    message = ""
    while running:
        #### View
        # screen.fill(COLOR_WHITE)
        if current_state == Screen.MENU:
            set_caption("Welcome to TicTacToe")
            screen.fill(COLOR_DARK_GRAY)
            # Text Label
            img = font_large.render("MAIN MENU", True, COLOR_WHITE)
            coordinates = img.get_rect(center=(SCREEN_WIDTH // 2, 100))
            screen.blit(img, coordinates)
            # Buttons
            btn_menu_start.draw(screen)
            btn_menu_exit.draw(screen)
        elif current_state == Screen.GAME or current_state == Screen.POPUP:
            set_caption("TicTacToe in play...")
            screen.fill(COLOR_BLUE)

            # # Text Label
            # img = font_med.render("Game Running...", True, COLOR_WHITE)
            # coordinates = img.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            # screen.blit(img, coordinates)

            # Buttons
            btn_game_back.draw(screen)

            # GAME BOARD RENDERING
            panel = pygame.Surface((SCREEN_HEIGHT, SCREEN_HEIGHT))
            panel.fill(COLOR_LIGHT_GREEN)
            for button in buttons:
                rect = button[0]
                state = button[1]
                pygame.draw.rect(panel, COLOR_BLACK, rect, BORDER_THICKNESS)
                if state == State.FILLO:    panel.blit(o_image, rect.topleft)
                if state == State.FILLX:    panel.blit(x_image, rect.topleft)
            
            # coord = panel.get_rect(center=(GAME_SCREEN_WIDTH // 2, GAME_SCREEN_HEIGHT // 2))
            screen.blit(panel, (0,0))

            
            # Overlay for Popup
            if current_state == Screen.POPUP:
                # Darken background
                SCR = get_screen_size()
                overlay = pygame.Surface((SCR[0], SCR[1]))
                overlay.set_alpha(150) 
                overlay.fill(COLOR_BLACK)
                screen.blit(overlay, (0,0))
                # Draw Box
                pygame.draw.rect(screen, COLOR_WHITE, rect_popup)
                pygame.draw.rect(screen, COLOR_BLACK, rect_popup, 3)
                # Message
                img = font_small.render(f"{message}, Return to Main Menu?", True, COLOR_BLACK)
                coordinates = img.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 20))
                screen.blit(img, coordinates)
                btn_popup_ok.draw(screen)



        #### Controller
        for event in pygame.event.get():
            # "esc" 
            if event.type == pygame.QUIT: running = False

            # Logic for MENU
            if current_state == Screen.MENU:
                if btn_menu_start.is_clicked(event):    
                    current_state = Screen.GAME
                    set_screen_size(GAME_SCREEN_WIDTH, GAME_SCREEN_HEIGHT)
                    turn=0
                    reset_buttons()
                if btn_menu_exit.is_clicked(event):     
                    running = False
            # Logic for GAME
            if current_state == Screen.GAME:
                if btn_game_back.is_clicked(event):     
                    current_state = Screen.POPUP



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
                    if isSubseq(win_combo,o_combinations):
                        message="O wins!"
                        turn=0
                        reset_buttons()
                        current_state = Screen.POPUP
                        break
                    if isSubseq(win_combo,x_combinations):
                        message="X wins!"
                        turn = 0
                        reset_buttons()
                        current_state = Screen.POPUP
                        break
                    if turn == 9:
                        message="It's a draw!"
                        turn=0
                        reset_buttons()
                        current_state = Screen.POPUP
                        break






            if current_state == Screen.POPUP:
                if btn_popup_ok.is_clicked(event):
                    current_state = Screen.MENU
                    set_screen_size(SCREEN_WIDTH, SCREEN_HEIGHT)




        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    run_game()



