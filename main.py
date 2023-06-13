import pygame
import random
import time

pygame.init()

# Variable 

crash_s = pygame.mixer.Sound('crashed.mp3')
pygame.mixer.music.load('game-sound.mp3')
car_img = pygame.image.load('mycar.png')
car_width = 50

clock = pygame.time.Clock()

dis_width = 800
dis_height = 500

black = '#000000'
disc = '#F0F070'
red = '#FF0000'
acred = '#FF5500'
green = '#00FF00'
acgreen = '#00FF55'
stepcolor = '#8D0EE2'

gameDis = pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption('Car Racing')


# Function

def button(massege,x,y,w,h,accolor,unaccolor,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDis,accolor,(x,y,w,h))
        if click[0] == 1 and action != None:
            if action == 'play':
                gameloop()
            elif action == 'quit':
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(gameDis,unaccolor,(x,y,w,h))
    smallText = pygame.font.Font('freesansbold.ttf',20)
    textSurf , textRect = textobject(massege,smallText)
    textRect.center = (x+(w/2),y+(h/2))
    gameDis.blit(textSurf,textRect)
    
def intro():
    introo = True
    while introo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDis.fill(disc)
        largeText = pygame.font.Font('freesansbold.ttf',70)
        textSurf , textRect = textobject('^^ CAR RACING ^^',largeText)
        textRect.center = ((dis_width/2),(dis_height/2))
        gameDis.blit(textSurf,textRect)
        button('PLAY',150,350,100,50,acgreen,green,action='play')
        button('Quit',550,350,100,50,acred,red,action='quit')
        pygame.display.update()

def step_dodged(count):
    font = pygame.font.SysFont(None,20)
    text = font.render('Score : '+ str(count),True,stepcolor)
    gameDis.blit(text,(10,10))

def step(stepx,stepy,stepw,steph,color):
    pygame.draw.rect(gameDis,stepcolor,[stepx,stepy,stepw,steph])

def car(x,y):
    gameDis.blit(car_img,(x,y))

def textobject(text,font):
    textSurface = font.render(text,True,black)
    return textSurface,textSurface.get_rect()

def massege_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',70)
    textSurf , textRect = textobject(text=text,font=largeText)
    textRect.center = ((dis_width/2),(dis_height/2))
    gameDis.blit(textSurf,textRect)
    pygame.display.update()
    time.sleep(2)
    gameloop()

def crash():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_s)
    largeText = pygame.font.Font('freesansbold.ttf',70)
    textSurf , textRect = textobject('CRASHED )-8',largeText)
    textRect.center = ((dis_width/2),(dis_height/2))
    gameDis.blit(textSurf,textRect)
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button('Replay',150,350,100,50,acgreen,green,action='play')
        button('Quit',550,350,100,50,acred,red,action='quit')
        pygame.display.update()

def gameloop():
    pygame.mixer.music.play(-1)
    x = dis_width * 0.46875
    y = dis_height * 0.75
    x_change = 0
    step_startx = random.randrange(0,dis_width)
    step_starty = -500
    step_speed = 5
    step_width = 100
    step_height = 100
    dodged = 0
    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                    x_change = 0
        x += x_change
        gameDis.fill(disc)

        step(step_startx,step_starty,step_width,step_height,stepcolor)
        step_starty += step_speed
        step_dodged(dodged)
        car(x=x,y=y)

        if x > dis_width - car_width or x < 0:
            crash()
        if step_starty > dis_height :
            step_starty = 0 - step_height
            step_startx = random.randrange(0,dis_width)
            dodged += 1
            if dodged % 10 == 0:
                step_speed += 4
        if y<step_starty + step_height:
            if (
                x > step_startx
                and x < step_startx + step_width
                or x + car_width > step_startx
                and x + car_width < step_startx + step_width
            ):
                crash()
        pygame.display.update()
        clock.tick(60)


intro()
gameloop()
pygame.quit()
quit()