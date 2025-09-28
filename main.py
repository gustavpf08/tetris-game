from config import *
from sys import exit

# Componentes da tela
from game import Game
from preview import Preview
from score import Score

from random import choice

class Main:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((LARG_JANELA, ALT_JANELA))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Tetris')

        # Formatos
        self.prox_formatos = [choice(list(FORMAS.keys())) for shape in range(3)]
        print(self.prox_formatos)

        # Componentes
        self.game = Game(self.pegando_prox_forma)
        self.preview = Preview(self.prox_formatos)
        self.score = Score()


    def pegando_prox_forma(self):
        prox_forma = self.prox_formatos.pop(0)
        self.prox_formatos.append(choice(list(FORMAS.keys())))
        return prox_forma

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # Cor de fundo
            self.display_surface.fill(CINZA)

            # Componentes
            self.game.run()
            self.preview.run()
            self.score.run()

            pygame.display.update()
            self.clock.tick()


if __name__ == '__main__':
    main = Main()
    main.run()



