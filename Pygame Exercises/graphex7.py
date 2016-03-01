#graph1.py

from pygame import *
from random import *

screen = display.set_mode((800, 600))
running = True
x = 400
y = 300

while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
    #--------------------------------------------
    screen.fill((0,0,0))
    mb = mouse.get_pressed()
    mx, my = mouse.get_pos()
    dist = ((mx-400)**2+(my-300)**2)**(1/2)
    dist = max(1,dist)
    inc = int(dist)
    ix = (mx - x)/dist
    iy = (my - y)/dist
    
    for j in range (0, inc):
        draw.circle(screen, (0,255, 0), (int(x+ix*j), int(y+iy*j)), 3)
    draw.circle(screen, (0,0,255), (x,y), 10)
    draw.circle(screen, (0,0,255), (mx,my), 10)
    #--------------------------------------------
    display.flip()

quit()
            
