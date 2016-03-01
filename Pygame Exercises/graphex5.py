#graph1.py

from pygame import *
from random import *

screen = display.set_mode((800, 600))
running = True

while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
    #--------------------------------------------
    mb = mouse.get_pressed()
    mx, my = mouse.get_pos()
    if mb[0] == 1:
        c = (randint(0,255),randint(0,255),randint(0,255))
        draw.line(screen,c,(0,0),(mx,my))
        draw.line(screen,c,(0,600),(mx,my))
        draw.line(screen,c,(800,0),(mx,my))
        draw.line(screen,c,(800,600),(mx,my))
    #--------------------------------------------
    display.flip()
    
quit()
            
