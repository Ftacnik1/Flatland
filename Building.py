import math
from Entity import Entity
class Building(Entity):
    def __init__(self, x, y, world, points=5, radius=80):
        super().__init__( x, y, world,False, points, radius,-math.pi/2,True)
        self.update()
    
    def update(self):
        lines=self.segments()
        for index,i in enumerate(lines):
            if index!=3:
                self.world.deathLine(i[0],i[1])
        
