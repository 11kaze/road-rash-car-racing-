import pygame
import time
import sys
import random
import os
pygame.init()
#color
gray=(119,118,110)
white=(255,255,255)
black=(0,0,0)
red=(200,0,0)
green=(0,200,0)
blue=(0,0,255)



window_width=800
window_hight=600

yo=[]
#display surface
gd=pygame.display.set_mode((window_width,window_hight))
pygame.display.set_caption('ROAD FIGHTER')
carimg=pygame.image.load('main-car-image.png')
car1=pygame.transform.scale(carimg,(70,100))
clock=pygame.time.Clock()
def load(name,x_pos,y_pos):
    v = pygame.image.load(name)
    gd.blit(v, (x_pos, y_pos))
    pygame.display.update()
def message(mess,colour,size,x,y):
     font=pygame.font.SysFont("arial",size,False,True)
     screen_text=font.render(mess,True,colour)
     gd.blit(screen_text,(x,y))
     pygame.display.update()

def button(x,y,w,h,mess,mess_color,actc,noc,size,tx,ty,func):
    mouse = pygame.mouse.get_pos()
    print(mouse)
    click=  pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:

        pygame.draw.rect(gd, actc, [x, y, w, h])
        message(mess, mess_color, size, tx, ty)
        pygame.display.update()
        if click==(1,0,0):
            func()

    else:
        pygame.draw.rect(gd, noc, [x, y, w, h])
        message(mess, mess_color, size, tx, ty)
        pygame.display.update()
    pygame.display.update()
def quit1():
    pygame.quit()
    quit()

def game_intro():
  load('background1.jpg', 0, 0)
  
  gameintro=False
  while gameintro==False:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameintro = True
            game_over=True

    window_width = 800
    window_hight = 600


    message('Road Fighter',(255,123,123),90,(window_width/2 - 220),100)
    button(90, 306, 200, 30, 'Play', black, (192,192,192,0.3), white,25,106,306,gameloop)
    button(90,336, 190, 30,'Setting', black, (192,192,192,0.3),white,25,106,336,None)
    button(90, 366, 180, 30, 'Quit', black, (192,192,192,0.3),white,25,106,366,quit1)

    pygame.display.update()



  pygame.display.update()
def crash_sound():
    pygame.mixer.music.load('crash sound.mp3')
    pygame.mixer.music.play()
    time.sleep(1)  

def back():
    blue_strip=pygame.image.load('grass.jpg')
    img=pygame.transform.scale(blue_strip,(100,600))
    gd.blit(img,(0,0))
    gd.blit(img,(700,0))
def crash(x,y):
    if 90>x  or x+90>700:
        
        crash_sound()

        font = pygame.font.SysFont(None, 100)
        screen_text = font.render('game_over', True, white)
        gd.blit(screen_text, (250, 280))
        pygame.display.update()
        time.sleep(1)
        game_intro()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()

    if y<0 or y>520:
        
        crash_sound()

        font = pygame.font.SysFont(None, 100)
        screen_text = font.render('game_over', True, white)
        gd.blit(screen_text, (250, 280))
        pygame.display.update()
        time.sleep(1)
        game_intro()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()

def car_crash(x,y,y_en,x_en):

    if x<x_en+75<x+149 and (y<y_en+96<y+100 or y<y_en<y+100):
        crash_sound()

        message('CRASHED!', red, 100, 250, 280)
        time.sleep(1)
        game_intro()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()


def score_and_level(count):
    font = pygame.font.SysFont(None, 30)
    screen_score_text = font.render('score :' + str(count), True, white)
    if count < 3:
        screen_level_text = font.render('Level :' + 'Novice', True, white)
    elif count < 6:
        screen_level_text = font.render('Level :' + 'Pro', True, white)    
    else:
        screen_level_text = font.render('Level :' + 'Ultra Pro', True, white)
    gd.blit(screen_level_text, (700, 0))
    gd.blit(screen_score_text, (0, 0))
    pygame.display.update()

def other_car(y_en,x,y,count):
    enmy1=pygame.image.load('car5.jpg')
    enmy=pygame.transform.scale(enmy1,(70,100))
    global  x_en
    other_car_stop = 0
    if y_en==0:
        x_en=random.randrange(100,600)
        yo.clear()
        yo.append(x_en)
        yo.append(0)
    else:
        x_en=yo[0]
        if 3<count and count<6:
            if yo[1]==0 or yo[1]==1:
                if x_en < x and y_en < y:
                    yo[0] += 10 
                    x_en = yo[0]
                    yo[1] = 1
            if yo[1]==0 or yo[1]==2:
                if x_en > x and y_en < y:
                    yo[0] -= 10
                    x_en = yo[0] 
                    yo[1] = 2
        elif count > 6:
            if x_en < x and y_en < y:
                yo[0] += 10 
                x_en = yo[0]
            elif x_en > x and y_en < y:
                yo[0] -= 10
                x_en = yo[0]         

    gd.blit(enmy,(x_en,y_en))
    pygame.display.update()

def gameloop():
     pygame.mixer.music.pause()
     x = 300
     y = 400
     x_change = 0
     y_change = 0
     global game_over
     game_over=False

     count = 0
     y_en=0
     while game_over==False:
         for event in pygame.event.get():
                 if event.type==pygame.QUIT:
                     game_over=True
                 if event.type==pygame.KEYDOWN:
                     if event.key==pygame.K_LEFT:
                         x_change=-10
                     elif event.key==pygame.K_RIGHT:
                         x_change=+10
                     if event.key==pygame.K_DOWN:
                         y_change=+10
                     elif event.key==pygame.K_UP:
                         y_change=-10    
                 if event.type==pygame.KEYUP:
                     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                         x_change = 0
                     if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                         y_change = 0

         x+=x_change
         y+=y_change

         gd.fill(white)

         back()
         gd.blit(car1, (x, y))
         if y_en>600:
           y_en=0
           count += 1
         other_car(y_en,x,y,count)
         y_en+=10
         crash(x,y)
         car_crash(x,y,y_en,x_en)
         score_and_level(count)



         clock.tick(30)
         pygame.display.update()

pygame.mixer.music.load('backgroung_music.mp3')
pygame.mixer.music.play(loops=-1)
game_intro()
pygame.quit()
quit()