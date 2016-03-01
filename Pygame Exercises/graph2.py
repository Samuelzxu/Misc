#graph1.py

from pygame import *

screen = display.set_mode((800, 600))
running = True

while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
    #--------------------------------------------
    for x in range (0, 600, 5):
        draw.line(screen, (0,255,0), (0,x), (800,x))
    for y in range (0, 800, 13):
        draw.line(screen, (255,0,0), (y,0), (y,600))
    #--------------------------------------------
    display.flip()
    
quit()
            
