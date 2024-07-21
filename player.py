import pygame

class Player():
    
    def __init__(self, player, screen) -> None:
        self.player = player
        self.screen = screen
        
    def draw_player(self, x, y):
        pygame.draw.rect(self.screen, (255, 255, 0), self.player)
        
    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_w] and self.player.y > 0:
            self.player.y -= 5
        
        if key[pygame.K_s] and self.player.y < 580:
            self.player.y += 5

        if key[pygame.K_a] and self.player.x > 0:
            self.player.x -= 5

        if key[pygame.K_d] and self.player.x < 780:
            self.player.x += 5