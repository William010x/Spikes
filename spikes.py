import pygame, time
from player import Player
from hazard import Hazard

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
PLAYER_SPEED = 5
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
floor = DISPLAY_HEIGHT * 0.6
ceiling = DISPLAY_HEIGHT * 0.3

display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Spikes')
clock = pygame.time.Clock()

exit = False

def generate_stage():
    spikes = Hazard()
    return 0

def display_level(level):
    font = pygame.font.SysFont(None, 30)
    text = font.render("Level: " + str(level), True, WHITE)
    display.blit(text, (10, 10))

def display_game_over():
    font = pygame.font.SysFont(None, 100)
    text_surf = font.render("Game over", True, WHITE)
    text_rect = text_surf.get_rect()
    text_rect.topleft = (250, 200)
    display.blit(text_surf, text_rect)
        
    pygame.display.update()
    time.sleep(5)
    #menu.display_menu()
    #game_loop()

def game_loop():
    player = Player()
    spikes = Hazard()
    left_change = 0
    right_change = 0
    ####################TESTING####################
    up_change = 0
    down_change = 0
    ####################TESTING####################
    
    level = 1
    generate_stage()
    
    crashed = False
    while not crashed:
        jump = False
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
                global exit
                exit = True
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    left_change = 1
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    right_change = 1
                elif event.key == pygame.K_SPACE:
                    jump = True
                ####################TESTING####################
                #elif event.key == pygame.K_UP or event.key == pygame.K_w:
                #    up_change = 1
                #elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                #    down_change = 1
                ####################TESTING####################
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    left_change = 0
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    right_change = 0
                ####################TESTING####################
                #elif event.key == pygame.K_UP or event.key == pygame.K_w:
                #    up_change = 0
                #elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                #    down_change = 0                
                ####################TESTING####################
    
        display.fill(BLACK)
        pygame.draw.rect(display, GRAY, 
                         [0, floor, DISPLAY_WIDTH, DISPLAY_HEIGHT])
        pygame.draw.rect(display, GRAY, [0, 0, DISPLAY_WIDTH, ceiling])
        display_level(level)
        player.move(left_change, right_change, jump)
        #player.fly(up_change, down_change)
        # Check for death
        #for spike in spikes:
        if (spikes.overlap(player)):
            print("1: " + str(player.get_x()) + "," + str(player.get_y()))
            print("2: " + str(player.get_x() + 25) + "," + str(player.get_y() + 25))
            player.draw(display)
            spikes.draw(display)            
            display_game_over()
            crashed = True
        
        if (player.is_level_complete()):
            level += 1
            generate_stage()
            player.reset()
        
        player.draw(display)
        spikes.draw(display)
        pygame.display.update()
        clock.tick(60)
    
while not exit:
    game_loop()
pygame.quit()
quit()