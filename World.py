from Square import Square
from collections import defaultdict
import tileGenerator
import random
import math
MAX_STEPS = 10000
def distance(x,y):
    return(math.sqrt((x[0]-y[0])**2+(x[1]-y[1])**2))
class World:
    def __init__(self):
        self.entities = []
        self.lines=[]
        self.deathLines=set()
        self.plan={"0,0": 0}
        self.oldX=None
        self.oldY=None
        self.oldTileX=None
        self.oldTileY=None
        self.lineTiles=defaultdict(list)
        self.charTiles=defaultdict(list)
        self.boolTiles=defaultdict(lambda: True)
        self.objectTiles=defaultdict(list)
        self.aliveLinesTiles=defaultdict(list)

    def registration(self,who,tile):
        
        if who.alive:
            self.charTiles[tile].append(who)
        else:
            self.objectTiles[tile].append(who)
            
        
    def deathLine(self,a,b):
        inTiles=self.lineToTiles(a,b)
        for i in inTiles:
            self.lineTiles[i].append((a,b))

    def generateDeathLines(self,cor):
        for i in self.objectTiles[cor]:
            i.update()

    def lineToTiles(self,a,b,tileSize=50):
        x1,y1=a
        x2,y2=b
        dx=x2-x1
        dy=y2-y1

        eps=10**-7

        lineEquationPoint=dx*y1-dy*x1
        xBegin=math.floor(x1/tileSize)*tileSize
        crossingx=[]
        crossingy=[]
        ndx=abs(x2-xBegin)
        crossPointsX=int(ndx/tileSize)
        xmultiplicator=1
        ymultiplicator=1
        if (x2<x1):
            xmultiplicator=-1
        if (y2<y1):
            ymultiplicator=-1

        if(dx!=0):

            for i in range(0,crossPointsX+1):
                newX=xBegin+i*tileSize*xmultiplicator+eps*xmultiplicator
                newY=(lineEquationPoint+dy*newX)/dx +eps*ymultiplicator
                crossingx.append((newX,newY))
        yBegin=math.floor(y1/tileSize)*tileSize
        ndy=abs(y2-yBegin)
        crossPointsY=int(ndy/tileSize)
        if(dy!=0):
            for i in range(0,crossPointsY+1):
                newY=yBegin+i*tileSize*ymultiplicator+eps*ymultiplicator
                newX=(dx*newY-lineEquationPoint)/dy + eps*xmultiplicator
                crossingy.append((newX,newY))
        result=[(math.floor(x1/tileSize),math.floor(y1/tileSize))]
        if (dx==0)and(dy!=0):
            for i in crossingy:
                result.append((math.floor(i[0]/tileSize),math.floor(i[1]/tileSize)))


        if (dx==0)and(dy==0):
                return result
        xiter=0
        yiter=0
        maxX=len(crossingx)
        maxY=len(crossingy)
        while(True):
            if(xiter==maxX):
                if(yiter==maxY):
                    return result

                else: 
                    memY=crossingy[yiter]
                    yiter+=1
                    new=(math.floor(memY[0]/tileSize),math.floor(memY[1]/tileSize))

            elif(yiter==maxY):
                if(xiter==maxX):
                    return result

                else: 
                    memX=crossingx[xiter]
                    xiter+=1
                    new=(math.floor(memX[0]/tileSize),math.floor(memX[1]/tileSize))
            else:

                memX=crossingx[xiter]
                memY=crossingy[yiter]
                if distance((x1,y1),memX)<distance((x1,y1),memY):
                    xiter+=1
                    new=(math.floor(memX[0]/tileSize),math.floor(memX[1]/tileSize))
                else:
                    yiter+=1
                    new=(math.floor(memY[0]/tileSize),math.floor(memY[1]/tileSize))





            if result[-1]!=new:
                result.append(new)

                   
            
        
    
    def update(self, player,dt,keys):
        tile_size=50
        x=int(player.x//1000)
        y=int(player.y//1000)
        if (x!=self.oldX)or(y!=self.oldY):
            print(x,y)
            self.oldX=x
            self.oldY=y
            for i in range(-1,2):
                for j in range(-1,2):
                    nCor=f"{x+i},{y+j}"
                    if nCor not in self.plan:
                        self.generateTile(x+i,y+j)
        tileX=math.floor(player.x / tile_size)
        tileY=math.floor(player.y / tile_size)
        self.lines=set()
        if (tileX!=self.oldTileX)or(tileY!=self.oldTileY):
            self.deathLines=set()
            self.oldTileX=tileX
            self.oldTileY=tileY
            for i in range(-5,6):
                for j in range(-5,6):
                    ncor=(tileX+i,tileY+j)
                    if self.boolTiles[ncor]:
                        self.generateDeathLines(ncor)
                        self.boolTiles[ncor]=False
                    self.deathLines. update(self.lineTiles[ncor])
        self.lines.update(self.deathLines)
        characterSet=set()
        for i in range(-5,6):
                for j in range(-5,6):
                    ncor=(tileX+i,tileY+j)
                    self.aliveLinesTiles[ncor]=[]
                    for k in self.charTiles[ncor]:
                        if isinstance(k, Square):
                            pass
                        else:
                            if k in characterSet:
                                continue
                            characterSet.add(k)
                            charLines=k.update(dt)
                            self.lines.update(charLines)
                            for k in charLines:
                                self.aliveLinesTiles[ncor].append(k)
        self.activeLinesList=[]
        player.update(dt,keys)
        for i in self.lines:
            nx=(i[0][0]+i[1][0])/2
            ny=(i[0][1]+i[1][1])/2
            if (((((player.x-nx)**2) +((player.y- ny)**2))**0.5 - (((i[0][0]-nx)**2) +((i[0][1]- ny)**2))**0.5)) <(player.vision*1.1):
                self.activeLinesList.append(i)
    def generateTile(self,x,y):
        number=random.randint(1,6)
        if number%2==0:
            self.plan[f"{x},{y}"]=1
        elif number==5:
            self.plan[f"{x},{y}"]=2
            tileGenerator.townGenerating(x,y,self)
        else:
            self.plan[f"{x},{y}"]=3
            tileGenerator.forestGenerating(x,y,self)

if __name__=="__main__":
    a=World()
    print(a.lineToTiles([0,0], [0,0]))
    print(a.lineToTiles([100,300], [500,100]))
            
