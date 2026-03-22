import pygame

class Player:
    def __init__(self):
        self.rect = pygame.Rect(100, 200, 100, 100)
        self.speed = 5


        self.sprite_sheet = pygame.image.load('./assets/player.png').convert_alpha()

        self.frame_width = 128
        self.frame_height = 128

        self.frames = []
        for i in range(4):
            frame = self.sprite_sheet.subsurface(
                (i * self.frame_width, 0, self.frame_width, self.frame_height)
            )
            frame = pygame.transform.scale(frame, (100, 100))
            self.frames.append(frame)

        self.frame_index = 0


        self.attack = False
        self.attack_timer = 0


    def run(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed


    def limit(self, width, height):
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > width:
            self.rect.right = width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > height:
            self.rect.bottom = height


    def attack_action(self):
        if not self.attack:  # evita spam bugado
            self.attack = True
            self.attack_timer = 12
            self.frame_index = 0  # reinicia animação


    def update_attack(self):
        if self.attack:
            self.frame_index += 0.5

            if self.frame_index >= len(self.frames):
                self.frame_index = 0

            self.attack_timer -= 1

            if self.attack_timer <= 0:
                self.attack = False
                self.frame_index = 0


    def get_hitbox(self):
        if self.attack:
            return pygame.Rect(
                self.rect.x + 70,  # frente do player
                self.rect.y + 20,
                60,
                60
            )
        else:
            return pygame.Rect(0, 0, 0, 0)  # sem ataque = sem hitbox


    def draw(self, window):
        window.blit(self.frames[int(self.frame_index)], self.rect)

