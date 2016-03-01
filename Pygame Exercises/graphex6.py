#graph1.py

from pygame import *
from random import *

screen = display.set_mode((800, 600))
running = True
x = 400
y = 300
for i in range (1,60):
    if i % 2 == 0:
        draw.line(screen,(0,255,0),(x,y),(x,y+i*10),1)
        y = y+i*10
        draw.line(screen,(0,255,0),(x,y),(x+i*10,y),1)
        x = x + 10*i
        
    elif i % 2 == 1:
        draw.line(screen,(0,255,0),(x,y),(x,y-i*10),1)
        y = y - i*10
        draw.line(screen,(0,255,0),(x,y),(x-i*10,y),1)
        x = x - 10*i

while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
    #--------------------------------------------
    #--------------------------------------------
    display.flip()

quit()
            
