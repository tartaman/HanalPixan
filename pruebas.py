import pygame
import random

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
        # radio por ahora pq ajam
        self.radius = 35
        self.color = (255, 0, 0)

    def dibujarDefensa(self):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
    #en cuadrado
    def dibujarDefensaEC(self, x, y):
        pygame.draw.circle(win, self.color, (x, y), self.radius)


class Piñata2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = ""
        # radio por ahora pq ajam
        self.radius = 35
        self.color = (255, 255, 0)
    def dibujarDefensa(self):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

    def dibujarDefensaEC(self, x, y):
        pygame.draw.circle(win, self.color, (x, y), self.radius)


class Piñata3:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = ""
        # radio por ahora pq ajam
        self.radius = 35
        self.color = (255, 0, 255)
    def dibujarDefensa(self):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

    def dibujarDefensaEC(self, x, y):
        pygame.draw.circle(win, self.color, (x, y), self.radius)


class Piñata4:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = ""
        # radio por ahora pq ajam
        self.radius = 35
        self.color = (255, 255, 255)
    def dibujarDefensa(self):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

    def dibujarDefensaEC(self, x, y):
        pygame.draw.circle(win, self.color, (x, y), self.radius)


class Piñata5:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = ""
        # radio por ahora pq ajam
        self.radius = 35
        self.color = (0, 255, 255)
    def dibujarDefensa(self):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

    def dibujarDefensaEC(self, x, y):
        pygame.draw.circle(win, self.color, (x, y), self.radius)


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
    def __init__(self, x, indice, y=5):
        self.color = (254, 214, 146)
        self.width = 70
        self.height = 70
        self.x = x
        self.y = y
        self.indice = indice
        # IMPORTANTE va a contener una piñata por pruebas, pero luego que hagamos para que escoja las plantas, va a
        # contener [] y luego vamos a recorrer el arreglo de plantas escogidas y ponerle a cada uno lo que contiene
        self.contains = []

    def dibujarCuadrado(self):
        pygame.draw.rect(win, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

    def detectarClick(self, mx, my):
        if (self.y + self.height) > my > self.y:
            if self.x < mx < (self.x + self.width):
                print(f"Escogio el cuadrado {self.indice}, que contiene {self.contains}")
                # si no tiene agarrado nada entonces agarra si no pues no vea
                if len(ahoritaTiene) == 0:
                    # Crea un objeto nuevo fuera de la pantalla para agregar
                    defensa = self.contains[self.indice]
                    ahoritaTiene.append(defensa)

    def mostrarLoQueContiene(self):
        self.contains[self.indice].x = self.x + self.width//2
        self.contains[self.indice].y = self.y + self.height//2
        self.contains[self.indice].dibujarDefensa()


class RectanguloOscuro:
    def __init__(self, x, y, columna, fila, indice):
        self.color = verdeoscuro
        self.width = ((width - 450) // 9)
        self.height = ((height - 200) // 5)
        self.x = x
        self.y = y
        self.columna = columna
        self.fila = fila
        self.indice = indice
        self.contiene = []

    def dibujar(self):
        pygame.draw.rect(win, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

    def detectarClick(self, mx, my):
        if (self.y + self.height) > my > self.y:
            if self.x < mx < (self.x + self.width):
                print(
                    f"hizo click en el cuadrado de la columna {self.columna}, fila {self.fila}. indice: {self.indice}contiene {self.contiene}")
                # si tienes algo en el mouse y la casilla no contiene nada:
                if ahoritaTiene != [] and self.contiene == []:
                    self.contiene.append(ahoritaTiene[0])
                    ahoritaTiene.pop(0)

    def mostrarLoQueContiene(self):
        if self.contiene:
            #Cambiar coordenadas
            self.contiene[0].x = self.x + self.width // 2
            self.contiene[0].y = self.y + self.height // 2
            self.contiene[0].dibujarDefensa()


class RectanguloClaro:
    def __init__(self, x, y, columna, fila, indice):
        self.color = verdefosfo
        self.width = ((width - 450) // 9)
        self.height = ((height - 200) // 5)
        self.x = x
        self.y = y
        self.columna = columna
        self.fila = fila
        self.indice = indice
        self.contiene = []

    def dibujar(self):
        pygame.draw.rect(win, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

    def detectarClick(self, mx, my):
        if (self.y + self.height) > my > self.y:
            if self.x < mx < (self.x + self.width):
                print(
                    f"hizo click en el cuadrado de la columna {self.columna}, fila {self.fila}. indice: {self.indice}, contiene {self.contiene}")
                # si tienes algo en el mouse y la casilla no contiene nada:
                if ahoritaTiene != [] and self.contiene == []:
                    self.contiene.append(ahoritaTiene[0])
                    ahoritaTiene.pop(0)

    def mostrarLoQueContiene(self):
        if self.contiene != []:
            #cambiar las coordenadas
            self.contiene[0].x = self.x + self.width // 2
            self.contiene[0].y = self.y + self.height // 2
            self.contiene[0].dibujarDefensa()


verdefosfo = (79, 222, 59)
verdeoscuro = (28, 184, 6)

mx, my = pygame.mouse.get_pos()

Rectangulos = []

CuadradosPlantas = []

defensasEscogidas = [Piñata(-100, -100), Piñata2(-100, -100), Piñata3(-100, -100), Piñata4(-100, -100),
                     Piñata5(-100, -100)]

ahoritaTiene = []

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
            for cuadrado in CuadradosPlantas:
                cuadrado.detectarClick(mx, my)

    # Crear cuadricula
    if len(Rectangulos) == 0:
        i = 0
        columna = 0
        fila = 0
        for y in range(100, height - 100, (height - 200) // 5):
            if fila % 2 == 0:
                for x in range(200, width - 250, (width - 450) // 9):
                    if columna % 2 == 0:
                        Rectangulos.append(RectanguloClaro(x, y, columna, fila, i))
                        columna += 1
                        i += 1
                    else:
                        Rectangulos.append(RectanguloOscuro(x, y, columna, fila, i))
                        columna += 1
                        i += 1
                fila += 1
            else:
                for x in range(200, width - 250, (width - 450) // 9):
                    if columna % 2 == 0:
                        Rectangulos.append(RectanguloOscuro(x, y, columna, fila, i))
                        columna += 1
                        i += 1
                    else:
                        Rectangulos.append(RectanguloClaro(x, y, columna, fila, i))
                        columna += 1
                        i += 1
                fila += 1
            if columna >= 9:
                columna = 0

    for rectangulo in Rectangulos:
        rectangulo.dibujar()
        rectangulo.mostrarLoQueContiene()

    # Dibujar cuadro plantas
    rectanguloPlantas.dibujarRectangulo()
    if len(CuadradosPlantas) == 0:
        i = 0
        for x in range(457, 853 - 75, 75):
            CuadradosPlantas.append(CuadroPlantas(x, i, 10))
            i += 1

    for cuadro in CuadradosPlantas:
        cuadro.dibujarCuadrado()
        #si esta vacio entonces le metemos el objeto
        if len(cuadro.contains) == 0:
            for defensa in defensasEscogidas:
                #se hace para que no quite de defensas escogidas
                objDefensa = defensa
                cuadro.contains.append(objDefensa)
        # Lo que contiene cada cuadrado
        cuadro.mostrarLoQueContiene()

    # print(mx, my)
    pygame.time.delay(10)
    pygame.display.update()
