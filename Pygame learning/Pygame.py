import pygame
import random

#pygame initialize all the components in the module
pygame.init()

#create screen
screen = pygame.display.set_mode((800,600))

#background
backimg = pygame.image.load('background.png')
background = pygame.transform.scale(backimg,(800,600))    

#title and icon
pygame.display.set_caption('Abyssal Advance')
icon = pygame.image.load('wizard.png')
pygame.display.set_icon(icon)

# Player
playerimg = pygame.image.load('main.png')
playerfinal = pygame.transform.scale(playerimg,(100,100))
playerx = 360
playerx_change = 0
playery = 480
playery_change = 0

# Enemies
enemyimg = pygame.image.load('enemy1.png')
enemyfinal = pygame.transform.scale(enemyimg,(80,80))
enemyx = random.randint(0,730)
enemyx_change = 0.3
enemyy = random.randint(50,150)
enemyy_change = 0.3

#blast
blastimg = pygame.image.load('blast.png')
blastx = random.randint(0,730)
enemyy = random.randint(50,150)
blastx = playerx
blasty = playery
enemyy_change = 0.3


def player(x,y):
    screen.blit(playerfinal, (x,y))

def enemy(x,y):
    screen.blit(enemyfinal, (x,y))

#To keep program running till closing it
ongoing = True
while ongoing:

    #Background color
    screen.fill((32,178,170))
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ongoing = False

        #for keyboard checking input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change -= 0.3
        
            if event.key == pygame.K_RIGHT:
                playerx_change += 0.3     

            if event.key == pygame.K_UP:
                playery_change -= 0.3

            if event.key == pygame.K_DOWN:
                playery_change += 0.3   

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playery_change = 0

    playerx += playerx_change
    playery += playery_change
    #blastx += blastx_change
    #blasty += blasty_change

    enemyx += enemyx_change
    #enemyy += enemyy_change

    #Boundaries player
    if playerx <= 0:
        playerx = 0
    elif playerx >= 700:
        playerx = 700

    if playery <= 0:
        playery = 0
    elif playery >= 500:
        playery = 500

    #Boundaries enemy
    if enemyx <= 0:
        enemyx_change = 0.3
    elif enemyx >= 736:
        enemyx_change = -0.3

    if enemyy <= 0:
        enemyy_change = 0.3
    elif enemyy >= 536:
        enemyy_change = -0.3 


    player(playerx,playery)
    enemy(enemyx,enemyy)

    #updating everything
    pygame.display.update()