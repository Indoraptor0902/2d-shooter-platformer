import pygame
from scripts.utils import load_images
from scripts.settings import *

NEIGHBOR_OFFSETS = [(0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 0)]
PHYSICS_TILES = {'grass', 'stone'}

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
            self.tilemap['10;' + str(1 + i)] = {'type': 'stone', 'variant': 1, 'pos': (10, 1 + i)}
    
    def tiles_around(self, pos):
        tiles = []
        tile_loc = (int(pos[0] // self.tile_size), int(pos[1] // self.tile_size))
        for offset in NEIGHBOR_OFFSETS:
            check_loc = str(tile_loc[0] + offset[0]) + ';' + str(tile_loc[1] + offset[1])
            if check_loc in self.tilemap:
                tiles.append(self.tilemap[check_loc])
        return tiles
    
    def physics_rects_around(self, pos):
        rects = []
        for tile in self.tiles_around(pos):
            if tile['type'] in PHYSICS_TILES:
                rects.append(pygame.Rect(tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size, self.tile_size, self.tile_size))
        return rects
    
    def draw(self, win, offset=(0, 0)):
        for loc in self.tilemap:
            tile = self.tilemap[loc]
            win.blit(self.sprites[tile['type']][tile['variant']], (tile['pos'][0] * self.tile_size - offset[0], tile['pos'][1] * self.tile_size - offset[1]))
        
        for tile in self.offgrid_tiles:
            win.blit(self.sprites[tile['type']][tile['variant']], tile['pos'])
    
