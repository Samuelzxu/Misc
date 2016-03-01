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
    
    if mb[0]==1:
        
    #--------------------------------------------
    display.flip()
    
quit()
            
