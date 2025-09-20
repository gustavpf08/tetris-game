from config import *

class Game:
    def __init__(self):
        self.surface = pygame.Surface((LARGURA_JOGO, ALTURA_JOGO))
        self.display_surface = pygame.display.get_surface()
        
        # Pegando o retângulo maior para desenhar seu perímetro
        self.rect = self.surface.get_rect(topleft = (PADDING, PADDING))

        # Retirando a cor do fundo preto, definindo uma cor e escondendo ela
        self.surface.fill((1, 0, 0))
        self.surface.set_colorkey((1, 0, 0))

        # Alterando a transparência do game
        self.surface.set_alpha(120)


    def draw_grid(self):
        # Grid na Vertical
        for col in range(1, COLUNAS):
            x = col * TAM_CELULA
            pygame.draw.line(self.surface, WHITE, (x, 0), (x,self.surface.get_height()), 1)
        
        # Grid na Horizontal 
        for lin in range(1, LINHAS):
            y = lin * TAM_CELULA
            pygame.draw.line(self.surface, WHITE, (0, y), (self.surface.get_height(), y), 1)
 

    def run(self):
        # O blit coloca um painel dentro de um outro
        self.display_surface.blit(self.surface, (PADDING, PADDING))
        self.draw_grid()
        pygame.draw.rect(self.display_surface, WHITE, self.rect, 1, 1)


