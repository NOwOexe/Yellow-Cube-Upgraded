import pygame
import random
from player import *

class Game():
    
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Yellow Cube")
        self.screen = pygame.display.set_mode((800, 600))
        self.player = pygame.Rect(400, 300, 20, 20)
        self.player = Player(self.player, self.screen)
        self.enemy = pygame.Rect(random.randint(0, 800), 0, 20, 20)
        self.background = pygame.image.load("image.png")
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
            self.enemy.draw_enemy(random.randint(0, 800), 0)
            self.player.move()
                
            pygame.display.update()
            
        pygame.quit()
        
if __name__ == "__main__":
    game = Game()
    game.run()