import pygame

hazard_img = pygame.image.load('images/spike80.png')
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
floor = DISPLAY_HEIGHT * 0.6
ceiling = DISPLAY_HEIGHT * 0.3
SPIKE_HEIGHT = 80
SPIKE_WIDTH = 80
PLAYER_SIZE = 25

class Hazard:
    def __init__(self):
        self.__left_x = 50
        self.__left_y = floor
        self.__right_x = self.__left_x + SPIKE_WIDTH
        self.__right_y = self.__left_y
        self.__top_x = self.__left_x + (SPIKE_WIDTH / 2)
        self.__top_y = self.__left_y - SPIKE_HEIGHT
        
    def get_left_x(self):
        return self.__left_x
    
    def get_left_y(self):
        return self.__left_y

    def get_right_x(self):
        return self.__right_x
    
    def get_right_y(self):
        return self.__right_y

    def get_top_x(self):
        return self.__top_x
    
    def get_top_y(self):
        return self.__top_y    
        
    def draw(self, display):
        #display.blit(hazard_img, (50, floor - SPIKE_HEIGHT))
        display.blit(hazard_img, (self.__left_x, self.__top_y))
        
    def overlap(self, player):
        player_x = player.get_x()
        player_y = player.get_y()
        player_end_x = player_x + PLAYER_SIZE
        player_bot_y = player_y + PLAYER_SIZE

        # Check if both front and end of player overlaps hazard
        if self.is_overlap(player_x) and self.is_overlap(player_end_x):
            for p in range(player_x, player_end_x + 1):
                if self.spike_height(p) <= player_bot_y:
                    print(str(player_bot_y) + " hit " + str(self.spike_height(p)) + " at " + str(p))
                    return True
        # Check if front of player overlaps hazard
        elif self.is_overlap(player_x):
            for p in range(player_x, self.__right_x + 1):
                if self.spike_height(p) <= player_bot_y:
                    print(str(player_bot_y) + " hit " + str(self.spike_height(p)) + " at " + str(p))
                    return True
        # Check if end of player overlaps hazard
        elif self.is_overlap(player_end_x):
            for p in range(self.__left_x, player_end_x + 1):
                if self.spike_height(p) <= player_bot_y:
                    print(str(player_bot_y) + " hit " + str(self.spike_height(p)) + " at " + str(p))
                    return True
        return False

    def is_overlap(self, x):
        if (x >= self.__left_x) and (x <= self.__right_x):
            return True
        return False
    
    def spike_height(self, x):
        return abs(2*(x - 40 - self.__left_x)) + self.__top_y
