import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT,OPCAO_JOGO
from code.Level import Level
from code.Menu import Menu

class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == OPCAO_JOGO[0]:
                level = Level(self.window,'Level1', menu_return)
                level_return = level.run()
            elif menu_return == OPCAO_JOGO[2]:
                pygame.quit()
                quit()

            else:
                pass





