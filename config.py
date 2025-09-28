import pygame
 
# Tamanho do Jogo
COLUNAS = 10
LINHAS = 20
TAM_CELULA = 40
LARGURA_JOGO, ALTURA_JOGO = COLUNAS * TAM_CELULA, LINHAS * TAM_CELULA

# Tamanho da Barra Lateral
SIDEBAR_LARG = 200
ALTURA_PREVIEW = 0.7
SCORE_PREVIEW = 1 - ALTURA_PREVIEW

# Janela
PADDING = 20
LARG_JANELA = LARGURA_JOGO + SIDEBAR_LARG + PADDING * 3
ALT_JANELA = ALTURA_JOGO + PADDING * 2

# Comportamento do jogo
VELOCIDADE_INICIO = 200
INICIO_BLOCO = pygame.Vector2(COLUNAS // 2 - 1, -1)
TEMPO_DE_MOVER = 200
TEMPO_ROTACAO = 200

# Cores
CINZA = '#1C1C1C'
BRANCO = '#FFFFFF'
AZUL = '#204b9b'
VERMELHO = '#FF0000'
LILAS = '#C8A2C8'
AMARELO = '#FFDE21' 
VERDE = '#00FF00'

FORMAS = {
    'T': {'shape': [(0,0), (-1,0), (1,0), (0,-1)], 'color': AZUL}, 
    'O': {'shape': [(0,0), (0,-1), (1,0), (1,-1)], 'color': BRANCO},
    'S': {'shape': [(0,0), (0,-1), (1,-1), (1,-2)], 'color': VERMELHO},
    'L': {'shape': [(0,0), (1,0), (0,-1), (0,-2)], 'color': VERMELHO},
    'C': {'shape': [(0,0), (0,-1), (1,0), (2,0), (2,-1)], 'color': AMARELO},
    'I': {'shape': [(0,0), (0,-1), (0,-2), (0,-3)], 'color': LILAS},
    'E': {'shape': [(0,0), (0,-1), (1,0)], 'color': VERDE},
}
