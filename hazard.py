import pygame

spike_img = pygame.image.load('images/spike80.png')
spike_img_2 = pygame.image.load('images/spike80_2.png')
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
floor = DISPLAY_HEIGHT * 0.6
ceiling = DISPLAY_HEIGHT * 0.3
SPIKE_HEIGHT = 80
SPIKE_WIDTH = 80
PLAYER_SIZE = 25

class Hazard:
    def __init__(self, x, orientation):
        self.__left_x = x
        self.__right_x = self.__left_x + SPIKE_WIDTH
        self.__tip_x = self.__left_x + (SPIKE_WIDTH / 2)
        self.__orientation = orientation
        
        if orientation == 0:
            self.__left_y = floor
            self.__right_y = self.__left_y
            self.__tip_y = self.__left_y - SPIKE_HEIGHT
        else:
            self.__left_y = ceiling
            self.__right_y = self.__left_y
            self.__tip_y = self.__left_y + SPIKE_HEIGHT            
        
    def get_left_x(self):
        return self.__left_x
    
    def get_left_y(self):
        return self.__left_y

    def get_right_x(self):
        return self.__right_x
    
    def get_right_y(self):
        return self.__right_y

    def get_tip_x(self):
        return self.__tip_x
    
    def get_tip_y(self):
        return self.__tip_y    
        
    def draw(self, display):
        if self.__orientation == 0:
            display.blit(spike_img, (self.__left_x, self.__tip_y))
        else:
            display.blit(spike_img_2, (self.__left_x, self.__left_y))
        
    def overlap(self, player):
        player_x = player.get_x()
        player_y = player.get_y()
        player_end_x = player_x + PLAYER_SIZE
        player_bot_y = player_y + PLAYER_SIZE
        
        if self.__orientation == 0:
            # Check if both front and end of player overlaps hazard
            if self.is_overlap(player_x) and self.is_overlap(player_end_x):
                for p in range(player_x, player_end_x + 1):
                    if self.spike_height(p) <= player_bot_y:
                        return True
            # Check if front of player overlaps hazard
            elif self.is_overlap(player_x):
                for p in range(player_x, self.__right_x + 1):
                    if self.spike_height(p) <= player_bot_y:
                        return True
            # Check if end of player overlaps hazard
            elif self.is_overlap(player_end_x):
                for p in range(self.__left_x, player_end_x + 1):
                    if self.spike_height(p) <= player_bot_y:
                        return True
            return False
        else:
            # Check if both front and end of player overlaps hazard
            if self.is_overlap(player_x) and self.is_overlap(player_end_x):
                for p in range(player_x, player_end_x + 1):
                    if self.spike_height(p) >= player_y:
                        return True
            # Check if front of player overlaps hazard
            elif self.is_overlap(player_x):
                for p in range(player_x, self.__right_x + 1):
                    if self.spike_height(p) >= player_y:
                        return True
            # Check if end of player overlaps hazard
            elif self.is_overlap(player_end_x):
                for p in range(self.__left_x, player_end_x + 1):
                    if self.spike_height(p) >= player_y:
                        return True
            return False            

    def is_overlap(self, x):
        if x >= self.__left_x and x <= self.__right_x:
            return True
        return False
    
    def spike_height(self, x):
        if self.__orientation == 0:
            return abs(2*(x - SPIKE_WIDTH / 2 - self.__left_x)) + self.__tip_y
        else:
            return -abs(2*(x - SPIKE_WIDTH / 2 - self.__left_x)) + \
                   SPIKE_HEIGHT + self.__left_y
