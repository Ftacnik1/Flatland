import math
from Entity import Entity
class Tree(Entity):
    def __init__(self, x, y, world, points=4, radius=30):
        super().__init__( x, y, world,False, points, radius,-math.pi/2)
    
    def draw_topdown(self, surface):
        rect = pygame.Rect(self.x-self.size/2, self.y-self.size/2, self.size, self.size)
        pygame.draw.rect(surface, (150, 150, 150), rect)
