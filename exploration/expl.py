import random as r
import queue as q
import json as js
from colorama import init
from termcolor import colored
s=15
worldmap=[ [0 for i in range(s*3)] for j in range(s*3)] 
#setting a world map to 0
def worldSet(map):
    points=[0 for x in range(s*3)]
    i=0
    while(i<s*3):
        #picking random coordinates to seed the land scape
        #x and y are literally the x and y coordinates
        x=r.randint(0,(s*3)-1)
        y=r.randint(0,(s*3)-1)
        xy=[x,y]
        if xy not in points:
            points[i]=xy
            i=i+1
    return points
def randomizer():
    if r.randint(1,10)<4:
        return True
    else:
        return False

def pointsGrow(points,wm):
    #here is where the  coordinates from world set will grow out into land masses
    que=q.Queue()
    
    for p in points:
            que.put(p)
            x=p[0]
            y=p[1]
            try:
                wm[x][y]= r.randint(1,6)
            except:
                pass
    while not que.empty():
        plot=que.get()
        x=plot[0]
        y=plot[1]
        try:
            if wm[x+1][y]==0:
                if randomizer()==True:
                    wm[x+1][y]=r.randint(1,6)
                else:    
                    wm[x+1][y]=wm[x][y]
                
                que.put([x+1,y])
            if wm[x-1][y]==0:
                if randomizer()==True:
                    wm[x-1][y]=r.randint(1,6)
                else:
                    wm[x-1][y]=wm[x][y]
              
                que.put([x-1,y])
            if wm[x][y+1]==0:
                if randomizer()==True:
                    wm[x][y+1]=r.randint(1,6)
                else:
                    wm[x][y+1]=wm[x][y]
                
                que.put([x,y+1])
            if wm[x][y-1]==0:
                if randomizer()==True:
                    wm[x][y-1]=r.randint(1,6)
                else:
                    wm[x][y-1]=wm[x][y] 
                que.put([x,y-1])
        except:        
           pass
    return wm         
def jRead(jsfile):
    intake=open(jsfile)
    output=js.load(intake)
    return output

def landSet(world):
    wm=world
    colors=[[0 for m in range(len(world))] for o in range(len(world))]
    biome=jRead("land.json")
    blist=[ x for x in biome["Land"]]

    
    for i in range(len(world)):
        for j in range(len(world[i])):
            for x in range(len(blist)):
                try:
                    if world[i][j]==blist[x]["id"]: 
                        wm[i][j]=blist[x]["dis"]
                        colors[i][j]=blist[x]["color"]
                except:
                    pass

               
    return wm,colors

a, color=landSet(pointsGrow(worldSet(worldmap), worldmap))

init()

for i in range(len(a)):
    for j in range(len(a[i])):
        
        print(colored(*a[i][j], color[i][j]), end="",sep="")

    print("")    