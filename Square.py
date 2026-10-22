from Entity import Entity
import math
import pygame
class Square(Entity):
    def __init__(self, x, y,world, size=20, speed=100):
        super().__init__(x, y,world,True)
        self.size = size
        self.speed = speed
        self.angle = 0
        self.vision=200
    
    def update(self, dt, keys):
        if keys[pygame.K_w]:
            self.x+= math.cos(self.angle)*self.speed*dt
            self.y+= math.sin(self.angle)*self.speed*dt
        if keys[pygame.K_s]:
            self.x-= math.cos(self.angle)*self.speed*dt
            self.y-= math.sin(self.angle)*self.speed*dt
        if keys[pygame.K_a]:
            self.angle-= 1*dt
        if keys[pygame.K_d]:
            self.angle+= 1*dt
        return(None)
    
