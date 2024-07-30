import pygame
import random

class Enemy():
    
    def __init__(self, enemy, screen) -> None:
        self.enemy = enemy
        self.screen = screen
        
    def draw_enemy(self, x, y):
        pygame.draw.rect(self.screen, (255, 0, 0), self.enemy)
        
    def pos_check(self):
        if self.enemy.x <= 0:
            self.enemy.x = 800
        if self.enemy.x >= 800:
            self.enemy.x = 0
        if self.enemy.y <= 0:
            self.enemy.y = 600
        if self.enemy.y >= 600:
            self.enemy.y = 0