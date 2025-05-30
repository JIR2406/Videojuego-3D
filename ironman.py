import pygame as py
from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import a_escenario as es

class Matrices:
    def __init__(self):
        self.rostro = [
            [-1, 1, 1.1],  # A
            [-1, 2, 1.1],  # B
            [1, 2, 1.1],  # C
            [1, 1, 1.1],  # D
            [-1, 1, 1],  # E
            [-1, 2, 1],  # F
            [1, 2, 1],  # G
            [1, 1, 1],  # H
        ]
        self.ojos = [
            [-0.5, 1.8, 1.21],  # A (ojo izquierdo)
            [-0.5, 1.6, 1.21],  # B (ojo izquierdo)
            [-0.3, 1.6, 1.21],  # C (ojo izquierdo)
            [-0.3, 1.8, 1.21],  # D (ojo izquierdo)
            [0.5, 1.8, 1.21],  # A (ojo derecho)
            [0.5, 1.6, 1.21],  # B (ojo derecho)
            [0.3, 1.6, 1.21],  # C (ojo derecho)
            [0.3, 1.8, 1.21],  # D (ojo derecho)
        ]
        self.cabeza = [
            # Cara Frontal
            [-1, 1, 1],  # A
            [-1, 3, 1],  # B
            [1, 3, 1],  # C
            [1, 1, 1],  # D
            # Cara Trasera
            [-1, 1, -1],  # E
            [-1, 3, -1],  # F
            [1, 3, -1],  # G
            [1, 1, -1],  # H
            # Cara Superior
            [-1, 1, 1],  # A
            [1, 1, 1],  # D
            [1, 1, -1],  # H
            [-1, 1, -1],  # E
            # Cara Inferior
            [-1, 3, 1],  # B
            [1, 3, 1],  # C
            [1, 3, -1],  # G
            [-1, 3, -1],  # F
            # Cara Izquierda
            [-1, 1, 1],  # A
            [-1, 1, -1],  # E
            [-1, 3, -1],  # F
            [-1, 3, 1],  # B
            # Cara Derecha
            [1, 3, 1],  # C
            [1, 3, -1],  # G
            [1, 1, -1],  # H
            [1, 1, 1],  # D
        ]
        self.tronco = [
            # Cara frontal
            [-2, 1, 0.5],  # A
            [-2, -4, 0.5],  # B
            [2, -4, 0.5],  # C
            [2, 1, 0.5],  # D
            # Cara trasera
            [-2, 1, -0.5],  # E
            [-2, -4, -0.5],  # F
            [2, -4, -0.5],  # G
            [2, 1, -0.5],  # H
            # Cara izquierda
            [-2, 1, 0.5],  # A
            [-2, 1, -0.5],  # E
            [-2, -4, -0.5],  # F
            [-2, -4, 0.5],  # B
            # Cara derecha
            [2, 1, 0.5],  # D
            [2, 1, -0.5],  # H
            [2, -4, -0.5],  # G
            [2, -4, 0.5],  # C
            # Cara superior
            [-2, 1, 0.5],  # A
            [2, 1, 0.5],  # D
            [2, 1, -0.5],  # H
            [-2, 1, -0.5],  # E
            # Cara inferior
            [-2, -4, 0.5],  # B
            [2, -4, 0.5],  # C
            [2, -4, -0.5],  # G
            [-2, -4, -0.5],  # F
        ]
        self.brazoIzq = [
            # Cara frontal
            [-2, 1, 0.5],      # A
            [-2.9, 1, 0.5],    # B
            [-2.9, -2, 0.5],   # C
            [-2, -2, 0.5],     # D
            # Cara trasera
            [-2, 1, -0.5],     # E
            [-2.9, 1, -0.5],   # F
            [-2.9, -2, -0.5],  # G
            [-2, -2, -0.5],    # H
            # Cara izquierda
            [-2.9, 1, -0.5],   # F
            [-2.9, 1, 0.5],    # B
            [-2.9, -2, 0.5],   # C
            [-2.9, -2, -0.5],  # G
            # Cara derecha
            [-2, 1, 0.5],      # A
            [-2, -2, 0.5],     # D
            [-2, -2, -0.5],    # H
            [-2, 1, -0.5],     # E
            # Cara superior
            [-2, 1, 0.5],      # A
            [-2.9, 1, 0.5],    # B
            [-2.9, 1, -0.5],   # F
            [-2, 1, -0.5],     # E
            # Cara inferior
            [-2.9, -2, 0.5],   # C
            [-2, -2, 0.5],     # D
            [-2, -2, -0.5],    # H
            [-2.9, -2, -0.5],  # G
        ]
        self.brazoDer = [
            # Cara frontal
            [2, 1, 0.5],      # A
            [2.9, 1, 0.5],    # B
            [2.9, -2, 0.5],   # C
            [2, -2, 0.5],     # D
            # Cara trasera
            [2, 1, -0.5],     # E
            [2.9, 1, -0.5],   # F
            [2.9, -2, -0.5],  # G
            [2, -2, -0.5],    # H
            # Cara izquierda
            [2.9, 1, -0.5],   # F
            [2.9, 1, 0.5],    # B
            [2.9, -2, 0.5],   # C
            [2.9, -2, -0.5],  # G
            # Cara derecha
            [2, 1, 0.5],      # A
            [2, -2, 0.5],     # D
            [2, -2, -0.5],    # H
            [2, 1, -0.5],     # E
            # Cara superior
            [2, 1, 0.5],      # A
            [2.9, 1, 0.5],    # B
            [2.9, 1, -0.5],   # F
            [2, 1, -0.5],     # E
            # Cara inferior
            [2.9, -2, 0.5],   # C
            [2, -2, 0.5],     # D
            [2, -2, -0.5],    # H
            [2.9, -2, -0.5],  # G
        ]
        self.manoIzq = [
            # Cara frontal
            [-2.5, -2, 0.5],  # A
            [-2, -2, 0.5],  # B
            [-2, -2.5, 0.5],  # C
            [-2.5, -2.5, 0.5],  # D
            # Cara trasera
            [-2.5, -2, -0.5],  # E
            [-2, -2, -0.5],  # F
            [-2, -2.5, -0.5],  # G
            [-2.5, -2.5, -0.5],  # H
            # Cara lateral izquierda
            [-2.5, -2, 0.5],  # A
            [-2.5, -2, -0.5],  # E
            [-2.5, -2.5, -0.5],  # H
            [-2.5, -2.5, 0.5],  # D
            # Cara lateral derecha
            [-2, -2, 0.5],  # B
            [-2, -2, -0.5],  # F
            [-2, -2.5, -0.5],  # G
            [-2, -2.5, 0.5],  # C
            # Cara superior
            [-2.5, -2, 0.5],  # A
            [-2, -2, 0.5],  # B
            [-2, -2, -0.5],  # F
            [-2.5, -2, -0.5],  # E
            # Cara inferior
            [-2.5, -2.5, 0.5],  # D
            [-2, -2.5, 0.5],  # C
            [-2, -2.5, -0.5],  # G
            [-2.5, -2.5, -0.5],  # H
        ]
        self.manoDer = [
            # Cara frontal
            [2.5, -2, 0.5],  # A
            [2, -2, 0.5],  # B
            [2, -2.5, 0.5],  # C
            [2.5, -2.5, 0.5],  # D
            # Cara trasera
            [2.5, -2, -0.5],  # E
            [2, -2, -0.5],  # F
            [2, -2.5, -0.5],  # G
            [2.5, -2.5, -0.5],  # H
            # Cara lateral izquierda
            [2.5, -2, 0.5],  # A
            [2.5, -2, -0.5],  # E
            [2.5, -2.5, -0.5],  # H
            [2.5, -2.5, 0.5],  # D
            # Cara lateral derecha
            [2, -2, 0.5],  # B
            [2, -2, -0.5],  # F
            [2, -2.5, -0.5],  # G
            [2, -2.5, 0.5],  # C
            # Cara superior
            [2.5, -2, 0.5],  # A
            [2, -2, 0.5],  # B
            [2, -2, -0.5],  # F
            [2.5, -2, -0.5],  # E
            # Cara inferior
            [2.5, -2.5, 0.5],  # D
            [2, -2.5, 0.5],  # C
            [2, -2.5, -0.5],  # G
            [2.5, -2.5, -0.5],  # H
        ]
        self.pierIzq = [
            # Cara frontal
            [-2, -4, 0.5],  # A
            [-2, -7, 0.5],  # B
            [0, -7, 0.5],  # C
            [0, -4, 0.5],  # D
            # Cara trasera
            [-2, -4, -0.5],  # E
            [-2, -7, -0.5],  # F
            [0, -7, -0.5],  # G
            [0, -4, -0.5],  # H
            # Cara lateral izquierda
            [-2, -4, -0.5],  # E
            [-2, -4, 0.5],  # A
            [-2, -7, 0.5],  # B
            [-2, -7, -0.5],  # F
            # Cara lateral derecha
            [0, -4, 0.5],  # D
            [0, -4, -0.5],  # H
            [0, -7, -0.5],  # G
            [0, -7, 0.5],  # C
            # Cara superior
            [-2, -4, 0.5],  # A
            [0, -4, 0.5],  # D
            [0, -4, -0.5],  # H
            [-2, -4, -0.5],  # E
            # Cara inferior
            [-2, -7, 0.5],  # B
            [0, -7, 0.5],  # C
            [0, -7, -0.5],  # G
            [-2, -7, -0.5],  # F
        ]
        self.pierDer = [
            # Cara frontal
            [0, -4, 0.5],  # A
            [2, -4, 0.5],  # B
            [2, -7, 0.5],  # C
            [0, -7, 0.5],  # D
            # Cara trasera
            [0, -4, -0.5],  # E
            [2, -4, -0.5],  # F
            [2, -7, -0.5],  # G
            [0, -7, -0.5],  # H
            # Cara lateral izquierda
            [0, -4, -0.5],  # E
            [0, -4, 0.5],  # A
            [0, -7, 0.5],  # D
            [0, -7, -0.5],  # H
            # Cara lateral derecha
            [2, -4, 0.5],  # B
            [2, -4, -0.5],  # F
            [2, -7, -0.5],  # G
            [2, -7, 0.5],  # C
            # Cara superior
            [0, -4, 0.5],  # A
            [0, -4, -0.5],  # E
            [2, -4, -0.5],  # F
            [2, -4, 0.5],  # B
            # Cara inferior
            [2, -7, 0.5],  # C
            [2, -7, -0.5],  # G
            [0, -7, -0.5],  # H
            [0, -7, 0.5],  # D
        ]
        self.pieIzq = [
            # Cara frontal
            [-2, -7, 0.5],  # A
            [0, -7, 0.5],  # B
            [0, -7.5, 0.5],  # C
            [-2, -7.5, 0.5],  # D
            # Cara trasera
            [-2, -7, -0.5],  # E
            [0, -7, -0.5],  # F
            [0, -7.5, -0.5],  # G
            [-2, -7.5, -0.5],  # H
            # Cara lateral izquierda
            [-2, -7, -0.5],  # E
            [-2, -7, 0.5],  # A
            [-2, -7.5, 0.5],  # D
            [-2, -7.5, -0.5],  # H
            # Cara lateral derecha
            [0, -7, 0.5],  # B
            [0, -7, -0.5],  # F
            [0, -7.5, -0.5],  # G
            [0, -7.5, 0.5],  # C
            # Cara superior
            [-2, -7, 0.5],  # A
            [0, -7, 0.5],  # B
            [0, -7, -0.5],  # F
            [-2, -7, -0.5],  # E
            # Cara inferior
            [-2, -7.5, 0.5],  # D
            [0, -7.5, 0.5],  # C
            [0, -7.5, -0.5],  # G
            [-2, -7.5, -0.5],  # H
        ]
        self.pieDer = [
            # Cara frontal
            [0, -7, 0.5],  # A
            [2, -7, 0.5],  # B
            [2, -7.5, 0.5],  # C
            [0, -7.5, 0.5],  # D
            # Cara trasera
            [0, -7, -0.5],  # E
            [2, -7, -0.5],  # F
            [2, -7.5, -0.5],  # G
            [0, -7.5, -0.5],  # H
            # Cara lateral izquierda
            [0, -7, -0.5],  # E
            [0, -7, 0.5],  # A
            [0, -7.5, 0.5],  # D
            [0, -7.5, -0.5],  # H
            # Cara lateral derecha
            [2, -7, 0.5],  # B
            [2, -7, -0.5],  # F
            [2, -7.5, -0.5],  # G
            [2, -7.5, 0.5],  # C
            # Cara superior
            [0, -7, 0.5],  # A
            [2, -7, 0.5],  # B
            [2, -7, -0.5],  # F
            [0, -7, -0.5],  # E
            # Cara inferior
            [0, -7.5, 0.5],  # D
            [2, -7.5, 0.5],  # C
            [2, -7.5, -0.5],  # G
            [0, -7.5, -0.5],  # H
        ]
        self.boca1 = [
            # Cara frontal
            [-0.5, 1.3, 1.3],  # B
            [0, 1.2, 1.3],  # C
            [0.5, 1.3, 1.3],  # D
            [0.5, 1.1, 1.3],  # F
            [0, 0.9, 1.3],  # E
            [-0.5, 1.1, 1.3],  # A
        ]
        self.boca2 = [
            # Cara 1
            [0.5, 1.3, 1.3],  # B
            [0.5, 1.1, 1.3],  # F
            [0, 1.0, 1.3],  # G
            [0, 1.2, 1.3],  # C
            # Cara 2
            [0.5, 1.1, 1.3],  # A
            [0, 0.8, 1.3],  # H
            [0, 1.0, 1.3],  # G
            [0.5, 1.3, 1.3],  # D
            # Cara 3
            [0, 0.8, 1.3],  # E
            [0.5, 1.1, 1.3],  # A
            [0, 1.0, 1.3],  # G
            [-0.5, 1.1, 1.3],  # I
        ]
        self.boca3 = [
            # Cara 4
            [-0.5, 1.1, 1.3],  # I
            [-0.5, 1.3, 1.3],  # J
            [0.5, 1.3, 1.3],  # K
            [0.5, 1.1, 1.3],  # L
        ]
        self.ojos1 = [
            [-0.5, 1.7, 1.21],  # Punto A (ojo izquierdo cerrado)
            [-0.3, 1.7, 1.21],  # Punto B (ojo izquierdo cerrado)
            [0.5, 1.8, 1.21],  # Punto A (ojo derecho abierto)
            [0.5, 1.6, 1.21],  # Punto B (ojo derecho abierto)
            [0.3, 1.6, 1.21],  # Punto C (ojo derecho abierto)
            [0.3, 1.8, 1.21],  # Punto D (ojo derecho abierto)
        ]
        self.ojos2 = [
            # Ojo izquierdo cerrado
            [
                [-0.5, 1.7, 1.21],  # Punto A
                [-0.5, 1.6, 1.21],  # Punto B
                [-0.3, 1.6, 1.21],  # Punto C
                [-0.3, 1.7, 1.21],  # Punto D
            ],
            # Ojo derecho cerrado
            [
                [0.5, 1.7, 1.21],  # Punto A
                [0.5, 1.6, 1.21],  # Punto B
                [0.3, 1.6, 1.21],  # Punto C
                [0.3, 1.7, 1.21],  # Punto D
            ],
        ]
        self.ojos3 = [
            [-0.5, 1.7, 1.21],  # Punto A
            [-0.5, 1.6, 1.21],  # Punto B
            [-0.3, 1.6, 1.21],  # Punto C
            [-0.3, 1.7, 1.21],  # Punto D
            [0.5, 1.7, 1.21],  # Punto A
            [0.5, 1.6, 1.21],  # Punto B
            [0.3, 1.6, 1.21],  # Punto C
            [0.3, 1.7, 1.21],  # Punto D
        ]


