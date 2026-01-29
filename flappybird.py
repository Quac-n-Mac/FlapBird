import pygame, random
from pygame.locals import *
screen = pygame.display.set_mode((850,750))
playing = True

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

class Bird(pygame.sprite.Sprite):
    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images = ["images/brd1.png", "images/brd2.png", "images/brd3.png"]
        self.index = 0
        self.counter = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.velocity = 0
        self.clicked = False
    def update(self):
        pass
bird = Bird(425, 340)


sprites = pygame.sprite.Group()
sprites.add(bird)

clock = pygame.time.Clock()

while playing:
    clock .tick(60)
    screen.blit(bg, (0,0))
    sprites.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            playing = False
    pygame.display.update()