from pico2d import *
import math


open_canvas()

grass = load_image('grass.png')
boy = load_image('character.png')

def draw_boy(x,y):
        clear_canvas_now()
        boy.draw_now(x, y)
        delay(0.1)

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

def run_top():
    print('top')
    for x in range(0,800, 10):
        draw_boy(x, 550)

def run_right():
    print('right')
    for y in range(550, 0, -10):
        draw_boy(790, y)

def run_bottom():
    print('bottom')
    for x in range(790, 0, -10):
        draw_boy(x, 30)


def run_left():
    print('left')
    
def run_rectangle():
    print('rectangle')
    #run_top()
    #run_right()
    run_bottom()
    run_left()
    
    
    pass

def run_triangle():
    pass

    
while True:
    #run_circle()
    run_rectangle()
    break
    
# fill here

close_canvas()
