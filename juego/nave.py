import pygame

class Nave:
    def __init__(self, a_game):
        self.screen = a_game.screen
        self.screen_rect = a_game.screen.get_rect()
        self.image = pygame.image.load("juego/nave.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.mover_derecha = False # creando movimiento
        self.mover_izquierda = False

    def mover(self): # mover teclas and Limite de pantalla 
        if self.mover_derecha and self.rect.right < self.screen_rect.right:
            self.rect.x += 1
        if self.mover_izquierda and self.rect.left > self.screen_rect.left: # segnda parte
            self.rect.x -= 1

    def corre(self):
        self.screen.blit(self.image, self.rect)