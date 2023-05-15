import pygame

# 초기화 반드시 필요
pygame.init() 

# 화면 크기 설정
screen_width = 480  # 가로길이
screen_height = 640 # 세로크기
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game")

# fps
clock = pygame.time.Clock()

#  배경 이미지 불러오기
background = pygame.image.load("C:/Users/user/OneDrive/바탕 화면/PythonWorkspace/__pycache__/pygame_basic/background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:/Users/user/OneDrive/바탕 화면/PythonWorkspace/__pycache__/pygame_basic/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = screen_height - character_height


to_x = 0
to_y = 0

# 이동속도
character_speed = 5


# 적 캐릭터
enemy = pygame.image.load("C:/Users/user/OneDrive/바탕 화면/PythonWorkspace/__pycache__/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = (screen_width/2) - (enemy_width/2)
enemy_y_pos = (screen_height/2) - (enemy_height/2)

# 이벤트 루프
running = True
while running:
    dt = clock.tick(30) # 초당 프레임수

    # print("fps:"+str(clock.get_fps()))

    for event in pygame.event.get():    # 이벤트 발생 종류
        if event.type == pygame.QUIT:   # 이벤트 종류 : 종료
            running = False             # 게임 진행중 아님으로 변경

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT : 
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN : 
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0 :
        character_y_pos = 0
    elif character_y_pos > screen_height- character_height:
        character_y_pos = screen_height - character_height


    #충돌처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False

    screen.blit(background,(0,0))   # 배경그리기
    screen.blit(character,(character_x_pos,character_y_pos))   # 캐릭터 그리기
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos))   # 적 그리기

    pygame.display.update() # 게임화면 다시그리기

# pygame 종료
pygame.quit()  