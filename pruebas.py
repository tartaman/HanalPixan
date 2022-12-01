import pygame
import random
import os.path

# todo Esto falta namas y nos podemos ir a matar
"""  
falta:,
no]]
"""
#toDO cosas para cargar imagenes
flame =[pygame.transform.scale(pygame.image.load(os.path.join(".vscode/Imagenes/flame", "0.png")), (70, 70)),
        pygame.transform.scale(pygame.image.load(os.path.join(".vscode/Imagenes/flame", "1.png")), (70, 70)),
        pygame.transform.scale(pygame.image.load(os.path.join(".vscode/Imagenes/flame", "2.png")), (70, 70)),
        pygame.transform.scale(pygame.image.load(os.path.join(".vscode/Imagenes/flame", "3.png")), (70, 70)),
        pygame.transform.scale(pygame.image.load(os.path.join(".vscode/Imagenes/flame", "4.png")), (70, 70)),
        pygame.transform.scale(pygame.image.load(os.path.join(".vscode/Imagenes/flame", "5.png")), (70, 70)),
        pygame.transform.scale(pygame.image.load(os.path.join(".vscode/Imagenes/flame", "6.png")), (70, 70)),
        pygame.transform.scale(pygame.image.load(os.path.join(".vscode/Imagenes/flame", "0.png")), (70, 70))]
cuadrosplantas = [pygame.image.load(os.path.join(".vscode/Imagenes/Plantas", "1.png")),
                  pygame.image.load(os.path.join(".vscode/Imagenes/Plantas", "2.png")),
                  pygame.image.load(os.path.join(".vscode/Imagenes/Plantas", "3.png")),
                  pygame.image.load(os.path.join(".vscode/Imagenes/Plantas", "4.png")),
                  pygame.image.load(os.path.join(".vscode/Imagenes/Plantas", "5.png"))]

girasol=pygame.transform.scale(pygame.image.load(os.path.join(".vscode/Imagenes", "calavera.png")), (70, 70))
mazapan= pygame.image.load(os.path.join(".vscode/Imagenes", "mazapan.png"))
piñata = pygame.image.load(os.path.join(".vscode/Imagenes", "pinnata.png"))
maiz = pygame.image.load(os.path.join(".vscode/Imagenes", "maiz.png"))
dulce= pygame.transform.scale(pygame.image.load(os.path.join(".vscode/Imagenes", "dulce.png")), (30,30))
balamaiz = pygame.transform.scale(pygame.image.load(os.path.join(".vscode/Imagenes", "balamaiz.png")),(30,30))
merengue = pygame.transform.scale(pygame.image.load(os.path.join(".vscode/Imagenes", "merengue.png")),(80, 80))

# todo Cosas importantes del juego
pygame.init()
width = 1280
height = 720
clock = pygame.time.Clock()
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Alpha")
XD= pygame.transform.scale(pygame.image.load(os.path.join(".vscode/Imagenes", "gameoverphrase.jpg")), (width, height))
background = pygame.transform.scale(pygame.image.load(os.path.join(".vscode/Imagenes", "aaa.png")), (width, height))
mx, my = pygame.mouse.get_pos()
Rectangulos = []
CuadradosPlantas = []
recursos = 1000
nuevacosa = 0
run = True
font = pygame.font.Font('freesansbold.ttf', 25)
text = font.render(str(recursos), True, (0,0,0))

# todo Cosas de los proyectiles
class Projectil:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velx = 5
        self.radio = 15
        self.image = dulce
    def dibujar(self):
        win.blit(self.image, (self.x-self.radio+2, self.y-self.radio))
    def mover(self):
        self.x += self.velx

    def fuera(self):
        return (self.x > width)


class ProjectilTeledirigido(Projectil):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.velx = 5
        self.vely = 5
        self.radio = 15
        self.image = balamaiz

    def dirigir(self, enemigox, enemigoy):
        if self.x > enemigox:
            self.x -= self.velx
        if self.x < enemigox:
            self.x += self.velx
        if self.y > enemigoy:
            self.y -= self.vely
        if self.y < enemigoy:
            self.y += self.vely


