import os
import pygame

class LoadImages:

    def load_from_folder(self, path, sprite_width, sprite_height):
        imagens = []
        for file in sorted(os.listdir(path)):
            img = pygame.image.load(f"{path}/{file}").convert_alpha()
            img = pygame.transform.scale(img, (sprite_width, sprite_height))
            imagens.append(img)
        return imagens