import pygame
import neat
import time
import os
import random

# SET DIMENSION OF SCREEN

WIN_WIDTH = 600
WIN_HEIGHT = 800

# LOAD THE IMAGES:
# scale2x makes the image twice as big.

BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird1.png"))),
             pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird2.png"))),
             pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird3.png")))]
PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "pipe.png")))
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "base.png")))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))

# Generate one bird to test out:
# Create Bird class:

class Bird:
    IMGS = BIRD_IMGS
    MAX_ROTATION = 25 # HOW MUCH BIRD IS GOING TO TILT
    ROT_VEL = 20 # HOW MUCH WE ARE GOING TO ROTATE ON EACH FRAME
    ANIMATION_TIME = 5 # HOW LONG WE ARE SHOWING EACH BIRD ANIMATION

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0 # initialize at 0 because our bird will start flat
        self.tick_count = 0
        self.vel = 0 # velocity starts at 0 because it is not moving
        self.height = self.y
        self.img_count = 0 #shows which image is currenlty showing of bird
        self.img = self.IMGS[0] # going to reference the first image in BIRD_IMGS

    def jump(self):
        self.vel = -10.5 #bird velocity
        self.tick_count = 0 # keep count of when we last jump, we need to reset it to 0
        self.height = self.y

    def move(self):
        self.tick_count += 1 # a tick happend

        displacement = self.vel*self.tick_count + 1.5*self.tick_count**2

        if displacement >= 16:
            displacement = 16

        if displacement < 0:
            displacement -= 2

        self.y = self.y + displacement

        if d < 0 or self.y < self.height + 50:
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else:
            if self.tilt > -90:
                self.tilt -= self.ROT_VEL

    def draw(self, win):
        self.img_count += 1

        if self.img_count < self.ANIMATION_TIME:
            self.img = self.IMGS[0]
        elif self.img_count < self.ANIMATION_TIME*2:
            self.img = self.IMGS[1]
        elif self.img_count < self.ANIMATION_TIME*3:
            self.img = self.IMGS[2]
        elif self.img_count < self.ANIMATION_TIME*4:
            self.img = self.IMGS[1]
        elif self.img_count < self.ANIMATION_TIME*4 + 1:
            self.img = self.IMGS[0]
            self.img_count = 0

        if self.tilt <= -80:
            self.img = self.IMGS[1]
            self.img_count = self.ANIMATION_TIME*2

        rotated_image = pygame.transform.rotate(self.img, self.tilt)
        new_rectangle = rotated_image.get_rect(center = self.img.get_rect(topleft = (self.x, self.y)).center)
        win.blit(rotated_image, new_rectangle.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.img)

def draw_window(win, bird): # create windows where it will display
    win.blit(BG_IMG, (0, 0))
    bird.draw(win)
    pygame.display.update()

def main(): # run main loop of game
    bird = Bird(200, 200)
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window(win, bird)
    pygame.quit()
    quit()

main()

































































