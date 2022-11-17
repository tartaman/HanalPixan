import pygame
import random
import os.path

pygame.init()
width = 1280
height = 720
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("xd wachin")
background = pygame.transform.scale(pygame.image.load(os.path.join(".vscode/Imagenes", "aaa.png")), (width, height))

""" 
-Hacer la pala (para quitar plantas) LISTO
- Crear varias plantas y que se ordenen según el cuadrado LISTO
falta:,

- Que disparen 
-Crear enemigos EN PROCESO
-Que se muevan en las líneas
-Que se creen aleatoriamente
-Que se puedan escoger las plantas 
-Segun las plantas escogidas, ordenarlas en la cuadricula de plantas
-Hacer sistema de oleadas
-Precio de las plantas y generador de dinero
-Mecanicas de cada planta
-si el enemigo esta en la fila entonces dispara
"""
run = True
class Projectil:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velx = 3
        self.radio = 10
        self.color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    def dibujar(self):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radio)
    def mover(self):
        self.x += self.velx

    def fuera(self):
        return (self.x > width)


class BotonSig:
    def __init__(self):
        self.x = 1150
        self.y = 0
        self.width = 100
        self.height = 100
        self.color = (60, 179, 113)
        self.clickeable = True
        self.Oleada = 0
    def dibujar(self):
        pygame.draw.rect(win, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

    def detectarClick(self, mx, my):
        if (self.y + self.height) > my > self.y:
            if self.x < mx < (self.x + self.width):
                print("Hizo click")
                self.Oleada += 1
                if len(Enemigos) == 0 and self.clickeable:
                    #si se puede clickear significa que acabo la oleada
                    self.clickeable = False
                    # 5 enemigos por oleada
                    for i in range(self.Oleada * 5):
                        #Aqui podemos poner algo random que agarre a un enemigo de todos los que vamos a tener
                        Enemigos.append(Enemigo())
                        # Lo que vamos a hacer es que cuando el enemigo muera, lo quitamos de la lista y pues muere, sabes
                        # y cuando la lista ya no tenga, va a volver a poner enemigos.
                    for enemigo in Enemigos:
                        enemigo.x += random.randint(0, 10)*35
                print(f"en enemigos hay: {Enemigos}")
                print(f"Oleada: {self.Oleada}")
    def yaSePuede(self, enemigos):
        if enemigos:
            self.clickeable = False
            self.color = (125, 40, 0)
        else:
            self.clickeable = True
            self.color = (60, 179, 113)



class Enemigo:
    def __init__(self):
        self.x = 1155
        self.y = -100
        self.velx = 1
        self.salud = 100
        self.radio = 35
        self.color = (255, 0, 0)
        self.fila = random.randint(0, 4)
        self.hitbox = (self.x - self.radio, self.y-self.radio, self.radio*2, self.radio*2)

    def dibujar(self):
        self.hitbox = (self.x-self.radio, self.y-self.radio, self.radio * 2, self.radio * 2)
        pygame.draw.rect(win, self.color, self.hitbox, 1)
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radio)
    def mover(self):
        self.x -= self.velx

    def fuera(self):
        return (self.x < 0)
    def ySegunSuFila(self):
        """"como no hay switch pos ajam puro if"""
        if self.fila == 0:
            self.y = 150
        if self.fila == 1:
            self.y = 250
        if self.fila == 2:
            self.y = 350
        if self.fila == 3:
            self.y = 450
        if self.fila == 4:
            self.y = 550

    def leDieron(self):
        self.salud -= 10
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
        self.color = (255, 0, 0)

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
        self.projectiles = []
        self.cooldown = 0
        self.daño = 10
        self.nombre = "Piñata"

    def dibujarDefensa(self):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

    # en cuadrado
    def dibujarDefensaEC(self, x, y):
        pygame.draw.circle(win, self.color, (x, y), self.radius)

    def Cooldown(self):
        if self.cooldown >= 30:
            self.cooldown = 0
        elif self.cooldown >= 0:
            self.cooldown += 1
    def atacar(self):
        self.Cooldown()
        if self.cooldown == 0:
            self.projectiles.append(Projectil(self.x, self.y))
        for projectil in self.projectiles:
            projectil.dibujar()
            projectil.mover()
            for enemigo in Enemigos:
                if projectil.y - projectil.radio < enemigo.hitbox[1] + enemigo.hitbox[3] and projectil.y + projectil.radio > enemigo.hitbox[1]:
                    if projectil.x + projectil.radio > enemigo.hitbox[0] and projectil.x - projectil.radio < enemigo.hitbox[0] + enemigo.hitbox[2]:
                        if len(self.projectiles) != 0:
                            self.projectiles.remove(projectil)
                            enemigo.leDieron()
            if projectil.fuera():
                self.projectiles.remove(projectil)



