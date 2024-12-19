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

import pygame # framework! You must learn how to use their abstraction!
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
    pygame.quit()
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
            print("Your score: ", level)
            level=1
            player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)
            obstacles = generate_obstacles()

        if detect_goal(player, star):
            level += 1
            print("Your level now: ", level)
            star = Star(random.randint(0, SCREEN_WIDTH - STAR_SIZE), random.randint(0, SCREEN_HEIGHT - STAR_SIZE), STAR_SIZE)
            obstacles = generate_obstacles()

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()













# import pygame # framework! You must learn how to use their abstraction!


# # Initialize constants
# SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
# BALL_RADIUS = 20
# BALL_SPEED = 5

# # Initialize Pygame
# pygame.init()
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("Ball Movement Example")
# CLOCK = pygame.time.Clock()
# FPS=120 # Higher FPS ensures smoother motion in video and gameplay

# def main():
#     # Ball setup
#     ball_x = SCREEN_WIDTH // 2
#     ball_y = SCREEN_HEIGHT // 2

#     # Velocity variables for the ball
#     velocity_x = 0
#     velocity_y = 0

#     running = True

#     while running:
#         # Get all currently pressed keys
#         keys = pygame.key.get_pressed()
#         # Logic for movements in general
#         velocity_x = 0
#         velocity_y = 0
#         if keys[pygame.K_LEFT]: velocity_x = -BALL_SPEED
#         if keys[pygame.K_RIGHT]: velocity_x = BALL_SPEED
#         if keys[pygame.K_UP]: velocity_y = -BALL_SPEED
#         if keys[pygame.K_DOWN]: velocity_y = BALL_SPEED
#         if keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]: velocity_x = 0
#         if keys[pygame.K_UP] and keys[pygame.K_DOWN]: velocity_y = 0
#         # Event handling
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
        
#         # Update ball position
#         ball_x += velocity_x
#         ball_y += velocity_y

#         # Boundary collision check
#         if ball_x - BALL_RADIUS < 0:
#             ball_x = BALL_RADIUS
#         elif ball_x + BALL_RADIUS > SCREEN_WIDTH:
#             ball_x = SCREEN_WIDTH - BALL_RADIUS

#         if ball_y - BALL_RADIUS < 0:
#             ball_y = BALL_RADIUS
#         elif ball_y + BALL_RADIUS > SCREEN_HEIGHT:
#             ball_y = SCREEN_HEIGHT - BALL_RADIUS

#         # Fill the screen with a color
#         screen.fill("purple")

#         # Draw the ball
#         pygame.draw.circle(screen, "white", (ball_x, ball_y), BALL_RADIUS)

#         # Flip the display to update the screen
#         pygame.display.flip()

#         # Limit the frame rate
#         CLOCK.tick(FPS)

#     pygame.quit()





if __name__ == "__main__":
    main()