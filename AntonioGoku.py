import turtle
import time
import random

# Imprime fecha y hora actual en la zona local
fecha = time.strftime("%c")
print(fecha)

# Inicia screen
screen = turtle.Screen()


def register():
    '''Registra todos los gifs del archivo register.txt'''
    f = open('register.txt', 'r')
    for p in f:
        p = p.strip('\n')
        screen.register_shape(p)
    f.close()


def life_bar():
    '''Inicia las barras de vida vacias'''
    # Barras
    life_p1 = turtle.Turtle()
    life_p2 = turtle.Turtle()
    ki_p1 = turtle.Turtle()
    ki_p2 = turtle.Turtle()
    life_p1.speed(0)
    life_p2.speed(0)
    ki_p1.speed(0)
    ki_p2.speed(0)

    life_p1.penup()
    life_p1.shape('square')
    life_p1.shapesize(2, 12, 4)
    life_p1.fillcolor('red')
    life_p1.goto(-130, 230)

    ki_p1.penup()
    ki_p1.shape('square')
    ki_p1.shapesize(1, 10, 4)
    ki_p1.fillcolor("black")
    ki_p1.goto(-150, 198)

    life_p2.penup()
    life_p2.shape('square')
    life_p2.shapesize(2, 12, 4)
    life_p2.fillcolor('red')
    life_p2.goto(130, 230)

    ki_p2.penup()
    ki_p2.shape('square')
    ki_p2.shapesize(1, 10, 4)
    ki_p2.fillcolor("black")
    ki_p2.goto(150, 198)


def delimitador():
    '''Define los limites del stage'''
    limit = turtle.Turtle()
    limit.speed(0)
    limit.penup()
    limit.goto(350, 300)
    limit.right(90)
    limit.forward(580)
    limit.right(90)
    limit.forward(691)
    limit.right(90)
    limit.forward(580)
    limit.right(90)
    limit.forward(691)


# Loading

#register()
nothing = turtle.Turtle()
#nothing.shape("loading.gif")
nothing.st()


class Controles:
    def __init__(self):
        self.control = turtle.Turtle()
        self.control.ht()
        self.control.speed(0)

    def carga_tecla(self, tecla):
        self.tecla = tecla
        #self.control.shape('controles/{}.gif'.format(self.tecla))
        self.control.pencolor('white')


class Vida:
    def __init__(self):
        self.life = turtle.Turtle()

    def life_p1(self):
        '''Inicia vida del jugador uno'''
        self.life.speed(0)
        self.life.penup()
        self.life.shape('square')
        self.life.shapesize(1.9, total_vida1, 0)
        self.life.fillcolor('yellow')
        self.life.goto(-130, 230)
        self.life.st()

    def life_p2(self):
        '''Inicia vida del jugador dos'''
        self.life.speed(0)
        self.life.penup()
        self.life.shape('square')
        self.life.shapesize(1.9, total_vida2, 0)
        self.life.fillcolor('yellow')
        self.life.goto(130, 230)
        self.life.st()


class Ki:
    def __init__(self):
        self.ki = turtle.Turtle()

    def cargaki_p1(self):
        '''Inicia ki del jugador uno'''
        self.ki.speed(0)
        self.ki.penup()
        self.ki.shape('square')
        self.ki.shapesize(0.9, ki_p1, 0)
        self.ki.fillcolor('green')
        self.ki.goto(-230, 198)
        self.ki.st()

    def cargaki_p2(self):
        '''Inicia ki del jugador dos'''
        self.ki.speed(0)
        self.ki.penup()
        self.ki.shape('square')
        self.ki.shapesize(0.9, ki_p2, 0)
        self.ki.fillcolor('green')
        self.ki.goto(230, 198)
        self.ki.st()


def vs():
    '''Crea y posiciona icono VS'''
    vs = turtle.Turtle()
    vs.speed(0)
    vs.penup()
    #vs.shape('vs.gif')
    vs.goto(0, 233)


class Explosion:
    def __init__(self):
        self.e = turtle.Turtle()

    def explo_anim(self):
        '''Animacion de explosion'''
        a = open('exp.txt', 'r')
        for p in a:
            p = p.strip('\n')
            #self.e.shape(p)
            nothing.speed(20)
            nothing.left(90)
        a.close()

    def aura(self, nombre):
        '''Animacion del aura de cada personaje'''
        self.nombre = nombre
        #self.e.shape("{}/{}_carga.gif".format(self.nombre, self.nombre))
        self.e.st()


class Avatar:
    def __init__(self, nombre):
        self.avatar = turtle.Turtle()
        self.nombre = nombre
        #self.avatar.shape("{}/{}_avatar.gif".format(self.nombre, self.nombre))


