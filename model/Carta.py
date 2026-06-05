import pygame

from config import Settings
from systems.Animation import Animation
from systems.GerenciadorAnimacoes import GerenciadorAnimacoes


class Carta:
    def __init__(self, frente, verso, gerenciador_imagens, silaba):

        self.gerenciador_animacoes = GerenciadorAnimacoes(gerenciador_imagens,silaba)

        self.rect = None
        self.frente = frente
        self.verso = verso
        self.silaba = silaba

        self.x = 0
        self.y = 0

        self.virada = False
        self.virando = False
        self.achada = False

    def virar(self):
        self.virando = True
        self.gerenciador_animacoes.play_animation(self.gerenciador_animacoes.VIRAR)

    def desvirar(self):
        self.virando = True
        self.gerenciador_animacoes.play_animation(self.gerenciador_animacoes.DESVIRAR)

    def draw(self, tela):
        if self.virando:
            tela.blit(self.gerenciador_animacoes.get_frame(), (self.x, self.y))
        elif self.virada:
            tela.blit(self.frente, (self.x, self.y))
        else:
            tela.blit(self.verso, (self.x, self.y))

    def update(self):
        if not self.gerenciador_animacoes.animacao_atual_finalizada():
            self.gerenciador_animacoes.update()
        else:
            if self.virando:
                self.virada = not self.virada
                self.virando = False

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def get_rect(self):
        return self.rect

    def esta_virada(self):
        return self.virada

    def foi_achada(self):
        return self.achada

    def set_achada(self):
        self.achada = not self.achada

    def get_silaba(self):
        return self.silaba

    def set_rect(self):
        self.rect = pygame.Rect(self.x, self.y, Settings.LARGURA_CARTA, Settings.ALTURA_CARTA)
