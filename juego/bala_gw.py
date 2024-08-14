import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, a_game):
        super().__init__()
        self.screen = a_game.screen
        self.color = a_game.colorbala
        self.rect = pygame.Rect(0,0, a_game.anchobala, a_game.altobala)
        self.rect.midtop = a_game.nave.rect.midtop
        self.juego = a_game
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.juego.velocidad
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect