import math

class Entity:
    def __init__(self, x, y,world,alive=False, points=0,radius=None,offset=0,strangeShape=False):
        self.x = x
        self.y = y
        tile_size=50
        self.tile=(math.floor(x / tile_size), math.floor(y / tile_size))
        self.points=points
        self.radius=radius
        self.angle=0
        self.world=world
        self.alive=alive
        self.offset=offset
        self._segments = self.segments()
        self.numOfSegments=len(self._segments)
        world.registration(self,self.tile)
            
    
    def update(self):
        for i in self._segments:
            self.world.deathLine(i[0],i[1])
            
            
        
        
        
            

    def segments(self):
        return(self.regular_polygon_segments())

    def regular_polygon_segments(self):
        originalAngle=self.angle
        x=self.x
        y=self.y
        r=self.radius
        n=self.points
        points = []
        for i in range(n):
            angle = (2 * math.pi * i / n) + originalAngle + self.offset
            px= x+r*math.cos(angle)
            py= y+r*math.sin(angle)
            points.append((px, py))
            
        segments = []
        for i in range(n):
            p1 = points[i]
            p2 = points[(i+1) % n]
            segments.append((p1, p2))
    
        return segments

    def draw_topdown(self, surface):
        raise NotImplementedError
    
    def sense(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        dist = math.hypot(dx, dy)
        angle = math.atan2(dy, dx)
        return dist, angle
