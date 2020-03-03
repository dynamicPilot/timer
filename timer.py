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
        self.current_timer_over = False

        self.objects = []

        self.timer_repeats = c.timer_repeats
        self.timer_rest_interval = c.timer_rest_interval
        self.timer_do_interval = c.timer_do_interval
        self.do_time = False
        self.rest_time = False
        self.set_time_in_minutes = 0
        self.set_time_in_seconds = 0

        pygame.mixer.pre_init(44100, 16, 2, 4096)
        pygame.init()
        pygame.font.init()

        self.sound_effect = {name: pygame.mixer.Sound(sound) for name, sound in c.sounds_effect.items()}
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
        while not self.current_timer_over:
            self.surface.fill(c.w_color)
            
            self.handle_events()
            self.update()
            self.draw()

            pygame.display.update()
            self.clock.tick(self.frame_rate) 

    def run_multiple_intervals(self):
        while not self.timer_over:
            if self.timer_repeats > 0:
                # To Do time
                print('Start To Do')
                self.current_timer_over = False
                self.do_time = True
                self.rest_time = False
                self.set_time_in_minutes = self.timer_do_interval
                self.set_time_in_seconds = self.set_time_in_minutes*60
                self.run()
                print('To do time is over')
                self.sound_effect['time_is_over'].play()

                # Rest time
                print('Start rest')
                self.current_timer_over = False
                self.do_time = False
                self.rest_time = True
                self.set_time_in_minutes = self.timer_rest_interval
                self.set_time_in_seconds = self.set_time_in_minutes*60
                self.run()
                print('Rest time is over')
                self.sound_effect['time_is_over'].play()

                self.timer_repeats -=1







