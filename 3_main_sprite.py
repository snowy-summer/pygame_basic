import pygame

pygame.init() # 초기화 (반드시 필요)

screen_width = 480 #가로
screen_height = 640 #세로
screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("first game")

#배경 이미지 불러오기
background = pygame.image.load("D:/bum/pygame_basic/background.png") #파일 경로 복사해서 넣기

#캐릭터(스프라이트) 불러오기
character = pygame.image.load("D:/bum/pygame_basic/character.png")
character_size = character.get_rect().size #이미지 크기를 구해옴
character_width = character_size[0] #캐릭터 가로
character_height = character_size[1] #캐릭터 새로
character_x_pos = (screen_width/2) -(character_width/2) #화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height #화면 세로크기 가장 아래에 해당하는 곳에 위치





# 이벤트 루프  안꺼지게 하려고 
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False

 
    screen.blit(background, (0,0)) #배경그리기

    screen.blit(character, (character_x_pos,character_y_pos))
    pygame.display.update() # 게임 화면을 다시 그리기

#게임 종료
pygame.quit()