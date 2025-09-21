from config import *

class Timer:
    def __init__(self, duracao, repetido = False, func = None):
        self.repetido = repetido
        self.func = func
        self.duracao = duracao

        self.inicio_tempo = 0
        self.ativo = False


    def ativar(self):
        self.ativo = True
        self.inicio_tempo = pygame.time.get_ticks()


    def desativar(self):
        self.ativo = False
        self.inicio_tempo = 0


    # Comparando para ver se a diff de tempo é superior a duração que eu quero para poder executar uma ação. Vai ser usado para fazer os blocos cairem em uma determinada fração de tempo
    def update(self):
        self.tempo_atual = pygame.time.get_ticks()
        if self.tempo_atual - self.inicio_tempo >= self.duracao and self.ativo:

            # Chama a função:
            if self.func and self.inicio_tempo != 0:
                self.func()

            # resetar o tempo
            self.desativar()

            if self.repetido:
                self.ativar()
