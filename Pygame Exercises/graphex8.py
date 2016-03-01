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
    mb = mouse.get_pressed()
    mx, my = mouse.get_pos()
    c = (randint(0,255), randint(0,255), randint(0,255))
    if mb[0]==1:
        if mx < 400 and my < 300:
            draw.line(screen, c, (0,0),(mx,my))
        elif mx > 400 and my < 300:
            draw.line(screen, c, (800,0),(mx,my))
        elif mx < 400 and my > 300:
            draw.line(screen, c, (0,600),(mx,my))
        elif mx > 400 and my > 300:
            draw.line(screen, c, (800,600),(mx,my))
    #--------------------------------------------
    display.flip()

quit()
            
