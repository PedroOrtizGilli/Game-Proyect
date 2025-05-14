import pygame
from Personajes import Personajes
import Comandos




class Jugador(Personajes):
    def __init__(self,vida_maxima,velocidad_mov,daño,experiencia,proyectil,hit_box,posicion,image, pincel, paleta, cantidad_tinta):
        super().__init__(vida_maxima,velocidad_mov,daño,experiencia,proyectil,hit_box,posicion,image)


        #Imagen
        self.image = image
        self.image.fill((255,0,0))
        #Rectangulo
        self.rect = self.image.get_rect()
        self.rect.topleft = posicion
        #Posicion Flexible y Velocidad
        self.direccion = pygame.math.Vector2(0,0)
        self.velocidad_movimiento = velocidad_mov

        
        self.pincel = pincel
        self.paleta = paleta
        self.cantidad_tinta = cantidad_tinta

    #Toma los datos del vector y modifica la posicion
    def movimiento_jugador(self):
        self.rect.x += self.direccion.x * self.velocidad_movimiento

    
    def update(self,pantalla):
        Comandos.detectar_comando(self)
        self.movimiento_jugador()
        pantalla.blit(self.image, self.rect)