class Ataque():
    def __init__(self, nombre):
        self.atq = turtle.Turtle()
        self.nombre = nombre

    def kamekameha(self):
        '''Animacion de kamekameha'''
        k = open('esp_{}.txt'.format(self.nombre), 'r')
        for p in k:
            p = p.strip('\n')
            #self.atq.shape(p)
        k.close()

    def bigbang(self):
        '''Animacion de bigbang'''
        b = open('esp_{}.txt'.format(self.nombre), 'r')
        for p in b:
            p = p.strip('\n')
            #self.atq.shape(p)
        b.close()


class Personaje:
    def __init__(self, nombre):
        self.pj = turtle.Turtle()
        self.nombre = nombre
        self.rival = None

    def carga_rival(self, rival):
        '''Define el rival de cada jugador'''
        self.rival = rival

    def forward_p1(self):
        '''Avanza jugador uno'''
        game_over('jaja')
        time.sleep(10)
        desactivar_p1()
        ##self.pj.shape("{}/{}_run (1).gif".format(self.nombre, self.nombre))
        if self.pj.xcor() < 280 and self.pj.xcor() + 100 < self.rival.pj.xcor():
         #   #self.pj.shape("{}/{}_run (2).gif".format(self.nombre, self.nombre))
            self.pj.speed(1)
            self.pj.forward(move_speed)
          #  #self.pj.shape("{}/{}_run (3).gif".format(self.nombre, self.nombre))
            self.pj.forward(move_speed - 5)
            nothing.speed(9)
            nothing.left(90)
        ##self.pj.shape("{}/{}_stance.gif".format(self.nombre, self.nombre))
        activar_p1()

    def backward_p1(self):
        '''Vuelve jugador uno'''
        desactivar_p1()
        ##self.pj.shape("{}/{}_atras (1).gif".format(self.nombre, self.nombre))
        if self.pj.xcor() > -300:
            self.pj.backward(move_speed)
         #   #self.pj.shape("{}/{}_atras (2).gif".format(self.nombre, self.nombre))
            self.pj.speed(1)
            self.pj.backward(move_speed - 5)
        ##self.pj.shape("{}/{}_stance.gif".format(self.nombre, self.nombre))
        activar_p1()

    def arriba_p1(self):
        '''Salta jugador uno'''
        desactivar_p1()
        self.pj.speed(0)
        ##self.pj.shape("{}/{}_salto.gif".format(self.nombre, self.nombre))
        self.pj.left(90)
        self.pj.speed(2)
        self.pj.forward(jump)
        self.pj.speed(4)
        ##self.pj.shape("{}/{}_abajo.gif".format(self.nombre, self.nombre))
        self.pj.backward(jump)
        self.pj.speed(7)
        self.pj.right(90)
        ##self.pj.shape("{}/{}_stance.gif".format(self.nombre, self.nombre))
        activar_p1()

    def abajo_p1(self):
        '''Agacha jugador uno'''
        desactivar_p1()
        self.pj.speed(0)
        ##self.pj.shape("{}/{}_suelo.gif".format(self.nombre, self.nombre))
        self.pj.right(90)
        self.pj.speed(5)
        self.pj.forward(plas)
        self.pj.speed(2)
        self.pj.backward(plas)
        self.pj.speed(0)
        self.pj.left(90)
        ##self.pj.shape("{}/{}_stance.gif".format(self.nombre, self.nombre))
        activar_p1()

    def puno_p1(self):
        '''Pega jugador uno'''
        global total_vida2
        global posx_life2
        desactivar_p1()
        ##self.pj.shape("{}/{}_puno (1).gif".format(self.nombre, self.nombre))
        nothing.speed(8)
        nothing.left(90)
        ##self.pj.shape("{}/{}_puno (2).gif".format(self.nombre, self.nombre))
        nothing.speed(9)
        nothing.left(90)
        ##self.pj.shape("{}/{}_puno (3).gif".format(self.nombre, self.nombre))
        nothing.speed(8)
        nothing.left(90)
        if self.pj.xcor() + 100 > self.rival.pj.xcor() and self.pj.xcor() < self.rival.pj.xcor() and self.rival.pj.ycor() == self.pj.ycor():
        #    #self.rival.pj.shape("{}/{}_dano.gif".format(self.rival.nombre, self.rival.nombre))
            if self.rival.pj.xcor() < 280:
                self.rival.pj.speed(1)
                self.rival.pj.forward(35)
            #self.rival.pj.shape("{}/{}_dano.gif".format(self.rival.nombre, self.rival.nombre))
            if total_vida2 >= (dano_puno + 0.1):
                lifep2.life.shapesize(1.9, total_vida2 - dano_puno, 0)
                total_vida2 = total_vida2 - dano_puno
                posx_life2 = posx_life2 + 5
                lifep2.life.goto(posx_life2, 230)
            else:
                lifep2.life.ht()
                self.rival.pj.right(90)
                self.rival.pj.forward(50)
                #self.rival.pj.shape("{}/{}_pierde.gif".format(self.rival.nombre, self.rival.nombre))
                #self.pj.shape("{}/{}_gana.gif".format(self.nombre, self.nombre))
                j1 = '!Jugador 1 gana¡'
                print(j1)
                game_over(j1)
            #self.rival.pj.shape("{}/{}_stance.gif".format(self.rival.nombre, self.rival.nombre))
            print('!Goku golpea a Vegeta¡')
        #self.pj.shape("{}/{}_puno (4).gif".format(self.nombre, self.nombre))
        #self.pj.shape("{}/{}_stance.gif".format(self.nombre, self.nombre))
        activar_p1()

    def patada_p1(self):
        '''Patada jugador uno'''
        global total_vida2
        global posx_life2
        desactivar_p1()
        #self.pj.shape("{}/{}_patada (1).gif".format(self.nombre, self.nombre))
        nothing.speed(10)
        nothing.left(90)
        #self.pj.shape("{}/{}_patada (2).gif".format(self.nombre, self.nombre))
        nothing.speed(9)
        nothing.left(90)
        #self.pj.shape("{}/{}_patada (3).gif".format(self.nombre, self.nombre))
        nothing.speed(8)
        nothing.left(90)
        if self.pj.xcor() + 100 > self.rival.pj.xcor() and self.pj.xcor() < self.rival.pj.xcor() and self.rival.pj.ycor() == self.pj.ycor():
            #self.rival.pj.shape("{}/{}_dano.gif".format(self.rival.nombre, self.rival.nombre))
            if self.rival.pj.xcor() < 280:
                self.rival.pj.speed(1)
                self.rival.pj.forward(35)
            #self.rival.pj.shape("{}/{}_dano.gif".format(self.rival.nombre, self.rival.nombre))
            if total_vida2 >= (dano_patada + 0.1):
                lifep2.life.shapesize(1.9, total_vida2 - dano_patada, 0)
                total_vida2 = total_vida2 - dano_patada
                posx_life2 = posx_life2 + 10
                lifep2.life.goto(posx_life2, 230)
            else:
                lifep2.life.ht()
                self.rival.pj.right(90)
                self.rival.pj.forward(50)
                #self.rival.pj.shape("{}/{}_pierde.gif".format(self.rival.nombre, self.rival.nombre))
                #self.pj.shape("{}/{}_gana.gif".format(self.nombre, self.nombre))
                j1 = '!Jugador 1 gana¡'
                print(j1)
                game_over(j1)
            #self.rival.pj.shape("{}/{}_stance.gif".format(self.rival.nombre, self.rival.nombre))
            print('!Goku da una patada a Vegeta!')
        #self.pj.shape("{}/{}_patada (4).gif".format(self.nombre, self.nombre))
        #self.pj.shape("{}/{}_stance.gif".format(self.nombre, self.nombre))
        activar_p1()

    def atq_esp_p1(self):
        '''Ataque especial de jugador uno'''
        global total_vida2
        global posx_life2
        global ki_p1
        global posx_ki1
        global kip1
        desactivar_p1()
        if ki_p1 >= 10:
            self.pj.speed(3)
            #self.pj.shape("{}/{}_tele.gif".format(self.nombre, self.nombre))
            self.pj.goto(-pos_ini, alt_ini)
            #self.pj.shape("{}/{}_esp (1).gif".format(self.nombre, self.nombre))
            nothing.speed(2)
            nothing.left(90)
            #self.pj.shape("{}/{}_esp (2).gif".format(self.nombre, self.nombre))
            kame.atq.speed(0)
            kame.atq.penup()
            kame.atq.goto(-25, -60)
            nothing.speed(8)
            nothing.left(90)
            #self.pj.shape("{}/{}_esp (3).gif".format(self.nombre, self.nombre))
            kame.atq.st()
            kip1.ki.fillcolor("green")
            ki_p1 = 1
            kip1.ki.shapesize(0.9, ki_p1, 0)
            kip1.ki.goto(-240, 198)
            posx_ki1 = posx_ki1 - 90
            kame.kamekameha()
            print('!Kameekameeehaaaaaaaa¡')
            kame.atq.ht()
            if self.pj.xcor() + 350 > self.rival.pj.xcor() and self.rival.pj.ycor() == self.pj.ycor():
                exp.e.goto(self.rival.pj.xcor(), self.rival.pj.ycor())
                exp.e.st()
                #self.rival.pj.shape("{}/{}_dano.gif".format(self.rival.nombre, self.rival.nombre))
                exp.explo_anim()
                self.rival.pj.speed(2.5)
                self.rival.pj.goto(pos_ini, alt_ini)
                if total_vida2 >= (dano_esp + 0.1):
                    lifep2.life.shapesize(1.9, total_vida2 - dano_esp, 0)
                    total_vida2 = total_vida2 - dano_esp
                    posx_life2 = posx_life2 + 30
                    lifep2.life.goto(posx_life2, 230)
                else:
                    lifep2.life.ht()
                    self.rival.pj.right(90)
                    self.rival.pj.forward(50)
                    exp.e.ht()
                    #self.rival.pj.shape("{}/{}_pierde.gif".format(self.rival.nombre, self.rival.nombre))
                    #self.pj.shape("{}/{}_gana.gif".format(self.nombre, self.nombre))
                    j1 = '!Jugador 1 gana¡'
                    print(j1)
                    game_over(j1)
                #self.rival.pj.shape("{}/{}_stance.gif".format(self.rival.nombre, self.rival.nombre))
                exp.e.ht()
        else:
            #self.pj.shape("{}/{}_carga_ki.gif".format(self.nombre, self.nombre))
            aura_p1.e.goto(self.pj.xcor(), alt_ini)
            aura_p1.aura('goku')
            nothing.speed(4)
            nothing.left(90)
            ki_p1 = ki_p1 + 1
            kip1.ki.shapesize(0.9, ki_p1, 0)
            posx_ki1 = posx_ki1 + 10
            kip1.ki.goto(posx_ki1 - 78, 198)
            aura_p1.e.ht()
            if ki_p1 >= 10:
                kip1.ki.fillcolor("green yellow")
            else:
                kip1.ki.fillcolor("green")
        #self.pj.shape("{}/{}_stance.gif".format(self.nombre, self.nombre))
        activar_p1()

    def backward_p2(self):
        '''Vuelve jugador dos'''
        desactivar_p2()
        #self.pj.shape("{}/{}_atras (1).gif".format(self.nombre, self.nombre))
        if self.pj.xcor() < 280:
            self.pj.forward(move_speed)
            #self.pj.shape("{}/{}_atras (2).gif".format(self.nombre, self.nombre))
            self.pj.speed(1)
            self.pj.forward(move_speed - 5)
        #self.pj.shape("{}/{}_stance.gif".format(self.nombre, self.nombre))
        activar_p2()

    def forward_p2(self):
        '''Avanza jugador dos'''
        desactivar_p2()
        #self.pj.shape("{}/{}_run (1).gif".format(self.nombre, self.nombre))
        if self.pj.xcor() > -300 and self.pj.xcor() - 100 > self.rival.pj.xcor():
            #self.pj.shape("{}/{}_run (2).gif".format(self.nombre, self.nombre))
            self.pj.speed(1)
            self.pj.backward(move_speed)
            #self.pj.shape("{}/{}_run (3).gif".format(self.nombre, self.nombre))
            self.pj.backward(move_speed - 5)
            nothing.speed(9)
            nothing.left(90)
        #self.pj.shape("{}/{}_stance.gif".format(self.nombre, self.nombre))
        activar_p2()

    def arriba_p2(self):
        '''Salta jugador dos'''
        desactivar_p2()
        self.pj.speed(0)
        #self.pj.shape("{}/{}_salto.gif".format(self.nombre, self.nombre))
        self.pj.left(90)
        self.pj.speed(2)
        self.pj.forward(jump)
        self.pj.speed(4)
        #self.pj.shape("{}/{}_abajo.gif".format(self.nombre, self.nombre))
        self.pj.backward(jump)
        self.pj.speed(7)
        self.pj.right(90)
        #self.pj.shape("{}/{}_stance.gif".format(self.nombre, self.nombre))
        activar_p2()

    def abajo_p2(self):
        '''Agacha jugador dos'''
        desactivar_p2()
        self.pj.speed(0)
        #self.pj.shape("{}/{}_suelo.gif".format(self.nombre, self.nombre))
        self.pj.right(90)
        self.pj.speed(5)
        self.pj.forward(plas)
        self.pj.speed(2)
        self.pj.backward(plas)
        self.pj.speed(0)
        self.pj.left(90)
        #self.pj.shape("{}/{}_stance.gif".format(self.nombre, self.nombre))
        activar_p2()

    def puno_p2(self):
        '''Pega jugador dos'''
        global total_vida1
        global posx_life1
        desactivar_p2()
        #self.pj.shape("{}/{}_puno (1).gif".format(self.nombre, self.nombre))
        nothing.speed(8)
        nothing.left(90)
        #self.pj.shape("{}/{}_puno (2).gif".format(self.nombre, self.nombre))
        nothing.speed(9)
        nothing.left(90)
        #self.pj.shape("{}/{}_puno (3).gif".format(self.nombre, self.nombre))
        nothing.speed(8)
        nothing.left(90)
        if self.pj.xcor() - 100 < self.rival.pj.xcor() and self.pj.xcor() > self.rival.pj.xcor() and self.rival.pj.ycor() == self.pj.ycor():
            #self.rival.pj.shape("{}/{}_dano.gif".format(self.rival.nombre, self.rival.nombre))
            if self.rival.pj.xcor() > -300:
                self.rival.pj.speed(1)
                self.rival.pj.backward(35)
            #self.rival.pj.shape("{}/{}_dano.gif".format(self.rival.nombre, self.rival.nombre))
            if total_vida1 >= (dano_puno + 0.1):
                lifep1.life.shapesize(1.9, total_vida1 - dano_puno, 0)
                total_vida1 = total_vida1 - dano_puno
                posx_life1 = posx_life1 - 5
                lifep1.life.goto(posx_life1, 230)
            else:
                lifep1.life.ht()
                self.rival.pj.right(90)
                self.rival.pj.forward(50)
                exp.e.ht()
                #self.rival.pj.shape("{}/{}_pierde.gif".format(self.rival.nombre, self.rival.nombre))
                #self.pj.shape("{}/{}_stance.gif".format(self.nombre, self.nombre))
                j2 = '!Jugador 2 gana¡'
                print(j2)
                game_over(j2)
            #self.rival.pj.shape("{}/{}_gana.gif".format(self.rival.nombre, self.rival.nombre))
            print('!Vegeta golpea a Goku¡')
        #self.pj.shape("{}/{}_puno (4).gif".format(self.nombre, self.nombre))
        #self.pj.shape("{}/{}_stance.gif".format(self.nombre, self.nombre))
        activar_p2()

    def patada_p2(self):
        '''Patada jugador dos'''
        global total_vida1
        global posx_life1
        desactivar_p2()
        #self.pj.shape("{}/{}_patada (1).gif".format(self.nombre, self.nombre))
        nothing.speed(10)
        nothing.left(90)
        #self.pj.shape("{}/{}_patada (2).gif".format(self.nombre, self.nombre))
        nothing.speed(9)
        nothing.left(90)
        #self.pj.shape("{}/{}_patada (3).gif".format(self.nombre, self.nombre))
        nothing.speed(8)
        nothing.left(90)
        if self.pj.xcor() - 100 < self.rival.pj.xcor() and self.pj.xcor() > self.rival.pj.xcor() and self.rival.pj.ycor() == self.pj.ycor():
            #self.rival.pj.shape("{}/{}_dano.gif".format(self.rival.nombre, self.rival.nombre))
            if self.rival.pj.xcor() > -300:
                self.rival.pj.speed(1)
                self.rival.pj.backward(35)
            #self.rival.pj.shape("{}/{}_dano.gif".format(self.rival.nombre, self.rival.nombre))
            if total_vida1 >= (dano_patada + 0.1):
                lifep1.life.shapesize(1.9, total_vida1 - dano_patada, 0)
                total_vida1 = total_vida1 - dano_patada
                posx_life1 = posx_life1 - 10
                lifep1.life.goto(posx_life1, 230)
            else:
                lifep1.life.ht()
                self.rival.pj.right(90)
                self.rival.pj.forward(50)
                #self.rival.pj.shape("{}/{}_pierde.gif".format(self.rival.nombre, self.rival.nombre))
                #self.pj.shape("{}/{}_gana.gif".format(self.nombre, self.nombre))
                j2 = '!Jugador 2 gana¡'
                print(j2)
                game_over(j2)
            #self.rival.pj.shape("{}/{}_stance.gif".format(self.rival.nombre, self.rival.nombre))
            print('!Vegeta da una patada a Goku¡')
        #self.pj.shape("{}/{}_patada (4).gif".format(self.nombre, self.nombre))
        #self.pj.shape("{}/{}_stance.gif".format(self.nombre, self.nombre))
        activar_p2()

    def atq_esp_p2(self):
        '''Ataque especial de jugador dos'''
        global total_vida1
        global posx_life1
        global ki_p2
        global posx_ki2
        global kip2
        global fecha
        desactivar_p2()
        if ki_p2 >= 10:
            self.pj.speed(3)
            #self.pj.shape("{}/{}_tele.gif".format(self.nombre, self.nombre))
            self.pj.goto(pos_ini, alt_ini)
            #self.pj.shape("{}/{}_esp (1).gif".format(self.nombre, self.nombre))
            nothing.speed(2)
            nothing.left(90)
            #self.pj.shape("{}/{}_esp (2).gif".format(self.nombre, self.nombre))
            bb.atq.speed(0)
            bb.atq.penup()
            bb.atq.goto(25, -60)
            nothing.speed(8)
            nothing.left(90)
            #self.pj.shape("{}/{}_esp (3).gif".format(self.nombre, self.nombre))
            bb.atq.st()
            kip2.ki.fillcolor("green")
            ki_p2 = 1
            kip2.ki.shapesize(0.9, ki_p2, 0)
            kip2.ki.goto(240, 198)
            posx_ki2 = posx_ki2 + 90
            bb.bigbang()
            print('!Big Bang Attack¡')
            bb.atq.ht()
            if self.pj.xcor() - 350 < self.rival.pj.xcor() and self.rival.pj.ycor() == self.pj.ycor():
                exp.e.goto(self.rival.pj.xcor(), self.rival.pj.ycor())
                exp.e.st()
                #self.rival.pj.shape("{}/{}_dano.gif".format(self.rival.nombre, self.rival.nombre))
                exp.explo_anim()
                self.rival.pj.speed(2.5)
                self.rival.pj.goto(-pos_ini, alt_ini)
                if total_vida1 >= (dano_esp + 0.1):
                    lifep1.life.shapesize(1.9, total_vida1 - dano_esp, 0)
                    total_vida1 = total_vida1 - dano_esp
                    posx_life1 = posx_life1 - 30
                    lifep1.life.goto(posx_life1, 230)
                else:
                    lifep1.life.ht()
                    self.rival.pj.right(90)
                    self.rival.pj.forward(50)
                    exp.e.ht()
                    #self.rival.pj.shape("{}/{}_pierde.gif".format(self.rival.nombre, self.rival.nombre))
                    #self.pj.shape("{}/{}_gana.gif".format(self.nombre, self.nombre))
                    j2 = '!Jugador 2 gana¡'
                    print(j2)
                    game_over(j2)
                #self.rival.pj.shape("{}/{}_stance.gif".format(self.rival.nombre, self.rival.nombre))
                exp.e.ht()
                exp.e.ht()
        else:
            #self.pj.shape("{}/{}_carga_ki.gif".format(self.nombre, self.nombre))
            aura_p2.e.goto(self.pj.xcor(), alt_ini)
            aura_p2.aura('veg')
            nothing.speed(4)
            nothing.left(90)
            ki_p2 = ki_p2 + 1
            kip2.ki.shapesize(0.9, ki_p2, 0)
            posx_ki2 = posx_ki2 - 10
            kip2.ki.goto(posx_ki2 + 78, 198)
            aura_p2.e.ht()
            if ki_p2 >= 10:
                kip2.ki.fillcolor("green yellow")
            else:
                kip2.ki.fillcolor("green")
        #self.pj.shape("{}/{}_stance.gif".format(self.nombre, self.nombre))
        activar_p2()


