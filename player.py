import pygame

class Player():
    
    def __init__(self, screen, x, y, w, h) -> None:
        self.player_rect = pygame.Rect(x, y, w, h)
        self.screen = screen
        
    def draw_player(self, x, y):
        pygame.draw.rect(self.screen, (255, 255, 0), (self.player_rect.x, self.player_rect.y,
                                                      self.player_rect.w, self.player_rect.h))
        
    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_w] and self.player_rect.x > 0:
            self.player_rect.y -= 5
        
        if key[pygame.K_s] and self.player_rect.y < 580:
            self.player_rect.y += 5

        if key[pygame.K_a] and self.player_rect.x > 0:
            self.player_rect.x -= 5

        if key[pygame.K_d] and self.player_rect.x < 780:
            self.player_rect.x += 5