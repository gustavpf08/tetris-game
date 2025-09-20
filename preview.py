from config import *

class Preview:
    def __init__(self):
        self.surface = pygame.Surface((SIDEBAR_LARG, ALTURA_PREVIEW * ALTURA_JOGO - PADDING))
        self.display_surface = pygame.display.get_surface()

    def run(self):
        self.display_surface.blit(self.surface, (PADDING + LARGURA_JOGO + PADDING, PADDING))

