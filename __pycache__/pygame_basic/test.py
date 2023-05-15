import pygame
# # 초기화 반드시 필요
pygame.init() 

# # 화면 크기 설정
screen_width = 480  # 가로길이
screen_height = 640 # 세로크기
screen = pygame.display.set_mode((screen_width,screen_height))

# # 화면 타이틀 설정
pygame.display.set_caption("Nado Game")

# #  배경 이미지 불러오기
# background = pygame.image.load("C:/Users/user/OneDrive/바탕 화면/PythonWorkspace/__pycache__/pygame_basic/background.png")

# # 이벤트 루프
running = True
while running:
    for event in pygame.event.get():    # 이벤트 발생 종류
        if event.type == pygame.QUIT:   # 이벤트 종류 : 종료
            running = False             # 게임 진행중 아님으로 변경1
    
#     # screen.fill((0,0,255))  # RGB색깔로 채우기
#     screen.blit(background,(0,0))   # 배경그리기

#     pygame.display.update() # 게임화면 다시그리기

# # pygame 종료
pygame.quit()  


