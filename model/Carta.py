import pygame

from config import Settings


class Carta:
    def __init__(self, frente, verso, silaba):
        self.rect = None
        self.frente = frente
        self.verso = verso
        self.silaba = silaba

        self.x = 0
        self.y = 0

        self.virada = False
        self.achada = False

    def virar(self):
        self.virada = not self.virada

    def draw(self, tela):
        if self.virada:
            tela.blit(self.frente, (self.x, self.y))
        else:
            tela.blit(self.verso, (self.x, self.y))

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
