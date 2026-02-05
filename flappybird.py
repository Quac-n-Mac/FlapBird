import pygame, random
from pygame.locals import *
screen = pygame.display.set_mode((850,750))
playing = True

brd1 = pygame.image.load("images/brd1.png")
brd2 = pygame.image.load("images/brd2.png")
brd3 = pygame.image.load("images/brd3.png")

flying = False
game_over = False
ground_scroll = 0
scroll_speed = 4
pipe_gap = 151
pipe_frequency = 1500
last_pipe = pygame.time.get_ticks() - pipe_frequency
score = 0
pass_pipe = False

bg = pygame.image.load("images/flapground.png")
bg = pygame.transform.scale(bg,(850,750))

floor = pygame.image.load("images/ground.png")

fx = 0

class Bird(pygame.sprite.Sprite):
    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images = [brd1,brd2,brd3]
        self.index = 0
        self.counter = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.velocity = 0
        self.clicked = False
    def update(self):
        if flying == True:
            self.velocity += 0.5
            if self.rect.bottom < 625:
                self.rect.y += int(self.velocity)
        if game_over==False:
            if pygame.mouse.get_pressed()[0]==1 and self.clicked == False:
                self.clicked = True
                self.velocity = -12
            if pygame.mouse.get_pressed()[0]==0:
                self.clicked=False
            flap_cooldown = 5
            self.counter+=1
            if self.counter>flap_cooldown:
                self.counter=0
                self.index+=1
                if self.index>=3:
                    self.index=0
                self.image = self.images[self.index]
            self.image = pygame.transform.rotate(self.images[self.index], self.velocity*-2)
        else:
            self.image = pygame.transform.rotate(self.images[self.index], -90)

bx = 130

bird = Bird(bx, 400)


sprites = pygame.sprite.Group()
sprites.add(bird)

clock = pygame.time.Clock()

while playing:
    clock .tick(60)
    fx -= 4
    if fx <=-30:
        fx = 0
    if bird.rect.y >= 625:
        bx -= 4
        game_over=True
        flying=False
    screen.blit(bg, (0,0))
    screen.blit(floor, (fx,625))
    sprites.draw(screen)
    sprites.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            playing = False
        if event.type==pygame.MOUSEBUTTONDOWN and flying==False and game_over==False:
            flying=True
    pygame.display.update()
