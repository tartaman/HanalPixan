import pygame
pygame.init()
width = 1280
height = 720
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("xd wachin")

verdefosfo= (79, 222, 59)
verdeoscuro= (28, 184, 6)
x = 250
y = 250
vel = 10
radius = 25
generar = 200

run = True

class RectanguloOscuro:
    def __init__(self, x, y):
        self.color = (28, 184, 6)
        self.size = (width//9, height//5)
        self.x = x
        self.y = y

class RectanguloClaro:
    pass

def dibujar_cuadricula():
    contador = 0
    #pa alternar
    fila = 0
#le voy a poner de que width y height pa que funcione aunque cambiemos algo
    for posicionesEnY in range(100, height, (height - 100)//5):
        if fila % 2 == 0:
            for generar in range(200, width - 250, (width - 450)//9):
                if contador % 2 == 0:
                    pygame.draw.rect(win, verdefosfo, pygame.Rect(generar, posicionesEnY, (width - 450)//9, (height-100)//5))
                else:
                    pygame.draw.rect(win, verdeoscuro, pygame.Rect(generar, posicionesEnY, (width - 450)//9, (height-100)//5))
                contador += 1
            fila += 1
        else:
            contador = 0
            for generar in range(200, width - 250, (width - 450)//9):
                if contador % 2 == 0:
                    pygame.draw.rect(win, verdeoscuro, pygame.Rect(generar, posicionesEnY, (width - 450)//9, (height-100)//5))
                else:
                    pygame.draw.rect(win, verdefosfo, pygame.Rect(generar, posicionesEnY, (width - 450)//9, (height-100)//5))
                contador += 1
            fila += 1





def detectar_cuadricula(x, y):
    divx = int(((x - 200)/((width - 500)//9)))
    divy = int((y-100)/((height-100)//5))
    print(f"Esta en la columna {divx}, fila {divy}")

def drag(event):
    for events in event:
        if events.type == pygame.MOUSEBUTTONDOWN:
            print("Hizo click")
        else:
            pass


def generar_tabla():
    pygame.draw.rect(win, (232, 118, 11), pygame.Rect(170, 0, 530, 100))
    for generar in range(175, 700, 75):
        pygame.draw.rect(win, (255, 183, 115), pygame.Rect(generar, 5, 70, 90))


while run:
    win.fill((0,0,0))
    mx, my = pygame.mouse.get_pos()
    detectar_cuadricula(mx, my)
    dibujar_cuadricula()
    generar_tabla()
    pygame.draw.circle(win, (255, 255, 255), (285, 36), 15)
    ev = pygame.event.get()
    drag(ev)
    for event in ev:
        if event.type == pygame.QUIT:
            run = False
    pygame.time.delay(10)
    pygame.display.update()