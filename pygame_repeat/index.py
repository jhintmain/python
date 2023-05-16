import pygame
import os
from random import *

# 초기화
pygame.init()

# 화면크기
screen_height = 480
screen_width = 640
screen = pygame.display.set_mode((screen_width,screen_height))

# 타이틀
pygame.display.set_caption("똥피하기 게임 - 복습")

# FPS
colock = pygame.time.Clock()

#############################################################

# 이미지 경로
# current_path = os.path.dirname(__file__)
# image_path = os.path.join(current_path,"images")
image_path = "C:/Users/user/OneDrive/바탕 화면/PythonWorkspace/images"

# 배경화면
background = pygame.image.load(os.path.join(image_path,"background.png"))

# 캐릭터
character = pygame.image.load(os.path.join(image_path,"character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = screen_height - character_height
character_speed = 5

# 똥
poop = pygame.image.load(os.path.join(image_path,"poop.png"))
poop_size = poop.get_rect().size
poop_x = poop_size[0]
poop_y = poop_size[1]
poop_x_pos = 0
poop_y_pos = 0
poop_speed = 10

to_x = 0

running = True
while running :
    # 프레임 설정
    dt = colock.tick(30)

    # 이벤트 종류별 액션 설정
    for event in pygame.event.get() :

        # 종료
        if event.type == pygame.QUIT : 
            running = False

        # 키 누를때
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        # 키 뗄ㄹ때
        if event.type == pygame.KEYUP :
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT : 
                to_x = 0


    # 이동위치 설정
    character_x_pos += to_x           

    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width :
        character_x_pos = screen_width - character_width

    poop_y_pos += poop_speed

    # 똥 떨어트리기
    if poop_y_pos > screen_height :
        poop_x_pos = randint(0, screen_width - poop_x)
        poop_y_pos = 0
        

    # 충돌처리
    character_rec = character.get_rect()
    character_rec.left = character_x_pos
    character_rec.top = character_y_pos

    poop_rec = poop.get_rect()
    poop_rec.left = poop_x_pos
    poop_rec.top = poop_y_pos
    

    if character_rec.colliderect(poop_rec) :
        print("충돌!")
        running = False

    # 그리기
    screen.blit(background,(0,0))   # 배경그리기
    screen.blit(character,(character_x_pos,character_y_pos))   # 캐릭터 그리기
    screen.blit(poop,(poop_x_pos,poop_y_pos))   # 똥 그리기

    # 화면 갱신
    pygame.display.update()

# 종료
pygame.quit()