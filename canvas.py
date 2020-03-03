"""
Canvas Class (based on Generalobject).

"""

import pygame
from general_object import GeneralObject

class Canvas(GeneralObject):
    def __init__(self, x, y, width, height, color):
        GeneralObject.__init__(self, x, y, width, height)
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
