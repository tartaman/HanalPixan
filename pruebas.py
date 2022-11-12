import pygame
pygame.init()
width = 1280
height = 720
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("xd wachin")

verdefosfo= (79, 222, 59)
verdeoscuro= (28, 184, 6)

mx,my = pygame.mouse.get_pos()

Rectangulos = []

run = True

class RectanguloOscuro:
    def __init__(self, x, y):
        self.color = verdeoscuro
        self.width = ((width-450)//9)
        self.height = ((height-100)//5)
        self.x = x
        self.y = y
    def dibujar(self):
        pygame.draw.rect(win, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

class RectanguloClaro:
    def __init__(self, x, y):
        self.color = verdefosfo
        self.width = ((width - 450) // 9)
        self.height = ((height - 100) // 5)
        self.x = x
        self.y = y
    def dibujar(self):
        pygame.draw.rect(win, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

while run:
    win.fill((0,0,0))
    mx, my = pygame.mouse.get_pos()
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.QUIT:
            run = False
    if len(Rectangulos) == 0:
        Clarito = RectanguloOscuro(0,100)
        Rectangulos.append(Clarito)
    for rectangulo in Rectangulos:
        rectangulo.dibujar()

    pygame.time.delay(10)
    pygame.display.update()