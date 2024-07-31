import pygame

class Player():
    
    def __init__(self, screen, x, y, w, h) -> None:
        self.player_rect = pygame.Rect(x, y, w, h)
        self.screen = screen
        self.velocity = 260
        
    def draw_player(self, x, y):
        pygame.draw.rect(self.screen, (255, 255, 0), (self.player_rect.x, self.player_rect.y,
                                                      self.player_rect.w, self.player_rect.h))
        
    def move(self, delta_time):
        key = pygame.key.get_pressed()
        if key[pygame.K_w] and self.player_rect.y >= 2:
            self.player_rect.y -= self.velocity * delta_time
        
        if key[pygame.K_s] and self.player_rect.y < 575:
            self.player_rect.y += self.velocity * delta_time

        if key[pygame.K_a] and self.player_rect.x > 2:
            self.player_rect.x -= self.velocity * delta_time

        if key[pygame.K_d] and self.player_rect.x < 775:
            self.player_rect.x += self.velocity * delta_time