import pygame

class Game():
    
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Yellow Cube")
        self.screen = pygame.display.set_mode((800, 600))
        self.player = self.player = pygame.Rect(400, 300, 20, 20)
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
            pygame.draw.rect(self.screen, (255, 255, 0), self.player)
            
            key = pygame.key.get_pressed()
            if key[pygame.K_w] and self.player.y > 0:
                self.player.y -= 5
            
            if key[pygame.K_s] and self.player.y < 580:
                self.player.y += 5

            if key[pygame.K_a] and self.player.x > 0:
                self.player.x -= 5

            if key[pygame.K_d] and self.player.x < 780:
                self.player.x += 5
                
            pygame.display.update()
            
        pygame.quit()
        
if __name__ == "__main__":
    game = Game()
    game.run()