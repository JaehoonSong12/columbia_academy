import pygame
from december_escapes.constants import YELLOW

class Star:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

    def draw(self, surface):
        pygame.draw.rect(surface, YELLOW, (self.x, self.y, self.size, self.size))