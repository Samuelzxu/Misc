def grid(x,y,l):
    draw.rect(screen,(255,255,255),(x,y,l,l))
    draw.line(screen,(255,255,255),(int(l/2),0),(int(l/2),w),1)
    draw.line(screen,(255,255,255),(0,int(l/2)),(l,int(l/2)),1)
    if l>10:
        grid(x,y,l/2)
        grid(x+l/2,y,l/2)
        grid(x,y+l/2,l/2)
        grid(x+l/2,y+l/2,l/2)
        

screen = display.set_mode((600, 600))
running = True

while running:
    for e in event.get():
        if e.type == QUIT:
            running = False

    
    display.flip()     
