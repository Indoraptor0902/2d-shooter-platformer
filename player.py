import pygame
from settings import *

class Player:
    def __init__(self, game, pos):
        self.game = game
        self.pos = list(pos)
        self.image = None
        self.velocity = [0, 0]
    
    def draw(self):
        self.game.win.blit(self.image, (self.x, self.y))