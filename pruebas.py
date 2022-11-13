import pygame

pygame.init()
width = 1280
height = 720
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("xd wachin")

run = True


class Piñata:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = ""
        #radio por ahora pq ajam
        self.radius = 35
    def dibujar(self):
        pygame.draw.circle(win, (255, 0, 0), (self.x, self.y), self.radius)


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
        self.color = (254, 214, 146)
        self.width = 70
        self.height = 70
        self.x = x
        self.y = y
        #IMPORTANTE va a contener una piñata por pruebas, pero luego que hagamos para que escoja las plantas, va a
        #contener [] y luego vamos a recorrer el arreglo de plantas escogidas y ponerle a cada uno lo que contiene
        self.contains = [Piñata(self.x + 35, self.y + 35)]

    def dibujarCuadrado(self):
        pygame.draw.rect(win, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
    def loQueContiene(self, defensasEscogidas):
        for defensa in defensasEscogidas:
            #aqui pondrias los sprites para que se dibuje pero por ahora va a ser un circulo
            defensa.dibujar()


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

defensasEscogidas = []

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
        for x in range(457, 853 - 75, 75):
            CuadradosPlantas.append(CuadroPlantas(x, 10))

    for cuadro in CuadradosPlantas:
        cuadro.dibujarCuadrado()

    # print(mx, my)
    pygame.time.delay(10)
    pygame.display.update()
