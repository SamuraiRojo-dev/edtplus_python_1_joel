import pygame
import random

pygame.init()

# Configurar la pantalla
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lluvia Espacial")

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Jugador
player_width = 40
player_height = 40
player = pygame.Rect(WIDTH // 2 - player_width // 2, 
                     HEIGHT - player_height - 10, player_width, player_height)

# Cargar imágenes
player_img = pygame.image.load("juego2.0/nave.png").convert_alpha()
meteor_img = pygame.image.load("juego2.0/meteorito.png").convert_alpha()
background_img = pygame.image.load("juego2.0/espacio.png")

# Define las nuevas dimensiones
player_size = (40, 40) # Nuevo tamaño para la imagen del jugador
meteor_size = (60, 60) # Nuevo tamaño para la imagen del meteorito

# Redimensiona las imagenes
player_img = pygame.transform.scale(player_img, player_size)
meteor_img = pygame.transform.scale(meteor_img, meteor_size)



# Meteoritos
meteor_width = 20
meteor_height = 20
meteors = []

# Puntuación
score = 0
font = pygame.font.Font(None, size=36)


# Reloj para controlar FPS
clock = pygame.time.Clock()

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= 5
    if keys[pygame.K_RIGHT] and player.left < WIDTH:
        player.x += 5
    if keys[pygame.K_UP] and player.top > 0:
        player.y -= 5
    if keys[pygame.K_DOWN] and player.bottom < HEIGHT:
        player.y += 5

    # Generar meteoritos
    if len(meteors) < 30:
        meteor = pygame.Rect(random.randint(0, WIDTH - meteor_width),
                         0, meteor_width, meteor_height)
        meteors.append(meteor)

    # Mover meteoritos
    for meteor in meteors:
        meteor.y += 5
        if meteor.top > HEIGHT:
            meteors.remove(meteor)
            score += 1

    # Detectar colisiones        
    for meteor in meteors:
        if player.colliderect(meteor):
            running = False



    screen.fill(BLACK)
    

    screen.blit(background_img, dest=(0, 0))
    
    # pygame.draw.rect(screen, WHITE, player)
    screen.blit(player_img, player)
    for meteor in meteors:
        screen.blit(meteor_img, meteor)
        # pygame.draw.rect(screen, RED, meteor)





    # Mostrar puntuación
    text = font.render(f"Puntuación: {score}", True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
