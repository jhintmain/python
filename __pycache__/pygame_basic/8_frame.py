import pygame

# 0. 기본 초기화 (반드시 해야하는 것들)
#########################################################################
pygame.init() 

# 화면 크기 설정
screen_width = 480  # 가로길이
screen_height = 640 # 세로크기
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game")

# FPS
clock = pygame.time.Clock()
#########################################################################

# 1. 사용자 게임 초기화 ( 배경화면, 게임 이미지,. 좌표, 폰트 )

running = True
while running:
    dt = clock.tick(30) # 초당 프레임수

    # 2. 이벤트 처리
    for event in pygame.event.get():    # 이벤트 발생 종류
        if event.type == pygame.QUIT:   # 이벤트 종류 : 종료
            running = False             # 게임 진행중 아님으로 변경

  
    # 3. 게임 캐릭터 위치 정의

    # 4. 충돌 처리

    # 5. 화면에 그리기


    pygame.display.update() # 게임화면 다시그리기


# pygame 종료
pygame.quit()  