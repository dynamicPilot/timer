"""
The main class of the timer that defines the display, objects, methods, etc.

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
        
        self.start_time = None
        self.pause_time = None
        self.time_over = False
        self.time_delta_to_stop = None
        self.current_delta = None
        
        self.menu_buttons = []
        self.start_timer = False
        self.is_timer_running = False
        self.pause_timer = False

        self.start_menu_objects = []
        
    def show_message(self, text, color=colors.GRAY24, font_name='Century', font_size=20, centralized=False):
        message = TextObject(c.w_x_size // 2, c.w_y_size // 2, lambda: text, color, font_name, font_size, True)
        self.draw()
        message.draw(self.surface)
        pygame.display.update()
        time.sleep(c.message_duration)

    # Create canvas
    def create_canvas(self):
        canvas = Canvas(c.margin, c.margin, c.can_x_size, c.can_y_size, c.can_color[self.style_mode])
        self.objects.append(canvas)

    # Create clock display
    def create_clock_display(self):
        clock_display = ClockDisplay(c.clock_x, c.clock_y, c.clock_x_size, c.clock_y_size, c.clock_color[self.style_mode])
        #text =  time.strftime("%H : %M", 
        clock_text = TextObject(clock_display.centerx, clock_display.centery, self.text_for_time, c.clock_text_color[self.style_mode], c.clock_font_name, c.clock_font_size, True)
        self.objects.append(clock_display)
        self.objects.append(clock_text)

    def create_mode_display(self):
        mode_display = ClockDisplay(c.mode_x, c.mode_y, c.mode_x_size, c.mode_y_size, c.mode_color[self.style_mode])
        mode_text = TextObject(mode_display.centerx, mode_display.centery, self.text_for_mode, c.mode_text_color[self.style_mode], c.mode_font_name, c.mode_font_size, True)
        self.objects.append(mode_display)
        self.objects.append(mode_text)

    def create_remain_repeate_display(self):
        rr_display = ClockDisplay(c.rr_x, c.rr_y, c.rr_x_size, c.rr_y_size, c.rr_color[self.style_mode])
        rr_text = TextObject(rr_display.centerx, rr_display.centery, self.text_for_rr, c.rr_text_color[self.style_mode], c.rr_font_name, c.rr_font_size, True)
        self.objects.append(rr_display)
        self.objects.append(rr_text)

    def create_start_menu_displays(self):
        display = ClockDisplay(c.start_menu_display_x, c.start_menu_down_display_y, c.start_menu_display_x_size, c.start_menu_display_y_size, c.start_menu_display_color)
        display_text = TextObject(display.centerx, display.centery, lambda: 'Set color mode...', c.start_menu_display_text_color, c.start_menu_display_font_name, c.start_menu_display_font_size, True)
        self.objects.append(display)
        self.objects.append(display_text)
        self.start_menu_objects.append(display)
        self.start_menu_objects.append(display_text)

        display = ClockDisplay(c.start_menu_display_x, c.start_menu_up_display_y, c.start_menu_display_x_size, c.start_menu_display_y_size, c.start_menu_display_color)
        display_text = TextObject(display.centerx, display.centery, lambda: 'Set cicles number...', c.start_menu_display_text_color, c.start_menu_display_font_name, c.start_menu_display_font_size, True)
        self.objects.append(display)
        self.objects.append(display_text)
        self.start_menu_objects.append(display)
        self.start_menu_objects.append(display_text)

    def text_for_rr(self):
        return '{}'.format(self.timer_repeats)

    def text_for_mode(self):
        if self.start_time is None:
            return 'Press Start...'
        else:
            if self.do_time:
                return 'Work time...'
            elif self.rest_time:
                return 'Rest time...'
            else:
                return ''

    def text_for_time(self):
        if self.start_time is None:
            return '{:02d} : 00'.format(self.set_time_in_minutes)
        else:
            if not self.pause_timer:
                self.current_delta = self.time_delta_to_stop.seconds - (datetime.now() - self.start_time).seconds
            return '{:02d} : {:02d}'.format(self.current_delta//60, self.current_delta % 60)

    # Create timer menu
    def create_menu(self):
        def on_start_timer(button):
            self.start_timer = True
            self.is_timer_running = True
            
        def on_pause_timer(button):
            self.pause_timer = True
            self.is_timer_running = False
            # Set time when pause
            if self.start_time is not None:
                self.pause_time = datetime.now()
            # To catch error when press Pause before start
            if self.start_time is None and not self.start_timer:
                self.pause_timer = False

        def on_end_timer(button):
            self.start_timer = False
            self.is_timer_running = False
            self.pause_timer = False
            self.start_time = None
            self.current_timer_over = True

        actions = {'Start': on_start_timer, 'Pause': on_pause_timer, 'End': on_end_timer}
        for key, value in actions.items():
            but = Button(c.button_params[key][0], c.button_params[key][1], c.button_x_size, c.button_y_size, c.button_color[self.style_mode], str(key), c.button_text_color[self.style_mode], value)
            self.objects.append(but)
            self.menu_buttons.append(but)
            self.mouse_handlers.append(but.handle_mouse_event)

    def new_circle_prep(self):

        self.start_timer = False
        self.pause_timer = False
        self.start_time = None
        self.pause_time = None
        self.time_delta_to_stop = None
        self.current_delta = None

        self.current_timer_over = False

        self.create_objects()

    # Create start menu
    def create_start_menu(self):
        
        self.is_timer_running = False

        def on_close_start_menu(button):
            self.remove_start_menu()

        def on_light_mode(button):
            self.style_mode = 'light'

        def on_dark_mode(button):
            self.style_mode = 'dark'

        def on_violet_mode(button):
            self.style_mode = 'violet'

        def on_key(button, key):
            self.timer_repeats = key


        # Create start menu canvas
        canvas = Canvas(c.margin, c.margin, c.can_x_size, c.can_y_size, c.start_can_color)
        self.start_menu_objects.append(canvas)
        self.objects.append(canvas)

        self.create_start_menu_displays()

        actions = {'Ok': on_close_start_menu, 'Light': on_light_mode, 'Dark': on_dark_mode, 'Violet': on_violet_mode}
        for key, value in actions.items():
            but = Button(c.start_menu_button_params[key][0], c.start_menu_button_params[key][1], c.start_menu_button_x_size, c.start_menu_button_y_size, c.start_menu_button_color, str(key), c.start_menu_button_text_color, value)
            self.objects.append(but)
            self.start_menu_objects.append(but)
            self.mouse_handlers.append(but.handle_mouse_event)

        for key in [1, 2, 3, 4]:
            but = Button(c.start_menu_n_button_params[key][0], c.start_menu_n_button_params[key][1], c.start_menu_n_button_x_size, c.start_menu_n_button_y_size, c.start_menu_button_color, str(key), c.start_menu_button_text_color, on_key, key)
            self.objects.append(but)
            self.start_menu_objects.append(but)
            self.mouse_handlers.append(but.handle_mouse_event)

    def remove_start_menu(self):
        self.objects = []
        self.new_circle_prep()
        self.create_objects()

    def create_objects(self):
        self.create_canvas()
        self.create_clock_display()
        self.create_menu()
        self.create_mode_display()
        self.create_remain_repeate_display()


    def update(self):

        if not self.is_timer_running:
            return
        
        if self.start_timer:
            self.start_timer = False
            # Set time when timer begins 
            if self.start_time is None:
                self.start_time = datetime.now()
                self.time_delta_to_stop = timedelta(seconds = self.set_time_in_seconds)
            # Handle the end of a pause
            if self.pause_timer == True:
                self.pause_timer = False
                if self.pause_time is not None:
                    self.time_delta_to_stop += datetime.now() - self.pause_time
      
        if not self.time_over:
            if datetime.now() - self.start_time >= self.time_delta_to_stop:
                self.time_over = True

        super().update()
        
        if self.time_over:
            self.start_time = None
            self.start_timer = True
            self.current_timer_over = True

    # Main
    def start_timer_run(self):
        while not self.timer_over:
            self.create_start_menu()
            self.run_multiple_intervals()

            
def main():
    SimpleTimer().start_timer_run()

if __name__ == '__main__':
    main()

