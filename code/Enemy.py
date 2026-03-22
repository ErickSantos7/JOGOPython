import pygame
import random

class Enemy:
    def __init__(self, width, height):
        self.image = pygame.image.load('./assets/busto.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.rect = self.image.get_rect()
        self.rect.x = width
        self.rect.y = random.randint(100, 300)

        self.speed = random.randint(3, 7)

    def update(self):
        self.rect.x -= self.speed

    def draw(self, window):
        window.blit(self.image, self.rect)