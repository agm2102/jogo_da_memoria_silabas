from systems.Animation import Animation


class GerenciadorAnimacoes:

    def __init__(self, gerenciador_imagens, silaba):
        self.VIRAR = "virar"
        self.DESVIRAR = "desvirar"

        self.gerenciador_imagens = gerenciador_imagens

        self.frames_verso_carta = gerenciador_imagens.get("verso")
        self.frames_frente_carta = gerenciador_imagens.get("silabas_" + silaba)

        self.frames_virar = []
        self.frames_virar.extend(self.frames_verso_carta)
        self.frames_virar.extend(self.frames_frente_carta)

        self.frames_desvirar = list(reversed(self.frames_virar))

        self.animacoes = {
            "virar": Animation(self.frames_virar),
            "desvirar": Animation(self.frames_desvirar)
        }

        self.animacao_atual = self.animacoes[self.DESVIRAR]

    def play_animation(self, nome_animacao):
        self.animacao_atual = self.animacoes[nome_animacao]
        self.animacao_atual.reset_animacao()

    def update(self):
        self.animacao_atual.update()

    def get_frame(self):
        return self.animacao_atual.get_frame()

    def animacao_atual_finalizada(self):
        return self.animacao_atual.get_finalisada()