def game_over(player):
    '''Termina el juego y guarda historial de partida'''
    h = open('historial.txt', 'a')
    h.write("{} \n {}\n".format(fecha, player))
    h.close()
    time.sleep(5)
    try:
        screen.bye()
    except:
        print('Game over')


def activar_p1():
    '''Desactiva controles del jugador dos'''
    screen.onkey(goku.patada_p1, "r")
    screen.onkey(goku.puno_p1, "f")
    screen.onkey(goku.arriba_p1, "w")
    screen.onkey(goku.abajo_p1, "s")
    screen.onkey(goku.backward_p1, "a")
    screen.onkey(goku.forward_p1, "d")
    screen.onkey(goku.atq_esp_p1, "e")
    screen.onkey(goku.patada_p1, "R")
    screen.onkey(goku.puno_p1, "F")
    screen.onkey(goku.arriba_p1, "W")
    screen.onkey(goku.abajo_p1, "S")
    screen.onkey(goku.backward_p1, "A")
    screen.onkey(goku.forward_p1, "D")
    screen.onkey(goku.atq_esp_p1, "E")


def desactivar_p1():
    '''Desactiva controles del jugador uno'''
    screen.onkey(None, "r")
    screen.onkey(None, "f")
    screen.onkey(None, "d")
    screen.onkey(None, "w")
    screen.onkey(None, "s")
    screen.onkey(None, "a")
    screen.onkey(None, "e")
    screen.onkey(None, "R")
    screen.onkey(None, "F")
    screen.onkey(None, "D")
    screen.onkey(None, "W")
    screen.onkey(None, "S")
    screen.onkey(None, "A")
    screen.onkey(None, "E")


