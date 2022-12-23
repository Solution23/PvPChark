import pygame
import os, sys

width, height = 1707,915
pantalla = pygame.display.set_mode((width,height))
img = pygame.image.load(os.path.join("pvpchark_code_game", "Fondo.jpg"))
imagen_de_fondo = pygame.transform.scale(img, (width,height))


def player(pantalla):
    jugador = pygame.draw.circle(pantalla,(255, 0, 0),(617,699), 20,30)
    pygame.display.flip()

def background(imagen_de_fondo): 
    #Camara_x = -pygame.mouse.get_pos()[0]
    pantalla.blit((imagen_de_fondo), (0,0))
    pygame.display.flip()
    
    #print(Camara_x)


while True:
    for eventos in pygame.event.get():
        if eventos == pygame.QUIT:
            pygame.quit()
        #Intenta hacer el manejo del personaje aqui a ver si puedes pls


    player(pantalla)
    background(imagen_de_fondo)   
    