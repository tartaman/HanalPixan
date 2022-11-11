import pygame
pygame.init()
win = pygame.display.set_mode((1100, 620))
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
    for ponery in range(100,580, 100):
        if contador%2 == 0:
            for generar in range(200, 900, 160):
                pygame.draw.rect(win, verdefosfo, pygame.Rect(generar, ponery, 80, 100))
        else:
            for generar in range(280, 900, 160):
                pygame.draw.rect(win, verdefosfo, pygame.Rect(generar, ponery, 80, 100))
        contador += 1
    contador = 0
    for ponery in range(100, 580, 100):
        if contador%2 == 0:
            for generar in range(280, 900, 160):
                pygame.draw.rect(win, verdeoscuro, pygame.Rect(generar, ponery, 80, 100))
        else:
            for generar in range(200, 900, 160):
                pygame.draw.rect(win, verdeoscuro, pygame.Rect(generar, ponery, 80, 100))
        contador += 1


def detectar_cuadricula(x, y):
    divx = int(((x + 200)/80)-5)
    divy = int(((y-100)/100))

def drag(press):
    if press:
        print("oprimiendo")
    else:
        print("No oprimiendo")


def generar_tabla():
    pygame.draw.rect(win, (232, 118, 11), pygame.Rect(170, 0, 530, 100))
    for generar in range(175, 700, 75):
        pygame.draw.rect(win, (255, 183, 115), pygame.Rect(generar, 5, 70, 90))


while run:
    win.fill((0,0,0))
    mx, my = pygame.mouse.get_pos()
    press= pygame.mouse.get_pressed()
    drag(press)
    detectar_cuadricula(mx, my)
    dibujar_cuadricula()
    generar_tabla()
    pygame.draw.circle(win, (255, 255, 255), (285, 36), 15)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            run = False
    pygame.time.delay(10)
    pygame.display.update()