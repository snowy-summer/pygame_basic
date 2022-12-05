import pygame

pygame.init() # 초기화 (반드시 필요)

screen_width = 480 #가로
screen_height = 640 #세로
screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("first game")

#배경 이미지 불러오기
background =pygame.image.load("D:/bum/python/pygame_basic/background.png") #파일 경로 복사해서 넣기


# 이벤트 루프  안꺼지게 하려고 
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False

    # screen.fill((0,0,255)) #RGB값  화면 채우기
    screen.blit(background, (0,0)) #배경그리기
    pygame.display.update() # 게임 화면을 다시 그리기

#게임 종료
pygame.quit()