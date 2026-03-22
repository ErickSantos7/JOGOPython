from code.Player import Player
from code.Enemy import Enemy
import pygame
import pygame.image

from utils import resource_path


class Level:
    def __init__(self, window, name, option):
        self.window = window
        self.player = Player()

        self.enemies = []
        self.spawn_timer = 0
        self.score = 0

        self.font = pygame.font.SysFont(None, 30)


        self.game_duration = 30
        self.start_time = pygame.time.get_ticks()


        self.bg1 = pygame.image.load(resource_path('assets/level1bg1.png')).convert_alpha()
        self.bg2 = pygame.image.load(resource_path('assets/level1bg2.png')).convert_alpha()
        self.bg3 = pygame.image.load(resource_path('assets/level1bg3.png')).convert_alpha()
        self.bg4 = pygame.image.load(resource_path('assets/level1bg4.png')).convert_alpha()

        self.bg1_x = 0
        self.bg2_x = 0
        self.bg3_x = 0
        self.bg4_x = 0


    def reset_game(self):
        self.enemies.clear()
        self.score = 0
        self.start_time = pygame.time.get_ticks()
        self.player.rect.x = 100
        self.player.rect.y = 200

    def run(self):
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)


            current_time = pygame.time.get_ticks()
            elapsed_time = (current_time - self.start_time) / 1000
            remaining_time = max(0, int(self.game_duration - elapsed_time))


            if remaining_time <= 0:
                return


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
                    if event.key == pygame.K_SPACE:
                        self.player.attack_action()

            self.player.update_attack()


            self.spawn_timer += 1
            if self.spawn_timer > 60:
                self.enemies.append(
                    Enemy(self.window.get_width(), self.window.get_height())
                )
                self.spawn_timer = 0


            for enemy in self.enemies[:]:
                enemy.update()

                if self.player.attack and self.player.get_hitbox().colliderect(enemy.rect):
                    self.enemies.remove(enemy)
                    self.score += 10

                elif enemy.rect.x < 0:
                    self.enemies.remove(enemy)


            self.window.fill((0, 0, 0))


            self.bg1_x -= 0.5
            self.bg2_x -= 2
            self.bg3_x -= 3
            self.bg4_x -= 4

            if self.bg1_x <= -self.bg1.get_width():
                self.bg1_x = 0
            if self.bg2_x <= -self.bg2.get_width():
                self.bg2_x = 0
            if self.bg3_x <= -self.bg3.get_width():
                self.bg3_x = 0
            if self.bg4_x <= -self.bg4.get_width():
                self.bg4_x = 0

            self.window.blit(self.bg1, (self.bg1_x, 0))
            self.window.blit(self.bg1, (self.bg1_x + self.bg1.get_width(), 0))

            self.window.blit(self.bg2, (self.bg2_x, 0))
            self.window.blit(self.bg2, (self.bg2_x + self.bg2.get_width(), 0))

            self.window.blit(self.bg3, (self.bg3_x, 0))
            self.window.blit(self.bg3, (self.bg3_x + self.bg3.get_width(), 0))

            self.window.blit(self.bg4, (self.bg4_x, 0))
            self.window.blit(self.bg4, (self.bg4_x + self.bg4.get_width(), 0))


            for enemy in self.enemies:
                enemy.draw(self.window)


            self.player.run()
            self.player.limit(self.window.get_width(), self.window.get_height())
            self.player.update_attack()
            self.player.draw(self.window)


            score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
            self.window.blit(score_text, (10, 10))


            time_text = self.font.render(f"Time: {remaining_time}s", True, (255, 255, 0))
            self.window.blit(time_text, (10, 40))

            pygame.display.flip()