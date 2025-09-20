from config import *

class Score:
    def __init__(self):
        # Superfície principal
        self.surface = pygame.Surface((SIDEBAR_LARG, ALTURA_JOGO * SCORE_PREVIEW))
        # Superfície secundária
        self.display_surface = pygame.display.get_surface()

    def run(self):
        # Colocando um painel sobre o outro
        self.display_surface.blit(self.surface, (PADDING + LARGURA_JOGO + PADDING, ALTURA_JOGO - (SCORE_PREVIEW * ALTURA_JOGO) + PADDING))
