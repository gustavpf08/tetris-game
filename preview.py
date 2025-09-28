from config import *
from pygame.image import load
from os import path

class Preview:
    def __init__(self):
        self.surface = pygame.Surface((SIDEBAR_LARG, ALTURA_PREVIEW * ALTURA_JOGO - PADDING))
        self.display_surface = pygame.display.get_surface()
        self.rect = self.surface.get_rect(topright = (LARG_JANELA - PADDING, PADDING))
        
        # Formatos
        self.superf_formato = {forma: load(path.join('.','assets',f'{forma}.png')).convert_alpha() for forma in FORMAS.keys()}

        # Centralizando as imagens na tela
        self.incremento_altura = self.surface.get_height() / 3


    def display_pecas(self, formas):
        for i, forma in enumerate(formas):
            forma_surface = self.superf_formato[forma]

            x = self.surface.get_width() / 2
            y = self.incremento_altura / 2 + i * self.incremento_altura

            rect = forma_surface.get_rect(center = (x,y))
            self.surface.blit(forma_surface, rect)

    def run(self, prox_formatos):
        self.surface.fill(CINZA)
        self.display_pecas(prox_formatos)
        self.display_surface.blit(self.surface, (PADDING + LARGURA_JOGO + PADDING, PADDING))
        pygame.draw.rect(self.display_surface, BRANCO, self.rect, 1, 1)

