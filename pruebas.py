import pygame

pygame.init()
width = 1280
height = 720
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("xd wachin")

run = True


class RectanguloPlantas:
    def __init__(self, x, y):
        self.color = (253, 187, 73)
        self.widthH = width // 3
        self.heightH = height // 8
        self.x = x
        self.y = y

    def dibujarRectangulo(self):
        pygame.draw.rect(win, self.color, pygame.Rect(self.x, self.y, self.widthH, self.heightH))


class CuadroPlantas:
    def __init__(self, x, y=5):
        self.color = (0, 0, 0)#(254, 214, 146)
        self.width = 50
        self.height = 50
        self.x = x
        self.y = y

    def dibujarCuadrado(self):
        pygame.draw.rect(win, self.color, pygame.Rect(self.x, self.y, self.width, self.height))


class RectanguloOscuro:
    def __init__(self, x, y, columna, fila):
        self.color = verdeoscuro
        self.width = ((width - 450) // 9)
        self.height = ((height - 200) // 5)
        self.x = x
        self.y = y
        self.columna = columna
        self.fila = fila

    def dibujar(self):
        pygame.draw.rect(win, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

    def detectarClick(self, mx, my):
        if (self.y + self.height) > my > self.y:
            if self.x < mx < (self.x + self.width):
                print(f"hizo click en el cuadrado de la columna {self.columna}, fila {self.fila}.")


class RectanguloClaro:
    def __init__(self, x, y, columna, fila):
        self.color = verdefosfo
        self.width = ((width - 450) // 9)
        self.height = ((height - 200) // 5)
        self.x = x
        self.y = y
        self.columna = columna
        self.fila = fila

    def dibujar(self):
        pygame.draw.rect(win, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

    def detectarClick(self, mx, my):
        if (self.y + self.height) > my > self.y:
            if self.x < mx < (self.x + self.width):
                print(f"hizo click en el cuadrado de la columna {self.columna}, fila {self.fila}.")


verdefosfo = (79, 222, 59)
verdeoscuro = (28, 184, 6)

mx, my = pygame.mouse.get_pos()

Rectangulos = []
CuadradosPlantas = []
rectanguloPlantas = RectanguloPlantas(((width - (width // 3)) // 2), 0)
while run:
    win.fill((255, 255, 255))
    mx, my = pygame.mouse.get_pos()
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            for rectangulo in Rectangulos:
                rectangulo.detectarClick(mx, my)

    # Crear cuadricula
    if len(Rectangulos) == 0:
        columna = 0
        fila = 0
        for y in range(100, height - 100, (height - 200) // 5):
            if fila % 2 == 0:
                for x in range(200, width - 250, (width - 450) // 9):
                    if columna % 2 == 0:
                        Rectangulos.append(RectanguloClaro(x, y, columna, fila))
                        columna += 1
                    else:
                        Rectangulos.append(RectanguloOscuro(x, y, columna, fila))
                        columna += 1
                fila += 1
            else:
                for x in range(200, width - 250, (width - 450) // 9):
                    if columna % 2 == 0:
                        Rectangulos.append(RectanguloOscuro(x, y, columna, fila))
                        columna += 1
                    else:
                        Rectangulos.append(RectanguloClaro(x, y, columna, fila))
                        columna += 1
                fila += 1
            if columna >= 9:
                columna = 0
    for rectangulo in Rectangulos:
        rectangulo.dibujar()

    # Dibujar cuadro plantas
    rectanguloPlantas.dibujarRectangulo()
    if len(CuadradosPlantas) == 0:
        for x in range(((width - width//3)//2) + 5, width//3, 50):
            CuadradosPlantas.append(CuadroPlantas(x, 5))

    for cuadro in CuadradosPlantas:
        cuadro.dibujarCuadrado()

    pygame.time.delay(10)
    pygame.display.update()
