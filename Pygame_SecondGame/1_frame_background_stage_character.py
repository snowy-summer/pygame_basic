import pygame

pygame.init()

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("거미 잡기")

clock = pygame.time.Clock()


backgroud = pygame.image.load("D:/bum/pygame_basic/Pygame_SecondGame/images/background.png")
stage = pygame.image.load("D:/bum/pygame_basic/Pygame_SecondGame/images/stage.png")

character = pygame.image.load("D:/bum/pygame_basic/Pygame_SecondGame/images/character.png")
character_size =character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2)-(character_width/2)
character_y_pos = screen_height - character_height

character_speed = 0.6

weapon = pygame.image.load("D:/bum/pygame_basic/Pygame_SecondGame/images/weapon.png")
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]
weapon_height = weapon_size[1]

enemy1 = pygame.image.load("D:/bum/pygame_basic/Pygame_SecondGame/images/enemy1.png")
enemy1_size= enemy1.get_rect().size
enemy1_width = enemy1_size[0]
enemy1_height = enemy1_size[1]
enemy1_x_pos = (screen_width/2)- (enemy1_width/2)
enemy1_y_pos = 0

enemy2 = pygame.image.load("D:/bum/pygame_basic/Pygame_SecondGame/images/enemy2.png")
enemy2_size= enemy1.get_rect().size
enemy2_width = enemy1_size[0]
enemy2_height = enemy1_size[1]

enemy3 = pygame.image.load("D:/bum/pygame_basic/Pygame_SecondGame/images/enemy3.png")
enemy3_size= enemy1.get_rect().size
enemy3_width = enemy1_size[0]
enemy3_height = enemy1_size[1]

game_font = pygame.font.Font(None,40)

total_time = 60
start_ticks = pygame.time.get_ticks()


running = True
while running:
    dt = clock.tick(30)
    
    screen.blit(backgroud,(0,0))
    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(enemy1,(enemy1_x_pos,enemy1_y_pos))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.display.update()

pygame.time.delay(3000)
pygame.quit()