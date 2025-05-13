import pygame

def detectar_comando(jugador):
        keys = pygame.key.get_pressed()
        
        
        #Si se aprieta x tecla se realizan los movimientos
        if keys[pygame.K_d]:
            jugador.direccion.x = 1
        elif keys[pygame.K_a]:
            jugador.direccion.x = -1   

        #Si no se aprieta nada la variabel que afecta al movimiento se vuelve 0 y no hay nueva pos de bliteo
        else:
            jugador.direccion.x = 0

