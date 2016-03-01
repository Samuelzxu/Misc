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
    for i in range (-600,1500,10):
        draw.line(screen,(0,255,0),(0,i),(i,0),1)
        draw.line(screen,(0,255,0),(i,0),(i+600,600),1)
    #--------------------------------------------
    display.flip()
    
quit()
            
