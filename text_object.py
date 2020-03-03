"""
Base TextObject Class for creating a text object.

"""

import pygame

class TextObject:
    def __init__(self, x, y, text_func, color, font_name, font_size, centralized=False):
        self.pos = (x, y)
        self.text_func = text_func
        self.color = color
        self.font = pygame.font.SysFont(font_name, font_size)
        self.text_surface_area  = self.get_surface(text_func())
        self.centralized = centralized

    def get_surface(self, text):
        text_surface = self.font.render(text, False, self.color)
        return text_surface, text_surface.get_rect()
    
    def draw(self, surface):
        text_surface, self.text_surface_area = self.get_surface(self.text_func())
        # centralized работает корректно, когда при создании тексовой поверхности передаются
        # координаты центра кнопки или поверхности для отрисовки
        if self.centralized:
            pos = (self.pos[0] - self.text_surface_area.width/2, self.pos[1] - self.text_surface_area.height/2)
        else:
            pos = self.pos
        surface.blit(text_surface, pos)

    def update(self):
        pass