# Todo cosas relacionadas a botones
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
        i = 0
        if (self.y + self.height) > my > self.y:
            if self.x < mx < (self.x + self.width):
                print("Hizo click")
                if len(Enemigos) == 0 and self.clickeable:
                    self.Oleada += 1
                    #si se puede clickear significa que acabo la oleada
                    self.clickeable = False
                    # 5 enemigos por oleada
                    for i in range(self.Oleada * 5):
                        #Aqui podemos poner algo random que agarre a un enemigo de todos los que vamos a tener
                        Enemigos.append(Enemigo())
                        # Lo que vamos a hacer es que cuando el enemigo muera, lo quitamos de la lista y pues muere, sabes
                        # y cuando la lista ya no tenga, va a volver a poner enemigos.
                    if self.Oleada >=3:
                        for i in range(self.Oleada//2):
                            Enemigos.append(Enemigo2())
                    for enemigo in Enemigos:
                        enemigo.x += i
                        i += 120
                        enemigo.velx += self.Oleada*0.1
                print(f"en enemigos hay: {Enemigos}")
                print(f"Oleada: {self.Oleada}")
    def yaSePuede(self, enemigos):
        if enemigos:
            self.clickeable = False
            self.color = (125, 40, 0)
        else:
            self.clickeable = True
            self.color = (60, 179, 113)


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


class cuadroSoles:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 90
        self.height = 85
        self.color = (91, 44, 111)
        self.color2= (165, 105, 189 )

    def dibujar(self,win):
        pygame.draw.rect(win, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
        pygame.draw.rect(win, self.color2, pygame.Rect(self.x+15, self.y+5, self.width-27, self.height-40))
        win.blit(flame[3],(self.x+13, self.y-5))
        text = font.render(str(recursos), True, (255,255,255))
        win.blit(text, (self.x+32,self.y+55))



# Todo cosas relacionadas a los enemigos
class Enemigo:
    def __init__(self):
        self.x = 1155
        self.y = -100
        self.velx = 1
        self.salud = 100
        self.radio = 35
        self.daño = 1
        self.color = (self.salud, 0, 0)
        self.fila = random.randint(0, 4)
        self.hitbox = (self.x - self.radio, self.y-self.radio, self.radio*2, self.radio*2)
        self.comiendo = False

    def dibujar(self):
        self.hitbox = (self.x-self.radio, self.y-self.radio, self.radio * 2, self.radio * 2)
        pygame.draw.circle(win,self.color, (self.x, self.y), self.radio)
    def mover(self):
        self.x -= self.velx
    def posicion(self):
        return self.x

    def fuera(self):
        return (self.x < 185)
    def ySegunSuFila(self):
        if self.fila == 0:
            self.y = 150
        elif self.fila == 1:
            self.y = 250
        elif self.fila == 2:
            self.y = 350
        elif self.fila == 3:
            self.y = 450
        elif self.fila == 4:
            self.y = 550

    def leDieron(self, daño):
        self.salud -= daño
    def seMurio(self):
        if self.salud > 0:
            return False
        else:
            return True

    def leDioAAlgo(self):
        for defensax in defensas:
            if self.y - self.radio < defensax.hitbox[1] + defensax.hitbox[3] and self.y + self.radio > defensax.hitbox[1]:
                if self.x + self.radio > defensax.hitbox[0] and self.x - self.radio < defensax.hitbox[0] + defensax.hitbox[2]:
                    if self.fila == defensax.fila:
                        self.velx = 0
                        self.color = (255, 255, 255)
                        defensax.leDieron(self.daño)
                        if defensax.semurio():
                            defensas.remove(defensax)
                            self.reset()

                    else:
                        self.reset()
    def reset(self):
        self.velx = 1
        self.color = (255, 0, 0)
        self.comiendo = False

#Enemigo 2 pq era muy bueno
class Enemigo2(Enemigo):
    def __init__(self):
        self.x = 1155
        self.y = -100
        self.velx = 2
        self.salud = 100
        self.radio = 35
        self.daño = 1
        self.color = (0, 255, 0)
        self.fila = random.randint(0, 4)
        self.hitbox = (self.x - self.radio, self.y - self.radio, self.radio * 2, self.radio * 2)
        self.comiendo = False


# todo cosas relacionadas a plantas

class Piñata:
    def __init__(self, x, y, fila= -3):
        self.x = x
        self.y = y
        self.image = ""
        self.fila = fila
        # radio por ahora pq ajam
        self.radius = 35
        self.color = (255, 0, 0)
        self.projectiles = []
        self.cooldown = 0
        self.daño = 10
        self.recursos = recursos
        self.vida = 100
        self.nombre = "Piñata"
        self.hitbox = (self.x - self.radius, self.y - self.radius, self.radius*2, self.radius*2)
        self.precio = 100
    def dibujarDefensa(self, win):
        self.hitbox = (self.x - self.radius, self.y - self.radius, self.radius*2, self.radius*2)
        win.blit(piñata, (self.x-self.radius-10, self.y-self.radius-15))

    def dibujarcarta(self,  win):
        win.blit(cuadrosplantas[0], (self.x-self.radius, self.y-self.radius-5))

    # en cuadrado
    def dibujarDefensaEC(self, x, y):
        pygame.draw.circle(win, self.color, (x, y), self.radius)

    def Cooldown(self):
        if self.cooldown >= 100:
            self.cooldown = 0
        elif self.cooldown >= 0:
            self.cooldown += 1
    def atacar(self):
        self.Cooldown()
        if self.cooldown == 0:
            self.projectiles.append(Projectil(self.x+30, self.y-5))
        for projectil in self.projectiles:
            projectil.dibujar()
            projectil.mover()
            for enemigo in Enemigos:
                if projectil.y - projectil.radio < enemigo.hitbox[1] + enemigo.hitbox[3] and projectil.y + projectil.radio > enemigo.hitbox[1]:
                    if projectil.x + projectil.radio > enemigo.hitbox[0] and projectil.x - projectil.radio < enemigo.hitbox[0] + enemigo.hitbox[2]:
                        if len(self.projectiles) != 0:
                            try:
                                self.projectiles.remove(projectil)
                            except:
                                pass
                            enemigo.leDieron(self.daño)
            if projectil.fuera():
                try:
                    self.projectiles.remove(projectil)
                except:
                    pass

    def semurio(self):
        if self.vida <= 0:
            return True
        elif self.vida > 0:
            return False

    def leDieron(self, daño):
        self.vida -= daño


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
        self.daño = 20
        self.vida = 100
        self.nombre = "Piñata2"
        self.hitbox = (self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)
        self.precio = 150
        self.soles = 0

    def dibujarDefensa(self,win):
        self.hitbox = (self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)
        win.blit(maiz, (self.x-self.radius-10, self.y-self.radius-15))

    def dibujarcarta(self,  win):
        win.blit(cuadrosplantas[4], (self.x-self.radius, self.y-self.radius-5))

    def dibujarDefensaEC(self, x, y):
        pygame.draw.circle(win, self.color, (x, y), self.radius)

    def Cooldown(self):
        if self.cooldown >= 500:
            self.cooldown = 0
        elif self.cooldown >= 0:
            self.cooldown += 1
    def atacar(self):
        self.Cooldown()
        if self.cooldown == 0:
            self.projectiles.append(ProjectilTeledirigido(self.x, self.y))
        for projectil in self.projectiles:
            projectil.dibujar()
            try:
                projectil.dirigir(Enemigos[0].x, Enemigos[0].y)
            except:
                pass
            for enemigo in Enemigos:
                if projectil.y - projectil.radio < enemigo.hitbox[1] + enemigo.hitbox[3] and projectil.y + projectil.radio > enemigo.hitbox[1]:
                    if projectil.x + projectil.radio > enemigo.hitbox[0] and projectil.x - projectil.radio < enemigo.hitbox[0] + enemigo.hitbox[2]:
                        if len(self.projectiles) != 0:
                            try:
                                self.projectiles.remove(self.projectiles[0])
                            except:
                                print("xd")
                            enemigo.leDieron(self.daño)
            if projectil.fuera():
                try:
                    self.projectiles.remove(projectil)
                except:
                    print("xd")
    def semurio(self):
        if self.vida <= 0:
            return True
        elif self.vida > 0:
            return False
    def leDieron(self, daño):
        self.vida -= daño


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
        self.vida = 50
        self.nombre = "Piñata3"
        self.hitbox = (self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)
        self.precio = 75
        self.soles = 0

    def dibujarDefensa(self, win):
        self.hitbox = (self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)
        win.blit(merengue, (self.x-self.radius-10, self.y-self.radius-15))

    def dibujarcarta(self,  win):
        win.blit(cuadrosplantas[3], (self.x-self.radius, self.y-self.radius-5))

    def dibujarDefensaEC(self, x, y):
        pygame.draw.circle(win, self.color, (x, y), self.radius)

    def Cooldown(self):
        if self.cooldown >= 40:
            self.cooldown = 0
        elif self.cooldown >= 0:
            self.cooldown += 1
    def atacar(self):
        print("a")

    def semurio(self):
        if self.vida <= 0:
            return True
        elif self.vida > 0:
            return False
    def leDieron(self, daño):
        self.vida -= daño


class Nuez:
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
        self.vida = 3000
        self.nombre = "Nuez"
        self.hitbox = (self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)
        self.precio = 50
        self.soles = 0

    def dibujarDefensa(self,win):
        self.hitbox = (self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)
        win.blit(mazapan, (self.x-self.radius-10, self.y-self.radius-10))

    def dibujarcarta(self,  win):
        win.blit(cuadrosplantas[2], (self.x-self.radius, self.y-self.radius-5))

    def dibujarDefensaEC(self, x, y):
        pygame.draw.circle(win, self.color, (x, y), self.radius)

    def atacar(self):
        print("o")

    def semurio(self):
        if self.vida <= 0:
            return True
        elif self.vida > 0:
            return False
    def leDieron(self, daño):
        self.vida -= daño


class Girasol:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = ""
        # radio por ahora pq ajam
        self.radius = 35
        self.color = (0, 255, 255)
        self.cooldown = 0
        self.vida = 100
        self.nombre = "Girasol"
        self.hitbox = (self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)
        self.precio = 50

    def dibujarDefensa(self,win):
        self.hitbox = (self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)
        win.blit(girasol, (self.x-self.radius, self.y-self.radius))

    def dibujarcarta(self,  win):
        win.blit(cuadrosplantas[1], (self.x-self.radius, self.y-self.radius-5))

    def dibujarDefensaEC(self, x, y):
        pygame.draw.circle(win, self.color, (x, y), self.radius)

    def Cooldowndesol(self):
        if self.cooldown >= 454:
            self.cooldown = 0
        elif self.cooldown >= 0:
            self.cooldown += 1

    def atacar(self):
        self.Cooldowndesol()
        if self.cooldown == 0:
            generarcalaveras(self.x, self.y, 1)

    def semurio(self):
        if self.vida <= 0:
            return True
        elif self.vida > 0:
            return False

    def leDieron(self, daño):
        self.vida -= daño


class null:
    def sepuede(self):
        return False


#todo cosas relacionadas a las calaveras
class calaveras:
    def __init__(self,x ,y):
        self.x = x
        self.y = y
        self.radio = 20
        self.hitbox = (self.x - self.radio, self.y - self.radio, self.radio * 2, self.radio * 2)
        self.mx = mx
        self.my = my
        self.vely = 4
        self.click = False
        self.stepIndex = 0

    def saltar(self,win):
        self.hitbox = (self.x-self.radio, self.y-self.radio, self.radio*2, self.radio*2)

        self.y -= self.vely
        self.vely -= 0.15
        if self.vely < -4:
            self.vely = 4
        if self.stepIndex >= 8:
            self.stepIndex = 0
        win.blit(flame[self.stepIndex], (self.x-self.radio*2+10, self.y-self.radio*2))
        self.stepIndex += 1


    def direction(self):
        pygame.draw.rect(win, (0, 0, 0), pygame.Rect(self.hitbox), 1)

    def detectar_click(self, mx, my):
        if (self.y + self.radio) > my > (self.y - self.radio):
            if self.x - self.radio < mx < (self.x + self.radio):
                self.click = True
        return self.click

def generarcalaveras(x,y,state):
    if state == 0:
        x = random.randint(15, 115)
        y = random.randint(161, 478)
    else:
        x = x
        y = y
    soles.append(calaveras(x, y))
    print("se genero sol xd")


#todo Cosas de la rejilla (NO TOCAR SI NO SE MUERE)
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
        self.height = 80
        self.x = x
        self.y = y
        self.indice = indice
        # todo //IMPORTANTE va a contener una piñata por pruebas, pero luego que hagamos para que escoja las plantas, va a
        # todo// contener [] y luego vamos a recorrer el arreglo de plantas escogidas y ponerle a cada uno lo que contiene
        self.contains = []

    def dibujarCuadrado(self):
        pygame.draw.rect(win, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

    def detectarClick(self, mx, my):
        global recursos
        global defensa
        if (self.y + self.height) > my > self.y:
            if self.x < mx < (self.x + self.width):
                print(f"Escogio el cuadrado {self.indice}, que contiene {self.contains}")
                # todo si no tiene agarrado nada entonces agarra si no pues no vea
                if len(ahoritaTiene) == 0:
                    # todo Crea un objeto nuevo fuera de la pantalla para agregar necesitamos if que digan que planta es para ponerla
                    if self.contains[self.indice].nombre == "Piñata":
                        defensa = Piñata(self.contains[self.indice].x, self.contains[self.indice].y)

                    elif self.contains[self.indice].nombre == "Piñata2":
                        defensa = Piñata2(self.contains[self.indice].x, self.contains[self.indice].y)

                    elif self.contains[self.indice].nombre == "Piñata3":
                        defensa = Piñata3(self.contains[self.indice].x, self.contains[self.indice].y)

                    elif self.contains[self.indice].nombre == "Nuez":
                        defensa = Nuez(self.contains[self.indice].x, self.contains[self.indice].y)

                    elif self.contains[self.indice].nombre == "Girasol":
                        defensa = Girasol(self.contains[self.indice].x, self.contains[self.indice].y)
                    if recursos >= defensa.precio:
                        recursos -= defensa.precio
                        ahoritaTiene.append(defensa)

                    print(f"ahorita tiene: {ahoritaTiene}")
                if ahoritaTiene:
                    if ahoritaTiene[0] == "Quitara":
                        ahoritaTiene.pop()
                        print(f"Ahorita tiene: {ahoritaTiene}")

    def mostrarLoQueContiene(self):
        self.contains[self.indice].x = self.x + self.width // 2
        self.contains[self.indice].y = self.y + self.height // 2
        self.contains[self.indice].dibujarcarta(win)


class RectanguloOscuro:
    def __init__(self, x, y, columna, fila, indice):
        self.color = (255, 255, 255)
        self.width = ((width - 450) // 9)
        self.height = ((height - 240) // 5)
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
                try:
                    print(
                        f"hizo click en el cuadrado de la columna {self.columna}, fila {self.fila}. indice: {self.indice}contiene {self.contiene} y este tiene de vida {self.contiene[0].vida}")
                except:
                    print("ups")
                # si tienes algo en el mouse y la casilla no contiene nada:
                if ahoritaTiene != [] and self.contiene == [] and ahoritaTiene[0] != "Quitara":
                    self.contiene.append(ahoritaTiene[0])
                    self.contiene[0].fila = self.fila
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
            self.contiene[0].dibujarDefensa(win)


def dibujar_cosas():
    win.blit(background, (0, 0))
defensasEscogidas = [Piñata(-100, -100), Piñata2(-100, -100), Piñata3(-100, -100), Nuez(-100, -100),
                     Girasol(-100, -100)]

def gameover(win):
    for rectangulo in Rectangulos:
        rectangulo.dibujar()
        rectangulo.mostrarLoQueContiene()
        if rectangulo.contiene:
            defensas.remove(rectangulo.contiene[0])
            rectangulo.contiene = []
    for enemigo in Enemigos:
        Enemigos.remove(enemigo)
    win.blit(XD, (0, 0))


# todo crear enemigos
Enemigos = []
ahoritaTiene = []
defensas = []
soles = []
cosasEnRectangulos = 0
rectanguloPlantas = RectanguloPlantas(((width - (width // 3)) // 2), 0)
cuadroPala = CuadroPala(0, 0)
cuadroSoles = cuadroSoles(360, 8)
botonSig = BotonSig()
click = False
cooldown= 0
temoriste = False

# Todo loop principal
while run:
    userInput = pygame.key.get_pressed()
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.QUIT:
            run = False
    if not temoriste:
        win.fill((0, 0, 0))
        mx, my = pygame.mouse.get_pos()
        dibujar_cosas()

        for event in ev:
            # todo aqui abajo se pone lo que necesite ser con click
            if event.type == pygame.MOUSEBUTTONDOWN:
                for rectangulo in Rectangulos:
                    rectangulo.detectarClick(mx, my)
                for cuadrado in CuadradosPlantas:
                    cuadrado.detectarClick(mx, my)
                for solesitos in soles:
                    click = solesitos.detectar_click(mx, my)
                    if (click):
                        recursos += 50
                        print(f"ahora tiene {recursos} soles")
                        soles.remove(solesitos)

                cuadroPala.detectarClick(mx, my)
                botonSig.detectarClick(mx, my)

        # Todo Crear cuadricula
        if len(Rectangulos) == 0:
            i = 0
            columna = 0
            fila = 0
            for y in range(112, height - 128, (height - 240) // 5):
                    for x in range(208, width - 242, (width - 450) // 9):
                            Rectangulos.append(RectanguloOscuro(x, y, columna, fila, i))
                            columna += 1
                            i += 1
                    fila += 1

        for rectangulo in Rectangulos:
            rectangulo.dibujar()
            rectangulo.mostrarLoQueContiene()
            if rectangulo.contiene:
                if rectangulo.contiene[0] not in defensas:
                    defensanueva = rectangulo.contiene[0]
                    defensas.append(defensanueva)
                if rectangulo.contiene[0].semurio():
                    print(f"semurio la planta {rectangulo.contiene[0].nombre}, en la fila {rectangulo.fila}, columna {rectangulo.columna}")
                    if rectangulo.contiene[0].nombre == "Piñata3":
                        ecosperoshion = ((rectangulo.contiene[0].x - rectangulo.contiene[0].radius) - 92, (rectangulo.contiene[0].y - rectangulo.contiene[0].radius) - 96, 276, 288)
                        pygame.draw.rect(win, (255,255,255), pygame.Rect(ecosperoshion))
                        for enemigo in Enemigos:
                            if enemigo.y - enemigo.radio <= ecosperoshion[1] + ecosperoshion[3] and enemigo.y + enemigo.radio >= ecosperoshion[1]:
                                if enemigo.x + enemigo.radio >= ecosperoshion[0] and enemigo.x - enemigo.radio <= ecosperoshion[0] + ecosperoshion[2]:
                                    Enemigos.remove(enemigo)
                    defensas.remove(rectangulo.contiene[0])
                    rectangulo.contiene.pop()
        for defensa in defensas:
            if not botonSig.clickeable:
                defensa.atacar()
            else:
                defensa.projectiles = []


        # Todo Dibujar cuadro plantas
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
        #dibujar soles
        cuadroSoles.dibujar(win)


        #TOdo Dibujar enemigos si hay enemigos
        for enemigo in Enemigos:
            enemigo.ySegunSuFila()
            enemigo.dibujar()
            enemigo.mover()
            enemigo.leDioAAlgo()
            if enemigo.fuera():
                temoriste = True
            if enemigo.seMurio():
                Enemigos.remove(enemigo)



        # Todo Siempre checar si el boton se puede clickear
        botonSig.yaSePuede(Enemigos)
        for cosa in ahoritaTiene:
            if cosa != "Quitara":
                if cosa.nombre == "Piñata":
                    nuevacosa = Piñata(mx,my)
                elif cosa.nombre == "Piñata2":
                    nuevacosa = Piñata2(mx,my)
                elif cosa.nombre == "Piñata3":
                    nuevacosa = Piñata3(mx,my)
                elif cosa.nombre == "Nuez":
                    nuevacosa = Nuez(mx,my)
                elif cosa.nombre == "Girasol":
                    nuevacosa = Girasol(mx,my)
                nuevacosa.dibujarDefensa(win)
            else:
                pygame.draw.circle(win, (0, 0, 0), (mx, my), 25)

        # Todo soles
        if not botonSig.clickeable:
            if not temoriste:
                if cooldown >= 500:
                    cooldown = 0
                    generarcalaveras(0,0,0)
                else:
                    cooldown += 1

                for solesitos in soles:
                    solesitos.saltar(win)

    #Todo VAS A VALER KBRON
    else:
        gameover(win)
        if userInput[pygame.K_r]:
            recursos = 50
            temoriste = False
            botonSig.Oleada = 0

    print(defensas)


    clock.tick(60)
    pygame.display.update()
