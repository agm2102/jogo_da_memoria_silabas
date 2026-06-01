import random

import pygame.mouse

from config import Settings
from model.Carta import Carta

class Partida:

    def __init__(self, gerenciador_imagens):

        self.SILABAS = {
            0: "BA", 1: "BE", 2: "BI", 3: "BO", 4: "BU",

            5: "CA", 6: "CE", 7: "CI", 8: "CO", 9: "CU",

            10: "DA", 11: "DE", 12: "DI", 13: "DO", 14: "DU",

            15: "FA", 16: "FE", 17: "FI", 18: "FO", 19: "FU",

            20: "GA", 21: "GE", 22: "GI", 23: "GO", 24: "GU",

            25: "JA", 26: "JE", 27: "JI", 28: "JO", 29: "JU",

            30: "LA", 31: "LE", 32: "LI", 33: "LO", 34: "LU",

            35: "MA", 36: "ME", 37: "MI", 38: "MO", 39: "MU",

            40: "NA", 41: "NE", 42: "NI", 43: "NO", 44: "NU",

            45: "PA", 46: "PE", 47: "PI", 48: "PO", 49: "PU",

            50: "RA", 51: "RE", 52: "RI", 53: "RO", 54: "RU",

            55: "SA", 56: "SE", 57: "SI", 58: "SO", 59: "SU",

            60: "TA", 61: "TE", 62: "TI", 63: "TO", 64: "TU",

            65: "VA", 66: "VE", 67: "VI", 68: "VO", 69: "VU",

            70: "XA", 71: "XE", 72: "XI", 73: "XO", 74: "XU",

            75: "ZA", 76: "ZE", 77: "ZI", 78: "ZO", 79: "ZU",
        }
        self.imagens = {
            letra: gerenciador_imagens.get(f"silabas_{letra}")
            for letra in ["B", "C", "D", "F", "G", "J", "L", "M", "N", "P", "R", "S", "T", "V"]
        }

        self.imagens_silabas = [
            imagem
            for lista_imagens in self.imagens.values()
            for imagem in lista_imagens
        ]

        self.imagem_verso_carta = gerenciador_imagens.get("verso")[0]

        self.tempo_desvirar_carta = 60
        self.timer = 0
        self.desvirando_carta = False

        self.deck_cartas = []
        self.pares_achados = 0

        self.qtd_cartas = len(self.imagens_silabas) * 2
        self.cartas_viradas = []

        self.jogadas_feitas = 0

        self.preencher_deck()
        self.posicionar_cartas()

    def preencher_deck(self):
        index = 0
        for i in range(self.qtd_cartas):
            if i % 2 == 0 and not i < 1:
                index += 1
            carta = Carta(self.imagens_silabas[index], self.imagem_verso_carta, self.SILABAS[index])
            self.deck_cartas.append(carta)

    def posicionar_cartas(self):
        random.shuffle(self.deck_cartas)
        linha = 0
        coluna = 0
        for carta in self.deck_cartas:
            carta.set_x(coluna * Settings.LARGURA_CARTA)
            carta.set_y(linha * Settings.ALTURA_CARTA)
            carta.set_rect()
            coluna += 1
            if coluna == Settings.QTD_COLUNAS:
                linha += 1
                coluna = 0

    def verificar_cartas_viradas(self):
        carta1 = self.cartas_viradas[0]
        carta2 = self.cartas_viradas[1]

        if carta1.get_silaba() == carta2.get_silaba():
            carta1.set_achada()
            carta2.set_achada()
            self.pares_achados += 1

            print("pares achados ", self.pares_achados)

            self.desvirando_carta = True
        else:
            self.desvirando_carta = True

    def desvirar_cartas_erradas(self):
        if self.desvirando_carta:
            self.timer += 1
            if self.timer >= self.tempo_desvirar_carta:
                for carta in self.cartas_viradas:
                    if not carta.foi_achada():
                        carta.virar()
                self.timer = 0
                self.jogadas_feitas = 0
                self.cartas_viradas.clear()
                self.desvirando_carta = False

    def draw(self, tela):
        for carta in self.deck_cartas:
            carta.draw(tela)

    def update(self, events):
        for carta in self.deck_cartas:
            self.input_handler(events, carta)

        self.desvirar_cartas_erradas()

    def input_handler(self, events, carta):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if carta.get_rect().collidepoint(event.pos) and carta.foi_achada() is False:
                        if self.jogadas_feitas < 2:
                            carta.virar()
                            self.jogadas_feitas += 1
                            self.cartas_viradas.append(carta)
                            print("jogadas: ",self.jogadas_feitas,"cartas viradas: ",len(self.cartas_viradas))
                        if self.jogadas_feitas == 2 and self.desvirando_carta is False:
                            self.verificar_cartas_viradas()
                        break




