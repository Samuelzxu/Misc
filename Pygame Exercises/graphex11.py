#graph1.py

from pygame import *
from random import *

screen = display.set_mode((800, 600))
running = True

screen.fill((247, 110, 110))
def distform(x1, y1, x2, y2):
    return int(((x1-x2)**2+(y1-y2)**2)**(1/2))

screen.fill((247, 110, 110))

while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONDOWN:
            screenPic = screen.copy()
    #--------------------------------------------
    mb = mouse.get_pressed()
    mx, my = mouse.get_pos()
    if mb[0] == 1:
        screen.blit(screenPic, (0,0))
        mouse.set_visible(False)
        draw.circle(screen, (0,255,0), (mx, my), 25)
        draw.circle(screen, (50,50,50), (mx, my), 26, 2)
    elif mb[2] == 1:
        screen.fill((247, 110, 110))
    mouse.set_visible(True)    
    #--------------------------------------------
    display.flip()

quit()
            