def activar_p2():
    '''Activa controles del jugador dos'''
    screen.onkey(veg.patada_p2, "y")
    screen.onkey(veg.puno_p2, "h")
    screen.onkey(veg.arriba_p2, "i")
    screen.onkey(veg.abajo_p2, "k")
    screen.onkey(veg.forward_p2, "j")
    screen.onkey(veg.backward_p2, "l")
    screen.onkey(veg.atq_esp_p2, "u")
    screen.onkey(veg.patada_p2, "Y")
    screen.onkey(veg.puno_p2, "H")
    screen.onkey(veg.arriba_p2, "I")
    screen.onkey(veg.abajo_p2, "K")
    screen.onkey(veg.forward_p2, "J")
    screen.onkey(veg.backward_p2, "L")
    screen.onkey(veg.atq_esp_p2, "U")


def desactivar_p2():
    '''Desactiva controles del jugador dos'''
    screen.onkey(None, "y")
    screen.onkey(None, "h")
    screen.onkey(None, "u")
    screen.onkey(None, "i")
    screen.onkey(None, "k")
    screen.onkey(None, "l")
    screen.onkey(None, "j")
    screen.onkey(None, "o")
    screen.onkey(None, "Y")
    screen.onkey(None, "U")
    screen.onkey(None, "I")
    screen.onkey(None, "K")
    screen.onkey(None, "L")
    screen.onkey(None, "J")
    screen.onkey(None, "O")
    screen.onkey(None, "H")