m = Matrices()


def ros():
    glBegin(GL_QUADS)
    glColor3f(1.0, 0.8, 0.6)
    for vertex_coords in m.rostro:
        glVertex3f(*vertex_coords)
    glEnd()

def eyes():
    glColor3f(0,0,0)
    glBegin(GL_QUADS)
    for i, cor in enumerate(m.ojos):
        if i == 0:
            glTexCoord2f(0, 1)
        elif i == 1:
            glTexCoord2f(0, 0)
        elif i == 2:
            glTexCoord2f(1, 0)
        elif i == 3:
            glTexCoord2f(1, 1)
        glVertex3f(*cor)
    glEnd()
    glColor3f(1.0, 1.0, 1.0)  # Blanco

def cabeza1():
    # Cara frontal
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, es.load_texture('Imagenes/casco.jpeg'))
    glBegin(GL_QUADS)
    glTexCoord2f(0, 1)
    glVertex3f(*m.cabeza[0])  # A
    glTexCoord2f(0, 0)
    glVertex3f(*m.cabeza[1])  # B
    glTexCoord2f(1, 0)
    glVertex3f(*m.cabeza[2])  # C
    glTexCoord2f(1, 1)
    glVertex3f(*m.cabeza[3])  # D
    glEnd()
    glDisable(GL_TEXTURE_2D)

    # Cara trasera
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, es.load_texture('Imagenes/casco.jpeg'))
    glBegin(GL_QUADS)
    glTexCoord2f(0, 1)
    glVertex3f(*m.cabeza[4])  # E
    glTexCoord2f(0, 0)
    glVertex3f(*m.cabeza[5])  # F
    glTexCoord2f(1, 0)
    glVertex3f(*m.cabeza[6])  # G
    glTexCoord2f(1, 1)
    glVertex3f(*m.cabeza[7])  # H
    glEnd()
    glDisable(GL_TEXTURE_2D)

    # Cara izquierda
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, es.load_texture('Imagenes/casco.jpeg'))
    glBegin(GL_QUADS)
    glTexCoord2f(0, 1)
    glVertex3f(*m.cabeza[0])  # A
    glTexCoord2f(0, 0)
    glVertex3f(*m.cabeza[4])  # E
    glTexCoord2f(1, 0)
    glVertex3f(*m.cabeza[5])  # F
    glTexCoord2f(1, 1)
    glVertex3f(*m.cabeza[1])  # B
    glEnd()
    glDisable(GL_TEXTURE_2D)

    # Cara derecha
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, es.load_texture('Imagenes/casco.jpeg'))
    glBegin(GL_QUADS)
    glTexCoord2f(0, 1)
    glVertex3f(*m.cabeza[3])  # D
    glTexCoord2f(0, 0)
    glVertex3f(*m.cabeza[7])  # H
    glTexCoord2f(1, 0)
    glVertex3f(*m.cabeza[6])  # G
    glTexCoord2f(1, 1)
    glVertex3f(*m.cabeza[2])  # C
    glEnd()
    glDisable(GL_TEXTURE_2D)

    # Cara superior
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, es.load_texture('Imagenes/casco.jpeg'))
    glBegin(GL_QUADS)
    glTexCoord2f(0, 1)
    glVertex3f(*m.cabeza[0])  # A
    glTexCoord2f(0, 0)
    glVertex3f(*m.cabeza[3])  # D
    glTexCoord2f(1, 0)
    glVertex3f(*m.cabeza[7])  # H
    glTexCoord2f(1, 1)
    glVertex3f(*m.cabeza[4])  # E
    glEnd()
    glDisable(GL_TEXTURE_2D)

    # Cara inferior
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, es.load_texture('Imagenes/mascara.jpeg'))
    glBegin(GL_QUADS)
    glTexCoord2f(0, 1)
    glVertex3f(*m.cabeza[1])  # B
    glTexCoord2f(0, 0)
    glVertex3f(*m.cabeza[2])  # C
    glTexCoord2f(1, 0)
    glVertex3f(*m.cabeza[6])  # G
    glTexCoord2f(1, 1)
    glVertex3f(*m.cabeza[5])  # F
    glEnd()
    glDisable(GL_TEXTURE_2D)

