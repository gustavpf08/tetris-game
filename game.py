from config import *
import random

from timer import Timer

class Game:
    def __init__(self):
        self.surface = pygame.Surface((LARGURA_JOGO, ALTURA_JOGO))
        self.display_surface = pygame.display.get_surface()
        self.rect = self.surface.get_rect(topleft = (PADDING, PADDING))

        # Agrupando os blocos
        self.sprites = pygame.sprite.Group()

        # Retirando a cor do fundo preto, definindo uma cor e escondendo ela
        self.surface.fill((1, 0, 0))
        self.surface.set_colorkey((1, 0, 0))

        # Alterando a transparência do game
        self.surface.set_alpha(120)
        
        # Blocos do Tetris
        self.bloco_tetris = Formatos(random.choice(list(FORMAS.keys())), self.sprites) 

        # Timer:
        self.timers = {
            'movimento_vertical': Timer(VELOCIDADE_INICIO, True, self.move_para_baixo),
        'movimento_horizontal': Timer(TEMPO_DE_MOVER)
        }
        self.timers['movimento_vertical'].ativar()



    def timer_update(self):
        for timer in self.timers.values():
            timer.update()


    def move_para_baixo(self):
        self.bloco_tetris.move_para_baixo()


    def draw_grid(self):
        # Grid na Vertical
        for col in range(1, COLUNAS):
            x = col * TAM_CELULA
            pygame.draw.line(self.surface, BRANCO, (x, 0), (x,self.surface.get_height()), 1)
        
        # Grid na Horizontal 
        for lin in range(1, LINHAS):
            y = lin * TAM_CELULA
            pygame.draw.line(self.surface, BRANCO, (0, y), (self.surface.get_height(), y), 1)
 

    def input(self):
        chaves = pygame.key.get_pressed()
        
        if not self.timers['movimento_horizontal'].ativo:
            if chaves[pygame.K_d]:
                self.bloco_tetris.move_horizontal(1)
                self.timers['movimento_horizontal'].ativar()

            if chaves[pygame.K_a]:
                self.bloco_tetris.move_horizontal(-1)
                self.timers['movimento_horizontal'].ativar()


    def run(self):
        self.input()
        self.timer_update()
        self.sprites.update()
        
        self.surface.fill(CINZA)
        self.sprites.draw(self.surface)
        self.draw_grid()

        self.display_surface.blit(self.surface, (PADDING, PADDING))
        pygame.draw.rect(self.display_surface, BRANCO, self.rect, 1, 1)


class Formatos:
    def __init__(self, forma, group):
        self.posicoes_bloco = FORMAS[forma]['shape'] 
        self.color = FORMAS[forma]['color'] 

        self.blocks = [Block(group, pos, self.color) for pos in self.posicoes_bloco]


    def move_para_baixo(self):
        if not self.prox_colisao_vertical_movi(self.blocks, 1):
            for block in self.blocks:
                block.pos.y += 1


    def move_horizontal(self, qntd):
        if not self.prox_colisao_horizontal_movi(self.blocks, qntd):
            for block in self.blocks:
                block.pos.x += qntd


    # Colisões
    def prox_colisao_horizontal_movi(self, blocks, qntd):
        colisoes_horizontais = [block.colisao_horizontal(int(block.pos.x + qntd)) for block in self.blocks]

        if True in colisoes_horizontais:
            return True
        else: 
            return False

    def prox_colisao_vertical_movi(self, blocks, qntd):
        colisoes_verticais = [block.colisao_vertical(int(block.pos.y + qntd)) for block in self.blocks]

        if True in colisoes_verticais:
            return True
        else:
            return False
    

# Criando um sprite e colocando ele dentro de um grupo de sprites
class Block(pygame.sprite.Sprite):
    def __init__(self, group, pos, color):
        super().__init__(group)
        self.image = pygame.Surface((TAM_CELULA, TAM_CELULA))
        self.image.fill(color)

        # Posição do Bloco
        self.pos = pygame.Vector2(pos) + INICIO_BLOCO
        x = self.pos.x * TAM_CELULA
        y = self.pos.y * TAM_CELULA
        self.rect = self.image.get_rect(topleft = (x, y))


    def colisao_horizontal(self, x):
        if not 0 <= x < COLUNAS:
            return True


    def colisao_vertical(self, y):
        if y >= LINHAS:
            return True


    def update(self):
        x = self.pos.x * TAM_CELULA
        y = self.pos.y * TAM_CELULA
        self.rect = self.image.get_rect(topleft = (x, y))


