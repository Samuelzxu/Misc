#graph1.py

from pygame import *

screen = display.set_mode((800, 600))
running = True

while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
    #--------------------------------------------
    mb = mouse.get_pressed()
    mx, my = mouse.get_pos()
    print(mx, my, mb)
    if mb[0]==1:
        draw.circle(screen,(255,200,200),(mx,my), 10)
    if mb[2]==1:
        draw.circle(screen,(0,0,0),(mx,my), 20)
    #--------------------------------------------
    display.flip()
    
quit()
            
