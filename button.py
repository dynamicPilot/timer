"""
Button Class (based on Gameobject).
---
Класс для кнопок (на основе GameOdject).
"""

import pygame

import config as c
import colors
from general_object import GeneralObject
from text_object import TextObject

class Button(GeneralObject):
    def __init__ (self, x, y, w, h, button_normal_back_color, text, on_click = lambda x: None, padding = 0):
        GeneralObject.__init__(self, x, y, w, h)
        self.state = 'normal'
        self.button_normal_back_color = button_normal_back_color
        self.on_click = on_click
        self.text = TextObject(self.centerx, self.centery, lambda: text, c.button_text_color, c.button_font_name, c.button_font_size, True)

    def draw(self, surface):
        pygame.draw.rect(surface, self.back_color, self.rect)
        self.text.draw(surface)

    def handle_mouse_event(self, type, pos):
        if type == pygame.MOUSEMOTION:
            self.handle_mouse_move(pos)
        elif type == pygame.MOUSEBUTTONDOWN:
            self.handle_mouse_down(pos)
        elif type == pygame.MOUSEBUTTONUP:
            self.handle_mouse_up(pos)

    def handle_mouse_move(self, pos):
        if self.rect.collidepoint(pos):
            if self.state != 'pressed':
                self.state = 'hover'
        else:
            self.state = 'normal'

    def handle_mouse_down(self, pos):
        if self.rect.collidepoint(pos):
            self.state = 'pressed'

    def handle_mouse_up(self, pos):
        if self.state == 'pressed':
            self.on_click(self)
            self.state = 'hover'

    @property
    def back_color(self):
        return {'normal': self.button_normal_back_color, 'hover': c.button_color_hover, 'pressed': c.button_color_pressed}[self.state]


    