def tronco1():
    # Cara frontal
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, es.load_texture('Imagenes/playera.jpeg'))
    glBegin(GL_QUADS)
    glTexCoord2f(0, 1)
    glVertex3f(*m.tronco[0])  # A
    glTexCoord2f(0, 0)
    glVertex3f(*m.tronco[1])  # B
    glTexCoord2f(1, 0)
    glVertex3f(*m.tronco[2])  # C
    glTexCoord2f(1, 1)
    glVertex3f(*m.tronco[3])  # D
    glEnd()
    glDisable(GL_TEXTURE_2D)

    # Cara trasera
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, es.load_texture('Imagenes/tt.jpeg'))
    glBegin(GL_QUADS)
    glTexCoord2f(0, 1)
    glVertex3f(*m.tronco[4])  # E
    glTexCoord2f(0, 0)
    glVertex3f(*m.tronco[5])  # F
    glTexCoord2f(1, 0)
    glVertex3f(*m.tronco[6])  # G
    glTexCoord2f(1, 1)
    glVertex3f(*m.tronco[7])  # H
    glEnd()
    glDisable(GL_TEXTURE_2D)

    # Cara izquierda
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, es.load_texture('Imagenes/tt.jpeg'))
    glBegin(GL_QUADS)
    glTexCoord2f(0, 1)
    glVertex3f(*m.tronco[0])  # A
    glTexCoord2f(0, 0)
    glVertex3f(*m.tronco[4])  # E
    glTexCoord2f(1, 0)
    glVertex3f(*m.tronco[5])  # F
    glTexCoord2f(1, 1)
    glVertex3f(*m.tronco[1])  # B
    glEnd()
    glDisable(GL_TEXTURE_2D)

    # Cara derecha
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, es.load_texture('Imagenes/tt.jpeg'))
    glBegin(GL_QUADS)
    glTexCoord2f(0, 1)
    glVertex3f(*m.tronco[3])  # D
    glTexCoord2f(0, 0)
    glVertex3f(*m.tronco[7])  # H
    glTexCoord2f(1, 0)
    glVertex3f(*m.tronco[6])  # G
    glTexCoord2f(1, 1)
    glVertex3f(*m.tronco[2])  # C
    glEnd()
    glDisable(GL_TEXTURE_2D)

    # Cara superior
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, es.load_texture('Imagenes/playera.jpeg'))
    glBegin(GL_QUADS)
    glTexCoord2f(0, 1)
    glVertex3f(*m.tronco[0])  # A
    glTexCoord2f(0, 0)
    glVertex3f(*m.tronco[3])  # D
    glTexCoord2f(1, 0)
    glVertex3f(*m.tronco[7])  # H
    glTexCoord2f(1, 1)
    glVertex3f(*m.tronco[4])  # E
    glEnd()
    glDisable(GL_TEXTURE_2D)

    # Cara inferior
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, es.load_texture('Imagenes/playera.jpeg'))
    glBegin(GL_QUADS)
    glTexCoord2f(0, 1)
    glVertex3f(*m.tronco[1])  # B
    glTexCoord2f(0, 0)
    glVertex3f(*m.tronco[2])  # C
    glTexCoord2f(1, 0)
    glVertex3f(*m.tronco[6])  # G
    glTexCoord2f(1, 1)
    glVertex3f(*m.tronco[5])  # F

    glEnd()
    glDisable(GL_TEXTURE_2D)

