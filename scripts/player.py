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
        self.size = [self.image.get_width(), self.image.get_height()]

        self.movement = [0, False]
        self.velocity = [0, 0]
        self.speed = 5

        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}
    
    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
    
    def handle_movement(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.movement[0] += -1
            if event.key == pygame.K_RIGHT:
                self.movement[0] += 1
            if event.key == pygame.K_UP:
                self.velocity[1] = -8
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.movement[0] -= -1
            if event.key == pygame.K_RIGHT:
                self.movement[0] -= 1
    
    def update(self, tilemap):
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}

        self.velocity[0] = self.movement[0] * self.speed
        self.velocity[1] = min(10, self.velocity[1] + 0.3)

        self.pos[0] += self.velocity[0]
        entity_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if self.velocity[0] > 0:
                    entity_rect.right = rect.left
                    self.collisions['right'] = True
                if self.velocity[0] < 0:
                    entity_rect.left = rect.right
                    self.collisions['left'] = True
                self.pos[0] = entity_rect.x

        self.pos[1] += self.velocity[1]
        entity_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if self.velocity[1] > 0:
                    entity_rect.bottom = rect.top
                    self.collisions['down'] = True
                if self.velocity[1] < 0:
                    entity_rect.top = rect.bottom
                    self.collisions['up'] = True
                self.pos[1] = entity_rect.y
        
        if self.collisions['down'] or self.collisions['up']:
            self.velocity[1] = 0
    
    def draw(self, win, offset=(0, 0)):
        win.blit(self.image, (self.pos[0] - offset[0], self.pos[1] - offset[1]))