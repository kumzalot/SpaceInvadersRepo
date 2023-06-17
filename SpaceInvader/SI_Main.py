import pygame as py
from pygame import mixer

import os
import random


#INITIAIZING
py.init()

#CREATING THE SCREEN
screen = py.display.set_mode((800,600))

running = True

#TITLE AND ICON
py.display.set_caption("SPACE INVADERS")

new_dir = 'C:\Projects\SpaceInvader\SI_IMAGESandAUDIO'
os.chdir(new_dir)

icon = py.image.load("spaceship.png")
py.display.set_icon(icon)

#BACKGROUND 
bg = py.image.load("background.png")

#SOUND
mixer.music.load("background.wav")
mixer.music.play(-1)

#PLAYER
playerImg = py.image.load("user1.png")
playerX = 370; playerY = 480
pXchange = 0

def player(x,y):
    screen.blit(playerImg,(x,y))

#ENEMY
enemyImgs = []
eX = []
eY = []
eXchange = []
eYchange = []

numOfEnemies = 6

for i in range(numOfEnemies):
    enemyImgs.append(py.image.load("enemy1.png"))
    eX.append(random.randint(40,730)); eY.append(random.randint(50,150))
    eXchange.append(3); eYchange.append(30)


def enemy(i,x,y):
    screen.blit(enemyImgs[i],(x,y))

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

#COLLISION
def isCollision(ex,ey,bx,by):

    d = ((ex-bx)**2 + (ey-by)**2)**0.5

    if d <= 27:
       return True

#SCORE
score = 0
font = py.font.Font("game_over.ttf",90)
textX = 10; textY = 10

def show_score(tx,ty):
    global score
    s = font.render(f"SCORE: {str(score)}",True,(255,255,255))
    screen.blit(s,(tx,ty))

#GAME OVER//
overFont = py.font.Font("game_over.ttf",200)
gameOverSound = mixer.Sound("gameover.wav")

def game_over():
    overText = overFont.render(f"GAME OVER",True,(255,255,255))
    screen.blit(overText,(170,215))
    py.mixer.music.stop()

#PLAY AGAIN
playAgainFont = py.font.Font("game_over.ttf",65)

def isPlayAgain():
    pa = playAgainFont.render("Press Enter to PLAY AGAIN.",True,(255,255,255))
    playAgain = True
    screen.blit(pa,(220,100))


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
            if event.key == py.K_SPACE:
                if bState is "ready":
                    bSound = mixer.Sound('laser.wav')
                    bSound.play()
                    bX = playerX
                    fire_bullet(bX,bY)

            #PLAYAGAIN
            if event.key == py.K_KP_ENTER:
                running = True
                    
                

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
    for i in range(numOfEnemies):

        #GAME OVER
        if eY[i] > 450:
            for j in range(numOfEnemies):
                eY[j] = 2000
            game_over()
            isPlayAgain()
            break
            ##########gameOverSound.play()####################


        eX[i] += eXchange[i]
        
        if eX[i] <= 0:
            eXchange[i] = 3
            eY[i] += eYchange[i]

        elif eX[i] >= 736:
            eXchange[i] = -3
            eY[i] += eYchange[i]
        
        #COLLISION
        collision = isCollision(eX[i],eY[i],bX,bY)

        if collision:
            bY = 480; bState = "ready"; score += 1
            eX[i] = random.randint(70,730)
            eY[i] = random.randint(50,150)
            expSound = mixer.Sound("explosion.wav")
            expSound.play()

        enemy(i,eX[i],eY[i])

    #BULLET MOVEMENT
    if bY <= 0:
        bY = 480; bState = "ready"

    if bState is "fire":
        fire_bullet(bX,bY)
        bY -= bYchange


    player(playerX,playerY)
    show_score(textX,textY)

    py.display.update()


py.quit()