def brazoIzq1():
    glEnable(GL_TEXTURE_2D)
    # Textura para todas las caras del brazo izquierdo
    glBindTexture(GL_TEXTURE_2D, es.load_texture('Imagenes/brazo.jpeg'))
    glBegin(GL_QUADS)
    # Cara frontal
    glTexCoord2f(0, 1)
    glVertex3f(*m.brazoIzq[0])  # A
    glTexCoord2f(0, 0)
    glVertex3f(*m.brazoIzq[1])  # B
    glTexCoord2f(1, 0)
    glVertex3f(*m.brazoIzq[2])  # C
    glTexCoord2f(1, 1)
    glVertex3f(*m.brazoIzq[3])  # D

    # Cara trasera
    glTexCoord2f(0, 1)
    glVertex3f(*m.brazoIzq[4])  # E
    glTexCoord2f(0, 0)
    glVertex3f(*m.brazoIzq[5])  # F
    glTexCoord2f(1, 0)
    glVertex3f(*m.brazoIzq[6])  # G
    glTexCoord2f(1, 1)
    glVertex3f(*m.brazoIzq[7])  # H

    # Cara izquierda
    glTexCoord2f(0, 1)
    glVertex3f(*m.brazoIzq[0])  # A
    glTexCoord2f(0, 0)
    glVertex3f(*m.brazoIzq[4])  # E
    glTexCoord2f(1, 0)
    glVertex3f(*m.brazoIzq[5])  # F
    glTexCoord2f(1, 1)
    glVertex3f(*m.brazoIzq[1])  # B

    # Cara derecha
    glTexCoord2f(0, 1)
    glVertex3f(*m.brazoIzq[3])  # D
    glTexCoord2f(0, 0)
    glVertex3f(*m.brazoIzq[7])  # H
    glTexCoord2f(1, 0)
    glVertex3f(*m.brazoIzq[6])  # G
    glTexCoord2f(1, 1)
    glVertex3f(*m.brazoIzq[2])  # C

    # Cara superior
    glTexCoord2f(0, 1)
    glVertex3f(*m.brazoIzq[0])  # A
    glTexCoord2f(0, 0)
    glVertex3f(*m.brazoIzq[3])  # D
    glTexCoord2f(1, 0)
    glVertex3f(*m.brazoIzq[7])  # H
    glTexCoord2f(1, 1)
    glVertex3f(*m.brazoIzq[4])  # E

    # Cara inferior
    glTexCoord2f(0, 1)
    glVertex3f(*m.brazoIzq[1])  # B
    glTexCoord2f(0, 0)
    glVertex3f(*m.brazoIzq[2])  # C
    glTexCoord2f(1, 0)
    glVertex3f(*m.brazoIzq[6])  # G
    glTexCoord2f(1, 1)
    glVertex3f(*m.brazoIzq[5])  # F

    glEnd()
    glDisable(GL_TEXTURE_2D)

