import pygame
import random

pygame.init()
width = 1280
height = 720
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("xd wachin")

""" 
-Hacer la pala (para quitar plantas) LISTO
- Crear varias plantas y que se ordenen según el cuadrado LISTO
falta:

- Que disparen 
-Crear enemigos EN PROCESO
-Que se muevan en las líneas
-Que se creen aleatoriamente
-Que se puedan escoger las plantas 
-Segun las plantas escogidas, ordenarlas en la cuadricula de plantas
-Hacer sistema de oleadas
-Precio de las plantas y generador de dinero
-Mecanicas de cada planta
"""
run = True
Oleada = 1


class BotonSig:
    def __init__(self):
        self.x = 1150
        self.y = 0
        self.width = 100
        self.height = 100
        self.color = (60, 179, 113)
        self.clickeable = True
    def dibujar(self):
        pygame.draw.rect(win, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

    def detectarClick(self, mx, my):
        if (self.y + self.height) > my > self.y:
            if self.x < mx < (self.x + self.width):
                print("Hizo click")

                if len(Enemigos) == 0 and self.clickeable:
                    #si se puede clickear significa que acabo la oleada
                    self.clickeable = False
                    # todo 5 enemigos por oleada
                    for i in range(Oleada * 5):
                        Enemigos.append(Enemigo())
                        # Lo que vamos a hacer es que cuando el enemigo muera, lo quitamos de la lista y pues muere, sabes
                        # y cuando la lista ya no tenga, va a volver a poner enemigos.
                print(f"en enemigos hay: {Enemigos}")



class Enemigo:
    def __init__(self):
        self.x = 1155
        self.y = -100
        self.velx = 3
        self.salud = 100
        self.fila = random.randint(0, 4)

    def dibujar(self):
        pygame.draw.circle(win, (0, 0, 0), (self.x, self.y), 35)
    def mover(self):
        self.x -= self.velx
    def ySegunSuFila(self):
        """"como no hay switch pos ajam puro if"""
        if fila == 0:
            self.y = 150
        if fila == 1:
            self.y = 250
        if fila == 2:
            self.y = 350
        if fila == 3:
            self.y = 450
        if fila == 4:
            self.y = 550
    def seMurio(self):
        if self.salud > 0:
            return False
        else:
            return True

class CuadroPala:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 100
        self.height = 100
        self.color = (0, 0, 0)

    def dibujar(self):
        pygame.draw.rect(win, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

    def detectarClick(self, mx, my):
        if (self.y + self.height) > my > self.y:
            if self.x < mx < (self.x + self.width):
                if len(ahoritaTiene) == 0:
                    print("pala")
                    ahoritaTiene.append("Quitara")
                    print(f"ahorita tiene: {ahoritaTiene}")


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

    # en cuadrado
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
        # todo// IMPORTANTE va a contener una piñata por pruebas, pero luego que hagamos para que escoja las plantas, va a
        # todo// contener [] y luego vamos a recorrer el arreglo de plantas escogidas y ponerle a cada uno lo que contiene
        self.contains = []

    def dibujarCuadrado(self):
        pygame.draw.rect(win, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

    def detectarClick(self, mx, my):
        if (self.y + self.height) > my > self.y:
            if self.x < mx < (self.x + self.width):
                print(f"Escogio el cuadrado {self.indice}, que contiene {self.contains}")
                # todo si no tiene agarrado nada entonces agarra si no pues no vea
                if len(ahoritaTiene) == 0:
                    # todo Crea un objeto nuevo fuera de la pantalla para agregar
                    defensa = self.contains[self.indice]
                    ahoritaTiene.append(defensa)
                    print(f"ahorita tiene: {ahoritaTiene}")
                if ahoritaTiene[0] == "Quitara":
                    ahoritaTiene.pop()
                    print(f"Ahorita tiene: {ahoritaTiene}")

    def mostrarLoQueContiene(self):
        self.contains[self.indice].x = self.x + self.width // 2
        self.contains[self.indice].y = self.y + self.height // 2
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
                if ahoritaTiene != [] and self.contiene == [] and ahoritaTiene[0] != "Quitara":
                    self.contiene.append(ahoritaTiene[0])
                    ahoritaTiene.pop(0)
                    print(f"ahorita tiene: {ahoritaTiene}")
                if len(ahoritaTiene) != 0:
                    if ahoritaTiene[0] == "Quitara" and self.contiene != []:
                        self.contiene.remove(self.contiene[0])
                        print("lo quito")
                    if ahoritaTiene[0] == "Quitara" and self.contiene == []:
                        ahoritaTiene.pop()
                        print(f"Ahorita tiene {ahoritaTiene}")

    def mostrarLoQueContiene(self):
        if self.contiene:
            # Cambiar coordenadas
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
                if ahoritaTiene != [] and self.contiene == [] and ahoritaTiene[0] != "Quitara":
                    self.contiene.append(ahoritaTiene[0])
                    ahoritaTiene.pop(0)
                    print(f"ahorita tiene: {ahoritaTiene}")
                if len(ahoritaTiene) != 0:
                    if ahoritaTiene[0] == "Quitara" and self.contiene != []:
                        self.contiene.remove(self.contiene[0])
                        print("lo quito")
                    if ahoritaTiene[0] == "Quitara" and self.contiene == []:
                        ahoritaTiene.pop()
                        print(f"Ahorita tiene {ahoritaTiene}")

    def mostrarLoQueContiene(self):
        if self.contiene != []:
            # cambiar las coordenadas
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
# todo crear enemigos
Enemigos = []

ahoritaTiene = []

rectanguloPlantas = RectanguloPlantas(((width - (width // 3)) // 2), 0)
cuadroPala = CuadroPala(0, 0)
botonSig = BotonSig()
while run:
    win.fill((255, 255, 255))
    mx, my = pygame.mouse.get_pos()
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.QUIT:
            run = False
        # todo aqui abajo se pone lo que necesite ser con click
        if event.type == pygame.MOUSEBUTTONUP:
            for rectangulo in Rectangulos:
                rectangulo.detectarClick(mx, my)
            for cuadrado in CuadradosPlantas:
                cuadrado.detectarClick(mx, my)
            cuadroPala.detectarClick(mx, my)
            botonSig.detectarClick(mx, my)

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
        # si esta vacio entonces le metemos el objeto
        if len(cuadro.contains) == 0:
            for defensa in defensasEscogidas:
                # se hace para que no quite de defensas escogidas
                objDefensa = defensa
                cuadro.contains.append(objDefensa)
        # Lo que contiene cada cuadrado
        cuadro.mostrarLoQueContiene()
    # Dibujar pala
    cuadroPala.dibujar()
    #Dibujar boton sig
    botonSig.dibujar()
    #Dibujar enemigos si hay enemigos
    
    for enemigo in Enemigos:
        enemigo.ySegunSuFila()
        enemigo.dibujar()
        enemigo.mover()

    #print(mx, my)
    pygame.time.delay(10)
    pygame.display.update()
