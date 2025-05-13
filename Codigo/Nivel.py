import pygame
from Funciones import *
from Niveles_Sectores_enum import *


class Nivel:
    def __init__(self,niveles_dict,surface):
        self.pantalla = surface
        self.niveles = niveles_dict  # Diccionario de niveles
        self.nivel_actual = 0
        self.sector_actual = 0
        self.layout = None  # Donde se guarda el diseño actual

    def crear_nivel(self):
        ruta_csv = self.niveles[self.nivel_actual][self.sector_actual]
        self.layout = importar_csv_diseño(ruta_csv)



