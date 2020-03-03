"""
ScoreDisplay Class (based on Gameobject).
"""

import pygame

import config as c
import colors
from general_object import GeneralObject
from text_object import TextObject

class ClockDisplay(GeneralObject):
    def __init__ (self, x, y, width, height, color):
        GeneralObject.__init__(self, x, y, width, height)
        self.color = color
      
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def update(self):
        super().update()





    