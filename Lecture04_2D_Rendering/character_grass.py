from pico2d import *
import math


open_canvas()

grass = load_image('grass.png')
boy = load_image('character.png')

def run_circle():
    print('circle')

    r, cx, cy = 300, 800//2, 600/2
    for deg in range(0, 360, 3):
        theta = math.radians(deg)
        x =  r * math.cos(theta) + cx
        y = r * math.sin(theta) + cy
        
        clear_canvas_now()
        boy.draw_now(x, y)
        delay(0.1)
    
    pass

def run_rectangle():
    print('rectangle')
    
    pass
    
while True:
    run_circle()
    run_rectangle()
    break
    
# fill here

close_canvas()
