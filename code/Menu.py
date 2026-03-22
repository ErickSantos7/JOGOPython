from tkinter.font import Font
from code.Player import Player
import pygame
import pygame.image
from pygame import Rect
from pygame import Surface

from code.Const import WIN_WIDTH, OPCAO_JOGO, menu_jogo, CONTROLES
from utils import resource_path


class Menu:
    def __init__(self,window):
        self.window = window
        self.surf = pygame.image.load(resource_path('assets/menu.png'))
        self.rect = self.surf.get_rect(left=0, top=0)



    def run(self, ):
        menu_jogo = 0
        pygame.mixer_music.load(resource_path('assets/menu.mp3'))
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)

            self.menu_text(60,"Cosmic",(0,0,0), ((WIN_WIDTH/2 - 50), 52))
            self.menu_text(70,"WAR",(255,0,0), ((WIN_WIDTH/2 - 50), 120))

            for i in range(len(OPCAO_JOGO)):
                if i == menu_jogo:
                    self.menu_text(20,OPCAO_JOGO[i],(0,0,0),((WIN_WIDTH/2 ),190 +20 * i))
                else:
                    self.menu_text(20, OPCAO_JOGO[i], (255, 255, 255), ((WIN_WIDTH / 2 ), 190 +20 * i))

            for i in range(len(CONTROLES)):
                self.menu_text(20,CONTROLES[i],(0,0,0),((WIN_WIDTH/ 5 -100 ),170 + 25 * i))
                self.menu_text(20, CONTROLES[i], (0, 0, 0), ((WIN_WIDTH / 5 -100), 170 + 25 *i ))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN: #TECLA PARA BAIXO
                        if menu_jogo < len(OPCAO_JOGO) - 1 :
                            menu_jogo += 1
                        else:
                            menu_jogo = 0

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP: # TECLA PARA CIMA
                            if menu_jogo > 0:
                                menu_jogo -= 1
                            else:
                             menu_jogo = len(OPCAO_JOGO) -1

                    if event.key == pygame.K_RETURN:
                        return OPCAO_JOGO[menu_jogo]
                    if event.key == pygame.K_RETURN:
                        return OPCAO_JOGO[0]


    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple) -> None:
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf : Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(midleft=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
