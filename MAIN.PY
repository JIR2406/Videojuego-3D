import pygame as py
from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from ironman import *
import a_escenario as es
import a_iluminacion as li
import a_draw as dr
import a_textos as txt
from a_objetos import *
import a_colision as col
import N1 as p
import N2 as pp
import N3 as ppp
import sys
import gc

def resetear_camara():
    global rotaciones_acumuladas
    for angle in rotaciones_acumuladas[::-1]:
        glRotatef(-angle, 0, 1, 0)
    rotaciones_acumuladas = []

def reset_camara():
    global camara_x, camara_y, camara_z, movimientos
    # Revertir los movimientos aplicados
    for movimiento in reversed(movimientos):
        direccion, distancia = movimiento
        if direccion == 'x':
            glTranslatef(-distancia, 0, 0)
        elif direccion == 'y':
            glTranslatef(0, -distancia, 0)
        elif direccion == 'z':
            glTranslatef(0, 0, -distancia)
    # Reiniciar las posiciones de la cámara
    camara_x, camara_y, camara_z = 0.0, 0.0, 0.0
    # Limpiar la lista de movimientos
    movimientos = []


def draw_panel():
    # Guardar la configuración actual de las matrices de proyección y modelo-vista
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    gluOrtho2D(0, display[0], 0, display[1])

    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()

    # Habilitar el blending para hacer el panel completamente transparente
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    # Dibujar el panel completamente transparente con una altura de 0.1
    glColor4f(0.5, 0.5, 0.5, 0.0)  # Color gris completamente transparente
    glBegin(GL_QUADS)
    glVertex2f(0, display[1] - 0.1)  # Posición superior de la barra
    glVertex2f(0, display[1])
    glVertex2f(display[0], display[1])
    glVertex2f(display[0], display[1] - 0.1)  # Altura de la barra
    glEnd()

   
    if per == 0:
        txt.nombresTxt("Jake", 450, 525, 0, 35, 232, 255, 0)
        txt.nombresTxt("Tony", 725, 510, 0, 35, 232, 255, 0)
        txt.nombresTxt("Añan", 985, 510, 0, 35, 232, 255, 0)

        txt.nombresTxt("F9", 470, 495, 0, 30, 231, 210, 10)
        txt.nombresTxt("F10", 737, 485, 0, 30, 231, 210, 10)
        txt.nombresTxt("F11", 988, 485, 0, 30, 231, 210, 10)
        txt.nombresTxt("Trash's Collector", 500, 700, 0, 100, 39, 58, 88)
        txt.nombresTxt("Elige tu personaje", 640, 650, 0, 50, 231, 210, 10)
        txt.nombresTxt("Creditos i", 100, 790, 0, 30, 231, 210, 10)
        if des == 1:
            txt.desarrollador()

    else:
        if tras == 0:
            txt.nombresTxt("Pulse espacio para jugar", 550, 650, 0, 50, 0, 0, 0)
        else :
            # Agregar tiempo y puntos
            txt.texto(str(formatoTime(tiempo)), 400, 780, 0, 30, 255, 255, 255, 0, 0, 0)
            txt.texto("Puntuación: " + str(puntos), 850, 780, 0, 30, 255, 255, 255, 0, 0, 0)
            txt.texto("i) Informacion", 1100, 780, 0, 30, 0, 122, 204, 255, 255, 255)


    # Informacion / Controles
    if (jake or panda or band) == 12:
        if per == 2:
            txt.controlesJake()
        elif per == 1:
            txt.controles()
        elif per == 3:
            txt.controlesPanda()

    if nivel == 1 and per != 0 and tras != 0:
        txt.texto("Nivel 1 ", 200, 780, 0, 30, 255, 255, 255, 0, 0, 0)
    elif nivel == 2 and per != 0 and tras != 0:
        txt.texto("Nivel 2 ", 200, 780, 0, 30, 255, 255, 255, 0, 0, 0)
    elif nivel == 3 and per != 0 and tras != 0:
        txt.texto("Nivel 3 ", 200, 780, 0, 30, 255, 255, 255, 0, 0, 0)


    # Winner
    if win and per != 0 and tras != 0:
        pos1[0] = pos1[1] = pos1[2] = 0
        txt.texto("! YOU WIN ¡", 550, 600, 0, 100, 251, 248, 21, 20, 126, 3)
        txt.texto("F12: Menu", 700, 550, 0, 30, 251, 248, 21, 20, 126, 3)

    # Restaurar la configuración anterior de las matrices de proyección y modelo-vista
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)
    glPopMatrix()

    # Deshabilitar el blending después de dibujar el panel
    glDisable(GL_BLEND)


