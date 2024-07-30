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
        
    def run(self):
        run = True
        while run:
            
            pygame.time.delay(20)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    
            self.screen.blit(self.background, (0, 0))
            self.player.draw_player(400, 300)
            self.player.move()
                
            pygame.display.update()
            
        pygame.quit()
        
if __name__ == "__main__":
    game = Game()
    game.run()