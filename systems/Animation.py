from config import Settings


class Animation:
    def __init__(self, frames):

        self.finalisada = False

        self.frames = frames
        self.frame_atual = frames[0]

        self.intervalo_troca = 1
        self.index = 0
        self.contador = 0

    def update(self):
        if self.contador >= self.intervalo_troca:
            self.frame_atual = self.frames[self.index]
            self.contador = 0
            self.index += 1

            if self.index == len(self.frames):
                self.index = 0
                self.finalisada = True

        self.contador+=1
    def get_frame(self):
        return self.frame_atual

    def get_finalisada(self):
        return self.finalisada

    # Animation.py
    def reset_animacao(self):
        self.finalisada = False
        self.index = 0
        self.contador = 0
        self.frame_atual = self.frames[0]