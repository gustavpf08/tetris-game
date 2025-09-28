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
AMARELO = '#f1e60d'
VERMELHO = '#e51b20'
AZUL = '#204b9b'
VERDE = '#65b32e'
ROXO = '#7b217f'
CIANO = '#6cc6d9'
LARANJA = '#f07e13'
CINZA= '#1C1C1C'
BRANCO = '#FFFFFF'

# Formas 
FORMAS = {
	'T': {'shape': [(0,0), (-1,0), (1,0), (0,-1)], 'color': AMARELO},
	'O': {'shape': [(0,0), (0,-1), (1,0), (1,-1)], 'color': VERMELHO},
	'J': {'shape': [(0,0), (0,-1), (0,1), (-1,1)], 'color': AZUL},
	'L': {'shape': [(0,0), (0,-1), (0,1), (1,1)], 'color': LARANJA},
	'I': {'shape': [(0,0), (0,-1), (0,-2), (0,1)], 'color': CIANO},
	'S': {'shape': [(0,0), (-1,0), (0,-1), (1,-1)], 'color': VERDE},
	'Z': {'shape': [(0,0), (1,0), (0,-1), (-1,-1)], 'color': ROXO}
}
