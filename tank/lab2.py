import pygame
from enum import Enum
import random
from time import sleep

pygame.init()
screen_width=800
screen_height=600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('TANK vs TANK. By Zhagypar Tolkyn')

pygame.draw.rect(screen, (255,255,255), (0, 0, screen_width, 20))
clock=pygame.time.Clock()

pygame.mixer.music.load('disco.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.05)


shoot_sound=pygame.mixer.Sound('shoot1.wav')
turn_sound=pygame.mixer.Sound('turn.wav')
hit_sound=pygame.mixer.Sound('hit.wav')
class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class Tank:

    def  __init__(self, x, y, speed, color,direction, fire=pygame.K_RETURN, d_right=pygame.K_RIGHT, 
                    d_left=pygame.K_LEFT, d_up=pygame.K_UP, 
                    d_down=pygame.K_DOWN,to_left=pygame.image.load("pleft.png"),to_right=pygame.image.load("pright.png"),
                    to_up=pygame.image.load("pup.png"),to_down=pygame.image.load("pdown.png")):
        self.x = x
        self.y = y
        self.speed = speed
        self.color = color
        self.width = 50
        self.height = 52
        self.direction = Direction
        self.to_left = to_left
        self.to_right = to_right
        self.to_up = to_up
        self.to_down = to_down
        self.score=3
        self.fire=fire

        self.KEY = {d_right: Direction.RIGHT, d_left: Direction.LEFT,
                    d_up: Direction.UP, d_down: Direction.DOWN}

    def draw(self): # changing pictures according to tanks direction

        if self.direction == Direction.RIGHT:
            screen.blit(self.to_right,(self.x,self.y))
        elif self.direction == Direction.LEFT:
            screen.blit(self.to_left,(self.x,self.y))
        elif self.direction == Direction.UP:
            screen.blit(self.to_up,(self.x,self.y))
        elif self.direction == Direction.DOWN:
            screen.blit(self.to_down,(self.x,self.y))
        else:
            screen.blit(self.to_up,(self.x,self.y))   

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

        if self.x < 0-self.width:               #infinite field
            self.x=800
        if self.x>800:
            self.x=0-self.width
        if self.y<0-self.height:
            self.y=600
        if self.y>600:
            self.y=0-self.height            
    
class Snaryad:

    def __init__(self, x=0, y=0, color=(255,255,255), direction=Direction.UP):
        self.x=x
        self.y=y
        self.color=color
        self.radius=7
        self.speed=25
        self.screen=screen
        self.direction=direction
        self.ready=True             

    def bullet_move(self): # if tank changes direction, it also will be changed for bullet
        
        if self.direction==Direction.RIGHT:
            self.x+=self.speed
        if self.direction==Direction.LEFT:
            self.x-=self.speed
        if self.direction==Direction.UP:
            self.y-=self.speed
        if self.direction==Direction.DOWN:
            self.y+=self.speed 


        if self.ready:
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius) # bullet form    

def bullet_position(tank): # giving the bullet approximately position of tank
    if tank.direction==Direction.RIGHT:
        x=tank.x+tank.width
        y=tank.y+int(tank.width/2)
    elif tank.direction==Direction.LEFT:
        x=tank.x-tank.width
        y=tank.y+int(tank.width/2)
    elif tank.direction==Direction.UP:
        x=tank.x+int(tank.height/2)
        y=tank.y-tank.height
    elif tank.direction==Direction.DOWN:
        x=tank.x+int(tank.width/2)
        y=tank.y+tank.height

    bullet=Snaryad(x,y,tank.color, tank.direction)
    snaryads.append(bullet)

def hit():
    for snaryad in snaryads:
        for tank in tanks:
            if snaryad.x>tank.x and snaryad.x < tank.x+tank.width:
                if snaryad.y > tank.y and snaryad.y < tank.y+tank.width:
                    snaryad.ready=False
                    tank.score-= 0.5
                    
                    hit_sound.play()
                    

    
def lives():
    health1=int(tank1.score)
    health2=int(tank2.score)
    font1 = pygame.font.SysFont("Arial", 20)
    text1 = font1.render("TANK 1 LIVES {}".format(health1), 1, (255, 255, 255))        
    place1 = [10, 10]
    font2 = pygame.font.SysFont("Arial", 20)
    text2 = font2.render('TANK 2 LIVES {}'.format(health2), 1, (255, 255, 255))
    place2 = [665, 10]
    screen.blit(text1, place1)
    screen.blit(text2, place2)

def game():
    for tank in tanks:
        if tank.score<=0:
            game_over=pygame.image.load('over.jpg')
                       
            screen.blit(game_over, (0,0)) 
    pygame.display.flip()        
mainloop = True

eleft = pygame.image.load("eleft.png")
eright = pygame.image.load("eright.png")
eup = pygame.image.load("eup.png")
edown = pygame.image.load("edown.png")


tank1 = Tank(random.randint(50, 400), random.randint(100, 500), 3, (0, 0, 255),Direction.UP,pygame.K_RETURN,pygame.K_RIGHT,pygame.K_LEFT,pygame.K_UP,pygame.K_DOWN)
tank2 = Tank(random.randint(450, 750), random.randint(100, 500), 3, (255, 0, 0),Direction.DOWN, pygame.K_SPACE, pygame.K_d, pygame.K_a, pygame.K_w, pygame.K_s,eleft,eright,eup,edown)
tanks = [tank1, tank2]

snaryad1=Snaryad()      # using class we give bullet tank's color, position and its direction 
snaryad2=Snaryad()
snaryads = [snaryad1, snaryad2]

while mainloop:
    clock.tick(40)
    background=pygame.image.load('background.jpg')
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainloop = False
            
            key = pygame.key.get_pressed()
            for tank in tanks:

                if event.key in tank.KEY.keys():
                    tank.change_direction(tank.KEY[event.key])   #turn sound when tank changes direction
                    turn_sound.play()

                if event.key in tank.KEY.keys():
                    tank.move() 
                
                if key[tank.fire]:
                    shoot_sound.play()
                    bullet_position(tank)

    screen.fill((136,178, 176))

    hit()
    
    for z in snaryads:
        z.bullet_move()
    for tank in tanks:
        tank.draw()
        tank.move()
        
    lives()
    game()

    pygame.display.flip()  

pygame.quit()