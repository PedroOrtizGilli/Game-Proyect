import pygame





class Personajes(pygame.sprite.Sprite):
    def __init__(self,vida_maxima,velocidad_mov,daño,experiencia,proyectil,hit_box,posicion,image):
        super().__init__()

        self.vida_maxima = vida_maxima  
        self.velocidad_movimiento = velocidad_mov
        self.daño = daño
        self.experiencia = experiencia
        self.proyectil = proyectil

        self.hit_box = hit_box
        self.posicion = posicion
        self.image = image

        



