#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A basic PyGame setup that displays a movable rectangle.

This script initializes PyGame, creates a window, and runs a simple game
loop. The player controls a blue rectangle with the arrow keys. All PyGame
events are printed to the console for educational purposes.
"""

import pygame


# Variable 
SCREEN_WIDTH = 1900                     # int variable (constant)
SCREEN_HEIGHT = 1080                    # int variable (constant)
SCREEN_CAPTION = "Abyss of Darkness"    # str variable (constant)

# --- Colors ---
# Define colors using RGB tuples for easy reference. (Red, Green, Blue)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255,0,0)
GREEN = (0,255,0)



# --- Game Objects ---
# Create a pygame.Rect object for our player.
# The arguments are (left, top, width, height).
# We start it in the center of the screen.
player_rect = pygame.Rect((SCREEN_WIDTH / 2) - 25, (SCREEN_HEIGHT / 2) - 25, 50, 50)
player_speed = 5 # highlights, short: how many pixels the rect moves per frame










def main():
    """Main function to run the PyGame application."""
    # --- Initialization ---
    # Initialize all imported pygame modules
    pygame.init()

    # --- Screen Setup ---
    # Informative notes, long:
    # We define the screen dimensions here. It's good practice to use
    # constants for these values so they can be easily changed and referenced
    # elsewhere in the code without using "magic numbers".
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(SCREEN_CAPTION)



    # --- Game Loop ---
    # The clock will be used to control the game's frame rate.
    clock = pygame.time.Clock()
    
    running = True # 1
    while running:
        # --- Event Handling ---
        # This is the core of the event loop. Pygame processes user input
        # (like key presses, mouse movements, etc.) as a series of events.
        # We iterate through each event that has happened since the last frame.
        for event in pygame.event.get():
            # Print the full event object to the console.
            # This is useful for learning what different actions generate.
            print(event)

            # Check if the event is the user clicking the window's close button.
            if event.type == pygame.QUIT: running = False # highlights, short: exits the loop

        # --- Player Movement ---
        # Get a dictionary of all keyboard keys currently being held down.
        keys_pressed = pygame.key.get_pressed()

        # Update the player's x-coordinate based on arrow key presses.
        if keys_pressed[pygame.K_LEFT]:
            player_rect.x -= player_speed
        if keys_pressed[pygame.K_RIGHT]:
            player_rect.x += player_speed

        # Update the player's y-coordinate based on arrow key presses.
        if keys_pressed[pygame.K_UP]:
            player_rect.y -= player_speed
        if keys_pressed[pygame.K_DOWN]:
            player_rect.y += player_speed

        # --- Screen Boundaries ---
        # This logic prevents the rectangle from moving off the screen.
        if player_rect.left < 0:
            player_rect.left = 0
        if player_rect.right > SCREEN_WIDTH:
            player_rect.right = SCREEN_WIDTH
        if player_rect.top < 0:
            player_rect.top = 0
        if player_rect.bottom > SCREEN_HEIGHT:
            player_rect.bottom = SCREEN_HEIGHT

        # --- Drawing ---
        # First, fill the screen with a background color (black).
        # This is done on each frame to clear the previous frame's drawings.
        screen.fill(BLACK)

        # Draw the player rectangle onto the screen surface.
        pygame.draw.rect(screen, BLUE, player_rect)

        # --- Update Display ---
        # This function updates the contents of the entire screen. It's the
        # final step in the drawing process for each frame.
        pygame.display.flip()

        # --- Frame Rate Control ---
        # This will pause the game for a short amount of time to ensure that
        # the loop runs at a maximum of 60 frames per second.
        clock.tick(60)

    # --- Shutdown ---
    # Once the `running` variable is False, the loop ends.
    # We call pygame.quit() to uninitialize the modules.
    pygame.quit()
    print("PyGame has been shut down.")
















if __name__ == "__main__":
    main() # main is where your program starts.