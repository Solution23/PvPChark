import pygame
import os

width, height = 1707,915
pantalla = pygame.display.set_mode((width,height))
img = pygame.image.load(os.path.join("pvpchark_code_game", "Fondo.jpg"))
imagen_de_fondo = pygame.transform.scale(img, (width,height))


def background(imagen_de_fondo):
    pygame.display.flip()
    pygame.display.update

while True:
    for eventos in pygame.event.get():
        if eventos == pygame.QUIT:
            quit()
    background(imagen_de_fondo)
    