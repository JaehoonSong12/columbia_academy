# december_escapes.app.py
# 
# Python vocab      vs      OS vocab                                    e.g.
# execution point           pwd (current working directory)             /c/ca_workplace/ca_project01/src
# package                   directory or subdirectory (namespace)       /c/ca_workplace/ca_project01/src/december_escapes
# module                    file with .py extension                     /c/ca_workplace/ca_project01/src/december_escapes/app.py
# 
# a module named `app` is in a package or packages named `december_escapes` 
# syntax: from <package>.<package>...<module>.py import <functions/classes>

# sytax rule for identifying classes and normal functions and variables
#
# [procedural programming, Abstraction (API)] 
#   - functions and variables:      snake_case
#   - constants:                    UPPER_SNAKE_CASE
# [Objected-Oriented Programming, Encapsulation (Data Type)] 
#   - classes:                      PascalCase
import pygame
import random
# 
from december_escapes.utils import detect_collision, detect_goal
from december_escapes.constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, WHITE, STAR_SIZE
# OOP components
from december_escapes.player import Player
from december_escapes.obstacle import Obstacle
from december_escapes.star import Star

def generate_obstacles():
    obstacles = []
    for _ in range(random.randint(3, 6)):  # Generate random number of obstacles
        x = random.randint(0, SCREEN_WIDTH - 50)
        y = random.randint(0, SCREEN_HEIGHT - 20)
        color = random.choice([(0, 0, 255), (128, 0, 128)])  # BLUE or PURPLE
        speed = random.randint(1, 3) if color == (0, 0, 255) else 0
        obstacles.append(Obstacle(x, y, 50, 20, color, speed))
    return obstacles

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Game: December Escapes")
    clock = pygame.time.Clock()

    # Game setup
    level = 1
    player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)
    star = Star(random.randint(0, SCREEN_WIDTH - STAR_SIZE), random.randint(0, SCREEN_HEIGHT - STAR_SIZE), STAR_SIZE)
    obstacles = generate_obstacles()

    running = True
    while running:
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player.move(keys)
        player.update_color()

        for obstacle in obstacles:
            obstacle.move(SCREEN_WIDTH)
            obstacle.draw(screen)

        player.draw(screen)
        star.draw(screen)

        if detect_collision(player, obstacles):
            print("Game Over")
            player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)
            obstacles = generate_obstacles()

        if detect_goal(player, star):
            level += 1
            star = Star(random.randint(0, SCREEN_WIDTH - STAR_SIZE), random.randint(0, SCREEN_HEIGHT - STAR_SIZE), STAR_SIZE)
            obstacles = generate_obstacles()

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()



# """
# A Pygame application where text starts in the middle of the screen and continuously moves
# in response to arrow key presses.

# Features:
# - Text starts centered on the screen.
# - Arrow keys allow continuous movement as long as they are held down.
# - Dynamic color updates with direction changes.

# Modules:
# - pygame: for graphics and event handling.
# - random: for generating random colors.
# - os: for setting environment variables.

# Author: Your Name
# Date: YYYY-MM-DD
# """
# import sys
# import pygame
# import random
# import os

# # Configure SDL audio driver for compatibility
# os.environ['SDL_AUDIODRIVER'] = 'dsp'




# # Initialize Pygame and its font module
# pygame.init()
# pygame.font.init()
# size = width, height = 800, 600  # Window size
# screen = pygame.display.set_mode(size, pygame.RESIZABLE)
# screen.fill((0, 0, 0))
# pygame.display.set_caption("December Escapes")
# clock = pygame.time.Clock()

# # Set up display properties


# # Initialize font and text
# font = pygame.font.Font(pygame.font.get_default_font(), 36)
# # Set up movement offsets and clock
# move_offset = 5
# # Movement state
# # moving_direction = None


# def loop(text_surface, text_rect):
#     moving_direction = None
#     # Main game loop
#     while True:
#         # Handle events
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             elif event.type == pygame.KEYDOWN:
#                 moving_direction, text_message, text_color = handle_key_down(event.key)
#                 text_surface = font.render(text_message, False, text_color)
#             elif event.type == pygame.KEYUP:
#                 moving_direction = None

#         # Update position if a key is being held
#         if moving_direction:
#             text_rect = update_position(moving_direction, text_rect, move_offset, width, height)

#         # Render updates
#         screen.fill((0, 0, 0))  # Clear the screen
#         screen.blit(text_surface, text_rect)  # Draw the text
#         pygame.display.flip()  # Update the display

#         clock.tick(60)  # Limit to 60 frames per second




# def main():
#     """
#     Main function to initialize and run the Pygame application.
#     """
#     text_message = "Centered Text"
#     text_color = get_random_color()
#     text_surface = font.render(text_message, False, text_color)
#     text_rect = text_surface.get_rect(center=(width // 2, height // 2))
#     print((width // 2, height // 2))
#     loop(text_surface, text_rect)










# def get_random_color():
#     """
#     Generates a random RGB color.

#     Returns:
#         tuple: A tuple representing an RGB color (R, G, B).
#     """
#     return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)











# def handle_key_down(key):
#     """
#     Returns the direction, new message, and random color based on the key input.

#     Args:
#         key (int): The key pressed.

#     Returns:
#         tuple: A tuple containing the direction (str), the new text message (str),
#                and a random color (tuple).
#     """
#     if key == pygame.K_UP:
#         return "UP", "Moving Up", get_random_color()
#     elif key == pygame.K_DOWN:
#         return "DOWN", "Moving Down", get_random_color()
#     elif key == pygame.K_LEFT:
#         return "LEFT", "Moving Left", get_random_color()
#     elif key == pygame.K_RIGHT:
#         return "RIGHT", "Moving Right", get_random_color()
#     return None, "Centered Text", get_random_color()






# def update_position(direction, rect, offset, max_width, max_height):
#     """
#     Updates the position of the text rectangle based on the direction.

#     Args:
#         direction (str): The direction of movement.
#         rect (pygame.Rect): The rectangle of the text surface.
#         offset (int): The number of pixels to move per frame.
#         max_width (int): The maximum width of the screen.
#         max_height (int): The maximum height of the screen.

#     Returns:
#         pygame.Rect: The updated rectangle with a new position.
#     """
#     if direction == "UP":
#         rect.y = max(0, rect.y - offset)
#     elif direction == "DOWN":
#         rect.y = min(max_height - rect.height, rect.y + offset)
#     elif direction == "LEFT":
#         rect.x = max(0, rect.x - offset)
#     elif direction == "RIGHT":
#         rect.x = min(max_width - rect.width, rect.x + offset)
#     return rect






# if __name__ == "__main__":
#     main()