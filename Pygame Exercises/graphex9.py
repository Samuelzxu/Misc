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
    mb = mouse.get_pressed()
    mx, my = mouse.get_pos()
    c = (randint(0,255), randint(0,255), randint(0,255))
    rad = distform(400,300,mx,my)//7
    if mb[0]==1:
        draw.circle(screen, c, (mx,my), rad)
    #--------------------------------------------
    display.flip()

quit()
            
