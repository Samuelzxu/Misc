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
    x = randint(0,800)
    y = randint(0,600)
    x1 = randint(0,800)
    y1 = randint(0,600)
    r = randint(0,300)
    c = (randint(0,255),randint(0,255),randint(0,255),)
    if x - r < 0:
        x = r
    if y - r < 0:
        y = r
    if x + r > 800:
        x = 800 - r
    if y + r > 600:
        y = 600 - r
    #draw.line(screen,c,(x1,y1),(x,y),randint(0,800))
    draw.circle(screen, c, (x,y), r)
    #--------------------------------------------
    display.flip()
    
quit()
            
