import pygame
import random
from player import *
from enemy import *

class Game():
    
    def __init__(self) -> None:
        #Setup
        pygame.init()
        pygame.display.set_caption("Yellow Cube")
        self.screen = pygame.display.set_mode((800, 600))

        #Icon
        self.icon = pygame.image.load("icon.png")
        pygame.display.set_icon(self.icon)
        self.font = pygame.font.Font("SuperPixel-m2L8j.ttf", 20)

        #Player
        self.is_start = False
        player_w, player_h = 20, 20
        self.player = Player(self.screen, (self.screen.get_width() - player_w) // 2, (self.screen.get_height() - player_h) // 2,
                                player_w, player_h)
        
        #Enemy
        self.enemy_h, self.enemy_w = 20, 20
        self.enemy_list = []
        random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        for i in range(2):
            self.enemy_list.append(Enemy(self.screen, -self.enemy_w, random.randint(0, random.randint(0, (self.screen.get_height() - self.enemy_h))),
                                         self.enemy_w, self.enemy_h, random_color, random.randint(200, 400)))
        for i in range(2):
            self.enemy_list.append(Enemy(self.screen, self.screen.get_width() + self.enemy_w, random.randint(0, random.randint(0, (self.screen.get_height() - self.enemy_h))),
                                         self.enemy_w, self.enemy_h, random_color, random.randint(200, 400)))

        #Background
        self.background = pygame.image.load("background.png").convert_alpha()
        self.background = pygame.transform.scale(self.background, (800, 600))

        self.clock = pygame.time.Clock()

        self.score = 0
        
    def start_menu(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            self.is_start = True
        
        self.screen.fill((0, 0, 0))
        draw_text = self.font.render(f"Yellow Cube", True, (255, 255, 0))
        draw_text2 = self.font.render(f"Press Spacebar To Continue.", True, (255, 255, 255))
        text_w, text_h = draw_text.get_width(), draw_text.get_height() + 150
        text2_w, text2_h = draw_text2.get_width(), draw_text2.get_height()
        self.screen.blit(draw_text, ((self.screen.get_width() - text_w) // 2, (self.screen.get_height() - text_h) // 2))
        self.screen.blit(draw_text2, ((self.screen.get_width() - text2_w) // 2, (self.screen.get_height() - text2_h) // 2))
                
    def run(self):
        run = True
        while run:
            
            delta_time = self.clock.tick(60) / 1000
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            if not self.is_start:
                self.start_menu()
            else:
                self.screen.blit(self.background, (0, 0))
                self.player.draw_player()
                self.player.move(delta_time)
                self.draw_text = self.font.render(f"Score: {self.score}", True, (255, 255, 0))
                self.screen.blit(self.draw_text, (20, 20))
                
                for enemy in self.enemy_list:
                    if enemy.enemy_rect.x >= self.screen.get_width() and enemy.move_right:
                        random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                        self.enemy_list.remove(enemy)
                        self.enemy_list.append(Enemy(self.screen, -self.enemy_w, random.randint(0, self.screen.get_height() - enemy.enemy_rect.h),
                                                      self.enemy_w, self.enemy_h, random_color, random.randint(200, 400)))
                        
                    if enemy.enemy_rect.x < 0 and enemy.move_left:
                        random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                        self.enemy_list.remove(enemy)
                        self.enemy_list.append(Enemy(self.screen, self.screen.get_width() + self.enemy_w, random.randint(0, self.screen.get_height() - enemy.enemy_rect.h),
                                                      self.enemy_w, self.enemy_h, random_color, random.randint(200, 400)))
                    enemy.draw()
                    enemy.move(delta_time)
            
            pygame.display.update()
        
    def enemy_pos(self):
        total_enemy = 5
        enemy_w = 50
        enemy_h = 50
        y_pos = 0
        lst = []
        
        for i in range(total_enemy):
            random_x = random.randint(0, 1)
            if random_x == 0:
                x_pos = -enemy_w - random.randint(0, 400)
            elif random_x == 1:
                x_pos = self.screen.get_width() + enemy_w + random.randint(0, 400)
            lst.append(Enemy(self.screen, x_pos, y_pos + (enemy_h + 5) * i, enemy_w, enemy_h))
            
        return lst
        
if __name__ == "__main__":
    game = Game()
    game.run()