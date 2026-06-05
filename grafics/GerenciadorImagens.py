import os
import sys

from grafics.LoadImages import LoadImages
from config import Settings


class GerenciadorImagens:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._load()
        return cls._instance

    @staticmethod
    def resource_path(relative_path):
        """
        Retorna o caminho correto tanto na IDE quanto no executável gerado pelo PyInstaller.
        """
        try:
            base_path = sys._MEIPASS
        except AttributeError:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    def _load(self):
        self.SPRITE_PATHS = {
            "verso": (
                self.resource_path("assets/verso"),
                Settings.LARGURA_CARTA,
                Settings.ALTURA_CARTA
            )
        }

        for consoante in ["B", "C", "D", "F", "G", "J", "L", "M", "N", "P", "R", "S", "T", "V"]:
            for vogal in ["A", "E", "I", "O", "U"]:
                self.SPRITE_PATHS[f"silabas_{consoante + vogal}"] = (
                    self.resource_path(f"assets/cartas_silabas/familia_{consoante}/{consoante + vogal}"),
                    Settings.LARGURA_CARTA,
                    Settings.ALTURA_CARTA
                )

        self._sprites = {}
        self._loader = LoadImages()

        # Carrega só o verso na inicialização (necessário imediatamente)
        self._carregar("verso")

    def _carregar(self, nome):
        if nome in self._sprites:
            return  # já carregado
        path, width, height = self.SPRITE_PATHS[nome]
        if not os.path.exists(path):
            print(f"[SpriteManager] ⚠️ Pasta não encontrada: {path}")
            self._sprites[nome] = []
            return
        self._sprites[nome] = self._loader.load_from_folder(path, width, height)
        print(f"[SpriteManager] ✓ {nome}: {len(self._sprites[nome])} imagens carregadas")

    def get(self, nome: str) -> list:
        if nome not in self._sprites:
            if nome not in self.SPRITE_PATHS:
                raise KeyError(f"[SpriteManager] Sprite '{nome}' não cadastrado.")
            self._carregar(nome)  # carrega só quando precisar
        return self._sprites[nome]