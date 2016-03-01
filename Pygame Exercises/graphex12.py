#graph1.py

from pygame import *
from random import *
from math import *

screen = display.set_mode((800, 600))
running = True
screen.fill((255,255,255))

def distform(x1, y1, x2, y2):
    return ((x1-x2)**2+(y1-y2)**2)**(1/2)

while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
    #--------------------------------------------
    screen.fill((255,255,255))
    mx, my = mouse.get_pos()
    for i in range (0,20):
        for j in range (0,15):
            x = i*40
            y = j*40
            a = mx-x
            b = my-y
            d = hypot(a,b)
            d = max(1, d)
            draw.line(screen,(0,0,0),(x,y),(20*a/d+x,20*b/d+y),2)
            draw.circle(screen,(255,0,0),(i*40, j*40),3)
    #--------------------------------------------
    display.flip()

quit()
            
