import pygame
import os

pygame.init()

# 화면크기
screen_height = 480
screen_width = 640
screen = pygame.display.set_mode((screen_width,screen_height))

# 타이틀
pygame.display.set_caption("나도팡!")

# FPS
clock = pygame.time.Clock()
####################################

image_path = "C:/Users/user/OneDrive/바탕 화면/PythonWorkspace/images"

# 배경화면
background = pygame.image.load(os.path.join(image_path,"background.png"))

# 스테이지 
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_width = stage_size[0]
stage_heigth = stage_size[1]
stage_x_pos = 0
stage_y_pos = screen_height - stage_heigth

# 캐릭터
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_heigth = character_size[1]
character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = screen_height - character_heigth - stage_heigth
character_speed = 5

# 무기
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]
weapon_heigth = weapon_size[1]
weapon_speed = 10
weapons = []

# 공
balls = []

to_x = 0

running = True
while running : 
    dt = clock.tick(30)

    for event in pygame.event.get() : 

        if event.type == pygame.QUIT : 
            running = False
            
        if event.type == pygame.KEYDOWN : 
            if event.key == pygame.K_RIGHT : 
                to_x += character_speed
            if event.key == pygame.K_LEFT : 
                to_x -= character_speed
            if event.key == pygame.K_SPACE : 
                # 무기발사
                weapon_x_pos = character_x_pos + (character_width/2) - (weapon_width/2) # 캐릭터 중간에 위치
                weapon_y_pos = character_y_pos # 캐릭터 위로 발사
                weapons.append([weapon_x_pos,weapon_y_pos])

        if event.type == pygame.KEYUP : 
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT : 
                to_x = 0

    character_x_pos += to_x

    # 캐릭터 이동범위 처리
    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width : 
        character_x_pos = screen_width - character_width


    # 무기 이동범위 처리    ( y위치만 빼준다 )
    # w[0] = x / w[1] = y
    weapons = [ [w[0], w[1]- weapon_speed] for w in weapons]
    weapons = [ [w[0], w[1] ] for w in weapons if w[1] > 0]

    # 충돌처리
    # character_rec = character.get_rect()
    # character_rec.left = character_x_pos
    # character_rec.top = character_y_pos

    # 그리기
    screen.blit(background,(0,0))

    # 무기 그리기
    for weapon_x_pos, weapon_y_pos in weapons : 
        screen.blit(weapon,(weapon_x_pos,weapon_y_pos))

    screen.blit(stage,(0,screen_height - stage_heigth))
    screen.blit(character,(character_x_pos,character_y_pos))

    # 화면 갱신
    pygame.display.update()


pygame.quit()