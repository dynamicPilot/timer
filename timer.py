"""
Base Game Class for creating a game.

"""

import pygame
import sys
from collections import defaultdict

import config as c

class MyTimer:
    def __init__(self, caption, width, height, frame_rate):
        self.frame_rate = frame_rate
        self.timer_over = False
        self.objects = []


        pygame.mixer.pre_init(44100, 16, 2, 4096)
        pygame.init()
        pygame.font.init()

        self.surface = pygame.display.set_mode((width, height))
  
        pygame.display.set_caption(caption)
        self.clock = pygame.time.Clock()
        self.mouse_handlers = []

    def update(self):
        for obj in self.objects:
            obj.update()

    def draw(self):
        for obj in self.objects:
            obj.draw(self.surface)


    def handle_events(self):
        for event in pygame.event.get(): #цепочка событий
            if event.type == pygame.QUIT:
                pygame.quit()
                #sys.exit()
            elif event.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION):
                for handler in self.mouse_handlers:
                    handler(event.type, event.pos)

    def run(self):
        while not self.timer_over:
            self.surface.fill(c.w_color)
            
            self.handle_events()
            self.update()
            self.draw()

            pygame.display.update()
            self.clock.tick(self.frame_rate) 

