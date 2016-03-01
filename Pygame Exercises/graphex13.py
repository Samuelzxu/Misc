#graph1.py

from pygame import *
from random import *
from math import *

screen = display.set_mode((800, 600))
running = True
up = True
ct = -20
x = 0
y = 20

while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
    #--------------------------------------------'
    screen.fill((0,0,0))
    for j in range (1,30):
        for i in range (0,20):
            x = 40*i
            y = 20*j
            draw.line(screen,(0,255,0),(x,y),(x+20,y+ct))
            draw.line(screen,(0,255,0),(x+20,y+ct),(x+40,y))
    if up == True:
        ct += 1
        if ct == 20:
            up = False
    elif up == False:
        ct -= 1
        if ct == -20:
            up = True
    #--------------------------------------------
    time.wait(75)
    display.flip()

quit()
            
