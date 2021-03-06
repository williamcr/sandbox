import pygame
from pygame.locals import *
from pygame.time import *
import sys, os
pygame.init()

#makes sure that the game is runnning
running = True
clock = pygame.time.Clock()
 
#sets the size and title of the screen
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('GAME')

#sets the intiail velocity of the player
velX = 0
velY = 0
playerx = 5
playery = 5

background_image = 'white.jpg'
guy = '4row_red.png'
def main():
    global playerx, playery, velX, velY, background_image, guy
    while running:
        keys_down = pygame.key.get_pressed() #This shortens the if statements down below
        pygame.key.set_repeat(1, 50)
        time = 50/1000

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    raise SystemExit("You quit!")

        if keys_down[K_w]:
            velX = 0
            velY = -50
            
        elif keys_down[K_s]:           
            velX = 0
            velY = 50
            
        elif keys_down[K_a]:
            velX = -50
            velY = 0
            
        elif keys_down[K_d]:
            velX = 50
            velY = 0
            
        else:
            velX = 0
            velY = 0

        
        background = pygame.image.load(background_image).convert() 
        screen.blit(background, (0,0))

        playerx = playerx + velX
        playery = playery + velY
        player = pygame.sprite.Sprite()
        player.image = pygame.image.load(guy).convert_alpha()
        player.rect = player.image.get_rect()
        player.rect.move_ip(playerx,playery)
        screen.blit(player.image, player.rect.topleft)

        pygame.display.flip()
        clock.tick(50)
        

if __name__ == '__main__':
    main()
    
