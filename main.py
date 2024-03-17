import pygame
import random

pygame.init()

FPS = 60

WIDTH, HEIGHT = 1000, 800

win = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Shooter Platformer')

def main():
    run = True

    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False
        
        pygame.display.flip()
    
    quit()

if __name__ == '__main__':
    main()