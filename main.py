import pygame
from scripts.settings import *
from scripts.colors import *
from scripts.player import Player
from scripts.tilemap import Tilemap


class Game:
    def __init__(self):
        pygame.init()

        self.win = pygame.display.set_mode((WIDTH, HEIGHT))

        pygame.display.set_caption('Shooter Platformer')

        self.running = True

        self.clock = pygame.time.Clock()

        self.player = Player(self, (50, 50))

        self.tilemap = Tilemap(self, tile_size=20)

    def run(self):
        while self.running:
            self.clock.tick(FPS)

            self.win.fill(WHITE)

            self.tilemap.draw(self.win)

            self.player.update()

            self.player.draw(self.win)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                self.player.handle_movement(event) 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.running = False
            
            pygame.display.flip()
        
        quit()

if __name__ == '__main__':
    game = Game()
    game.run()
