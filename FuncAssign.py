def numFactors(num):
    facts = []
    for i in range (1,num+1):
        if num % i == 0:
            facts.append(i)
    return len(facts)

def subtract(list1,list2):
    list3 = list1[:]
    for i in range (len(list2)):
        if list2[i] in list3:
            list3.remove(list2[i])
    return list3

def justify(words,length):
    rem = 0
    for i in range (len(words)):
        space = length - len(words[i])
    if space > len(words):
        rem = int(space%len(words))
        space = int(space/len(words))
    else:
        return"invalid"
    if rem == 0:
        for i in range (len(words)):
            print(words[i]," "*space,end="")
        print(words[len(words)]

def grid(x,y,l,w):
    draw.line(screen,(255,255,255),(l/2,0),(l/2,w),3)
    draw.line(screen,(255,255,255),(0,w/2),(l,w/2),3)
    if l>40 and w>30:
        for i in range (
              

screen = display.set_mode((800, 600))
running = True

while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
    
    display.flip()     


    
        