def formatoTime(tiempo):
    minutos = tiempo // 600  # 600 frames = 1 minuto
    segundos = (tiempo // 10) % 60  # 10 frames = 1 segundo
    milisegundos = (tiempo % 10) * 100  # 1 frame = 100 milisegundos
    texto_cronometro = "{:02}:{:02}:{:03}".format(minutos, segundos, milisegundos)
    return texto_cronometro


py.init()
py.mixer.init()


display = (1500, 810)
ventana = py.display.set_mode(display, py.DOUBLEBUF | py.OPENGL)
gluPerspective(
    70, display[0] / display[1], 0.1, 1000.0
)  # Ajuste de la matriz de proyección
glTranslatef(0, 0, -90)  # Ajuste de la posición de la cámara

# Variables para el control del movimiento de la cámara
camara_speed = 0.1
rotacion_speed = 0.1
mouse_sensibilidad = 0.1

glShadeModel(GL_SMOOTH)
glEnable(GL_COLOR_MATERIAL)
glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

tiempo = 0

colisiones_detectadas = []
rotaciones_acumuladas = []

puntos = 0
nivel = 1
win = False

tras = 0
band = 0
esc = -1
luz = 0
per = 0
jake = 0
panda = 0
des = 0
pos1 = [0, 0, 0]
pos2 = [-13, 0, 1]
pos3 = [13, 0, 1]
pos4 = [4, 0, 3]


def MENU(x, y, z):
    global pos1
    pos1[0] += x  # Actualizar la coordenada x
    pos1[1] += y  # Actualizar la coordenada y
    pos1[2] += z  # Actualizar la coordenada z

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    es.piso("Imagenes/menu.jpeg")
    es.techo("Imagenes/cielo.jpg")
    es.escenario("Imagenes/menu.jpeg")

    # ----------------------------Gestos-----------------------------
    glEnable(GL_DEPTH_TEST)
    glPushMatrix()
    glTranslatef(0,0,40)

    if band == 0:
        glScalef(1.5, 1.5, 1.5)
        dr.orig()

        glTranslatef(20, -5, 5)
        glRotatef(-90, 1, 0, 0)
        glRotatef(180, 0, 0, 1)
        glScalef(1.5, 1.5, 1.5)
        dr.panda()

        glRotatef(90, 1, 0, 0)
        glRotatef(180, 0, 1, 0)
        glTranslatef(-30, 5, -15)
        glScalef(0.63, 0.63, 0.63)
        # glTranslatef(-27, 5.5, -7)
        # glScalef(0.5, 0.5, 0.5)
        dr.Jake()

    glPopMatrix()

# ----------------------------Draw-----------------------------
def dibujar1(x, y, z):
    global pos1
    pos1[0] += x  # Actualizar la coordenada x
    pos1[1] += y  # Actualizar la coordenada y
    pos1[2] += z  # Actualizar la coordenada z

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    if tras == 1:
        if nivel == 1:
            drawObj1()
        elif nivel == 2:
            drawObj2()
        elif nivel == 3:
            drawObj3()


    es.piso("Imagenes/piso.jpg")
    es.techo("Imagenes/cielo.jpg")

    if esc in (0, -1):
        es.escenario("Imagenes/fp.jpg")
    if esc == 1:
        es.escenario("Imagenes/salon.jpg")
    if esc == 2:
        es.escenario("Imagenes/calle.jpg")
    if esc == 3:
        es.escenario("Imagenes/tunel.jpg")
    if esc == 4:
        es.escenario("Imagenes/tol.jpg")

    # ----------------------------Gestos-----------------------------
    glEnable(GL_DEPTH_TEST)
    glPushMatrix()
    glTranslatef(pos1[0], pos1[1], pos1[2])
    if per == 1 and tras == 0:
        glTranslatef(0,0,60)

    if band == 0:
        dr.orig()
    elif band == 1:
        dr.g1()
    elif band == 2:
        dr.g2()
    elif band == 3:
        dr.g3()
    elif band == 4:
        dr.g4()
    elif band == 5:
        dr.g5()
    # ----------------------------Movimientos-----------------------------
    elif band == 6:
        dr.g6()
    elif band == 7:
        dr.g7()
    elif band == 8:
        dr.g8()
    elif band == 9:
        dr.g9()
    elif band == 10:
        dr.g10()
    elif band == 12:
        dr.orig()
    elif band == 30:
        txt.desarrollador()
    elif band == 200:
        dr.g11()
    elif band == 300:
        dr.g12()
    glPopMatrix()

def dibujar2(x, y, z):
    pos1[0] += x  # Actualizar la coordenada x
    pos1[1] += y  # Actualizar la coordenada y
    pos1[2] += z  # Actualizar la coordenada z

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    if tras == 2:
        if nivel == 1:
            drawObj1()
        elif nivel == 2:
            drawObj2()
        elif nivel == 3:
            drawObj3()

    es.piso("Imagenes/piso.jpg")
    es.techo("Imagenes/cielo.jpg")

    if esc in (0, -1):
        es.escenario("Imagenes/fp.jpg")
    if esc == 1:
        es.escenario("Imagenes/escenario2.jpg")
    if esc == 2:
        es.escenario("Imagenes/escenario3.jpg")
    if esc == 3:
        es.escenario("Imagenes/escenario4.jpg")
    if esc == 4:
        es.escenario("Imagenes/escenario5.jpg")
    if esc == 5:
        es.escenario("Imagenes/escenario6.jpg")
    glEnable(GL_DEPTH_TEST)
    glPushMatrix()
    glTranslatef(pos1[0], pos1[1], pos1[2])

    if per == 2 and tras == 0:
        glTranslatef(2,0,60)

    if jake in (0, 11):
        glTranslatef(-8, 4, -14)
        glScalef(0.9, 0.9, 0.9)
        dr.Jake()
    elif jake == 1:  # cerrar ojos
        glTranslatef(-8, 4, -14)
        glScalef(0.9, 0.9, 0.9)
        dr.jakeCerrarOjos()
    elif jake == 2:  # enojado
        glTranslatef(-8, 4, -14)
        glScalef(0.9, 0.9, 0.9)
        dr.jakeEnojado()
    elif jake == 3:  # saca la lengua
        glTranslatef(-8, 4, -14)
        glScalef(0.9, 0.9, 0.9)
        dr.jakeLengua()
    elif jake == 4:  # guiño
        glTranslatef(-8, 4, -14)
        glScalef(0.9, 0.9, 0.9)
        dr.jakeGuiño()
    elif jake == 5:  # sonrisa
        glTranslatef(-8, 4, -14)
        glScalef(0.9, 0.9, 0.9)
        dr.jakeSonrisa()
    elif jake == 6:
        glTranslatef(-8, 4, -14)
        glScalef(0.9, 0.9, 0.9)
        dr.jakebdUp()
    elif jake == 7:
        glTranslatef(-8, 4, -14)
        glScalef(0.9, 0.9, 0.9)
        dr.jakebUp()
    elif jake == 8:
        glTranslatef(-8, 4, -14)
        glScalef(0.9, 0.9, 0.9)
        dr.jakemp()
    elif jake == 9:
        glTranslatef(-8, 4, -14)
        glScalef(0.9, 0.9, 0.9)
        dr.jake4()
    elif jake == 10:
        glTranslatef(-8, 4, -14)
        glScalef(0.9, 0.9, 0.9)
        dr.jake5()
    elif jake == 12:
        # txt.controlesJake()
        glTranslatef(-8, 4, -14)
        glScalef(0.9, 0.9, 0.9)
        dr.jake5()

    glPopMatrix()

def dibujar3(x, y, z):
    pos1[0] += x  # Actualizar la coordenada x
    pos1[1] += y  # Actualizar la coordenada y
    pos1[2] += z  # Actualizar la coordenada z

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    if tras == 3:
        if nivel == 1:
            drawObj1()
        elif nivel == 2:
            drawObj2()
        elif nivel == 3:
            drawObj3()

    es.piso("Imagenes/piso.jpg")
    es.techo("Imagenes/cielo.jpg")

    if esc in (0, -1):
        es.escenario("Imagenes/fp.jpg")
    if esc == 1:
        es.escenario("Imagenes/f2.jpg")
    if esc == 2:
        es.escenario("Imagenes/escenario2.jpg")
    if esc == 3:
        es.escenario("Imagenes/f5.jpg")
    if esc == 4:
        es.escenario("Imagenes/f6.jpeg")

    glEnable(GL_DEPTH_TEST)
    glPushMatrix()
    glTranslatef(pos1[0], pos1[1], pos1[2])

    if per == 3 and tras == 0:
        glTranslatef(0,0,50)

    if panda in (0, 11):
        glTranslatef(7, -5, 5)
        glRotatef(-90, 1, 0, 0)
        glRotatef(180, 0, 0, 1)
        glScalef(2, 2, 2)
        dr.panda()
    if panda == 1:
        glTranslatef(7, -5, 5)
        glRotatef(-90, 1, 0, 0)
        glRotatef(180, 0, 0, 1)
        glScalef(2, 2, 2)
        dr.panda1()
    if panda == 2:
        glTranslatef(7, -5, 5)
        glRotatef(-90, 1, 0, 0)
        glRotatef(180, 0, 0, 1)
        glScalef(2, 2, 2)
        dr.panda2()
    if panda == 3:
        glTranslatef(7, -5, 5)
        glRotatef(-90, 1, 0, 0)
        glRotatef(180, 0, 0, 1)
        glScalef(2, 2, 2)
        dr.panda3()
    if panda == 4:
        glTranslatef(7, -5, 5)
        glRotatef(-90, 1, 0, 0)
        glRotatef(180, 0, 0, 1)
        glScalef(2, 2, 2)
        dr.panda4()
    if panda == 5:
        glTranslatef(7, -5, 5)
        glRotatef(-90, 1, 0, 0)
        glRotatef(180, 0, 0, 1)
        glScalef(2, 2, 2)
        dr.panda5()
    if panda == 6:
        glTranslatef(7, -5, 5)
        glRotatef(-90, 1, 0, 0)
        glRotatef(180, 0, 0, 1)
        glScalef(2, 2, 2)
        dr.panda6()
    if panda == 7:
        glTranslatef(7, -5, 5)
        glRotatef(-90, 1, 0, 0)
        glRotatef(180, 0, 0, 1)
        glScalef(2, 2, 2)
        dr.panda7()
    if panda == 8:
        glTranslatef(7, -5, 5)
        glRotatef(-90, 1, 0, 0)
        glRotatef(180, 0, 0, 1)
        glScalef(2, 2, 2)
        dr.panda8()
    if panda == 9:
        glTranslatef(7, -5, 5)
        glRotatef(-90, 1, 0, 0)
        glRotatef(180, 0, 0, 1)
        glScalef(2, 2, 2)
        dr.panda9()
    if panda == 10:
        glTranslatef(7, -5, 5)
        glRotatef(-90, 1, 0, 0)
        glRotatef(180, 0, 0, 1)
        glScalef(2, 2, 2)
        dr.panda10()
    if panda == 12:
        # txt.controlesPanda()
        glTranslatef(7, -5, 5)
        glRotatef(-90, 1, 0, 0)
        glRotatef(180, 0, 0, 1)
        glScalef(2, 2, 2)
        dr.panda()

    glPopMatrix()

def drawObj1():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)
    glPushMatrix()
    p.crea_basura()
    glPopMatrix()

