from os import walk
from csv import reader
from Settings import tamaño_loseta
import pygame

def importar_carpeta(path):
    lista_imagenes = []
    for _,__,imagen_archivo in walk(path):
        for imagen in imagen_archivo:
            full_path = path + '/' + imagen

            load_image = pygame.image.load(full_path).convert_alpha()
            lista_imagenes.append(load_image)
    return lista_imagenes


def importar_csv_diseño(diseño):
    terreno_mapa = []
    with open(diseño, 'r') as map:
        for fila in map:
            fila = fila.strip().split(',')
            terreno_mapa.append(fila)
    return terreno_mapa
    

def importar_imagenes_terreno(path):
    
    losetas_cortadas = []
    try:

        surface = pygame.image.load(path).convert_alpha()
    except pygame.error as e:
            print(f"Error al cargar la imagen: {e}")
            return []
    
    numero_loseta_x = int(surface.get_size()[0] / tamaño_loseta)
    numero_loseta_y = int(surface.get_size()[1] / tamaño_loseta)
    
    for fila in range(numero_loseta_y):
            for columna in range(numero_loseta_x):
                x = columna * tamaño_loseta
                y = fila * tamaño_loseta
                nueva_superficie = pygame.Surface((tamaño_loseta,tamaño_loseta),flags = pygame.SRCALPHA)
                nueva_superficie.blit(surface,(0,0),pygame.Rect(x,y,tamaño_loseta,tamaño_loseta))
                losetas_cortadas.append(nueva_superficie)
    
    
    return losetas_cortadas