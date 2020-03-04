import math
import colors

w_x_size = 300
w_y_size = 300
w_color = {'light': colors.WHITE, 'dark': colors.SGIGRAY32,'violet': colors.MEDIUMPURPLE4}

frame_rate = 10
message_duration = 2

timer_repeats = 1
timer_rest_interval = 5
timer_do_interval = 25

margin = 10

can_x_size = w_x_size - 2*margin
can_y_size = w_y_size - 2*margin
can_color = {'light': colors.EGGSHELL, 'dark': colors.PALETURQUOISE4,'violet': colors.MEDIUMPURPLE4}

x_center = 150
y_center = 130

clock_x_size = 200
clock_y_size = 70
clock_x = (w_x_size - clock_x_size)/2
clock_y = (w_y_size - clock_y_size)/2
clock_ramp_width = 1

clock_ramp_color = colors.DIMGRAY
clock_color = {'light': colors.WHITE, 'dark': colors.SGIGRAY32,'violet': colors.LAVENDER} 

clock_text_color = {'light': colors.DIMGRAY, 'dark': colors.WHITE, 'violet': colors.MEDIUMPURPLE4}
clock_font_size = 25
clock_font_name = 'Century'

button_x_size = 60
button_y_size = 50
button_y = w_y_size/2 + clock_y/2 + margin
button_center_x = w_x_size/2 - button_x_size/2
button_margin = 15

button_color = {'light': {'normal': colors.WHITE, 'hover': colors.SANDYBROWN, 'pressed': colors.WHITE},
'dark': {'normal': colors.SGIGRAY32, 'hover': colors.SGIGRAY16, 'pressed': colors.SGIGRAY32},
'violet': {'normal': colors.LAVENDER, 'hover': colors.ORANGE, 'pressed': colors.LAVENDER}}

button_params = {'Start': [button_center_x - button_margin - button_x_size, button_y], 'Pause': [button_center_x, button_y], 'End': [button_center_x + button_margin + button_x_size, button_y]}
button_font_size = 15
button_font_name = 'Century'
button_text_color = {'light': colors.DIMGRAY, 'dark': colors.WHITE, 'violet': colors.MEDIUMPURPLE4}

mode_x_size = 150
mode_y_size = 50

rr_x_size = 50
rr_y_size = 50

mode_rr_x_size = mode_x_size + rr_x_size + 15

mode_x = x_center - mode_rr_x_size/2
mode_y = w_y_size/2 - clock_y/2 - margin - mode_y_size
mode_color = {'light': colors.WHITE, 'dark': colors.SGIGRAY32,'violet': colors.LAVENDER}

mode_text_color = {'light': colors.DIMGRAY, 'dark': colors.WHITE, 'violet': colors.MEDIUMPURPLE4}
mode_font_size = 20
mode_font_name = 'Century'

rr_x = x_center + mode_rr_x_size/2 - rr_x_size
rr_y = w_y_size/2 - clock_y/2 - margin - mode_y_size
rr_color = {'light': colors.WHITE, 'dark': colors.SGIGRAY32,'violet': colors.LAVENDER}

rr_text_color = {'light': colors.DIMGRAY, 'dark': colors.WHITE, 'violet': colors.MEDIUMPURPLE4}
rr_font_size = 20
rr_font_name = 'Century'

sounds_effect = {'time_is_over': 'uku.wav'}

#start menu
start_can_color = colors.GRAY

start_menu_button_margin = 15
start_menu_button_x_size = 60
start_menu_button_y_size = 50
start_menu_button_color = {'normal': colors.WHITE, 'hover': colors.BANANA, 'pressed': colors.BANANA}

start_menu_button_params = {'Ok': [w_x_size - 2*margin - start_menu_button_x_size, w_y_size - 2*margin - start_menu_button_y_size],
'Light': [x_center - start_menu_button_margin - start_menu_button_x_size*3/2, w_y_size - 2*margin - start_menu_button_y_size - start_menu_button_margin - start_menu_button_y_size],
'Dark': [x_center - start_menu_button_x_size/2, w_y_size - 2*margin - start_menu_button_y_size - start_menu_button_margin - start_menu_button_y_size],
'Violet': [x_center + start_menu_button_margin + start_menu_button_x_size/2, w_y_size - 2*margin - start_menu_button_y_size - start_menu_button_margin - start_menu_button_y_size]}
start_menu_button_font_name = 'Century'
start_menu_button_text_color = colors.DIMGRAY

start_menu_display_x_size = 200
start_menu_display_y_size = 40
start_menu_display_x = x_center - start_menu_display_x_size/2
start_menu_up_display_y = 2*margin
start_menu_down_display_y = w_y_size - 2*margin - start_menu_button_y_size - 2*start_menu_button_margin - start_menu_button_y_size - start_menu_display_y_size

start_menu_display_color = colors.WHITE
start_menu_display_text_color = colors.DIMGRAY
start_menu_display_font_size = 18
start_menu_display_font_name = 'Century'

start_menu_n_button_margin = 15
start_menu_n_button_x_size = 30
start_menu_n_button_y_size = 30

start_menu_n_button_params ={1: [x_center - start_menu_n_button_margin*3/2 - 2*start_menu_n_button_x_size, start_menu_display_y_size + 8 + 2*margin],
2: [x_center - start_menu_n_button_margin/2 - start_menu_n_button_x_size, start_menu_display_y_size + 8 + 2*margin],
3: [x_center + start_menu_n_button_margin/2, start_menu_display_y_size + 8 + 2*margin],
4: [x_center + start_menu_n_button_margin*3/2 + start_menu_n_button_x_size, start_menu_display_y_size + 8 + 2*margin]}




