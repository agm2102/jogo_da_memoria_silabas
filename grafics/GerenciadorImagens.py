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

        for letra in ["B", "C", "D", "F", "G", "J", "L", "M", "N", "P", "R", "S", "T", "V"]:
            self.SPRITE_PATHS[f"silabas_{letra}"] = (
                self.resource_path(f"assets/cartas_silabas/familia_{letra}"),
                Settings.LARGURA_CARTA,
                Settings.ALTURA_CARTA
            )

        loader = LoadImages()
        self._sprites = {}

        for nome, (path, width, height) in self.SPRITE_PATHS.items():
            if not os.path.exists(path):
                print(f"[SpriteManager] ⚠️ Pasta não encontrada: {path}")
                self._sprites[nome] = []
                continue

            self._sprites[nome] = loader.load_from_folder(
                path,
                width,
                height
            )

            print(
                f"[SpriteManager] ✓ {nome}: "
                f"{len(self._sprites[nome])} imagens carregadas"
            )

    def get(self, nome: str) -> list:
        if nome not in self._sprites:
            raise KeyError(f"[SpriteManager] Sprite '{nome}' não cadastrado.")

        return self._sprites[nome]