def main():
    '''Inicializa varibles, personajes, stage y otras clases'''
    # Crea las varibale como globales
    global goku
    global veg
    global kame
    global exp
    global bb
    global avatar_p1
    global avatar_p2
    global alt_ini
    global pos_ini
    global move_speed
    global jump
    global plas
    global total_vida1
    global total_vida2
    global lifep1
    global lifep2
    global dano_puno
    global dano_patada
    global dano_esp
    global posx_life1
    global posx_life2
    global ki_p1
    global ki_p2
    global aura_p1
    global aura_p2
    global posx_ki1
    global posx_ki2
    global kip1
    global kip2

    alt_ini = -80
    pos_ini = 200
    move_speed = 20
    jump = 150
    plas = 50
    total_vida1 = 12
    total_vida2 = 12
    dano_puno = 0.5
    dano_patada = 1
    dano_esp = 3
    posx_life1 = -132
    posx_life2 = 132
    posx_ki1 = -152
    posx_ki2 = 152
    ki_p1 = 2
    ki_p2 = 2

    # Crea las clases
    aura_p1 = Explosion()
    aura_p2 = Explosion()
    exp = Explosion()
    goku = Personaje('goku')
    goku.pj.ht()
    veg = Personaje('veg')
    veg.pj.ht()
    goku.carga_rival(veg)
    veg.carga_rival(goku)
    kame = Ataque('goku')
    bb = Ataque('veg')

    # Esconde ataques
    aura_p1.e.penup()
    aura_p2.e.penup()
    aura_p1.e.ht()
    aura_p2.e.ht()
    aura_p1.e.speed()
    aura_p2.e.speed()
    kame.atq.ht()
    bb.atq.ht()
    exp.e.penup()
    exp.e.speed(0)
    #exp.e.shape("exp/exp (0).gif")
    exp.e.ht()

    # Inicia stage y personajes
    #goku.pj.shape("goku/goku_stance.gif")
    #veg.pj.shape("veg/veg_stance.gif")

    stg4 = ["stages/stage (1).png", "stages/stage (2).png", "stages/stage (3).png", "stages/stage (4).png"]
    stg3 = ["stages/stage (1).png", "stages/stage (2).png", "stages/stage (3).png"]
    stg2 = ["stages/stage (1).png", "stages/stage (2).png"]
    stg1 = ["stages/stage (2).png"]
    screen.bgcolor("black")
    #screen.bgpic(random.choice(stg1))

    # Inicia avatares y barras
    lifep1 = Vida()
    lifep1.life.ht()
    lifep2 = Vida()
    lifep2.life.ht()
    lifep1.life.speed(0)
    lifep1.life.speed(0)
    lifep1.life_p1()
    lifep2.life_p2()

    kip1 = Ki()
    kip1.ki.ht()
    kip2 = Ki()
    kip2.ki.ht()
    kip1.ki.speed(0)
    kip1.ki.speed(0)
    kip1.cargaki_p1()
    kip2.cargaki_p2()

    avatar_p1 = Avatar('goku')
    avatar_p1.avatar.ht()
    avatar_p2 = Avatar('veg')
    avatar_p2.avatar.ht()
    avatar_p1.avatar.speed(0)
    avatar_p2.avatar.speed(0)
    #avatar_p1.avatar.shape("goku/goku_avatar.gif")
    avatar_p1.avatar.penup()
    avatar_p1.avatar.goto(-290, 220)
    #avatar_p2.avatar.shape("veg/veg_avatar.gif")
    avatar_p2.avatar.penup()
    avatar_p2.avatar.goto(290, 220)
    avatar_p1.avatar.st()
    avatar_p2.avatar.st()

    # Muestra controles

    # Jugador 1

    # w
    w = Controles()
    w.control.penup()
    w.carga_tecla('w')
    w.control.goto(-640, 270)
    w.control.write('      Saltar', False, align="left", font=("Arial", 18, "bold"))
    w.control.st()

    # a
    a = Controles()
    a.control.penup()
    a.carga_tecla('a')
    a.control.goto(-640, 130)
    a.control.write('      Atrás', False, align="left", font=("Arial", 18, "bold"))
    a.control.st()

    # s
    s = Controles()
    s.control.penup()
    s.carga_tecla('s')
    s.control.goto(-640, 60)
    s.control.write('      Abajo', False, align="left", font=("Arial", 18, "bold"))
    s.control.st()

    # d
    d = Controles()
    d.control.penup()
    d.carga_tecla('d')
    d.control.goto(-640, 200)
    d.control.write('      Avanzar', False, align="left", font=("Arial", 18, "bold"))
    d.control.st()

    # e
    e = Controles()
    e.control.penup()
    e.carga_tecla('e')
    e.control.goto(-640, -70)
    e.control.write('      At. especial', False, align="left", font=("Arial", 18, "bold"))
    e.control.st()

    # f
    f = Controles()
    f.control.penup()
    f.carga_tecla('f')
    f.control.goto(-640, -140)
    f.control.write('      Puñetazo', False, align="left", font=("Arial", 18, "bold"))
    f.control.st()

    # r
    r = Controles()
    r.control.penup()
    r.carga_tecla('r')
    r.control.goto(-640, -210)
    r.control.write('      Patada', False, align="left", font=("Arial", 18, "bold"))
    r.control.st()

    # Jugador 2

    # i
    i = Controles()
    i.control.penup()
    i.carga_tecla('i')
    i.control.goto(640, 270)
    i.control.write('Saltar      ', False, align="right", font=("Arial", 18, "bold"))
    i.control.st()

    # l
    l = Controles()
    l.control.penup()
    l.carga_tecla('l')
    l.control.goto(640, 130)
    l.control.write('Atrás      ', False, align="right", font=("Arial", 18, "bold"))
    l.control.st()

    # k
    k = Controles()
    k.control.penup()
    k.carga_tecla('k')
    k.control.goto(640, 60)
    k.control.write('Abajo      ', False, align="right", font=("Arial", 18, "bold"))
    k.control.st()

    # j
    j = Controles()
    j.control.penup()
    j.carga_tecla('j')
    j.control.goto(640, 200)
    j.control.write('Avanzar      ', False, align="right", font=("Arial", 18, "bold"))
    j.control.st()

    # u
    u = Controles()
    u.control.penup()
    u.carga_tecla('u')
    u.control.goto(640, -70)
    u.control.write('At. especial      ', False, align="right", font=("Arial", 18, "bold"))
    u.control.st()

    # h
    h = Controles()
    h.control.penup()
    h.carga_tecla('h')
    h.control.goto(640, -140)
    h.control.write('Puñetazo      ', False, align="right", font=("Arial", 18, "bold"))
    h.control.st()

    # y
    y = Controles()
    y.control.penup()
    y.carga_tecla('y')
    y.control.goto(640, -210)
    y.control.write('Patada      ', False, align="right", font=("Arial", 18, "bold"))
    y.control.st()

    # Posiciona personajes

    goku.pj.penup()
    goku.pj.speed(0)
    goku.pj.goto(-pos_ini, alt_ini)
    goku.pj.st()

    veg.pj.penup()
    veg.pj.speed(0)
    veg.pj.goto(pos_ini, alt_ini)
    veg.pj.st()


def loading_complete():
    '''Hace la carga de toda la interfaz'''
    life_bar()
    main()
    vs()
    time.sleep(1)
    nothing.ht()

try:
    loading_complete()
    activar_p1()
    activar_p2()
    screen.listen()
    screen.mainloop()
except:
    print('Pringao de los cojones')