def brazoDer1():
    glEnable(GL_TEXTURE_2D)
    # Textura para todas las caras del brazo derecho
    glBindTexture(GL_TEXTURE_2D, es.load_texture('Imagenes/brazo.jpeg'))
    glBegin(GL_QUADS)
    # Cara frontal
    glTexCoord2f(0, 1)
    glVertex3f(*m.brazoDer[0])  # A
    glTexCoord2f(0, 0)
    glVertex3f(*m.brazoDer[1])  # B
    glTexCoord2f(1, 0)
    glVertex3f(*m.brazoDer[2])  # C
    glTexCoord2f(1, 1)
    glVertex3f(*m.brazoDer[3])  # D

    # Cara trasera
    glTexCoord2f(0, 1)
    glVertex3f(*m.brazoDer[4])  # E
    glTexCoord2f(0, 0)
    glVertex3f(*m.brazoDer[5])  # F
    glTexCoord2f(1, 0)
    glVertex3f(*m.brazoDer[6])  # G
    glTexCoord2f(1, 1)
    glVertex3f(*m.brazoDer[7])  # H

    # Cara izquierda
    glTexCoord2f(0, 1)
    glVertex3f(*m.brazoDer[0])  # A
    glTexCoord2f(0, 0)
    glVertex3f(*m.brazoDer[4])  # E
    glTexCoord2f(1, 0)
    glVertex3f(*m.brazoDer[5])  # F
    glTexCoord2f(1, 1)
    glVertex3f(*m.brazoDer[1])  # B

    # Cara derecha
    glTexCoord2f(0, 1)
    glVertex3f(*m.brazoDer[3])  # D
    glTexCoord2f(0, 0)
    glVertex3f(*m.brazoDer[7])  # H
    glTexCoord2f(1, 0)
    glVertex3f(*m.brazoDer[6])  # G
    glTexCoord2f(1, 1)
    glVertex3f(*m.brazoDer[2])  # C

    # Cara superior
    glTexCoord2f(0, 1)
    glVertex3f(*m.brazoDer[0])  # A
    glTexCoord2f(0, 0)
    glVertex3f(*m.brazoDer[3])  # D
    glTexCoord2f(1, 0)
    glVertex3f(*m.brazoDer[7])  # H
    glTexCoord2f(1, 1)
    glVertex3f(*m.brazoDer[4])  # E

    # Cara inferior
    glTexCoord2f(0, 1)
    glVertex3f(*m.brazoDer[1])  # B
    glTexCoord2f(0, 0)
    glVertex3f(*m.brazoDer[2])  # C
    glTexCoord2f(1, 0)
    glVertex3f(*m.brazoDer[6])  # G
    glTexCoord2f(1, 1)
    glVertex3f(*m.brazoDer[5])  # F

    glEnd()
    glDisable(GL_TEXTURE_2D)

