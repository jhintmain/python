import pygame
import os

pygame.init()

# 화면크키
screen_x = 640
screen_y = 480
screen = pygame.display.set_mode((screen_x,screen_y))

# 타이틀
pygame.display.set_caption("나도팡!")

# FPS
clock = pygame.time.Clock()
###########################################

# 사용자 게임 초기화
# current_path = os.path.dirname(__file__)
# image_path = os.path.join(current_path,"images")
image_path = "C:/Users/user/OneDrive/바탕 화면/PythonWorkspace/images"

# 배경화면
background = pygame.image.load(os.path.join(image_path,"background.png"))

# 스테이지
stage = pygame.image.load(os.path.join(image_path,"stage.png"))
stage_size = stage.get_rect().size
stage_y = stage_size[1]

# 캐릭터 만들기
character = pygame.image.load(os.path.join(image_path,"character.png"))
character_size = character.get_rect().size
character_x = character_size[0]
character_y = character_size[1]
character_x_pos = (screen_x/2)-(character_x/2)
character_y_pos = screen_y - stage_y - character_y

# 시작시간
start_tick = pygame.time.Clock()

character_to_x = 0
character_speed = 5

# 무기 만들기
weapon = pygame.image.load(os.path.join(image_path,"weapon.png"))
weapon_size = weapon.get_rect().size
weapon_x = weapon_size[0]

# 무기 한번에 여러발 발사가능
weapons = []
weapon_speed = 10

# 공만들기 (4개크기)
ball_images = [
     pygame.image.load(os.path.join(image_path,"balloon1.png")),
     pygame.image.load(os.path.join(image_path,"balloon2.png")),
     pygame.image.load(os.path.join(image_path,"balloon3.png")),
     pygame.image.load(os.path.join(image_path,"balloon4.png")),
]


# 공 크기에 따른 최초 스피드
ball_speed_y = [-18,-15,-12.-9]  # index 0,1,2,3에 해당하는 값
ball_speed_x = [] 

# 공들
balls = []
balls.append({
    "pos_x" : 50,   # 공의 x 좌표
    "pos_y" : 50,   # 공의 y 좌표
    "img_idx" :0,    # 공의 이미지 인덱스
    "to_x" : 3, # x축이동방향 + 오른쪽 - 왼쪽
    "to_y" : -6, # y축이동방향 + 위 - 아래
    "init_spd_y" : ball_speed_y[0]
})

running = True
while running:
    dt = clock.tick(30) # 초당 프레임수

    for event in pygame.event.get():    # 이벤트 발생 종류
        if event.type == pygame.QUIT:   # 이벤트 종류 : 종료
            running = False             # 게임 진행중 아님으로 변

        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_LEFT :
                character_to_x -= character_speed
            elif event.key == pygame.K_SPACE :
                weapon_x_pos = character_x_pos  + (character_x/2) - (weapon_x/2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos,weapon_y_pos])


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0
        

    character_x_pos += character_to_x

    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_x - character_x :
        character_x_pos = screen_x - character_x


    # 무기 위치조정
    # 100, 200 -> 180,160,140 ....
    weapons = [ [w[0], w[1] - weapon_speed] for w in weapons]

    # 천장에 닿은 무기 없애기
    weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0]


    # 화면 그리기
    screen.blit(background,(0,0))

    for weapon_x_pos, weapon_y_pos in weapons :
        screen.blit(weapon,(weapon_x_pos,weapon_y_pos))

    screen.blit(stage,(0,screen_y-stage_y))
    screen.blit(character,(character_x_pos,character_y_pos))

    pygame.display.update()

pygame.quit()