from config import *

class Preview:
    def __init__(self, prox_formato):
        self.surface = pygame.Surface((SIDEBAR_LARG, ALTURA_PREVIEW * ALTURA_JOGO - PADDING))
        self.display_surface = pygame.display.get_surface()
        
        # Formatos
        self.prox_formato = prox_formato

    def run(self):
        self.display_surface.blit(self.surface, (PADDING + LARGURA_JOGO + PADDING, PADDING))

