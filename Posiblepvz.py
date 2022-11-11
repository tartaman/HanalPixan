import pygame
pygame.init()
win = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("xd wachin")

verdefosfo= (79, 222, 59)
verdeoscuro= (28, 184, 6)
x = 250
y = 250
vel = 10
radius= 25
generar = 200

run = True

def dibujar_cuadricula():
    contador = 0
    ponery = 680
    for ponery in range(680, 180, -100):
        if contador%2 == 0:
            for generar in range(200, 900, 160):
                pygame.draw.rect(win, verdefosfo, pygame.Rect(generar, ponery, 80, 100))
        else:
            for generar in range(280, 900, 160):
                pygame.draw.rect(win, verdefosfo, pygame.Rect(generar, ponery, 80, 100))
        contador += 1
    contador = 0
    ponery = 680
    for ponery in range(680, 180, -100):
        if contador%2 == 0:
            for generar in range(280, 900, 160):
                pygame.draw.rect(win, verdeoscuro, pygame.Rect(generar, ponery, 80, 100))
        else:
            for generar in range(200, 900, 160):
                pygame.draw.rect(win, verdeoscuro, pygame.Rect(generar, ponery, 80, 100))
        contador += 1

def detectar_cuadricula(x, y):
    divx = int(((x + 200)/80)-5)
    divy = int(((y-180)/100)-1)
    print(f"Esta en la columna {divx}, fila {divy}")

class plantas:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def lanzaguizantes(self):
        pygame.draw.circle(win, (255,255,255), (100, 100), 25)



defensas= plantas(250,250)
while run:
    win.fill((0,0,0))
    mx, my = pygame.mouse.get_pos()

    detectar_cuadricula(mx, my)
    dibujar_cuadricula()
    defensas.lanzaguizantes()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            run = False
    pygame.time.delay(10)
    pygame.display.update()
