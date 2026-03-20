from tkinter.font import Font

import pygame
import pygame.image
from pygame import Rect
from pygame import Surface
from pygame.examples.grid import WINDOW_WIDTH

from code.Const import WIN_WIDTH, OPCAO_JOGO


class Menu:
    def __init__(self,window):
        self.window = window
        self.surf = pygame.image.load('./assets/menu.png')
        self.rect = self.surf.get_rect(left=0, top=0)



    def run(self, ):
        pygame.mixer_music.load('./assets/menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)

            self.menu_text(60,"Cosmic",(0,0,0), ((WIN_WIDTH/2), 52))
            self.menu_text(70,"WAR",(255,0,0), ((WIN_WIDTH/2), 120))

            for i in range(len(OPCAO_JOGO)):
                self.menu_text(20, OPCAO_JOGO[i], (255, 255, 255), ((WIN_WIDTH / 2), 190 +20 * i))


            pygame.display.flip()



            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple) -> None:
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf : Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
