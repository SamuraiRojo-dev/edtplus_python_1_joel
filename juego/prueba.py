import pygame
import sys
"""from nave import Nave
from bala_gw import Bullet"""

# pygame setup
class GalaxiaWar:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 500))
        pygame.display.set_caption("Galaxia War")
        self.color = (230, 230, 230)
    """ self.velocidad = 1
        self.anchobala = 3
        self.altobala = 15
        self.colorbala = (255, 0, 0)"""
        #self.nave = Nave(self)
       # self.bullets = pygame.sprite.Group()

    def corre_juego(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                """elif event.type == pygame.KEYDOWN: #Mover teclas Segunda parte
                    if event.key == pygame.K_RIGHT: # primero derecha
                        self.nave.mover_derecha = True 
                    if event.key == pygame.K_LEFT:
                        self.nave.mover_izquierda = True
                    if event.key == pygame.K_SPACE:
                        self.fire_bullet()
                elif event.type == pygame.KEYUP: # primero derecha
                    if event.key == pygame.K_RIGHT:
                        self.nave.mover_derecha = False
                    if event.key == pygame.K_LEFT:
                        self.nave.mover_izquierda = False"""

           # self.nave.mover()
            self.screen.fill(self.color)
            #self.nave.corre()
            """self.bullets.update() #Tercera parte
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()"""
            pygame.display.flip()

    """def fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)"""

if __name__ == "__main__":
    a = GalaxiaWar()
    a.corre_juego()