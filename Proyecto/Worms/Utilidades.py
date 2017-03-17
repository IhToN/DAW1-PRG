import math


# Utilidades de Turtle
def setworldcoordinates(screen, llx, lly, urx, ury):
    """ Cambio a la función principal de Turtle para que NO limpie la pantalla al cambiar las coordenadas
    Set up a user defined coordinate-system.

    Arguments:
    llx -- coordenada X de la esquina inferior izquierda
    lly -- coordenada Y de la esquina inferior izquierda
    urx -- coordenada X de la esquina superior derecha
    ury -- coordenada Y de la esquina superior derecha
    """
    xspan = float(urx - llx)
    yspan = float(ury - lly)
    wx, wy = screen._window_size()
    screen.screensize(wx - 20, wy - 20)
    oldxscale, oldyscale = screen.xscale, screen.yscale
    screen.xscale = screen.canvwidth / xspan
    screen.yscale = screen.canvheight / yspan
    srx1 = llx * screen.xscale
    sry1 = -ury * screen.yscale
    srx2 = screen.canvwidth + srx1
    sry2 = screen.canvheight + sry1
    screen._setscrollregion(srx1, sry1, srx2, sry2)
    screen._rescale(screen.xscale / oldxscale, screen.yscale / oldyscale)
    screen.update()


def followobject(screen, screencords, turtobj):
    slx, sly, srx, sry = screencords

    llx = (-screen.window_width() / 4) + turtobj.xcor()
    lly = (-screen.window_height() / 4) + turtobj.ycor()
    urx = (screen.window_width() / 4) + turtobj.xcor()
    ury = (+screen.window_height() / 4) + turtobj.ycor()

    setworldcoordinates(screen, llx, lly, urx, ury)


# Utilidades Matemáticas

def rad_a_deg(angle_rads):
    return (math.degrees(angle_rads) + 360) % 360


def tiro_parabolico(x0, y0, posx, angulo, potencia, gravedad):
    vel_inicial = potencia
    vx = vel_inicial * math.cos(angulo)
    vy = vel_inicial * math.sin(angulo)
    posy = y0 + vy * ((posx - x0) / vx) - 1 / 2 * gravedad * ((posx - x0) / vx) ** 2
    """posy = y0 + posx * math.tan(angulo) - (_GRAVEDAD * (posx + x0) ** 2) / \
                                          (2 * vel_inicial ** 2 * math.cos(angulo) ** 2)"""
    return posy


def tiro_parabolico_tiempo(x0, y0, vx, vy, t, gravedad):
    posx = x0 + vx * t
    posy = y0 + vy * t - gravedad * t ** 2 / 2
    return posx, posy
