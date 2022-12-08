import pygame
import os

pygame.init()

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("거미 잡기")

clock = pygame.time.Clock()

# 현재 파일의 위치 반환
current_path = os.path.dirname(__file__)
#이미지 폴더 위치 반환
image_path = os.path.join(current_path,"images")
#배경
backgroud = pygame.image.load(os.path.join(image_path,"background.png"))

stage = pygame.image.load(os.path.join(image_path,"stage.png"))
stage_size = stage.get_rect().size
stage_width = stage_size[0]
stage_height = stage_size[1]
stage_x_pos = 0
stage_y_pos = screen_height - stage_height

character = pygame.image.load(os.path.join(image_path,"character.png"))
character_size =character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2)-(character_width/2)
character_y_pos = screen_height - stage_height -character_height
character_to_x = 0
character_to_y = 0
character_speed = 10

weapon = pygame.image.load(os.path.join(image_path,"weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]
weapon_height = weapon_size[1]

weapons = []

weapon_speed =10

enemy_images =[
    pygame.image.load(os.path.join(image_path,"enemy1.png")),
    pygame.image.load(os.path.join(image_path,"enemy2.png")),
    pygame.image.load(os.path.join(image_path,"enemy3.png")),]

# 공 크기에 따른 최초 스피드
enemy_speed_y =[-18,-15,-12] #index 0,1,2 에 해당하는 값  튕겨서 뒤로 가야하기 때문에 -값

enemys=[]

enemys.append({
    "pos_x": 50, #공의 x좌표
    "pos_y": 50, # 공의 y좌표
    "img_idx": 0, #공의 이미지 인덱스
    "to_x":3,   #x축 이동방향  , -면 왼쪽 +면 오른쪽
    "to_y":-6, #y축 이동방향
    "init_spd_y": enemy_speed_y[0] })# y의 최초 속도

#사라질 무기, 공 저장 변수
weapon_to_remove = -1
enemy_to_remove = -1

game_font = pygame.font.Font(None,40)

total_time = 100
start_ticks = pygame.time.get_ticks()

#게임 종료

game_result ="game over"


running = True
while running:
    dt = clock.tick(30)
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed

            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos+ (character_width/2)-(weapon_width/2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos,weapon_y_pos])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0
            elif event.key == pygame.K_SPACE:
                pass

    character_x_pos += character_to_x

    if character_x_pos < 0:
        character_x_pos =0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    
    #무기 위치 조정
    weapons = [ [w[0] ,w[1]-weapon_speed] for w in weapons] #무기 위치 위로 올리기

    #천장에 닿은 무기 없애기
    weapons = [[w[0], w[1]] for w in weapons if w[1]>0]


    # 적 위치 정의
    for enemy_idx, enemy_val in enumerate(enemys):
        enemy_x_pos = enemy_val["pos_x"]
        enemy_y_pos = enemy_val["pos_y"]
        enemy_img_idx = enemy_val["img_idx"]
        enemy_size  = enemy_images[enemy_img_idx].get_rect().size
        enemy_width = enemy_size[0]
        enemy_height = enemy_size[1]
     #가로벽에 닿았을 때 공 이동 위치 변경 (뒹겨 나오는 효과)
        if enemy_x_pos < 0 or enemy_x_pos > screen_width -enemy_width:
            enemy_val["to_x"] = enemy_val["to_x"]*-1

        #세로 위치
        #스테이지에 튕겨서 올라가는 처리
        if enemy_y_pos >= screen_height- stage_height -enemy_height:
            enemy_val["to_y"] = enemy_val["init_spd_y"]
        else: #그 외의 모든 경우에는 속도를 증가
            enemy_val["to_y"] += 0.5

        enemy_val["pos_x"] += enemy_val["to_x"]
        enemy_val["pos_y"] += enemy_val["to_y"]


 # 충돌처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    for enemy_idx, enemy_val in enumerate(enemys):
        enemy_x_pos = enemy_val["pos_x"]
        enemy_y_pos = enemy_val["pos_y"]
        enemy_img_idx = enemy_val["img_idx"]

        #적 rect정보 업데이트
        enemy_rect  = enemy_images[enemy_img_idx].get_rect()
        enemy_rect.left = enemy_x_pos
        enemy_rect.top = enemy_y_pos
        if character_rect.colliderect(enemy_rect):
            running = False
            break

        #적과 무기 충돌
        for weapon_idx, weapon_val in enumerate(weapons):
            weapon_x_pos = weapon_val[0] 
            weapon_y_pos = weapon_val[1]

            #무기 rect 정보 업데이트 
            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_x_pos 
            weapon_rect.top = weapon_y_pos

            #충돌 체크 
            if weapon_rect.colliderect(enemy_rect):
                weapon_to_remove = weapon_idx # 해당 무기 없애기 위한 값 설정
                enemy_to_remove = enemy_idx
                
                if enemy_img_idx <2: #가장 다음 적이 아니라면 다음 단계 적으로 나누기
                    
                    #현재 적 사이즈 정보 가지고 옴
                    enemy_width = enemy_rect[0]
                    enemy_height = enemy_rect[1]

                    #나눠진 공 정보
                    small_enemy_rect = enemy_images[enemy_img_idx+1].get_rect()
                    small_enemy_width = small_enemy_rect.size[0]
                    small_enemy_height = small_enemy_rect.size[1]
                    #왼쪽으로 튕겨 나가는 작은적
                    enemys.append({
                        "pos_x": enemy_x_pos+(enemy_width/2)-(small_enemy_width/2), #공의 x좌표
                        "pos_y": enemy_y_pos+(enemy_height/2)-(small_enemy_height/2), # 공의 y좌표
                        "img_idx": enemy_img_idx+1, #공의 이미지 인덱스
                        "to_x": -3,   #x축 이동방향  , -면 왼쪽 +면 오른쪽
                        "to_y": -6, #y축 이동방향
                        "init_spd_y": enemy_speed_y[enemy_img_idx+1] })# y의 최초 속도

                    #우측으로 튕기는 적
                    enemys.append({
                        "pos_x": enemy_x_pos+(enemy_width/2)-(small_enemy_width/2), #공의 x좌표
                        "pos_y": enemy_y_pos+(enemy_height/2)-(small_enemy_height/2), # 공의 y좌표
                        "img_idx": enemy_img_idx+1, #공의 이미지 인덱스
                        "to_x": 3,   #x축 이동방향  , -면 왼쪽 +면 오른쪽
                        "to_y": -6, #y축 이동방향
                        "init_spd_y": enemy_speed_y[enemy_img_idx+1] })# y의 최초 속도
                                            
                break
        else: #계속 게임진행
            continue   #안쪽 for 문 조건이 맞지 않으면 continue 바깥  for문 계속 수행
        #안쪽 for 문에서 break 만나면 여기로 진입 가능
        break

    #충돌된 공 , 무기 없애기 
    if enemy_to_remove > -1:
        del enemys[enemy_to_remove]
        enemy_to_remove = -1

    if weapon_to_remove > -1:
        del weapons[weapon_to_remove]
        weapon_to_remove = -1

    
    #모든 적 없앤 경우 게임 종료
    if len(enemys) == 0:
        game_result = "Mission Complete"
        running = False



    elapsed_time = (pygame.time.get_ticks()- start_ticks) / 1000
    timer = game_font.render("time:{}".format(int(total_time - elapsed_time)),True, (255,255,255))
   
   # 시간 초과 했다면 
    if total_time - elapsed_time <= 0:
        game_result = "Time Over"
        running = False

    screen.blit(backgroud,(0,0))

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon,(weapon_x_pos,weapon_y_pos))
    screen.blit(stage,(stage_x_pos,stage_y_pos))
    
    for idx,val in enumerate(enemys):
        enemy_x_pos = val["pos_x"]
        enemy_y_pos = val["pos_y"]
        enemy_img_idx = val["img_idx"]
        screen.blit(enemy_images[enemy_img_idx],(enemy_x_pos,enemy_y_pos))
    

    
    
    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(timer,(screen_width/2,10))    

    pygame.display.update()

msg = game_font.render(game_result, True, (255,255,0))
msg_rect = msg.get_rect(center=(int(screen_width/2),int(screen_height/2)))
screen.blit(msg,msg_rect)
pygame.display.update()

pygame.time.delay(3000)
pygame.quit()