import pygame
from scripts.utils import load_images
from scripts.settings import *

NEIGHBOR_OFFSETS = [(0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 0)]

class Tilemap:
    def __init__(self, game, tile_size=16*IMG_SCALE):
        self.game = game
        self.tile_size = tile_size
        self.tilemap = {}
        self.offgrid_tiles = []

        self.sprites = {
            'decor': load_images('tiles/decor'),
            'grass': load_images('tiles/grass'),
            'large_decor': load_images('tiles/large_decor'),
            'stone': load_images('tiles/stone')
        }

        for i in range(10):
            self.tilemap[str(3 + i) + ';5'] = {'type': 'grass', 'variant': 1, 'pos': (3 + i, 5)}
            self.tilemap['10;' + str(5 + i)] = {'type': 'stone', 'variant': 1, 'pos': (10, 5 + i)}
    
    def draw(self, win):
        for loc in self.tilemap:
            tile = self.tilemap[loc]
            win.blit(self.sprites[tile['type']][tile['variant']], (tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size))
        
        for tile in self.offgrid_tiles:
            win.blit(self.sprites[tile['type']][tile['variant']], tile['pos'])
    
