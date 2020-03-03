import math
import colors

w_x_size = 300
w_y_size = 300
w_color = colors.WHITE

frame_rate = 10
message_duration = 2

margin = 10

can_x_size = w_x_size - 2*margin
can_y_size = w_y_size - 2*margin
can_color = colors.EGGSHELL

x_center = 150
y_center = 130

clock_x_size = 200
clock_y_size = 70
clock_x = (w_x_size - clock_x_size)/2
clock_y = (w_y_size - clock_y_size)/2
clock_ramp_width = 1

clock_ramp_color = colors.DIMGRAY
clock_color = colors.WHITE

clock_text_color = colors.DIMGRAY
clock_font_size = 25
clock_font_name = 'Century'

button_x_size = 50
button_y_size = 50
button_y = w_y_size/2 + clock_y/2 + margin
button_center_x = w_x_size/2 - button_x_size/2
button_margin = 15

button_color_normal = colors.WHITE
button_color_hover = colors.MEDIUMPURPLE4
button_color_pressed = colors.WHITE

button_params = {'Start': [button_center_x - button_margin - button_x_size, button_y], 'Pause': [button_center_x, button_y], 'End': [button_center_x + button_margin + button_x_size, button_y]}
button_font_size = 15
button_font_name = 'Century'
button_text_color = colors.DIMGRAY