class Piñata2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = ""
        # radio por ahora pq ajam
        self.radius = 35
        self.color = (255, 255, 0)
        self.projectiles = []
        self.cooldown = 0
        self.daño = 10
        self.nombre = "Piñata2"
    def dibujarDefensa(self):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

    def dibujarDefensaEC(self, x, y):
        pygame.draw.circle(win, self.color, (x, y), self.radius)

    def Cooldown(self):
        if self.cooldown >= 50:
            self.cooldown = 0
        elif self.cooldown >= 0:
            self.cooldown += 1
    def atacar(self):
        self.Cooldown()
        if self.cooldown == 0:
            self.projectiles.append(Projectil(self.x, self.y))
        for projectil in self.projectiles:
            projectil.dibujar()
            projectil.mover()
            for enemigo in Enemigos:
                if projectil.y - projectil.radio < enemigo.hitbox[1] + enemigo.hitbox[3] and projectil.y + projectil.radio > enemigo.hitbox[1]:
                    if projectil.x + projectil.radio > enemigo.hitbox[0] and projectil.x - projectil.radio < enemigo.hitbox[0] + enemigo.hitbox[2]:
                        if len(self.projectiles) != 0:
                            self.projectiles.remove(self.projectiles[0])
                            enemigo.leDieron()
            if projectil.fuera():
                self.projectiles.remove(projectil)

class Piñata3:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = ""
        # radio por ahora pq ajam
        self.radius = 35
        self.color = (255, 0, 255)
        self.projectiles = []
        self.cooldown = 0
        self.daño = 10
        self.nombre = "Piñata3"
    def dibujarDefensa(self):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

    def dibujarDefensaEC(self, x, y):
        pygame.draw.circle(win, self.color, (x, y), self.radius)

    def Cooldown(self):
        if self.cooldown >= 40:
            self.cooldown = 0
        elif self.cooldown >= 0:
            self.cooldown += 1
    def atacar(self):
        self.Cooldown()
        if self.cooldown == 0:
            self.projectiles.append(Projectil(self.x, self.y))
        for projectil in self.projectiles:
            projectil.dibujar()
            projectil.mover()
            for enemigo in Enemigos:
                if projectil.y - projectil.radio < enemigo.hitbox[1] + enemigo.hitbox[3] and projectil.y + projectil.radio > enemigo.hitbox[1]:
                    if projectil.x + projectil.radio > enemigo.hitbox[0] and projectil.x - projectil.radio < enemigo.hitbox[0] + enemigo.hitbox[2]:
                        if len(self.projectiles) != 0:
                            self.projectiles.remove(self.projectiles[0])
                            enemigo.leDieron()
            if projectil.fuera():
                self.projectiles.remove(projectil)


class Piñata4:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = ""
        # radio por ahora pq ajam
        self.radius = 35
        self.color = (255, 255, 255)
        self.projectiles = []
        self.cooldown = 0
        self.daño = 10
        self.nombre = "Piñata4"
    def dibujarDefensa(self):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

    def dibujarDefensaEC(self, x, y):
        pygame.draw.circle(win, self.color, (x, y), self.radius)

    def Cooldown(self):
        if self.cooldown >= 10:
            self.cooldown = 0
        elif self.cooldown >= 0:
            self.cooldown += 1
    def atacar(self):
        self.Cooldown()
        if self.cooldown == 0:
            self.projectiles.append(Projectil(self.x, self.y))
        for projectil in self.projectiles:
            projectil.dibujar()
            projectil.mover()
            for enemigo in Enemigos:
                if projectil.y - projectil.radio < enemigo.hitbox[1] + enemigo.hitbox[3] and projectil.y + projectil.radio > enemigo.hitbox[1]:
                    if projectil.x + projectil.radio > enemigo.hitbox[0] and projectil.x - projectil.radio < enemigo.hitbox[0] + enemigo.hitbox[2]:
                        if len(self.projectiles) != 0:
                            self.projectiles.remove(self.projectiles[0])
                            enemigo.leDieron()
            if projectil.fuera():
                self.projectiles.remove(projectil)

