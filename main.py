import pygame
import math
from Square import Square
from World import World
from Building import Building
from Tree import Tree
def draw_player(screen, angle, x=200, y=200, size=15, color=(0,200,0)):
    dx=math.cos(angle)
    dy=math.sin(angle)

    tip=(x+dx*size, y+dy*size)

    left=(x+math.cos(angle+math.pi/2)*size*0.5, y+math.sin(angle+math.pi/2)*size*0.5)
    right=(x+math.cos(angle-math.pi/2)*size*0.5, y+math.sin(angle-math.pi/2)*size*0.5)

    pygame.draw.polygon(screen,color,[tip, left, right])
    
def intersect_ray_segment(px, py, dx, dy, x1, y1, x2, y2):
    sx=x2-x1
    sy=y2-y1       
    inter=dx*(-sy)-dy*(-sx)
    if abs(inter) < (1/(10**9)):
        return None

    difx=x1-px
    dify=y1-py
    t=(difx*(-sy)-dify*(-sx))/inter
    u = (dx*dify-dy*difx)/inter

    if (t>=0) and (0<=u<=1):
        return t
    return None


def flat_view(surface, player, world):
    width, height = surface.get_size()
    observe= math.radians(70)
    start= player.angle-observe/2
    num_of_rays= 200

    col_width= width/num_of_rays

    for i in range(num_of_rays):
        tested_lines=set()
        ang= start+observe*(i/(num_of_rays-1))

        dx, dy = math.cos(ang), math.sin(ang)
        end_x= player.x+dx*player.vision
        end_y= player.y+dy*player.vision
        path=world.lineToTiles((player.x,player.y),(end_x,end_y))
        best_dist=player.vision
        for j in path:
            line_list=world.lineTiles[j];
            for (p1,p2) in line_list:
                if((p1,p2) in tested_lines):
                    continue
                tested_lines.add((p1,p2))
                t = intersect_ray_segment(player.x, player.y, dx, dy, p1[0], p1[1], p2[0], p2[1])
                if t is not None:
                    if best_dist> t:
                        best_dist=t

            line_list=world.aliveLinesTiles[j];
            for (p1,p2) in line_list:
                if((p1,p2) in tested_lines):
                    continue
                tested_lines.add((p1,p2))

                t = intersect_ray_segment(player.x, player.y, dx, dy, p1[0], p1[1], p2[0], p2[1])
                if t is not None:
                    if best_dist> t:
                        best_dist=t
            if best_dist<player.vision:
                break
        shade= min(255, int(best_dist * (255/player.vision)))
        color= (shade, shade, shade)

        x1= int(i*col_width)
        x2= int((i+1)*col_width)

        pygame.draw.rect(surface, color, (x1, 0, x2 - x1, height))
            
            
        

    
    
def main():
    pygame.init()
    clock = pygame.time.Clock()
    width=1000
    height=400
    screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF | pygame.HWSURFACE)

    topdown = screen.subsurface(pygame.Rect(0, 0, 400, 400))
    flatview = screen.subsurface(pygame.Rect(400, 0, 600, 400))

    
    world=World()
    player = Square(0, 0,world,True)
    Building(0,0,world)
    
    
    running = True
    while running:
        dt = clock.tick(60) / 1000
        keys = pygame.key.get_pressed()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        world.update(player,dt,keys)
        
        topdown.fill((255, 255, 255))

        for (p1, p2) in world.activeLinesList:
            p1=[p1[0]-player.x+200,p1[1]-player.y+200]
            p2=[p2[0]-player.x+200,p2[1]-player.y+200]
            pygame.draw.line(topdown, (0, 0, 0), p1, p2, 2)
    
        draw_player(topdown, player.angle)
    
        

        
        flat_view(flatview, player, world)
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()
