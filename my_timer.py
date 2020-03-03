"""
The main class of the game that defines the display, game objects, methods, rules, etc.

"""

import pygame
import time
import math
import random
from datetime import datetime, timedelta

import colors
import config as c

from timer import MyTimer
from clock_display import ClockDisplay
from canvas import Canvas
from text_object import TextObject
from button import Button


class SimpleTimer(MyTimer):
    def __init__ (self):
        MyTimer.__init__(self, 'Timer', c.w_x_size, c.w_y_size, c.frame_rate)

        self.clock_display = None
        self.set_time_in_minutes = 1
        self.set_time_in_seconds = self.set_time_in_minutes*60
        self.start_time = None
        self.pause_time = None
        self.time_over = False
        self.time_delta_to_stop = None
        self.current_delta = None
        
        self.menu_buttons = []
        self.start_timer = False
        self.is_timer_running = False
        self.pause_timer = False
        
    def show_message(self, text, color=colors.GRAY24, font_name='Arial', font_size=20, centralized=False):
        message = TextObject(c.w_x_size // 2, c.w_y_size // 2, lambda: text, color, font_name, font_size, True)
        self.draw()
        message.draw(self.surface)
        pygame.display.update()
        time.sleep(c.message_duration)

    # Create canvas
    def create_canvas(self):
        canvas = Canvas(c.margin, c.margin, c.can_x_size, c.can_y_size, c.can_color)
        self.objects.append(canvas)

    # Create clock display
    def create_clock_display(self):
        self.clock_display = ClockDisplay(c.clock_x, c.clock_y, c.clock_x_size, c.clock_y_size, c.clock_color)
        #text =  time.strftime("%H : %M", 
        self.clock_text = TextObject(self.clock_display.centerx, self.clock_display.centery, self.text_for_time, c.clock_text_color, c.clock_font_name, c.clock_font_size, True)
        self.objects.append(self.clock_display)
        self.objects.append(self.clock_text)

    def text_for_time(self):
        if self.start_time is None:
            return '{:02d} : 00'.format(self.set_time_in_minutes)
        else:
            if not self.pause_timer:
                self.current_delta = self.time_delta_to_stop.seconds - (datetime.now() - self.start_time).seconds
            return '{:02d} : {:02d}'.format(self.current_delta//60, self.current_delta % 60)

    # Create menu
    def create_menu(self):
        def on_start_timer(button):
            self.start_timer = True
            self.is_timer_running = True

        def on_pause_timer(button):
            self.pause_timer = True
            self.is_timer_running = False
            self.pause_time = datetime.now()

        def on_end_timer(button):
            self.start_timer = False
            self.is_timer_running = False
            self.pause_timer = False
            self.start_time = None

        actions = {'Start': on_start_timer, 'Pause': on_pause_timer, 'End': on_end_timer}
        for key, value in actions.items():
            but = Button(c.button_params[key][0], c.button_params[key][1], c.button_x_size, c.button_y_size, c.button_color_normal, str(key), value)
            self.objects.append(but)
            self.menu_buttons.append(but)
            self.mouse_handlers.append(but.handle_mouse_event)


    def create_objects(self):
        self.create_canvas()
        self.create_clock_display()
        self.create_menu()


    def update(self):
        if not self.is_timer_running:
            return
        

        if self.start_timer:
            self.start_timer = False
            self.time_over = False
            #self.show_message('Start Timer...', centralized=True)
            if self.start_time is None:
                self.start_time = datetime.now()
                self.time_delta_to_stop = timedelta(seconds = self.set_time_in_seconds)
            if self.pause_timer == True:
                self.pause_timer = False
                self.time_delta_to_stop += datetime.now() - self.pause_time
      
        if not self.time_over:
            if datetime.now() - self.start_time >= self.time_delta_to_stop:
                self.time_over = True

        super().update()
        
        if self.time_over:
            #self.show_message('Time is over!', centralized=True)
            #self.timer_over = True
            self.start_time = None
            self.start_timer = False

    # Main
    def start_timer_run(self):
        self.create_objects()
        self.run()

            
def main():
    SimpleTimer().start_timer_run()

if __name__ == '__main__':
    main()

