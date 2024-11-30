import pygame
from constants import RED, GREEN, PLAYER_RADIUS, LEVEL_TIME

class Player:
    def __init__(self, screen_width, screen_height):
        self.x = screen_width // 2
        self.y = screen_height // 2
        self.color = RED
        self.radius = PLAYER_RADIUS
        self.speed = 5
        self.time_since_color_change = 0

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed

    def update_color(self):
        print("Time in milliseconds:", pygame.time.get_ticks())
        print("Time in seconds:", pygame.time.get_ticks() // 1000)
        current_time = pygame.time.get_ticks() // 1000  # Time in seconds
        color_state = current_time % 10  # Ranges from 0 to 9
        # Interpolate between RED and GREEN
        ratio = color_state / 9  # Normalize to a value between 0 and 1
        r = int((1 - ratio) * 255 + ratio * 0)  # Gradually decrease red channel
        g = int((1 - ratio) * 0 + ratio * 255)  # Gradually increase green channel
        b = 0  # Blue channel remains constant
        self.color = (r, g, b)  # Update the player's color


    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
