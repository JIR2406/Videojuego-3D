import pygame as py
from OpenGL.GLU import *
from OpenGL.GL import * 
from OpenGL.GLUT import *

def texto(text, posx, posy, posz, sizeFont, R,G,B,RB,GB,BB):
    font = py.font.Font(None, sizeFont)
    text_surface = font.render(text, True, (R,G,B), (RB,GB,BB))
    text_data = py.image.tostring(text_surface, "RGBA", True)
    glRasterPos3d(posx,posy,posz) #posicion de texto en el espacio 
    glDrawPixels(text_surface.get_width(), text_surface.get_height(),GL_RGBA, GL_UNSIGNED_BYTE, text_data)

def nombresTxt(texto, posx, posy, posz, sizeFont, R, G, B):
    font = py.font.Font(None, sizeFont)
    text_surface = font.render(texto, True, (R, G, B))
    text_data = py.image.tostring(text_surface, "RGBA", True)
    glRasterPos3d(posx, posy, posz)  # Posición de texto en el espacio 
    glDrawPixels(text_surface.get_width(), text_surface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, text_data)



def controles():
    texto("1: Gesto 1", 825, 375, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("2: Gesto 2", 825, 345, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("3: Gesto 3", 825, 315, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("4: Gesto 4", 825, 285, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("5: Gesto 5", 825, 255, 0, 30, 0, 122, 204, 255, 255, 255)

    texto("6: Escenario 1", 590, 375, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("7: Escenario 2", 590, 345, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("8: Escenario 3", 590, 315, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("9: Escenario 4", 590, 285, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("0: Escenario 5", 590, 255, 0, 30, 0, 122, 204, 255, 255, 255)

    texto("Q: Levantar Brazo Derecho", 160, 375, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("E: Mirar Arriba", 160, 345, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("R: Voltear", 160, 315, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("T: Mover pies", 160, 285, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("Y: Posicion Original", 160, 255, 0, 30, 0, 122, 204, 255, 255, 255)

    texto("Flecha Up: Camara Arriba", 250, 675, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("Flecha Left: Camara a la Izquierda", 250, 645, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("Flecha Right: Camara a la Derecha", 250, 615, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("Flecha Down: Camara Abajo", 250, 585, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("Z: Acercar Camara", 250, 555, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("X: Alejar Camara", 250, 525, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("P: Activar Sombra", 250, 495, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("O: Activar Luz", 250, 465, 0, 30, 0, 122, 204, 255, 255, 255)

    texto("W: Mover Adelante", 1225, 375, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("S: Mover Atras", 1225, 345, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("A: Mover Izquierda", 1225, 315, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("D: Mover Derecha", 1225, 285, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("N: Posicion Original", 1225, 255, 0, 30, 0, 122, 204, 255, 255, 255)

    texto("F1: Sonido ON", 1020, 375, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("F2: Sonido OFF", 1020, 345, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("ESC: Cerrar ", 1020, 315, 0, 30, 0, 122, 204, 255, 255, 255)

def controlesJake():
    texto("1: Gesto 1", 825, 375, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("2: Gesto 2", 825, 345, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("3: Gesto 3", 825, 315, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("4: Gesto 4", 825, 285, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("5: Gesto 5", 825, 255, 0, 30, 0, 122, 204, 255, 255, 255)

    texto("6: Escenario 1", 590, 375, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("7: Escenario 2", 590, 345, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("8: Escenario 3", 590, 315, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("9: Escenario 4", 590, 285, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("0: Escenario 5", 590, 255, 0, 30, 0, 122, 204, 255, 255, 255)

    texto("Q: Levantar Brazo Derecho", 160, 375, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("E: Mirar Arriba", 160, 345, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("R: Voltear", 160, 315, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("T: Mover pies", 160, 285, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("Y: Posicion Original", 160, 255, 0, 30, 0, 122, 204, 255, 255, 255)

    texto("Flecha Up: Camara Arriba", 250, 675, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("Flecha Left: Camara a la Izquierda", 250, 645, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("Flecha Right: Camara a la Derecha", 250, 615, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("Flecha Down: Camara Abajo", 250, 585, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("Z: Acercar Camara", 250, 555, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("X: Alejar Camara", 250, 525, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("P: Activar Sombra", 250, 495, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("O: Activar Luz", 250, 465, 0, 30, 0, 122, 204, 255, 255, 255)

    texto("W: Mover Adelante", 1225, 375, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("S: Mover Atras", 1225, 345, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("A: Mover Izquierda", 1225, 315, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("D: Mover Derecha", 1225, 285, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("N: Posicion Original", 1225, 255, 0, 30, 0, 122, 204, 255, 255, 255)

    texto("F1: Sonido ON", 1020, 375, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("F2: Sonido OFF", 1020, 345, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("ESC: Cerrar ", 1020, 315, 0, 30, 0, 122, 204, 255, 255, 255)

def controlesPanda():
    texto("1: Gesto 1", 825, 375, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("2: Gesto 2", 825, 345, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("3: Gesto 3", 825, 315, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("4: Gesto 4", 825, 285, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("5: Gesto 5", 825, 255, 0, 30, 0, 122, 204, 255, 255, 255)

    texto("6: Escenario 1", 590, 375, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("7: Escenario 2", 590, 345, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("8: Escenario 3", 590, 315, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("9: Escenario 4", 590, 285, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("0: Escenario 5", 590, 255, 0, 30, 0, 122, 204, 255, 255, 255)

    texto("Q: Pieran DD Up", 160, 375, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("E: Pieran DI Up", 160 , 345, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("R: Pieran TD Up", 160 , 315, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("T: Pieran DI Up", 160, 285, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("Y: Piernas D Up", 160, 255, 0, 30, 0, 122, 204, 255, 255, 255)

    texto("Flecha Up: Camara Arriba", 250, 675, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("Flecha Left: Camara a la Izquierda", 250, 645, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("Flecha Right Camara a la Derecha", 250, 615, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("Flecha Down Camara Abajo", 250, 585, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("Z: Acercar Camara", 250, 555, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("X: Alejar Camara", 250, 525, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("P: Activar Sombra", 250, 495, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("O: Activar Luz", 250, 465, 0, 30, 0, 122, 204, 255, 255, 255)

    texto("W: Mover Adelante", 1225, 375, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("S: Mover Atras", 1225, 345, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("A: Mover Izquierda", 1225, 315, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("D: Mover Derecha", 1225, 285, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("N: Posicion Original", 1225, 255, 0, 30, 0, 122, 204, 255, 255, 255)

    texto("F1: Sonido ON", 1020, 375, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("F2: Sonido OFF", 1020, 345, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("ESC: Cerrar Programa", 1020, 315, 0, 30, 0, 122, 204, 255, 255, 255)


        
def desarrollador():
    texto("Raul Millan Desales", 100, 375, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("Jonathan Esquivel Flores", 100, 345, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("Jair Garduño Rodriguez", 100, 315, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("Ing Sistemas", 100, 285, 0, 30, 0, 122, 204, 255, 255, 255)
    texto("r) Ocultar", 100, 255, 0, 30, 0, 122, 204, 255, 255, 255)