def drawObj2():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)
    glPushMatrix()
    pp.crea_basura()
    glPopMatrix()

def drawObj3():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)
    glPushMatrix()
    ppp.crea_basura()
    glPopMatrix()


# Variables para el control del movimiento de la cámara
camara_x = 0
camara_y = 0
camara_z = 0

movimientos = []

def mover_camara(dx, dy, dz):
    global camara_x, camara_y, camara_z, movimientos
    camara_x += dx
    camara_y += dy
    camara_z += dz
    glTranslatef(dx, dy, dz)
    
    # Registra el movimiento en la lista
    if dx != 0:
        movimientos.append(('x', dx))
    if dy != 0:
        movimientos.append(('y', dy))
    if dz != 0:
        movimientos.append(('z', dz))


while True:
    for event in py.event.get():
        sys.stdin.flush()
        gc.collect()
        if event.type == py.QUIT:
            py.quit()
            quit()
        elif event.type == py.KEYDOWN:
            if event.key == py.K_ESCAPE:
                py.quit()
                quit()
            if event.key == py.K_F12:
                per = 5
                tras = 0
                reset_camara()
                resetear_camara()
            if tras not in (1,2,3):
                if event.key == py.K_F9:
                    per = 2
                if event.key == py.K_F10:
                    per = 1
                if event.key == py.K_F11:
                    per = 3

            # ----------------------------Raul-----------------------------
            if per == 1:
                if event.key == py.K_1:
                    band = 1
                elif event.key == py.K_2:
                    band = 2
                elif event.key == py.K_3:
                    band = 3
                elif event.key == py.K_4:
                    band = 4
                elif event.key == py.K_5:
                    band = 5
                elif event.key == py.K_q:
                    band = 6
                    py.mixer.music.load("Sonidos/s1.wav")
                    py.mixer.music.play()
                elif event.key == py.K_u:
                    band = 7
                    py.mixer.music.load("Sonidos/s2.wav")
                    py.mixer.music.play()
                elif event.key == py.K_e:
                    band = 8
                    py.mixer.music.load("Sonidos/s3.wav")
                    py.mixer.music.play()
                elif event.key == py.K_r:
                    band = 9
                    py.mixer.music.load("Sonidos/s4.wav")
                    py.mixer.music.play()
                elif event.key == py.K_t:
                    band = 10
                    py.mixer.music.load("Sonidos/s5.wav")
                    py.mixer.music.play()
                elif event.key == py.K_y:
                    band = 0
                    py.mixer.music.load("Sonidos/s_orig.wav")
                    py.mixer.music.play()

                # ----------------------------Escenarios-----------------------------
                elif event.key == py.K_0:
                    esc = 0
                    py.mixer.music.load("Sonidos/s6.wav")
                    py.mixer.music.play()
                elif event.key == py.K_6:
                    esc = 1
                    py.mixer.music.load("Sonidos/s7.wav")
                    py.mixer.music.play()
                elif event.key == py.K_7:
                    esc = 2
                    py.mixer.music.load("Sonidos/s8.wav")
                    py.mixer.music.play()
                elif event.key == py.K_8:
                    esc = 3
                    py.mixer.music.load("Sonidos/s9.wav")
                    py.mixer.music.play()
                elif event.key == py.K_9:
                    esc = 4
                    py.mixer.music.load("Sonidos/s10.wav")
                    py.mixer.music.play()
                elif event.key == py.K_i:
                    band = 12
                    py.mixer.music.load("Sonidos/s5.wav")
                    py.mixer.music.play()
                elif event.key == py.K_SPACE:
                    tras = 1
                    mover_camara(0,0,20)
                elif event.key == py.K_m:
                    band = 30
                elif event.key == py.K_F1:
                    py.mixer.music.load("Sonidos/ON.wav")
                    py.mixer.music.play()
                elif event.key == py.K_F2:
                    py.mixer.music.stop()
            # ----------------------------Jonathan-----------------------------
            if per == 2:
                if event.key == py.K_1:
                    jake = 1
                if event.key == py.K_2:
                    jake = 2
                if event.key == py.K_3:
                    jake = 3
                if event.key == py.K_4:
                    jake = 4
                if event.key == py.K_5:
                    jake = 5
                if event.key == py.K_q:
                    py.mixer.music.load("Sonidos/s1.wav")
                    py.mixer.music.play()
                    jake = 6
                if event.key == py.K_e:
                    py.mixer.music.load("Sonidos/s2.wav")
                    py.mixer.music.play()
                    jake = 7
                if event.key == py.K_r:
                    py.mixer.music.load("Sonidos/s2.wav")
                    py.mixer.music.play()
                    jake = 8
                if event.key == py.K_t:
                    py.mixer.music.load("Sonidos/s4.wav")
                    py.mixer.music.play()
                    jake = 9
                if event.key == py.K_y:
                    py.mixer.music.load("Sonidos/s5.wav")
                    py.mixer.music.play()
                    jake = 10
                if event.key == py.K_u:
                    py.mixer.music.load("Sonidos/s6.wav")
                    py.mixer.music.play()
                    jake = 11
                if event.key == py.K_6:
                    esc = 1
                    py.mixer.music.load("Sonidos/s7.wav")
                    py.mixer.music.play()
                if event.key == py.K_7:
                    esc = 2
                    py.mixer.music.load("Sonidos/s8.wav")
                    py.mixer.music.play()
                if event.key == py.K_8:
                    esc = 3
                    py.mixer.music.load("Sonidos/s9.wav")
                    py.mixer.music.play()
                if event.key == py.K_9:
                    esc = 4
                    py.mixer.music.load("Sonidos/s10.wav")
                    py.mixer.music.play()
                if event.key == py.K_0:
                    esc = 5
                    py.mixer.music.load("Sonidos/s2.wav")
                    py.mixer.music.play()
                if event.key == py.K_i:
                    jake = 12
                    py.mixer.music.load("Sonidos/s5.wav")
                    py.mixer.music.play()
                if event.key == py.K_SPACE:
                    tras = 2
                if event.key == py.K_m:
                    band = 30
                if event.key == py.K_F1:
                    py.mixer.music.load("Sonidos/ON.wav")
                    py.mixer.music.play()
                if event.key == py.K_F2:
                    py.mixer.music.stop()
            # ----------------------------Jair-----------------------------
            if per == 3:
                if event.key == py.K_1:
                    panda = 1
                if event.key == py.K_2:
                    panda = 2
                if event.key == py.K_3:
                    panda = 3
                if event.key == py.K_4:
                    panda = 4
                if event.key == py.K_5:
                    panda = 5
                if event.key == py.K_q:
                    py.mixer.music.load("Sonidos/1.wav")
                    py.mixer.music.play()
                    panda = 6
                if event.key == py.K_e:
                    py.mixer.music.load("Sonidos/2.wav")
                    py.mixer.music.play()
                    panda = 7
                if event.key == py.K_r:
                    py.mixer.music.load("Sonidos/3.wav")
                    py.mixer.music.play()
                    panda = 8
                if event.key == py.K_t:
                    py.mixer.music.load("Sonidos/4.wav")
                    py.mixer.music.play()
                    panda = 9
                if event.key == py.K_y:
                    py.mixer.music.load("Sonidos/5.wav")
                    py.mixer.music.play()
                    panda = 10
                if event.key == py.K_u:
                    py.mixer.music.load("Sonidos/zelda.wav")
                    py.mixer.music.play()
                    panda = 11
                key3 = py.key.get_pressed()
                if event.key == py.K_i:
                    panda = 12
                if event.key == py.K_6:
                    py.mixer.music.load("Sonidos/4.wav")
                    py.mixer.music.play()
                    esc = 1
                if event.key == py.K_7:
                    py.mixer.music.load("Sonidos/s2.wav")
                    py.mixer.music.play()
                    esc = 2
                if event.key == py.K_8:
                    py.mixer.music.load("Sonidos/s6.wav")
                    py.mixer.music.play()
                    esc = 3
                if event.key == py.K_9:
                    py.mixer.music.load("Sonidos/1.wav")
                    py.mixer.music.play()
                    esc = 4
                if event.key == py.K_0:
                    py.mixer.music.load("Sonidos/2.wav")
                    py.mixer.music.play()
                    esc = 0
                if event.key == py.K_SPACE:
                    tras = 3
                # ----------------------------Camara-----------------------------
                elif event.key == py.K_m:
                    band = 30
                elif event.key == py.K_F1:
                    py.mixer.music.load("Sonidos/ON.wav")
                    py.mixer.music.play()
                elif event.key == py.K_F2:
                    py.mixer.music.stop()

            if per == 0:
                if event.key == py.K_i:
                    des = 1
                elif event.key == py.K_r:
                    des = 0
        # ----------------------------Movs-----------------------------
    iteraciones = 3  # Aumenta este valor para más velocidad

    if per != 0 and tras != 0:
        keys = py.key.get_pressed()
        if keys[py.K_w]:
            if pos1[2] <= 70:
                for _ in range(iteraciones):
                    dibujar1(0, 0, 1)
                    if pos1[2] <= 69:
                        mover_camara(0, 0, -1)
        if keys[py.K_s]:
            if pos1[2] >= -70:
                for _ in range(iteraciones):
                    dibujar1(0, 0, -1)
                    mover_camara(0, 0, 1)
        if keys[py.K_d]:
            if pos1[0] <= 80:
                for _ in range(iteraciones):
                    dibujar1(1, 0, 0)
                    mover_camara(-1, 0, 0)
        if keys[py.K_a]:
            if pos1[0] >= -80:
                for _ in range(iteraciones):
                    dibujar1(-1, 0, 0)
                    mover_camara(1, 0, 0)

    x, y = py.mouse.get_rel()
    x *= mouse_sensibilidad
    y *= mouse_sensibilidad

    if x != 0 and per != 0 and tras not in (1,2,3):
        if pos1[0] >= -38:
            #glRotate(x, 0, 1, 0)
            rotaciones_acumuladas.append(x)
        else:
            resetear_camara()
        py.mouse.set_pos(display[0] // 2, display[1] // 2)  # Centramos el raton

    MENU(0, 0, 0)
    if per == 1:
        if tras == 1:
            if win == False != 11:
                tiempo += 1
        dibujar1(0, 0, 0)
    elif per == 2:
        if tras == 2:
            if win == False:
                tiempo += 1
        dibujar2(0, 0, 0)
    elif per == 3:
        dibujar3(0, 0, 0)
        if tras == 3:
            if win == False:
                tiempo += 1
    elif per == 5:
        esc = 0
        band = 0
        per = 0
        jake = 0
        panda = 0
        pos1 = [0, 0, 0]
        tiempo = 0
        puntos = 0
        colisiones_detectadas = []
        nivel = 1
        win = False
        MENU(0, 0, 0)

    # -----------Colisiones--------------
    if tras == 1:
        pt = [pos1[0],pos1[1],pos1[2]-50]
        if nivel == 1:
            pts = p.puntos
        elif nivel == 2:
            pts = pp.puntos
        elif nivel == 3:
            pts = ppp.puntos
        for i in range(len(pts)):
            if (
                col.check_collision_inters(pos1, pts[i])
                and i not in colisiones_detectadas
            ):
                txt.texto(" +1 ", -13, 12 - 3, 0, 50, 0, 122, 204, 255, 255, 255)
                colisiones_detectadas.append(i)
                puntos += 1
                py.mixer.music.load("Sonidos/bonus.wav")
                py.mixer.music.play()

    if tras == 2:
        posJake = [
            pos1[0] - 3,
            pos1[1],
            pos1[2] - 6.5,
        ]  # Ajustar la posición según la traslación
        if nivel == 1:
            pts = p.puntos
        elif nivel == 2:
            pts = pp.puntos
        elif nivel == 3:
            pts = ppp.puntos
        for i in range(len(pts)):
            if (
                col.check_collision_inters(posJake, pts[i])
                and i not in colisiones_detectadas
            ):
                txt.texto(" +1 ", -13, 12 - 3, 0, 50, 0, 122, 204, 255, 255, 255)
                colisiones_detectadas.append(i)
                puntos += 1
                py.mixer.music.load("Sonidos/bonus.wav")
                py.mixer.music.play()

    if tras == 3:
        if nivel == 1:
            pts = p.puntos
        elif nivel == 2:
            pts = pp.puntos
        elif nivel == 3:
            pts = ppp.puntos
        for i in range(len(pts)):
            if (
                col.check_collision_inters(pos1, pts[i])
                and i not in colisiones_detectadas
            ):
                txt.texto(" +1 ", -13, 12 - 3, 0, 50, 0, 122, 204, 255, 255, 255)
                colisiones_detectadas.append(i)
                puntos += 1
                py.mixer.music.load("Sonidos/bonus.wav")
                py.mixer.music.play()


    if (formatoTime(tiempo)) == "02:00:000" and puntos < 8:
        per = 5
    #Cambio de nivel
    if nivel == 1 and puntos == 3:
        nivel = 2
        puntos = 0
        resetear_camara()
        colisiones_detectadas = []
        tiempo = 0
    if nivel == 2 and puntos == 3:
        nivel = 3
        puntos = 0
        resetear_camara()
        colisiones_detectadas = []
        tiempo = 0
    if per == 5:
        reset_camara()
        resetear_camara()

    #Ganar
    if nivel == 3 and puntos == 5:
        win = True
        reset_camara()
        resetear_camara()
        
    draw_panel()
    
    py.display.flip()
