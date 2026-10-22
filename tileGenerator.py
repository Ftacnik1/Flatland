from Tree import Tree
from Building import Building
import random
from Shape import Shape

def forestGenerating(x,y,world):
    x=x*1000
    y=y*1000
    numOfTrunks=random.randint(80,120)
    controlList=[]
    for i in range(numOfTrunks):
        done=False
        counter=0
        while not done:
            counter+=1
            newX=random.randint(1,19)
            newY=random.randint(1,19)
            if f"{newX},{newY}" not in controlList:
                trunkX=x+newX*50+random.randint(-5,5)
                trunkY=y+newY*50+random.randint(-5,5)
                controlList.append(f"{newX},{newY}")
                Tree(trunkX,trunkY, world, random.randint(3,4), random.randint(5,10))
                done=True
    numOfPeople=random.randint(3,5)
    for i in range(numOfPeople):
        done =False
        while not done:
            newX=random.randint(1,19)
            newY=random.randint(1,19)
            if f"{newX},{newY}" not in controlList:
                guyX=x+newX*50+random.randint(-5,5)
                guyY=y+newY*50+random.randint(-5,5)
                controlList.append(f"{newX},{newY}")
                Shape(guyX,guyY, world, False)
                done=True

            


def townGenerating(x,y,world):
    x=x*1000
    y=y*1000
    numOfHouses=random.randint(10,15)
    controlList=[]
    for i in range(numOfHouses):
        done=False
        while not done:
            newX=random.randint(1,4)
            newY=random.randint(1,4)
            if f"{newX},{newY}" not in controlList:
                houseX=x+newX*200+random.randint(-5,5)
                houseY=y+newY*200+random.randint(-5,5)
                controlList.append(f"{newX},{newY}")
                Building(houseX,houseY, world, 5, random.randint(70,90))
                done=True
    for i in range(numOfHouses*2):
        done =False
        while not done:
            newX=random.randint(1,9)
            newY=random.randint(1,9)
            if f"{newX},{newY}" not in controlList:
                guyX=x+newX*50+random.randint(-5,5)
                guyY=y+newY*50+random.randint(-5,5)
                controlList.append(f"{newX},{newY}")
                Shape(guyX,guyY, world, False)
                done=True

    