def manoIzq1():
    glBegin(GL_QUADS)
    #glColor3f(1.0, 0.8, 0.6)
    for cor in m.manoIzq:
        glVertex3f(*cor)
    glEnd()

def manoDer1():
    glBegin(GL_QUADS)
    #glColor3f(1.0, 0.8, 0.6)
    for cor in m.manoDer:
        glVertex(*cor)
    glEnd()

def piernaIzq1():    
    # Cara frontal
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, es.load_texture('Imagenes/playera.jpeg'))
    glBegin(GL_QUADS)
    glTexCoord2f(0, 1)
    glVertex3f(*m.pierIzq[0])  # A
    glTexCoord2f(0, 0)
    glVertex3f(*m.pierIzq[1])  # B
    glTexCoord2f(1, 0)
    glVertex3f(*m.pierIzq[2])  # C
    glTexCoord2f(1, 1)
    glVertex3f(*m.pierIzq[3])  # D
    glEnd()
    glDisable(GL_TEXTURE_2D)

    # Cara trasera
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, es.load_texture('Imagenes/pt.jpeg'))
    glBegin(GL_QUADS)
    glTexCoord2f(0, 1)
    glVertex3f(*m.pierIzq[4])  # E
    glTexCoord2f(0, 0)
    glVertex3f(*m.pierIzq[5])  # F
    glTexCoord2f(1, 0)
    glVertex3f(*m.pierIzq[6])  # G
    glTexCoord2f(1, 1)
    glVertex3f(*m.pierIzq[7])  # H
    glEnd()
    glDisable(GL_TEXTURE_2D)

    # Cara izquierda
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, es.load_texture('Imagenes/playera.jpeg'))
    glBegin(GL_QUADS)
    glTexCoord2f(0, 1)
    glVertex3f(*m.pierIzq[0])  # A
    glTexCoord2f(0, 0)
    glVertex3f(*m.pierIzq[4])  # E
    glTexCoord2f(1, 0)
    glVertex3f(*m.pierIzq[5])  # F
    glTexCoord2f(1, 1)
    glVertex3f(*m.pierIzq[1])  # B
    glEnd()
    glDisable(GL_TEXTURE_2D)

    # Cara derecha
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, es.load_texture('Imagenes/playera.jpeg'))
    glBegin(GL_QUADS)
    glTexCoord2f(0, 1)
    glVertex3f(*m.pierIzq[3])  # D
    glTexCoord2f(0, 0)
    glVertex3f(*m.pierIzq[7])  # H
    glTexCoord2f(1, 0)
    glVertex3f(*m.pierIzq[6])  # G
    glTexCoord2f(1, 1)
    glVertex3f(*m.pierIzq[2])  # C
    glEnd()
    glDisable(GL_TEXTURE_2D)

    # Cara superior
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, es.load_texture('Imagenes/playera.jpeg'))
    glBegin(GL_QUADS)
    glTexCoord2f(0, 1)
    glVertex3f(*m.pierIzq[0])  # A
    glTexCoord2f(0, 0)
    glVertex3f(*m.pierIzq[3])  # D
    glTexCoord2f(1, 0)
    glVertex3f(*m.pierIzq[7])  # H
    glTexCoord2f(1, 1)
    glVertex3f(*m.pierIzq[4])  # E
    glEnd()
    glDisable(GL_TEXTURE_2D)

    # Cara inferior
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, es.load_texture('Imagenes/playera.jpeg'))
    glBegin(GL_QUADS)
    glTexCoord2f(0, 1)
    glVertex3f(*m.pierIzq[1])  # B
    glTexCoord2f(0, 0)
    glVertex3f(*m.pierIzq[2])  # C
    glTexCoord2f(1, 0)
    glVertex3f(*m.pierIzq[6])  # G
    glTexCoord2f(1, 1)
    glVertex3f(*m.pierIzq[5])  # F
    glEnd()
    glDisable(GL_TEXTURE_2D)

def piernaDer1():
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, es.load_texture('Imagenes/playera.jpeg'))
    glBegin(GL_QUADS)
    
    # Cara frontal
    glTexCoord2f(0, 1)
    glVertex3f(*m.pierDer[0])  # A
    glTexCoord2f(1, 1)
    glVertex3f(*m.pierDer[1])  # B
    glTexCoord2f(1, 0)
    glVertex3f(*m.pierDer[2])  # C
    glTexCoord2f(0, 0)
    glVertex3f(*m.pierDer[3])  # D
    glEnd()
    glDisable(GL_TEXTURE_2D)

    # Cara trasera
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, es.load_texture('Imagenes/pt.jpeg'))
    glBegin(GL_QUADS)
    glTexCoord2f(0, 1)
    glVertex3f(*m.pierDer[4])  # E
    glTexCoord2f(1, 1)
    glVertex3f(*m.pierDer[5])  # F
    glTexCoord2f(1, 0)
    glVertex3f(*m.pierDer[6])  # G
    glTexCoord2f(0, 0)
    glVertex3f(*m.pierDer[7])  # H
    glEnd()
    glDisable(GL_TEXTURE_2D)

    # Cara izquierda
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, es.load_texture('Imagenes/playera.jpeg'))
    glBegin(GL_QUADS)
    glTexCoord2f(0, 1)
    glVertex3f(*m.pierDer[0])  # A
    glTexCoord2f(1, 1)
    glVertex3f(*m.pierDer[4])  # E
    glTexCoord2f(1, 0)
    glVertex3f(*m.pierDer[5])  # F
    glTexCoord2f(0, 0)
    glVertex3f(*m.pierDer[1])  # B
    glEnd()
    glDisable(GL_TEXTURE_2D)

    # Cara derecha
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, es.load_texture('Imagenes/playera.jpeg'))
    glBegin(GL_QUADS)
    glTexCoord2f(0, 1)
    glVertex3f(*m.pierDer[3])  # D
    glTexCoord2f(1, 1)
    glVertex3f(*m.pierDer[7])  # H
    glTexCoord2f(1, 0)
    glVertex3f(*m.pierDer[6])  # G
    glTexCoord2f(0, 0)
    glVertex3f(*m.pierDer[2])  # C
    glEnd()
    glDisable(GL_TEXTURE_2D)

    # Cara superior
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, es.load_texture('Imagenes/playera.jpeg'))
    glBegin(GL_QUADS)
    glTexCoord2f(0, 1)
    glVertex3f(*m.pierDer[0])  # A
    glTexCoord2f(1, 1)
    glVertex3f(*m.pierDer[3])  # D
    glTexCoord2f(1, 0)
    glVertex3f(*m.pierDer[7])  # H
    glTexCoord2f(0, 0)
    glVertex3f(*m.pierDer[4])  # E

    glEnd()
    glDisable(GL_TEXTURE_2D)

    # Cara inferior
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, es.load_texture('Imagenes/playera.jpeg'))
    glBegin(GL_QUADS)
    glTexCoord2f(0, 1)
    glVertex3f(*m.pierDer[1])  # B
    glTexCoord2f(1, 1)
    glVertex3f(*m.pierDer[2])  # C
    glTexCoord2f(1, 0)
    glVertex3f(*m.pierDer[6])  # G
    glTexCoord2f(0, 0)
    glVertex3f(*m.pierDer[5])  # F
    glEnd()
    glDisable(GL_TEXTURE_2D)

