import pygame
######################################################################################################################################
# 기본 초기화 (반드시 해야 하는 것들)

pygame.init() # 초기화 (반드시 필요)

#화면 크기 설정
screen_width = 480 #가로
screen_height = 640 #세로
screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("first game")

#FPS
clock =pygame.time.Clock()


########################################################################################################################################
# 1. 사용자 게임 초기화 ( 배경 화면 , 게임 이미지, 속도 ,  폰트 등)

running = True 
while running:
    dt = clock.tick(60)#게임화면의 초당 프레임 수 설정
    #캐릭터가 1초동안 100만큼 이동해야함
    #10fps : 1초동안 10번 동작 -> 1번에 10만큼   10*10
    #20fps : 1초동안 20번 동작 -> 1번에 5만큼    5*20  



 #######################################################################################################
  #2. 이벤트 처리(키보드 , 마우스)
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False
        
        
 
 #############################################################################################################
  # 3. 게임 캐릭터 위치 정의

    

   ##############################################################################################
   # 4. 충돌 처리

    

 ##########################################################################################
 # 5. 화면에 그리기
 
   
    # 게임 화면을 다시 그리기
    pygame.display.update() 

# 약간 늦게 종료
pygame.time.delay(2000) # 2초 정도 대기
 
#게임 종료
pygame.quit()