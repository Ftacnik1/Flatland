from Entity import Entity
import math
import random
class Shape(Entity):
    def __init__(self, x, y,world,home,size=None, speed=None):
        hierarchie=random.randint(1,10)
        if hierarchie<5:
            points=3
        elif hierarchie<8:
            points=4
        elif hierarchie<10:
            points=random.randint(5,8)
        else:
            points=random.randint(10,20)
        self.size=size
        if size==None:
            self.size=random.randint(5,30)
        super().__init__(x, y,world,True,points,self.size)
        self.speed=speed
        if self.speed==None:
            self.speed=random.randint(50,150)
        self.angle = 0
        self.home=home
        self.update(0)

    def update(self, dt):
        tile_size=50
        number=random.randint(1,5)
        if number==1:
            self.angle -= 1 * dt
        if number==5:
            self.angle += 1 * dt
        self.x+= math.cos(self.angle)*self.speed*dt
        self.y+= math.sin(self.angle)*self.speed*dt
        lines=self.segments()
        ntile=(math.floor(self.x / tile_size), math.floor(self.y / tile_size))
        if self.tile!=ntile:
            self.world.charTiles[self.tile].remove(self)
            self.tile=ntile
            self.world.charTiles[self.tile].append(self)
        return(lines)
