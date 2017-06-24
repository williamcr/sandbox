import pygame
from pygame.locals import *
from pygame.time import *
import sys
pygame.init()

velX = 0
velY = 0


running = True
clock = pygame.time.Clock()
 
global playerx 
global playery

screen = pygame.display.set_mode((700,300))
pygame.display.set_caption('something')



def draw():
    global velX
    global velY
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255,255,255))
    screen.blit(background, (0,0))

    playerx = playerx + velX
    playery = playery + velY
    player_filename = 'player.png'
    player = pygame.image.load(player_filename)
    screen.blit(player, (playerx,playery))

    pygame.display.flip()

def main():
    global velX
    global velY
    global running

    while running:

        keys_down = pygame.key.get_pressed()
        pygame.key.set_repeat(1, 50)
        time = 50/1000

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running=False

        if keys_down[K_d]:
            velX = 10
        if keys_down[K_w]:
            velY = -10
        if keys_down[K_s]:
            velY = 10
        if keys_down[K_a]:
            velX = -10

        clock.tick(50)
        draw()

if __name__ == '__main__':
    main()