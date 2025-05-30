import pygame as py
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PIL import Image


def load_texture(filename):
    im = Image.open(filename)
    ix, iy, image = im.size[0], im.size[1], im.tobytes("raw", "RGBX", 0, -1)
    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    return texture_id


def escenario(filename):
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, load_texture(filename))
    
    # Primer panel (frontal)
    glBegin(GL_QUADS)
    glColor3f(1, 1, 1)
    glTexCoord2f(0, 0)
    glVertex3f(-140, -80, 170)  # ESQUINA INFERIOR IZQUIERDA (expandido en 30 unidades en Z)
    glTexCoord2f(1, 0)
    glVertex3f(170, -80, 170)  # ESQUINA INFERIOR DERECHA (expandido en 30 unidades en X y Z)
    glTexCoord2f(1, 1)
    glVertex3f(170, 80, 170)   # ESQUINA SUPERIOR DERECHA (expandido en 30 unidades en X y Z)
    glTexCoord2f(0, 1)
    glVertex3f(-140, 80, 170)  # ESQUINA SUPERIOR IZQUIERDA (expandido en 30 unidades en Z)
    glEnd()
    
    # Segundo panel (lateral derecho)
    glBegin(GL_QUADS)
    glColor3f(1, 1, 1)
    glTexCoord2f(0, 0)
    glVertex3f(170, -80, 170)  # ESQUINA INFERIOR IZQUIERDA (expandido en 30 unidades en X y Z)
    glTexCoord2f(1, 0)
    glVertex3f(170, -80, -200)  # ESQUINA INFERIOR DERECHA (expandido en 30 unidades en X y -60 unidades en Z)
    glTexCoord2f(1, 1)
    glVertex3f(170, 80, -200)  # ESQUINA SUPERIOR DERECHA (expandido en 30 unidades en X y -60 unidades en Z)
    glTexCoord2f(0, 1)
    glVertex3f(170, 80, 170)  # ESQUINA SUPERIOR IZQUIERDA (expandido en 30 unidades en X y Z)
    glEnd()
    
    # Tercer panel (posterior)
    glBegin(GL_QUADS)
    glColor3f(1, 1, 1)
    glTexCoord2f(0, 0)
    glVertex3f(170, -80, -200)  # ESQUINA INFERIOR IZQUIERDA (expandido en 30 unidades en X y -60 unidades en Z)
    glTexCoord2f(1, 0)
    glVertex3f(-140, -80, -200)  # ESQUINA INFERIOR DERECHA (expandido en -60 unidades en Z)
    glTexCoord2f(1, 1)
    glVertex3f(-140, 80, -200)  # ESQUINA SUPERIOR DERECHA (expandido en -60 unidades en Z)
    glTexCoord2f(0, 1)
    glVertex3f(170, 80, -200)  # ESQUINA SUPERIOR IZQUIERDA (expandido en 30 unidades en X y -60 unidades en Z)
    glEnd()
    
    # Cuarto panel (lateral izquierdo)
    glBegin(GL_QUADS)
    glColor3f(1, 1, 1)
    glTexCoord2f(0, 0)
    glVertex3f(-140, -80, -200)  # ESQUINA INFERIOR IZQUIERDA (expandido en -60 unidades en Z)
    glTexCoord2f(1, 0)
    glVertex3f(-140, -80, 170)  # ESQUINA INFERIOR DERECHA (expandido en 30 unidades en Z)
    glTexCoord2f(1, 1)
    glVertex3f(-140, 80, 170)  # ESQUINA SUPERIOR DERECHA (expandido en 30 unidades en Z)
    glTexCoord2f(0, 1)
    glVertex3f(-140, 80, -200)  # ESQUINA SUPERIOR IZQUIERDA (expandido en -60 unidades en Z)
    glEnd()

    glDisable(GL_TEXTURE_2D)






def piso(filename):
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, load_texture(filename))
    glBegin(GL_QUADS)
    glColor3f(1, 1, 1)
    glTexCoord2f(0, 0)
    glVertex3f(-140, -80, -200)  # ESQUINA INFERIOR IZQUIERDA (ajustado en Z)
    glTexCoord2f(1, 0)
    glVertex3f(170, -80, -200)  # ESQUINA INFERIOR DERECHA (expandido en 30 unidades en X y ajustado en Z)
    glTexCoord2f(1, 1)
    glVertex3f(170, -80, 170)  # ESQUINA SUPERIOR DERECHA (expandido en 30 unidades en X y Z)
    glTexCoord2f(0, 1)
    glVertex3f(-140, -80, 170)  # ESQUINA SUPERIOR IZQUIERDA (ajustado en Z)
    glEnd()
    glDisable(GL_TEXTURE_2D)

def techo(filename):
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, load_texture(filename))
    glBegin(GL_QUADS)
    glColor3f(1, 1, 1)
    glTexCoord2f(0, 0)
    glVertex3f(-140, 80, -200)  # ESQUINA INFERIOR IZQUIERDA (ajustado en Z)
    glTexCoord2f(1, 0)
    glVertex3f(170, 80, -200)  # ESQUINA INFERIOR DERECHA (expandido en 30 unidades en X y ajustado en Z)
    glTexCoord2f(1, 1)
    glVertex3f(170, 80, 170)  # ESQUINA SUPERIOR DERECHA (expandido en 30 unidades en X y Z)
    glTexCoord2f(0, 1)
    glVertex3f(-140, 80, 170)  # ESQUINA SUPERIOR IZQUIERDA (ajustado en Z)
    glEnd()
    glDisable(GL_TEXTURE_2D)









