import pygame
from scripts.settings import *
from scripts.colors import *

pygame.init()

class Player:
    def __init__(self, game, pos):
        self.game = game
        self.pos = list(pos)
        self.unscaled_image = pygame.image.load('data/images/entities/player.png').convert()
        self.scale = 5
        self.image = pygame.transform.scale(self.unscaled_image, (self.unscaled_image.get_width() * self.scale, self.unscaled_image.get_height() * self.scale))
        self.image.set_colorkey(BLACK)
        self.velocity = [0, 0]
    
    def draw(self, win):
        win.blit(self.image, self.pos)