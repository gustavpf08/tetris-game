from config import *
import random

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
        
        # Agrupando os blocos
        self.sprites = pygame.sprite.Group()
        
        # Randomizando os shapes
        diff_shapes = list(FORMAS.keys())
        chave_aleatoria = random.choice(diff_shapes)
    
        # Blocos do Tetris
        self.bloco_tetris = Formatos(chave_aleatoria, self.sprites) 


    def draw_grid(self):
        # Grid na Vertical
        for col in range(1, COLUNAS):
            x = col * TAM_CELULA
            pygame.draw.line(self.surface, BRANCO, (x, 0), (x,self.surface.get_height()), 1)
        
        # Grid na Horizontal 
        for lin in range(1, LINHAS):
            y = lin * TAM_CELULA
            pygame.draw.line(self.surface, BRANCO, (0, y), (self.surface.get_height(), y), 1)
 

    def run(self):
        self.display_surface.blit(self.surface, (PADDING, PADDING))
        self.sprites.draw(self.surface)
        self.draw_grid()
        pygame.draw.rect(self.display_surface, BRANCO, self.rect, 1, 1)


class Formatos:
    def __init__(self, forma, group):
        self.posicoes_bloco = FORMAS[forma]['shape'] 
        self.color = FORMAS[forma]['color'] 

        self.blocks = [Block(group, pos, self.color) for pos in self.posicoes_bloco]


# Criando um sprite e colocando ele dentro de um grupo de sprites
class Block(pygame.sprite.Sprite):
    def __init__(self, group, pos, color):
        super().__init__(group)
        self.image = pygame.Surface((TAM_CELULA, TAM_CELULA))
        self.image.fill(color)

        # Posição do Bloco
        self.pos = pygame.Vector2(pos) + pygame.Vector2(3,5)
        x = self.pos.x * TAM_CELULA
        y = self.pos.y * TAM_CELULA
        self.rect = self.image.get_rect(topleft = (x, y))


