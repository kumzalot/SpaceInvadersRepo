import pygame as py
import os
import random


#INITIAIZING
py.init()

#CREATING THE SCREEN
screen = py.display.set_mode((800,600))

running = True

#TITLE AND ICON
py.display.set_caption("SPACE INVADERS")

new_dir = 'C:\Projects\SpaceInvader\SI_IMAGES'
os.chdir(new_dir)

icon = py.image.load("spaceship.png")
py.display.set_icon(icon)

#BACKGROUND 
bg = py.image.load("background.png")


#PLAYER
playerImg = py.image.load("user1.png")
playerX = 370; playerY = 480
pXchange = 0

def player(x,y):
    screen.blit(playerImg,(x,y))

#ENEMY
enemy1Img = py.image.load("enemy1.png"); enemy2Img = py.image.load("enemy2.png")

eX = random.randint(70,730); eY = random.randint(50,150)
eXchange = 3; eYchange = 30

def enemy(img,x,y):
    screen.blit(img,(x,y))

#BULLET
bullet = py.image.load("bullet.png")
bX = 0
bY = 480
bYchange = 5
bState = "ready"

def fire_bullet(x,y):
    global bState
    bState = "fire"
    screen.blit(bullet,(x+16,y+10))

#GAMELOOP
while running:

    screen.fill((0,0,0)) # R,G,B # Navy=0,0,128

    #BG IMAGE
    screen.blit(bg,(0,0))

    for event in py.event.get():

        #CHECKING FOR QUIT
        if event.type == py.QUIT:
            running = False

        #PLAYER MOVEMENT DETECTION
        if event.type == py.KEYDOWN:

            if event.key == py.K_a or event.key == py.K_LEFT:
                pXchange = -3.5

            elif event.key == py.K_d or event.key == py.K_RIGHT:
                pXchange = 3.5

            #BULLET DETECTION
            if event.key == py.K_SPACE or event.key == py.K_KP_ENTER:
                if bState is "ready":
                    bX = playerX
                    fire_bullet(bX,bY)
                

        if event.type == py.KEYUP:

            if event.key == py.K_a or event.key == py.K_d:
                pXchange = 0
            elif event.key == py.K_LEFT or event.key == py.K_RIGHT:
                pXchange = 0
            
        

    #CHECKING FOR PLAYER BOUNDARIES
    playerX += pXchange

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    #ENEMY MOVEMENT
    eX += eXchange

    if eX <= 0:
        eXchange = 2.5
        eY += eYchange

    elif eX >= 736:
        eXchange = -2.5
        eY += eYchange

    #BULLET MOVEMENT
    if bY <= 0:
        bY = 480; bState = "ready"

    if bState is "fire":
        fire_bullet(bX,bY)
        bY -= bYchange
        

    
    player(playerX,playerY)

    enemy(enemy1Img,eX,eY)
    

    py.display.update()



py.quit()