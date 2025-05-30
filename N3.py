import pygame as py
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PIL import Image
import random
from a_escenario import load_texture

puntos = [None] * 15  # Inicializa la lista p con 15 elementos None

class Nivel3:
    def __init__(self):
        self.planos_basura = []
    
    def crear_planos_laterales_random(self):
        for _ in range(15):  # Crear 15 planos
            x = random.uniform(-60, 55)  # Rango de -60 a 55 para que el plano tenga una anchura de 5 unidades
            z = random.uniform(-60, 60)  # Valor constante para z
            plano = [
                (x, -7.5, z),
                (x + 5, -7.5, z),
                (x + 5, -2.4, z),
                (x, -2.5, z)
            ]
            puntos[_] = (x + 2.5, 0, z)
            self.planos_basura.append(plano)

    def dibujar_planos_basura(self, filename):
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, load_texture(filename))
        glBegin(GL_QUADS)
        glColor(1, 1, 1)
        for plano in self.planos_basura:
            glTexCoord2f(0, 0)
            glVertex3f(*plano[0])
            glTexCoord2f(1, 0)
            glVertex3f(*plano[1])
            glTexCoord2f(1, 1)
            glVertex3f(*plano[2])
            glTexCoord2f(0, 1)
            glVertex3f(*plano[3])
        glEnd()
    

obj = Nivel3()

# Llamar a esta función para generar un nuevo plano de basura
obj.crear_planos_laterales_random()

def crea_basura():
    # Dibujar otros objetos si es necesario
    obj.dibujar_planos_basura("Imagenes/basura.jpg")

