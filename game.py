from config import *

class Game:
    def __init__(self):
        # Superfície principal
        self.surface = pygame.Surface((LARGURA_JOGO, ALTURA_JOGO))

        # Superfície secundária
        self.display_surface = pygame.display.get_surface()

    def run(self):
        # O blit coloca um painel dentro de um outro
        self.display_surface.blit(self.surface, (PADDING, PADDING))


