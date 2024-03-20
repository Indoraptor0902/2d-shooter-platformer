import pygame
from scripts.settings import *
from scripts.colors import *
from scripts.utils import load_image

pygame.init()

class Player:
    def __init__(self, game, pos):
        self.game = game
        self.pos = list(pos)
        
        self.image = load_image('entities/player.png')
        self.image.set_colorkey(BLACK)

        self.movement = [0, False]
        self.velocity = [0, 0]
        self.speed = 5
    
    def handle_movement(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.movement[0] += -1
            if event.key == pygame.K_RIGHT:
                self.movement[0] += 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.movement[0] -= -1
            if event.key == pygame.K_RIGHT:
                self.movement[0] -= 1
    
    def update(self):
        self.velocity[0] = self.movement[0] * self.speed
        self.velocity[1] = min(5, self.velocity[1] + 0.1)

        self.pos[0] += self.velocity[0]
        self.pos[1] += self.velocity[1]
    
    def draw(self, win):
        win.blit(self.image, self.pos)