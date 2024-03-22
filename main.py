import pygame
from scripts.settings import *
from scripts.utils import load_image
from scripts.colors import *
from scripts.player import Player
from scripts.tilemap import Tilemap


class Game:
    def __init__(self):
        pygame.init()

        self.win = pygame.display.set_mode((WIDTH, HEIGHT))

        pygame.display.set_caption('Shooter Platformer')

        self.assets = {
            'background': load_image('background.png')
        }

        self.running = True

        self.clock = pygame.time.Clock()

        self.player = Player(self, (200, 50))

        self.tilemap = Tilemap(self)
        
        self.scroll = [0, 0]

    def run(self):
        while self.running:
            self.clock.tick(FPS)

            self.win.blit(self.assets['background'], (0, 0))

            self.scroll[0] += (self.player.rect().centerx - WIDTH / 2 - self.scroll[0]) / 30
            self.scroll[1] += (self.player.rect().centery - HEIGHT / 2 - self.scroll[1]) / 30
            render_scroll = (int(self.scroll[0]), int(self.scroll[1]))

            self.tilemap.draw(self.win, offset=render_scroll)

            self.player.update(self.tilemap)

            self.player.draw(self.win, offset=render_scroll)

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
