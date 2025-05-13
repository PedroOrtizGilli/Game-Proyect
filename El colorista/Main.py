import pygame
from PJ import Jugador
import Constantes


pygame.init()

pantalla = pygame.display.set_mode((Constantes.ANCHO_VENTANA,Constantes.ALTO_VENTANA))
pygame.display.set_caption("Mi primer juego")

mi_personaje = Jugador(10,5,5,0,"proyectil",12,(100,100),pygame.Surface((64, 64)),"pincel","paleta",10)


corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False


    pantalla.fill((0, 0, 0))  # Negro
    mi_personaje.update(pantalla)
    pygame.display.flip()

pygame.quit()