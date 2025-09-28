from config import *
import random

from timer import Timer

class Game:
    def __init__(self, pegando_prox_forma):
        self.surface = pygame.Surface((LARGURA_JOGO, ALTURA_JOGO))
        self.display_surface = pygame.display.get_surface()
        self.rect = self.surface.get_rect(topleft = (PADDING, PADDING))

        self.pegando_prox_forma = pegando_prox_forma
        print(pegando_prox_forma)

        # Agrupando os blocos
        self.sprites = pygame.sprite.Group()

        # Retirando a cor do fundo preto, definindo uma cor e escondendo ela
        self.surface.fill((1, 0, 0))
        self.surface.set_colorkey((1, 0, 0))

        # Alterando a transparência do game
        self.surface.set_alpha(250)
        
        # Blocos do Tetris
        self.area_ocupada = [[0 for x in range(COLUNAS)] for y in range(LINHAS)]
        self.bloco_tetris = Formatos(random.choice(list(FORMAS.keys())), self.sprites, self.criando_novo_bloco, self.area_ocupada) 

        # Timer:
        self.timers = {
            'movimento_vertical': Timer(VELOCIDADE_INICIO, True, self.move_para_baixo),
            'movimento_horizontal': Timer(TEMPO_DE_MOVER),
            'rotacao': Timer(TEMPO_ROTACAO),
        }
        self.timers['movimento_vertical'].ativar()

    
    def criando_novo_bloco(self):
        self.verifica_linhas_concluidas()
        self.bloco_tetris = Formatos(self.pegando_prox_forma(), self.sprites, self.criando_novo_bloco, self.area_ocupada)


    def timer_update(self):
        for timer in self.timers.values():
            timer.update()


    def move_para_baixo(self):
        self.bloco_tetris.move_para_baixo()


    def verifica_linhas_concluidas(self):
        linhas_deletadas = []
        for i, linha in enumerate(self.area_ocupada):
            if all(linha):
                linhas_deletadas.append(i)

        if linhas_deletadas:
            for linha_del in linhas_deletadas:
                for bloco in self.area_ocupada[linha_del]:
                    bloco.kill()

                for linha in self.area_ocupada:
                    for bloco in linha:
                        if bloco and bloco.pos.y < linha_del:
                            bloco.pos.y += 1
            
            self.area_ocupada = [[0 for x in range(COLUNAS)] for y in range(LINHAS)]

            for block in self.sprites:
                self.area_ocupada[int(block.pos.y)][int(block.pos.x)] = block
            

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
        
        # verifica movimento na horizontal
        if not self.timers['movimento_horizontal'].ativo:
            if chaves[pygame.K_d]:
                self.bloco_tetris.move_horizontal(1)
                self.timers['movimento_horizontal'].ativar()

            if chaves[pygame.K_a]:
                self.bloco_tetris.move_horizontal(-1)
                self.timers['movimento_horizontal'].ativar()

        # verifica rotação
        if not self.timers['rotacao'].ativo:
            if chaves[pygame.K_w]:
                self.bloco_tetris.rotate()
                self.timers['rotacao'].ativar()


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
    def __init__(self, forma, group, criando_novo_bloco, area_ocupada):
        self.forma = forma
        self.posicoes_bloco = FORMAS[forma]['shape'] 
        self.color = FORMAS[forma]['color'] 
        self.criando_novo_bloco = criando_novo_bloco
        self.area_ocupada = area_ocupada

        self.blocks = [Block(group, pos, self.color) for pos in self.posicoes_bloco]


    def move_para_baixo(self):
        if not self.prox_colisao_vertical_movi(self.blocks, 1):
            for block in self.blocks:
                block.pos.y += 1
        else:
            for block in self.blocks:
                self.area_ocupada[int(block.pos.y)][int(block.pos.x)] = block
            self.criando_novo_bloco()


    def move_horizontal(self, qntd):
        if not self.prox_colisao_horizontal_movi(self.blocks, qntd):
            for block in self.blocks:
                block.pos.x += qntd


    # Colisões
    def prox_colisao_horizontal_movi(self, blocks, qntd):
        colisoes_horizontais = [block.colisao_horizontal(int(block.pos.x + qntd), self.area_ocupada) for block in self.blocks]

        if True in colisoes_horizontais:
            return True
        else: 
            return False

    
    def prox_colisao_vertical_movi(self, blocks, qntd):
        colisoes_verticais = [block.colisao_vertical(int(block.pos.y + qntd), self.area_ocupada) for block in self.blocks]

        if True in colisoes_verticais:
            return True
        else:
            return False
    
    # rotate
    def rotate(self):
        if self.forma != 'O':
            pos_centro = self.blocks[0].pos
            nova_pos_bloco = [block.rotate(pos_centro) for block in self.blocks]

            for pos in nova_pos_bloco:
                # colisao na horizontal 
                if pos.x < 0 or pos.x >= COLUNAS:
                    return

                # entre blocos
                if self.area_ocupada[int(pos.y)][int(pos.x)]:
                    return

                # Vertical
                if pos.y > LINHAS:
                    return
            
            for i, block in enumerate(self.blocks):
                block.pos = nova_pos_bloco[i]


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


    def rotate(self, pos_centro):
        return pos_centro + (self.pos - pos_centro).rotate(90)  


    def colisao_horizontal(self, x, area_ocupada):
        if not 0 <= x < COLUNAS:
            return True

        if area_ocupada[int(self.pos.y)][x]:
            return True


    def colisao_vertical(self, y, area_ocupada):
        if y >= LINHAS:
            return True
        
        if y >= 0 and area_ocupada[y][int(self.pos.x)]:
            return True


    def update(self):
        x = self.pos.x * TAM_CELULA
        y = self.pos.y * TAM_CELULA
        self.rect = self.image.get_rect(topleft = (x, y))


