import pygame, time, random
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
SPIKE_WIDTH = 80

display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Spikes')
clock = pygame.time.Clock()

exit = False
spikes = []

def generate_stage(level):
    # Display instructions
    if level == 1:
        font = pygame.font.SysFont(None, 35)
        text_surf = font.render("Press space to jump. Use arrow keys to move.",
                                True, WHITE)
        text_rect = text_surf.get_rect()
        text_rect.center = ((DISPLAY_WIDTH / 2) , (DISPLAY_HEIGHT / 2) - 175)
        display.blit(text_surf, text_rect)
        
    global spikes
    spikes = []
    for i in range(1, level + 1):
        orientation = random.randint(0, 1)
        x = random.randint(50, DISPLAY_WIDTH - 50 - SPIKE_WIDTH)
        spikes.append(Hazard(x, orientation))

def display_level(level):
    font = pygame.font.SysFont(None, 40)
    text_surf = font.render("Level: " + str(level), True, WHITE)
    display.blit(text_surf, (10, 10))

def display_game_over():
    font = pygame.font.SysFont(None, 150)
    text_surf = font.render("Game over", True, WHITE)
    text_rect = text_surf.get_rect()
    text_rect.center = ((DISPLAY_WIDTH / 2) , (DISPLAY_HEIGHT / 2))
    display.blit(text_surf, text_rect)
    
    font = pygame.font.SysFont(None, 30)
    text_surf = font.render("Press enter to restart", True, WHITE)
    text_rect = text_surf.get_rect()
    text_rect.center = ((DISPLAY_WIDTH / 2) , (DISPLAY_HEIGHT / 2) + 120)
    display.blit(text_surf, text_rect)
    
    restart = False
    while not restart:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                restart = True
                global exit
                exit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    restart = True
        pygame.display.update()

def game_loop():
    player = Player()
    left_change = 0
    right_change = 0
    ####################TESTING####################
    #up_change = 0
    #down_change = 0
    ####################TESTING####################
    
    level = 1
    generate_stage(level)
    
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
        for spike in spikes:
            spike.draw(display)
            if (spike.overlap(player)):
                #player.draw(display)
                #for spike in spikes:
                #    spike.draw(display)
                display.fill(BLACK)
                display_level(level)
                display_game_over()
                crashed = True
        
        if (player.is_level_complete()):
            level += 1
            generate_stage(level)
            player.reset()
        
        player.draw(display)
        pygame.display.update()
        clock.tick(60)
    
while not exit:
    game_loop()
pygame.quit()
quit()