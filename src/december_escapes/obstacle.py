import pygame

class Obstacle:
    def __init__(self, x, y, width, height, color, speed=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed

    def move(self, screen_width):
        if self.speed != 0:  # If it's a moving obstacle
            self.x += self.speed
            if self.x > screen_width or self.x < 0:
                self.speed = -self.speed

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))
