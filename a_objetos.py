import pygame as py
from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


class Objetos:
    def __init__(self):
        self.obj1 = [
            # Cara inferior
            (-14, -7, 0),
            (-12, -7, 0),
            (-12, -5, 0),
            (-14, -5, 0),
            # Cara superior
            (-14, -7, 2),
            (-12, -7, 2),
            (-12, -5, 2),
            (-14, -5, 2),
            # Lado izquierdo
            (-14, -7, 0),
            (-14, -5, 0),
            (-14, -5, 2),
            (-14, -7, 2),
            # Lado derecho
            (-12, -7, 0),
            (-12, -5, 0),
            (-12, -5, 2),
            (-12, -7, 2),
            # Cara frontal
            (-14, -7, 0),
            (-12, -7, 0),
            (-12, -7, 2),
            (-14, -7, 2),
            # Cara trasera
            (-14, -5, 0),
            (-12, -5, 0),
            (-12, -5, 2),
            (-14, -5, 2),
        ]
        self.obj2 = [
            # Cara inferior
            (14, -7, 0),
            (12, -7, 0),
            (12, -5, 0),
            (14, -5, 0),
            # Cara superior
            (14, -7, 2),
            (12, -7, 2),
            (12, -5, 2),
            (14, -5, 2),
            # Lado izquierdo
            (14, -7, 0),
            (14, -5, 0),
            (14, -5, 2),
            (14, -7, 2),
            # Lado derecho
            (12, -7, 0),
            (12, -5, 0),
            (12, -5, 2),
            (12, -7, 2),
            # Cara frontal
            (14, -7, 0),
            (12, -7, 0),
            (12, -7, 2),
            (14, -7, 2),
            # Cara trasera
            (14, -5, 0),
            (12, -5, 0),
            (12, -5, 2),
            (14, -5, 2),
        ]
        self.obj3 = [
            # Cara inferior
            (5, -7, 2),
            (3, -7, 2),
            (3, -5, 2),
            (5, -5, 2),
            # Cara superior
            (5, -7, 4),
            (3, -7, 4),
            (3, -5, 4),
            (5, -5, 4),
            # Lado izquierdo
            (5, -7, 2),
            (5, -5, 2),
            (5, -5, 4),
            (5, -7, 4),
            # Lado derecho
            (3, -7, 2),
            (3, -5, 2),
            (3, -5, 4),
            (3, -7, 4),
            # Cara frontal
            (5, -7, 2),
            (3, -7, 2),
            (3, -7, 4),
            (5, -7, 4),
            # Cara trasera
            (5, -5, 2),
            (3, -5, 2),
            (3, -5, 4),
            (3, -5, 4),
        ]


obj = Objetos()


def Obj1():
    glBegin(GL_QUADS)
    glColor3f(0, 1, 0)
    for vertex_coords in obj.obj1:
        glVertex3f(*vertex_coords)
    glEnd()


def Obj2():
    glBegin(GL_QUADS)
    glColor3f(0, 1, 0)
    for vertex_coords in obj.obj2:
        glVertex3f(*vertex_coords)
    glEnd()

def Obj3():
    glBegin(GL_QUADS)
    glColor3f(0, 1, 0)
    for vertex_coords in obj.obj3:
        glVertex3f(*vertex_coords)
    glEnd()

