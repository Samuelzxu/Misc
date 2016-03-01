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
    mouse.set_visible(False)
    screen.fill((0,0,0))
    mx, my = mouse.get_pos()
    draw.line(screen,(0,255,0),(mx,0),(mx,600))
    draw.line(screen,(0,255,0),(0,my),(800,my))
    #--------------------------------------------
    display.flip()
    
quit()
            
