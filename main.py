import pygame
from player import *

class Game():
    
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Yellow Cube")
        self.screen = pygame.display.set_mode((800, 600))
        player_w, player_h = 20, 20
        self.player = Player(self.screen, (self.screen.get_width() - player_w) // 2, (self.screen.get_height() - player_h) // 2,
                                player_w, player_h)
        self.background = pygame.image.load("background.png").convert_alpha()
        self.background = pygame.transform.scale(self.background, (800, 600))
        self.clock = pygame.time.Clock()
        self.score = 0
        self.icon = pygame.image.load("icon.png")
        pygame.display.set_icon(self.icon)
        self.font = pygame.font.Font("SuperPixel-m2L8j.ttf", 20)
        
    def start_menu(self):
        
        run = True
        while run:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
                run = False
                game.run()
            
            self.screen.fill((0, 0, 0))
            draw_text = self.font.render(f"Yellow Cube", True, (255, 255, 0))
            draw_text2 = self.font.render(f"Press Spacebar To Continue.", True, (255, 255, 0))
            text_w, text_h = draw_text.get_width(), draw_text.get_height() + 150
            text2_w, text2_h = draw_text2.get_width(), draw_text2.get_height()
            self.screen.blit(draw_text, ((self.screen.get_width() - text_w) // 2, (self.screen.get_height() - text_h) // 2))
            self.screen.blit(draw_text2, ((self.screen.get_width() - text2_w) // 2, (self.screen.get_height() - text2_h) // 2))
                
            pygame.display.update()
        
        pygame.quit()
        
    def run(self):
        run = True
        while run:
            
            delta_time = self.clock.tick(60) / 1000
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    
            self.screen.blit(self.background, (0, 0))
            self.player.draw_player(400, 300)
            self.player.move(delta_time)
            self.draw_text = self.font.render(f"Score: {self.score}", True, (255, 255, 0))
            self.screen.blit(self.draw_text, (20, 20))
            
            pygame.display.update()
            
        pygame.quit()
        
if __name__ == "__main__":
    game = Game()
    game.start_menu()