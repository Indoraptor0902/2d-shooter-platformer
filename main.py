import pygame
from settings import *
from player import *


class Game:
    def __init__(self):
        pygame.init()

        self.win = pygame.display.set_mode((WIDTH, HEIGHT))

        pygame.display.set_caption('Shooter Platformer')

        self.running = True

        self.clock = pygame.time.Clock()

    def run(self):
        while self.running:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.running = False
            
            pygame.display.flip()
        
        quit()

if __name__ == '__main__':
    game = Game()
    game.run()
