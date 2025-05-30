from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *

def iluminacion(R, G, B):
    glEnable(GL_LIGHTING)  # Habilita la iluminación
    glEnable(GL_LIGHT0)  # Fuente de luz frontal
    glEnable(GL_LIGHT1)  # Fuente de luz trasera
    glEnable(GL_LIGHT2)  # Fuente de luz izquierda
    glEnable(GL_LIGHT3)  # Fuente de luz derecha
    glEnable(GL_DEPTH_TEST)  # Habilita la primera frontera de luz

    # Propiedades de la fuente de luz frontal
    posicion_luz_frontal = (0.0, 10.0, 30.0, 1.0)
    glLightfv(GL_LIGHT0, GL_POSITION, posicion_luz_frontal)
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.0, 0.0, 0.0, 1.0))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (R, G, B, 1.0))

    # Propiedades de la fuente de luz trasera
    posicion_luz_trasera = (0.0, 10.0, -30.0, 1.0)
    glLightfv(GL_LIGHT1, GL_POSITION, posicion_luz_trasera)
    glLightfv(GL_LIGHT1, GL_AMBIENT, (0.0, 0.0, 10, 1.0))
    glLightfv(GL_LIGHT1, GL_DIFFUSE, (R, G, B, 1.0))

    # Propiedades de la fuente de luz izquierda
    posicion_luz_izquierda = (-30.0, 10.0, 20, 1.0)
    glLightfv(GL_LIGHT2, GL_POSITION, posicion_luz_izquierda)
    glLightfv(GL_LIGHT2, GL_AMBIENT, (0.0, 0.0, 0.0, 1.0))
    glLightfv(GL_LIGHT2, GL_DIFFUSE, (R, G, B, 1.0))

    # Propiedades de la fuente de luz derecha
    posicion_luz_derecha = (30.0, 10.0, 20, 1.0)
    glLightfv(GL_LIGHT3, GL_POSITION, posicion_luz_derecha)
    glLightfv(GL_LIGHT3, GL_AMBIENT, (0.0, 0.0, 0.0, 1.0))
    glLightfv(GL_LIGHT3, GL_DIFFUSE, (R, G, B, 1.0))

def set_material(ambient_r, ambient_g, ambient_b, diffuse_r, diffuse_g, diffuse_b, specular_r, specular_g, specular_b, shininess):
    ambient = [ambient_r, ambient_g, ambient_b, 1.0]
    diffuse = [diffuse_r, diffuse_g, diffuse_b, 1.0]
    specular = [specular_r, specular_g, specular_b, 1.0]
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, ambient)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, diffuse)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, specular)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, shininess)

def setup_lighting():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    light_pos = (1, 10, 1, 0)
    glLightfv(GL_LIGHT0, GL_POSITION, light_pos)