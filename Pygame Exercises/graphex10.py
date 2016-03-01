#graph1.py

from pygame import *
from random import *

screen = display.set_mode((800, 600))
running = True
x = 400
y = 300

def distform(x1, y1, x2, y2):
    return int(((x1-x2)**2+(y1-y2)**2)**(1/2))

while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
    #--------------------------------------------
    screen.fill((0,0,0))
    mb = mouse.get_pressed()
    mx, my = mouse.get_pos()
    for i in range (0,11):
        draw.line(screen,(255,0,0),(i*80,0),(mx-50+i*10, my-50))
        draw.line(screen,(255,0,0),(i*80,600),(mx-50+i*10, my+50))
        draw.line(screen,(255,0,0),(0,i*60),(mx-50, my-50+i*10))
        draw.line(screen,(255,0,0),(800,i*60),(mx+50, my-50+i*10))

    #--------------------------------------------
    display.flip()

quit()
            
