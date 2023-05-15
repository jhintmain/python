import pygame
from random import *

# 초기화
pygame.init()

# 화면 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

# 타이틀
pygame.display.set_caption("똥피하기 게임")

# FPS
fps = pygame.time.Clock()


##############################
# 배경화면 생성
background = pygame.image.load("C:/Users/user/OneDrive/바탕 화면/PythonWorkspace/__pycache__/pygame_basic/background.png")

# 캐릭터 생성
character = pygame.image.load("C:/Users/user/OneDrive/바탕 화면/PythonWorkspace/__pycache__/pygame_basic/character.png")
character_size = character.get_rect().size
character_x = character_size[0]
character_y = character_size[1]
character_x_pos = (screen_width/2) - (character_x/2)
character_y_pos = screen_height - character_y

# 똥 생성
poop = pygame.image.load("C:/Users/user/OneDrive/바탕 화면/PythonWorkspace/__pycache__/pygame_basic/enemy.png")
poop_size = poop.get_rect().size
poop_x = poop_size[0]
poop_y = poop_size[1]
poop_x_pos = randint(0, screen_width-poop_x)
poop_y_pos = 0
poop_speed = 5


speed = 4
to_x = 0

running = True
while running :
    frame = fps.tick(30)    # 초당 프레임수
    # 이벤트 처리
    for event in pygame.event.get():    # 이벤트 발생 종류
        if event.type == pygame.QUIT:   # 이벤트 종류 : 종료
            running = False     

        # 키 누를때
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= speed
            elif event.key == pygame.K_RIGHT:
                to_x += speed

        # 키 땔떼
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT : 
                to_x = 0
                
    character_x_pos += to_x * frame
    
    if character_x_pos < 0:
        character_x_pos =0
    elif character_x_pos > screen_width - character_x:
        character_x_pos = screen_width - character_x

    poop_y_pos += poop_speed

    if poop_y_pos > screen_height:
        poop_x_pos = randint(0, screen_width-poop_x)
        poop_y_pos = 0


    # 충돌처리
    character_rec = character.get_rect()
    character_rec.left = character_x_pos
    character_rec.top = character_y_pos
 
    poop_rec = poop.get_rect()
    poop_rec.left = poop_x_pos
    poop_rec.top = poop_y_pos

    if character_rec.colliderect(poop_rec):
        print("충돌")
        running = False

    # 배경그리기
    screen.blit(background,(0,0))   # 배경그리기
    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(poop,(poop_x_pos,poop_y_pos))


    pygame.display.update()


##############################
# 종료
pygame.quit()