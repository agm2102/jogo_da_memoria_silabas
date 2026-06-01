import os
import  pygame

from config import Settings
from grafics.GerenciadorImagens import GerenciadorImagens
from model.Partida import Partida


def create_new_screen(width, height):
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    return pygame.display.set_mode((width, height))

class Game:

    def __init__(self):
        pygame.init()
        # Cria a tela do jogo
        self.screenGame = create_new_screen(Settings.LARGURA_TELA, Settings.ALTURA_TELA)
        # Variavel que gerencia e limita o FPS do jogo
        self.clock = pygame.time.Clock()

        self.gerenciador_imagens = GerenciadorImagens()

        self.runningGame = True
        self.events = None

        self.partida = Partida(self.gerenciador_imagens)


    def run(self):
        while self.runningGame:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(30)
        pygame.quit()

    def handle_events(self):

        self.events = pygame.event.get()
        for event in self.events:
            if event.type == pygame.QUIT:
                self.runningGame = False


    def render(self):

        self.screenGame.fill((0, 0, 0))  # limpa tela (preto)
        self.partida.draw(self.screenGame)
        pygame.display.flip()

    def update(self):
        self.partida.update(self.events)
