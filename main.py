from config import *
from sys import exit

from game import Game
from preview import Preview
from score import Score

class Main:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((LARG_JANELA, ALT_JANELA))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Tetris')

        # Componentes
        self.game = Game()
        self.preview = Preview()
        self.score = Score()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # Cor de fundo
            self.display_surface.fill(CINZA)
            self.game.run()
            self.preview.run()
            self.score.run()

            pygame.display.update()
            self.clock.tick()

if __name__ == '__main__':
    main = Main()
    main.run()



