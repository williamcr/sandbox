import pygame
from pygame.locals import *
from pygame.time import *
import sys, os
pygame.init()

#makes sure that the game is runnning
running = True
clock = pygame.time.Clock()
 
#sets the size and title of the screen
screen = pygame.display.set_mode((655,470))
pygame.display.set_caption('GAME')

#sets the intiail velocity of the player
velX = 0
velY = 0
playerx = 5
playery = 5


npcvelx = 0
npcvely = 0
npcx = 1
npcy = 1
    
def draw():

    global playerx, playery, velX, velY, npcvelx, npcvely, npcx, npcy
    
    
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255,255,254))
    screen.blit(background, (0,0))

    playerx = playerx + velX
    playery = playery + velY
    player_filename = '4row_red.png'
    player = pygame.image.load(player_filename)

    npcx = npcx + npcvelx
    npcy = npcy + npcvely
    npc_filename = 'cat.png'
    npc = pygame.image.load(npc_filename)

    screen.blit(npc, (npcx, npcy))
    screen.blit(player, (playerx,playery))
    

    pygame.display.flip()


def main():
    global velX, velY, running
    
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
                    

#The player moves using WASD. W moves the player up, S down, A left, and
#right. If the player lets go of any of these keys, the player's movement speed
# is set to 0.

        if keys_down[K_w]:
            velX = 0
            velY = -5
            
        elif keys_down[K_s]:           
            velX = 0
            velY = 5
            
        elif keys_down[K_a]:
            velX = -5
            velY = 0
            
        elif keys_down[K_d]:
            velX = 5
            velY = 0
            
        else:
            velX = 0
            velY = 0


        
        
        clock.tick(50)
        draw()

if __name__ == '__main__':
    main()


'''
elif keys_down[K_w] and keys_down[K_d]:
            velX = 5
            velY = -5
        elif keys_down[K_w] and keys_down[K_a]:
            velX = -5
            velY = -5
        elif keys_down[K_s] and keys_down[K_d]:
            velX = 5
            velY = 5
        elif keys_down[K_w] and keys_down[K_a]:
            velX = -5
            velY = -5
            
'''
