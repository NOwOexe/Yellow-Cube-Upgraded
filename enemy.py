import pygame
import random

class Enemy():
    
    def __init__(self, screen, x, y, w, h) -> None:
        self.screen = screen
        self.enemy_rect = pygame.Rect(x, y, w, h)
        self.velocity = 100
        self.move_right = False
        self.move_left = False
        self.direction()
        
    def draw(self):
        r_channel = random.randint(0, 255)
        g_channel = random.randint(0, 255)
        b_channel = random.randint(0, 255)
        
        pygame.draw.rect(self.screen, (r_channel, b_channel, g_channel), (self.enemy_rect.x, self.enemy_rect.y,
                                                                          self.enemy_rect.x, self.enemy_rect.h))
        
    def direction(self):
        if self.enemy_rect.x < self.screen.get_width():
            self.move_right = True
        elif self.enemy_rect.x > self.screen.get_width():
            self.move_left = True
    
    def move(self, delta_time):
        if self.move_right:
            self.enemy_rect.x += self.velocity * delta_time
        if self.move_left:
            self.enemy_rect.x -= self.velocity * delta_time
            
    def set_left(self, new_move):
        self.move_left = new_move
        
    def set_right(self, new_move):
        self.move_right = new_move