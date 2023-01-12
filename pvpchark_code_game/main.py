import pygame
import os, sys

#Movimiento
Movimiento_x = 662
Movimiento_y = 620
Velocidad_De_Movimiento_x = 0
Velocidad_De_Movimiento_y = 0
Movimiento_x = Movimiento_x + Velocidad_De_Movimiento_x
Movimiento_y = Movimiento_y + Velocidad_De_Movimiento_y
#Pantalla
width, height = 1707,915
pantalla = pygame.display.set_mode((width,height))

#Fondo
img = pygame.image.load(os.path.join("C:/Users/User/Desktop/PvPChark/pvpchark_code_game","Fondo.jpg"))
imagen_de_fondo = pygame.transform.scale(img, (width,height))



#Personaje
def player(pantalla,Movimiento_x, Movimiento_y):
    pygame.draw.circle(pantalla,(255, 0, 0),(Movimiento_x,Movimiento_y), 20,30)
    pygame.display.flip()


#Fondo
def background(imagen_de_fondo): 
    Camara_x = -pygame.mouse.get_pos()[0]
    Camara_y = -pygame.mouse.get_pos()[0]
    pantalla.blit((imagen_de_fondo), (0,0))
    
    
    #print(Camara_x,Camara_y)
fps = 60
On = True
while On:
    Clock =pygame.time.Clock()
    Clock.tick(fps)

    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            On = False
        if eventos.type == pygame.KEYDOWN:
            teclas = pygame.key.name(eventos.key)
            print(teclas)
            if pygame.key.get_pressed()[pygame.K_w]:
                Velocidad_De_Movimiento_x = Velocidad_De_Movimiento_x + Velocidad_De_Movimiento_x 


    player(pantalla,Movimiento_x, Movimiento_y)
    background(imagen_de_fondo)
    