def pieIzq1():
    glBegin(GL_QUADS)
    #glColor3f(1.0, 1.0, 1.0)
    for cor in m.pieIzq:
        glVertex3f(*cor)
    glEnd()

def pieDer1():
    glBegin(GL_QUADS)
    #glColor3f(1.0, 1.0, 1.0)  # Color blanco
    for cor in m.pieDer:
        glVertex3f(*cor)
    glEnd()

def boca1():
    # Boca sonriente
    glBegin(GL_POLYGON)
    glColor3f(1.0, 0.0, 0.0)  # Rojo para la boca
    for cor in m.boca1:
        glVertex3f(*cor)
    glEnd()
    # Restablecer el color a blanco después de dibujar la boca
    glColor3f(1.0, 1.0, 1.0)  # Blanco

def boca2():
    glBegin(GL_POLYGON)
    glColor3f(1.0, 0.0, 0.0)  # Rojo para la boca
    for cor in m.boca2:
        glVertex3f(*cor)
    glEnd()
    glColor3f(1.0, 1.0, 1.0)  # Blanco

def boca3():
    glBegin(GL_QUADS)
    glColor3f(1.0, 0.0, 0.0)  # Rojo para la boca
    for cor in m.boca3:
        glVertex3f(*cor)
    glEnd()
    glColor3f(1.0, 1.0, 1.0)  # Blanco

def ojos11():
    glLineWidth(2.0)  # Ancho de la línea
    glBegin(GL_LINES)
    glColor3f(0.0, 0.0, 0.0)  # Color negro
    for cor in m.ojos1:
        glVertex3f(*cor)
    glEnd()
    glColor3f(1.0, 1.0, 1.0)  # Blanco

def ojos22():
    glLineWidth(2.0)  # Ancho de la línea

    # Dibuja el ojo izquierdo cerrado
    glBegin(GL_LINE_LOOP)
    glColor3f(0.0, 0.0, 0.0)  # Color negro
    for punto in m.ojos2[0]:
        glVertex3f(*punto)
    glEnd()
    glColor3f(1.0, 1.0, 1.0)  # Blanco

    # Dibuja el ojo derecho cerrado
    glBegin(GL_LINE_LOOP)
    glColor3f(0.0, 0.0, 0.0)  # Color negro
    for punto in m.ojos2[1]:
        glVertex3f(*punto)
    glEnd()
    glColor3f(1.0, 1.0, 1.0)  # Blanco

def ojos3():
    glLineWidth(2.0)  # Ancho de la línea
    # Ojo izquierdo cerrado
    glBegin(GL_LINE_LOOP)
    glColor3f(0.0, 0.0, 0.0)  # Color negro
    for cor in m.ojos3:
        glVertex3f(*cor)
    glEnd()
    glColor3f(1.0, 1.0, 1.0)  # Blanco

def brazoIzqUp():
    glPushMatrix()  # Guarda la matriz de transformación actual
    glTranslatef(-0.4, 0.0, 0.0)  # Traslada el brazo izquierdo a su posición original
    glRotatef(
        -65, 1, 0, 0
    )  # Aplica una rotación de 45 grados alrededor del eje X (para rotar hacia arriba)
    glTranslatef(
        0.4, 0.0, 0.0
    )  # Traslada el brazo izquierdo a su posición después de la rotación
    brazoIzq1()
    glPopMatrix()  # Restaura la matriz de transformación original

    glPushMatrix()  # Guarda la matriz de transformación actual
    glTranslatef(-0.4, 0.0, 0.0)  # Traslada la mano izquierda a su posición original
    glRotatef(-65, 1, 0, 0)  # Aplica una rotación de -90 grados alrededor del eje X
    glTranslatef(
        0.4, 0.0, 0.0
    )  # Traslada la mano izquierda a su posición después de la rotación
    manoIzq1()
    glPopMatrix()  # Restaura la matriz de transformación original

