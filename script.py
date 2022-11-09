import pygame

pygame.init()
width = 1000
height = 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hanal Pixan")

#Posicion mouse
mx, my = pygame.mouse.get_pos()

# por ahora veremos
class Cuadricula:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas


class Defensa:
    def __int__(self):
        self.salud = 100
        self.cuadricula = [[]]


cuadricula = Cuadricula(5, 10)  # tablero de juego

run = True

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
