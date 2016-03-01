#graph1.py

from pygame import *

screen = display.set_mode((800, 600))
running = True

while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
    #--------------------------------------------
    draw.line(screen, (255,0,0),(0,0),(300,400),2)
    draw.rect(screen, (0,0,255),(400,40,100,50))
    draw.circle(screen, (231,87,87),(100,300),100)
    #--------------------------------------------
    display.flip()
    
quit()
            
