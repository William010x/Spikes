import pygame

player_img = pygame.image.load('images/player.png')
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
floor = DISPLAY_HEIGHT * 0.6
ceiling = DISPLAY_HEIGHT * 0.3
MOVE_SPEED = 5
JUMP_SPEED = 5
JUMP_HEIGHT = 22
PLAYER_SIZE = 25

class Player:
    def __init__(self):
        self.__x = 0
        self.__y = floor - PLAYER_SIZE
        self.__apex = 0
        self.__double_jump = False
    
    ####################TESTING#################### 
    #def fly(self, up_change, down_change):
    #    if (up_change == 1 and down_change == 0):
    #        new_y = self.__y - MOVE_SPEED
    #        if (not (new_y < 0)):
    #            self.__y -= MOVE_SPEED
    #    elif (up_change == 0 and down_change == 1):
    #        new_y = self.__y + MOVE_SPEED
    #        if (not (new_y > DISPLAY_WIDTH - 25)):
    #            self.__y += MOVE_SPEED
    ####################TESTING####################
    
    def move(self, left_change, right_change, jump):
        if (left_change == 1 and right_change == 0):
            new_x = self.__x - MOVE_SPEED
            if (not (new_x < 0)):
                self.__x -= MOVE_SPEED
        elif (left_change == 0 and right_change == 1):
            new_x = self.__x + MOVE_SPEED
            if (not (new_x > DISPLAY_WIDTH - 25)):
                self.__x += MOVE_SPEED
            
        if (jump == True):
            self.jump()
        
        # Player jumping
        if (self.__apex > 0):
            if (self.__apex >= JUMP_HEIGHT):
                self.__apex = -1
            else:
                self.__apex += 1
            new_y = self.__y - JUMP_SPEED
            if (new_y <= ceiling):
                self.__y = ceiling
                self.__apex = -1
            else:
                self.__y -= JUMP_SPEED
        # Player falling
        elif (self.__apex < 0):
            new_y = self.__y + JUMP_SPEED
            if (new_y >= floor - PLAYER_SIZE):
                self.__y = floor - PLAYER_SIZE
                self.__apex = 0
                self.__double_jump = 0
            else:
                self.__y += JUMP_SPEED
                
    def jump(self):
        if (self.__y == floor - PLAYER_SIZE):
            self.__apex = 1
        elif (self.__double_jump == False):
            self.__apex = 1
            self.__double_jump = True
        
    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y
    
    def reset(self):
        self.__x = 0
        self.__y = floor - PLAYER_SIZE
        
    def draw(self, display):
        display.blit(player_img, (self.__x, self.__y))
        
    def is_level_complete(self):
        if (self.__x >= DISPLAY_WIDTH - 25):
            return True
        return False
