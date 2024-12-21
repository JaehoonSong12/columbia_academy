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















# import pygame # framework! You must learn how to use their abstraction!
# import random
# # 
# from december_escapes.utils import detect_collision, detect_goal
# from december_escapes.constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, WHITE, STAR_SIZE
# # OOP components
# from december_escapes.player import Player
# from december_escapes.obstacle import Obstacle
# from december_escapes.star import Star

# def generate_obstacles():
#     obstacles = []
#     for _ in range(random.randint(3, 6)):  # Generate random number of obstacles
#         x = random.randint(0, SCREEN_WIDTH - 50)
#         y = random.randint(0, SCREEN_HEIGHT - 20)
#         color = random.choice([(0, 0, 255), (128, 0, 128)])  # BLUE or PURPLE
#         speed = random.randint(1, 3) if color == (0, 0, 255) else 0
#         obstacles.append(Obstacle(x, y, 50, 20, color, speed))
#     return obstacles


# def main():
#     pygame.quit()
#     pygame.init()
#     screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#     pygame.display.set_caption("Game: December Escapes")
#     clock = pygame.time.Clock()

#     # Game setup
#     level = 1
#     player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)
#     star = Star(random.randint(0, SCREEN_WIDTH - STAR_SIZE), random.randint(0, SCREEN_HEIGHT - STAR_SIZE), STAR_SIZE)
#     obstacles = generate_obstacles()

#     running = True
#     while running:
#         screen.fill(WHITE)
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False

#         keys = pygame.key.get_pressed()
#         player.move(keys)
#         player.update_color()

#         for obstacle in obstacles:
#             obstacle.move(SCREEN_WIDTH)
#             obstacle.draw(screen)

#         player.draw(screen)
#         star.draw(screen)

#         if detect_collision(player, obstacles):
#             print("Game Over")
#             print("Your score: ", level)
#             level=1
#             player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)
#             obstacles = generate_obstacles()

#         if detect_goal(player, star):
#             level += 1
#             print("Your level now: ", level)
#             star = Star(random.randint(0, SCREEN_WIDTH - STAR_SIZE), random.randint(0, SCREEN_HEIGHT - STAR_SIZE), STAR_SIZE)
#             obstacles = generate_obstacles()

#         pygame.display.flip()
#         clock.tick(FPS)

#     pygame.quit()








# def traffic_light_fsm(state, event):
#     """Finite State Machine for a traffic light with integer states."""
#     match (state, event):
#         case (0, "TIMER"): return 1  # RED -> GREEN
#         case (1, "TIMER"): return 2  # GREEN -> YELLOW
#         case (2, "TIMER"): return 0  # YELLOW -> RED
#         case (_, "EMERGENCY"): return 0  # Any state -> RED
#         case _: return -1  # INVALID state

# # State mappings
# states = {0: "RED", 1: "GREEN", 2: "YELLOW"}

# # Example usage
# current_state = 0  # RED
# print(f"Current state: {states[current_state]}")

# next_state = traffic_light_fsm(current_state, "TIMER")
# print(f"Next state: {states[next_state]}")

# next_state = traffic_light_fsm(next_state, "TIMER")
# print(f"Next state: {states[next_state]}")

# next_state = traffic_light_fsm(next_state, "EMERGENCY")
# print(f"Next state: {states[next_state]}")





import pygame # framework! You must learn how to use their abstraction!
from december_escapes.my_player import Player 

# Initialize constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BALL_RADIUS = 20
BALL_SPEED = 5

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ball Movement Example")
CLOCK = pygame.time.Clock()
FPS=120 # Higher FPS ensures smoother motion in video and gameplay

object_me = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, BALL_SPEED)

def main():
    # Ball setup
    ball_x = SCREEN_WIDTH // 2
    ball_y = SCREEN_HEIGHT // 2

    # Velocity variables for the ball
    velocity_x = 0
    velocity_y = 0
    player_state = -1 # none

    running = True

    while running:
        # Get all currently pressed keys
        keys = pygame.key.get_pressed()
        # ./package/module/function
        #   
        # Logic for movements in general
        velocity_x = 0
        velocity_y = 0
        # state #1: normal condition ................................... (0: right,1: up,2: left,3: down)
        # state #2: freezed condition .................................. (-1: freezed / none)
        # state #3: diagonal condition ................................... (4: diagonal)
        match True:
            case _ if keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]: object_me.set_state(-1)
            case _ if keys[pygame.K_UP] and keys[pygame.K_DOWN]: object_me.set_state(-1)
            case _ if keys[pygame.K_RIGHT]: object_me.set_state(0)
            case _ if keys[pygame.K_UP]: object_me.set_state(1)
            case _ if keys[pygame.K_LEFT]: object_me.set_state(2)
            case _ if keys[pygame.K_DOWN]: object_me.set_state(3)
        
        print(object_me.get_state())
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Update ball position
        ball_x += velocity_x
        ball_y += velocity_y

        # Boundary collision check
        if ball_x - BALL_RADIUS < 0:
            ball_x = BALL_RADIUS
        elif ball_x + BALL_RADIUS > SCREEN_WIDTH:
            ball_x = SCREEN_WIDTH - BALL_RADIUS

        if ball_y - BALL_RADIUS < 0:
            ball_y = BALL_RADIUS
        elif ball_y + BALL_RADIUS > SCREEN_HEIGHT:
            ball_y = SCREEN_HEIGHT - BALL_RADIUS

        # Fill the screen with a color
        screen.fill("purple")

        # Draw the ball
        pygame.draw.circle(screen, "white", (ball_x, ball_y), BALL_RADIUS)

        # Flip the display to update the screen
        pygame.display.flip()

        # Limit the frame rate
        CLOCK.tick(FPS)

    pygame.quit()





if __name__ == "__main__":
    main()