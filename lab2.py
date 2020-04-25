import pygame
from enum import Enum
import random

pygame.init()
screen_width=800
screen_height=600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.draw.rect(screen, (255,255,255), (0, 0, screen_width, 20))
clock=pygame.time.Clock()

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class Tank:

    def __init__(self, x, y, speed, color, d_right=pygame.K_RIGHT, d_left=pygame.K_LEFT, d_up=pygame.K_UP, d_down=pygame.K_DOWN):
        self.x = x
        self.y = y
        self.dx=30
        self.dy=30
        self.speed = speed
        self.color = color
        self.width = 40
        self.direction = Direction

        self.KEY = {d_right: Direction.RIGHT, d_left: Direction.LEFT,
                    d_up: Direction.UP, d_down: Direction.DOWN}

    def draw(self):
        tank_c = (self.x + int(self.width / 2), self.y + int(self.width / 2))
        pygame.draw.rect(screen, self.color,
                         (self.x, self.y, self.width, self.width), 4)
        pygame.draw.circle(screen, self.color, tank_c, int(self.width / 2))

        if self.direction == Direction.RIGHT:
            pygame.draw.line(screen, self.color, tank_c, (self.x + self.width + int(self.width / 2), self.y + int(self.width / 2)), 4)

        if self.direction == Direction.LEFT:
            pygame.draw.line(screen, self.color, tank_c, (
            self.x - int(self.width / 2), self.y + int(self.width / 2)), 4)

        if self.direction == Direction.UP:
            pygame.draw.line(screen, self.color, tank_c, (self.x + int(self.width / 2), self.y - int(self.width / 2)), 4)

        if self.direction == Direction.DOWN:
            pygame.draw.line(screen, self.color, tank_c, (self.x + int(self.width / 2), self.y + self.width + int(self.width / 2)), 4)


    def change_direction(self, direction):
        self.direction = direction
    

    def move(self):                 #key pressed on keyboard movement
        if self.direction == Direction.LEFT:
            self.x -= self.speed
        if self.direction == Direction.RIGHT:
            self.x += self.speed
        if self.direction == Direction.UP:
            self.y -= self.speed
        if self.direction == Direction.DOWN:
            self.y += self.speed
        self.draw()


        if self.x < 0:               #infinite field
            self.x+=screen_width
        if self.x>screen_width:
            self.x-=screen_width
        if self.y<0:
            self.y+=screen_height
        if self.y>screen_height:
            self.y-=screen_height            
    
class Snaryad:
    def __init__(self, x, y, radius, color):
        self.x=x
        self.y=y
        self.color=color
        self.radius=radius
        self.speed=10
        self.score=3
        self.screen=screen
        
    def lives(self):
        font1 = pygame.font.SysFont("Arial", 18)
        text1 = font1.render("TANK 1 LIVES {}".format(self.score), 1, (255, 255, 255))
        place1 = [10, 10]
        font2 = pygame.font.SysFont("Arial", 18)
        text2 = font2.render('TANK 2 LIVES {}'.format(self.score), 1, (255, 255, 255))
        place2 = [650, 10]
        self.screen.blit(text1, place1)
        self.screen.blit(text2, place2)
        pygame.display.flip()

    def draw_bullet(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        self.lives()
        pygame.display.flip()
 
        

mainloop = True

tank1 = Tank(random.randint(100, 700), random.randint(100, 500), 2, (80, 250, 5))
tank2 = Tank(random.randint(100, 700), random.randint(100, 500), 2, (255, 113, 85), pygame.K_d, pygame.K_a, pygame.K_w, pygame.K_s)
tanks = [tank1, tank2]

snaryad1=Snaryad(300, 400, 9, (255,0,0))
snaryad2=Snaryad(400, 300, 9, (0, 255,0))
snaryads = [snaryad1, snaryad2]

while mainloop:
    clock.tick(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainloop = False
            
            for tank in tanks:
                if event.key in tank.KEY.keys():
                    tank.change_direction(tank.KEY[event.key])
                    
            if pygame.key==pygame.K_SPACE:
                snaryad1.x==tank1.x
                snaryad1.y==tank1.y
                if tank1.direction==Direction.RIGHT:
                    snaryad1.x+=snaryad1.speed


    screen.fill((0, 0, 0))

    for tank in tanks:
        tank.move()
    
    for snaryad in snaryads:
        snaryad.draw_bullet()
    pygame.display.flip()    

pygame.quit()