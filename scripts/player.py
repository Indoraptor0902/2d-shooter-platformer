import pygame
from scripts.settings import *
from scripts.colors import *
from scripts.utils import load_image

pygame.init()

class Player:
    def __init__(self, game, pos):
        self.game = game
        self.pos = list(pos)
        
        self.unscaled_image = load_image('entities/player.png')
        self.scale = 5
        self.image = pygame.transform.scale(self.unscaled_image, (self.unscaled_image.get_width() * self.scale, self.unscaled_image.get_height() * self.scale))
        self.image.set_colorkey(BLACK)

        self.movement = [0, False]
        self.velocity = [0, 0]
        self.speed = 5
    
    def handle_movement(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.movement[0] = -1
            if event.key == pygame.K_RIGHT:
                self.movement[1] = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.movement[0] -= -1
            if event.key == pygame.K_RIGHT:
                self.movement[1] -= 1
    
    def update(self):
        self.velocity = [self.movement[0] * self.speed + self.movement[1] * self.speed, 0]

        self.pos[0] += self.velocity[0]
        self.pos[1] += self.velocity[1]
    
    def draw(self, win):
        win.blit(self.image, self.pos)