def brazoDerUp():
    glPushMatrix()  # Guarda la matriz de transformación actual
    glTranslatef(-0.4, 0.0, 0.0)  # Traslada el brazo izquierdo a su posición original
    glRotatef(
        -65, 1, 0, 0
    )  # Aplica una rotación de 45 grados alrededor del eje X (para rotar hacia arriba)
    glTranslatef(
        0.4, 0.0, 0.0
    )  # Traslada el brazo izquierdo a su posición después de la rotación
    brazoDer1()
    glPopMatrix()  # Restaura la matriz de transformación original

    glPushMatrix()  # Guarda la matriz de transformación actual
    glTranslatef(-0.4, 0.0, 0.0)  # Traslada la mano izquierda a su posición original
    glRotatef(-65, 1, 0, 0)  # Aplica una rotación de -90 grados alrededor del eje X
    glTranslatef(
        0.4, 0.0, 0.0
    )  # Traslada la mano izquierda a su posición después de la rotación
    manoDer1()
    glPopMatrix()  # Restaura la matriz de transformación original

def cabezaUp():
    glPushMatrix()  # Guarda la matriz de transformación actual
    glTranslatef(-0.4, 0.0, 0.0)  # Traslada el brazo izquierdo a su posición original
    glRotatef(
        -50, 1, 0, 0
    )  # Aplica una rotación de 45 grados alrededor del eje X (para rotar hacia arriba)
    glTranslatef(
        0.4, 0.0, 0.0
    )  # Traslada el brazo izquierdo a su posición después de la rotación
    casco()
    glPopMatrix()  # Restaura la matriz de transformación original

def voltear():
    glPushMatrix()  # Guarda la matriz de transformación actual
    glTranslatef(-0.4, 0.0, 0.0)  # Traslada el brazo izquierdo a su posición original
    glRotatef(
        -50, 0, 1, 0
    )  # Aplica una rotación de 45 grados alrededor del eje X (para rotar hacia arriba)
    glTranslatef(
        0.4, 0.0, 0.0
    )  # Traslada el brazo izquierdo a su posición después de la rotación
    casco()
    glPopMatrix()  # Restaura la matriz de transformación original

def caminar():
    glPushMatrix()
    glTranslatef(-0.4, -4.0, 0.0)
    glRotatef(-20, 1, 0, 0)
    glTranslatef(0.4, 4.0, 0.0)
    piernaDer1()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-0.4, -4.0, 0.0)
    glRotatef(20, 1, 0, 0)
    glTranslatef(0.4, 4.0, 0.0)
    piernaIzq1()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-0.4, -4.0, 0.0)
    glRotatef(-20, 1, 0, 0)
    glTranslatef(0.4, 4.0, 0.0)
    pieDer1()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-0.4, -4.0, 0.0)
    glRotatef(20, 1, 0, 0)
    glTranslatef(0.4, 4.0, 0.0)
    pieIzq1()
    glPopMatrix()

def casco():
    # Cara frontal
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, es.load_texture('Imagenes/mascara.jpeg'))
    glBegin(GL_QUADS)
    glTexCoord2f(0, 1)
    glVertex3f(*m.cabeza[0])  # A
    glTexCoord2f(0, 0)
    glVertex3f(*m.cabeza[1])  # B
    glTexCoord2f(1, 0)
    glVertex3f(*m.cabeza[2])  # C
    glTexCoord2f(1, 1)
    glVertex3f(*m.cabeza[3])  # D
    glEnd()
    glDisable(GL_TEXTURE_2D)

    # Cara trasera
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, es.load_texture('Imagenes/casco.jpeg'))
    glBegin(GL_QUADS)
    glTexCoord2f(0, 1)
    glVertex3f(*m.cabeza[4])  # E
    glTexCoord2f(0, 0)
    glVertex3f(*m.cabeza[5])  # F
    glTexCoord2f(1, 0)
    glVertex3f(*m.cabeza[6])  # G
    glTexCoord2f(1, 1)
    glVertex3f(*m.cabeza[7])  # H
    glEnd()
    glDisable(GL_TEXTURE_2D)

    # Cara izquierda
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, es.load_texture('Imagenes/casco.jpeg'))
    glBegin(GL_QUADS)
    glTexCoord2f(0, 1)
    glVertex3f(*m.cabeza[0])  # A
    glTexCoord2f(0, 0)
    glVertex3f(*m.cabeza[4])  # E
    glTexCoord2f(1, 0)
    glVertex3f(*m.cabeza[5])  # F
    glTexCoord2f(1, 1)
    glVertex3f(*m.cabeza[1])  # B
    glEnd()
    glDisable(GL_TEXTURE_2D)

    # Cara derecha
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, es.load_texture('Imagenes/casco.jpeg'))
    glBegin(GL_QUADS)
    glTexCoord2f(0, 1)
    glVertex3f(*m.cabeza[3])  # D
    glTexCoord2f(0, 0)
    glVertex3f(*m.cabeza[7])  # H
    glTexCoord2f(1, 0)
    glVertex3f(*m.cabeza[6])  # G
    glTexCoord2f(1, 1)
    glVertex3f(*m.cabeza[2])  # C
    glEnd()
    glDisable(GL_TEXTURE_2D)

    # Cara superior
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, es.load_texture('Imagenes/casco.jpeg'))
    glBegin(GL_QUADS)
    glTexCoord2f(0, 1)
    glVertex3f(*m.cabeza[0])  # A
    glTexCoord2f(0, 0)
    glVertex3f(*m.cabeza[3])  # D
    glTexCoord2f(1, 0)
    glVertex3f(*m.cabeza[7])  # H
    glTexCoord2f(1, 1)
    glVertex3f(*m.cabeza[4])  # E
    glEnd()
    glDisable(GL_TEXTURE_2D)

    # Cara inferior
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, es.load_texture('Imagenes/casco.jpeg'))
    glBegin(GL_QUADS)
    glTexCoord2f(0, 1)
    glVertex3f(*m.cabeza[1])  # B
    glTexCoord2f(0, 0)
    glVertex3f(*m.cabeza[2])  # C
    glTexCoord2f(1, 0)
    glVertex3f(*m.cabeza[6])  # G
    glTexCoord2f(1, 1)
    glVertex3f(*m.cabeza[5])  # F
    glEnd()
    glDisable(GL_TEXTURE_2D)