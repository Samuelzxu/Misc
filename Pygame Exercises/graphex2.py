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
        for i in range (-2,3):
            draw.circle(screen,(0,255,0),(mx+i*10,my+20),5)
        draw.circle(screen,(255,0,0),(mx+20,my+10),5)
        draw.circle(screen,(255,0,0),(mx+20,my),5)
        draw.circle(screen,(255,0,0),(mx+20,my-10),5)
        draw.circle(screen,(255,0,0),(mx-20,my+10),5)
        draw.circle(screen,(255,0,0),(mx-20,my),5)
        draw.circle(screen,(255,0,0),(mx-20,my-10),5)
        for j in range (-2,3):
            draw.circle(screen,(255,0,0),(mx+j*10,my-20),5)

            
          
    
    #--------------------------------------------
    display.flip()
    
quit()
            