class Piñata5:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = ""
        # radio por ahora pq ajam
        self.radius = 35
        self.color = (0, 255, 255)
        self.projectiles = []
        self.cooldown = 0
        self.daño = 10
        self.nombre = "Piñata5"
    def dibujarDefensa(self):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

    def dibujarDefensaEC(self, x, y):
        pygame.draw.circle(win, self.color, (x, y), self.radius)

    def Cooldown(self):
        if self.cooldown >= 20:
            self.cooldown = 0
        elif self.cooldown >= 0:
            self.cooldown += 1
    def atacar(self):
        self.Cooldown()
        if self.cooldown == 0:
            self.projectiles.append(Projectil(self.x, self.y))
        for projectil in self.projectiles:
            projectil.dibujar()
            projectil.mover()
            for enemigo in Enemigos:
                if projectil.y - projectil.radio < enemigo.hitbox[1] + enemigo.hitbox[3] and projectil.y + projectil.radio > enemigo.hitbox[1]:
                    if projectil.x + projectil.radio > enemigo.hitbox[0] and projectil.x - projectil.radio < enemigo.hitbox[0] + enemigo.hitbox[2]:
                        if len(self.projectiles) != 0:
                            self.projectiles.remove(self.projectiles[0])
                            enemigo.leDieron()
            if projectil.fuera():
                self.projectiles.remove(projectil)

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
        # todo //IMPORTANTE va a contener una piñata por pruebas, pero luego que hagamos para que escoja las plantas, va a
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
                    # todo Crea un objeto nuevo fuera de la pantalla para agregar necesitamos if que digan que planta es para ponerla
                    if self.contains[self.indice].nombre == "Piñata":
                        defensa = Piñata(self.contains[self.indice].x, self.contains[self.indice].y)
                        ahoritaTiene.append(defensa)
                    elif self.contains[self.indice].nombre == "Piñata2":
                        defensa = Piñata2(self.contains[self.indice].x, self.contains[self.indice].y)
                        ahoritaTiene.append(defensa)
                    elif self.contains[self.indice].nombre == "Piñata3":
                        defensa = Piñata3(self.contains[self.indice].x, self.contains[self.indice].y)
                        ahoritaTiene.append(defensa)
                    elif self.contains[self.indice].nombre == "Piñata4":
                        defensa = Piñata4(self.contains[self.indice].x, self.contains[self.indice].y)
                        ahoritaTiene.append(defensa)
                    elif self.contains[self.indice].nombre == "Piñata5":
                        defensa = Piñata5(self.contains[self.indice].x, self.contains[self.indice].y)
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
        pygame.draw.rect(win, self.color, pygame.Rect(self.x, self.y, self.width, self.height), 1)

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
                        defensas.remove(self.contiene[0])
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
        pygame.draw.rect(win, self.color, pygame.Rect(self.x, self.y, self.width, self.height),1)

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
                        defensas.remove(self.contiene[0])
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


verdefosfo = (255, 255, 255)
verdeoscuro = (255, 255, 255)

mx, my = pygame.mouse.get_pos()

Rectangulos = []

CuadradosPlantas = []

defensasEscogidas = [Piñata(-100, -100), Piñata2(-100, -100), Piñata3(-100, -100), Piñata4(-100, -100),
                     Piñata5(-100, -100)]
# todo crear enemigos
Enemigos = []

ahoritaTiene = []

defensas = []

cosasEnRectangulos = 0
rectanguloPlantas = RectanguloPlantas(((width - (width // 3)) // 2), 0)
cuadroPala = CuadroPala(0, 0)
botonSig = BotonSig()
while run:
    win.fill((0, 0, 0))
    mx, my = pygame.mouse.get_pos()
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.QUIT:
            run = False
        # todo aqui abajo se pone lo que necesite ser con click
        if event.type == pygame.MOUSEBUTTONDOWN:
            for rectangulo in Rectangulos:
                rectangulo.detectarClick(mx, my)
            for cuadrado in CuadradosPlantas:
                cuadrado.detectarClick(mx, my)
            cuadroPala.detectarClick(mx, my)
            botonSig.detectarClick(mx, my)
    win.blit(background, (0, 0))
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
        if rectangulo.contiene and rectangulo.contiene[0] not in defensas:
            defensanueva = rectangulo.contiene[0]
            defensas.append(defensanueva)
    for defensa in defensas:
        if not botonSig.clickeable:
            defensa.atacar()
        else:
            defensa.projectiles = []



    # Dibujar cuadro plantas
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
        if enemigo.fuera():
            Enemigos.remove(enemigo)
        if enemigo.seMurio():
            Enemigos.remove(enemigo)
    #Siempre checar si el boton se puede clickear
    botonSig.yaSePuede(Enemigos)
    for cosa in ahoritaTiene:
        if cosa != "Quitara":
            if cosa.nombre == "Piñata":
                nuevacosa = Piñata(mx,my)
                pygame.draw.circle(win,nuevacosa.color,(nuevacosa.x,nuevacosa.y),nuevacosa.radius)
            if cosa.nombre == "Piñata2":
                nuevacosa = Piñata2(mx,my)
                pygame.draw.circle(win,nuevacosa.color,(nuevacosa.x,nuevacosa.y),nuevacosa.radius)
            if cosa.nombre == "Piñata3":
                nuevacosa = Piñata3(mx,my)
                pygame.draw.circle(win,nuevacosa.color,(nuevacosa.x,nuevacosa.y),nuevacosa.radius)
            if cosa.nombre == "Piñata4":
                nuevacosa = Piñata4(mx,my)
                pygame.draw.circle(win,nuevacosa.color,(nuevacosa.x,nuevacosa.y),nuevacosa.radius)
            if cosa.nombre == "Piñata5":
                nuevacosa = Piñata5(mx,my)
                pygame.draw.circle(win,nuevacosa.color,(nuevacosa.x,nuevacosa.y),nuevacosa.radius)
    #print(mx, my)
    #print(defensas)
    pygame.display.update()
