from config import *
from os.path import join

class Score:
    def __init__(self):
        self.surface = pygame.Surface((SIDEBAR_LARG, ALTURA_JOGO * SCORE_PREVIEW))
        self.display_surface = pygame.display.get_surface()
        self.rect = self.surface.get_rect(bottomright = (LARG_JANELA - PADDING, ALT_JANELA - PADDING))

        # font
        self.font = pygame.font.Font(join('.','assets','Russo_One.ttf'), 30)

        # incremento
        self.incremento_altura = self.surface.get_height() / 3

        self.score = 0
        self.level = 1
        self.linhas = 0


    def display_texto(self, pos, texto):
        surface_texto = self.font.render(f'{texto[0]}: {texto[1]}', True, 'white')
        texto_rect = surface_texto.get_rect(center = pos)
        self.surface.blit(surface_texto, texto_rect)


    def run(self, ):
        self.surface.fill(CINZA)

        for i, texto in enumerate([('Score', self.score), ('Level', self.level), ('Linhas', self.linhas)]):
            x = self.surface.get_width() / 2
            y = self.incremento_altura / 2 + i * self.incremento_altura

            self.display_texto((x,y), texto)

        self.display_surface.blit(self.surface, (PADDING + LARGURA_JOGO + PADDING, ALTURA_JOGO - (SCORE_PREVIEW * ALTURA_JOGO) + PADDING))
        pygame.draw.rect(self.display_surface, BRANCO, self.rect, 1, 1)
