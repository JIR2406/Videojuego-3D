import pygame as py
from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from ironman import *
import a_escenario as es
import a_iluminacion as li
from panda import *
from jake import * 

p = Panda()

# ----------------------------IronMan-----------------------------
def orig():
    casco()
    tronco1()
    brazoDer1()
    brazoIzq1()
    manoDer1()
    manoIzq1()
    piernaDer1()
    piernaIzq1()
    pieDer1()
    pieIzq1()

def g1():
    cabeza1()
    ros()
    eyes()
    boca1()
    tronco1()
    brazoDer1()
    brazoIzq1()
    manoDer1()
    manoIzq1()
    piernaDer1()
    piernaIzq1()
    pieDer1()
    pieIzq1()

def g2():
    cabeza1()
    ros()
    ojos22()
    boca2()
    tronco1()
    brazoDer1()
    brazoIzq1()
    manoDer1()
    manoIzq1()
    piernaDer1()
    piernaIzq1()
    pieDer1()
    pieIzq1()

def g3():
    cabeza1()
    ros()
    ojos3()
    boca3()
    tronco1()
    brazoDer1()
    brazoIzq1()
    manoDer1()
    manoIzq1()
    piernaDer1()
    piernaIzq1()
    pieDer1()
    pieIzq1()

def g4():
    cabeza1()
    ros()
    ojos11()
    boca1()
    tronco1()
    brazoDer1()
    brazoIzq1()
    manoDer1()
    manoIzq1()
    piernaDer1()
    piernaIzq1()
    pieDer1()
    pieIzq1()

def g5():
        cabeza1()
        ros()
        ojos22()
        boca3()
        tronco1()
        brazoDer1()
        brazoIzq1()
        manoDer1()
        manoIzq1()
        piernaDer1()
        piernaIzq1()
        pieDer1()
        pieIzq1()

def g6():
        casco()
        tronco1()
        brazoDer1()
        brazoIzqUp()
        manoDer1()
        piernaDer1()
        piernaIzq1()
        pieDer1()
        pieIzq1()

def g7():
        casco()
        tronco1()
        brazoDerUp()
        brazoIzq1()
        manoIzq1()
        piernaDer1()
        piernaIzq1()
        pieDer1()
        pieIzq1()

def g8():
        cabezaUp()
        tronco1()
        brazoDer1()
        brazoIzq1()
        manoDer1()
        manoIzq1()
        piernaDer1()
        piernaIzq1()
        pieDer1()
        pieIzq1()

def g9():
        voltear()
        tronco1()
        brazoDer1()
        brazoIzq1()
        manoDer1()
        manoIzq1()
        piernaDer1()
        piernaIzq1()
        pieDer1()
        pieIzq1()

def g10():
        casco()
        tronco1()
        brazoDer1()
        brazoIzq1()
        manoDer1()
        manoIzq1()
        caminar()

def g11():
        cabeza1()
        ros()
        ojos3()
        boca3()
        tronco1()
        brazoDerUp()
        brazoIzq1()
        manoIzq1()
        piernaDer1()
        piernaIzq1()
        pieDer1()
        pieIzq1()

def g12():
        cabezaUp()
        tronco1()
        brazoDerUp()
        brazoIzqUp()
        caminar()

def panda():
      p.draw_body()
      p.draw_face()
      p.draw_ears()
      p.draw_eye1((0,0,0),(1,1,1))
      p.draw_eye2((0,0,0),(1,1,1))
      p.draw_leg_inf_right()
      p.draw_leg_sup_right()
      p.draw_leg_inf_left()
      p.draw_leg_sup_left()
      p.draw_muzzle()
      
# ----------------------------Jake-----------------------------
def Jake():
        somCp()
        somBas()
        cuerpo()
        orejaDe()
        orejaIz()
        brazoDe()
        brazoIz()
        parpadoDe()
        parpadosIz()
        ojoDe()
        ojoIz()
        nariz()
        narizA()
        narizB()
        narizC()
        pantalones()
        piernaDe()
        piernaIz()
        pieDe()
        pieIz()

def jakeCerrarOjos():
        somCp()
        somBas()
        cuerpo()
        orejaDe()
        orejaIz()
        brazoDe()
        brazoIz()
        parDeCe()
        parIzCe()
        nariz()
        narizA()
        narizB()
        narizC()
        pantalones()
        piernaDe()
        piernaIz()
        pieDe()
        pieIz()

def jakeEnojado():
        somCp()
        somBas()
        cuerpo()
        orejaDe()
        orejaIz()
        brazoDe()
        brazoIz()
        cejaDe()
        cejaIz()
        parpadoDe()
        parpadosIz()
        ojoDe()
        ojoIz()
        nariz()
        narizA()
        narizB()
        narizC()
        pantalones()
        piernaDe()
        piernaIz()
        pieDe()
        pieIz()

def jakeLengua():
        somCp()
        somBas()
        cuerpo()
        orejaDe()
        orejaIz()
        brazoDe()
        brazoIz()
        parpadoDe()
        parpadosIz()
        ojoDe()
        ojoIz()
        nariz()
        narizA()
        narizB()
        narizC()
        lengua()
        pantalones()
        piernaDe()
        piernaIz()
        pieDe()
        pieIz()

def jakeGuiño():
        somCp()
        somBas()
        cuerpo()
        orejaDe()
        orejaIz()
        brazoDe()
        brazoIz()
        parpadoDe()
        ojoDe()
        guino()
        nariz()
        narizA()
        narizB()
        narizC()
        pantalones()
        piernaDe()
        piernaIz()
        pieDe()
        pieIz()

def jakeSonrisa():
        somCp()
        somBas()
        cuerpo()
        orejaDe()
        orejaIz()
        brazoDe()
        brazoIz()
        parpadoDe()
        parpadosIz()
        ojoDe()
        ojoIz()
        nariz()
        narizA()
        narizB()
        narizC()
        boca()
        dientes()
        pantalones()
        piernaDe()
        piernaIz()
        pieDe()
        pieIz()

def jakebdUp():
        somCp()
        somBas()
        cuerpo()
        orejaDe()
        orejaIz()
        saludo()
        brazoIz()
        parpadoDe()
        parpadosIz()
        ojoDe()
        ojoIz()
        nariz()
        narizA()
        narizB()
        narizC()
        pantalones()
        piernaDe()
        piernaIz()
        pieDe()
        pieIz()

def jakebUp():
        somCp()
        somBas()
        cuerpo()
        orejaDe()
        orejaIz()
        brazoDe2()
        brazoIz2()
        parpadoDe()
        parpadosIz()
        ojoDe()
        ojoIz()
        nariz()
        narizA()
        narizB()
        narizC()
        pantalones()
        piernaDe()
        piernaIz()
        pieDe()
        pieIz()

def jakemp():
        somCp()
        somBas()
        cuerpo()
        orejaDe()
        orejaIz()
        brazoDe()
        brazoIz()
        parpadoDe()
        parpadosIz()
        ojoDe()
        ojoIz()
        nariz()
        narizA()
        narizB()
        narizC()
        pantalones()
        piernaDe2()
        piernaIz2()
        pieDe2()
        pieIz2()   

def jake4():
        somCp()
        somBas()
        cuerpo()
        orejaDe()
        orejaIz()
        brazoDe()
        brazoIz()
        parpadoDe()
        parpadosIz()
        ojoDe()
        ojoIz()
        nariz()
        narizA()
        narizB()
        narizC()
        pantalones()
        piernaDe3A()
        piernaDe3B()
        piernaIz3A()
        piernaIz3B()
        pieDe3()
        pieIz3()

def jake5():
        somCp2()
        somBas2()
        cuerpo()
        orejaDe()
        orejaIz()
        saludo()
        brazoIz()
        parpadoDe()
        parpadosIz()
        ojoDe()
        ojoIz()
        nariz()
        narizA()
        narizB()
        narizC()
        pantalones()
        piernaDe()
        piernaIz()
        pieDe()
        pieIz()

# ----------------------------Panda-----------------------------

def panda1(): #Cerrar Ojo izq
      p.draw_body()
      p.draw_face()
      p.draw_ears()
      p.draw_eye1((0, 0.2, 0.6),(0, 0.2, 0.6))
      p.draw_eye2((0,0,0),(1,1,1))
      p.draw_leg_inf_right()
      p.draw_leg_sup_right()
      p.draw_leg_inf_left()
      p.draw_leg_sup_left()
      p.draw_muzzle()
      
def panda2(): #Cerrar Ojo der
      p.draw_body()
      p.draw_face()
      p.draw_ears()
      p.draw_eye1((0,0,0),(1,1,1))
      p.draw_eye2((0, 0.2, 0.6),(0, 0.2, 0.6))
      p.draw_leg_inf_right()
      p.draw_leg_sup_right()
      p.draw_leg_inf_left()
      p.draw_leg_sup_left()
      p.draw_muzzle()
      
def panda3(): #Tristeza
      p.draw_body()
      p.draw_face()
      p.draw_ears()
      p.draw_eye1((0,0,0),(1,1,1))
      p.draw_eye2((0,0,0),(1,1,1))
      p.draw_leg_inf_right()
      p.draw_leg_sup_right()
      p.draw_leg_inf_left()
      p.draw_leg_sup_left()
      p.draw_muzzle()
      p.draw_mouth()

def panda4(): #Sonrisa
      p.draw_body()
      p.draw_face()
      p.draw_ears()
      p.draw_eye1((0,0,0),(1,1,1))
      p.draw_eye2((0,0,0),(1,1,1))
      p.draw_leg_inf_right()
      p.draw_leg_sup_right()
      p.draw_leg_inf_left()
      p.draw_leg_sup_left()
      p.draw_muzzle()
      p.draw_mouth_happy()

def panda5(): #Lengua
      p.draw_body()
      p.draw_face()
      p.draw_ears()
      p.draw_eye1((0,0,0),(1,1,1))
      p.draw_eye2((0,0,0),(1,1,1))
      p.draw_leg_inf_right()
      p.draw_leg_sup_right()
      p.draw_leg_inf_left()
      p.draw_leg_sup_left()
      p.draw_muzzle()
      p.draw_mouth_leng()

def panda6(): #Pierna D Derecha Up
      p.draw_body()
      p.draw_face()
      p.draw_ears()
      p.draw_eye1((0,0,0),(1,1,1))
      p.draw_eye2((0,0,0),(1,1,1))
      p.draw_leg_inf_right()
      p.draw_leg_inf_left()
      p.draw_leg_sup_left()
      p.draw_muzzle()
      glRotatef(20, 1, 0, 0)  # Rotar 90 grados alrededor del eje X
      glTranslatef(0,0,1)
      p.draw_leg_sup_right()

def panda7(): #Pierna D Izquierda Up
      p.draw_body()
      p.draw_face()
      p.draw_ears()
      p.draw_eye1((0,0,0),(1,1,1))
      p.draw_eye2((0,0,0),(1,1,1))
      p.draw_leg_inf_right()
      p.draw_leg_inf_left()
      p.draw_leg_sup_right()
      p.draw_muzzle()
      glRotatef(20, 1, 0, 0)  # Rotar 90 grados alrededor del eje X
      glTranslatef(0,0,1)
      p.draw_leg_sup_left()

def panda8(): #Pierna T Izquierda Up
      p.draw_body()
      p.draw_face()
      p.draw_ears()
      p.draw_eye1((0,0,0),(1,1,1))
      p.draw_eye2((0,0,0),(1,1,1))
      p.draw_leg_inf_left()
      p.draw_leg_sup_right()
      p.draw_leg_sup_left()
      p.draw_muzzle()
      glRotatef(20, 1, 0, 0)  # Rotar 90 grados alrededor del eje X
      glTranslatef(0,0,2)
      p.draw_leg_inf_right()
      

def panda9(): #Pierna T Derecha Up
      p.draw_body()
      p.draw_face()
      p.draw_ears()
      p.draw_eye1((0,0,0),(1,1,1))
      p.draw_eye2((0,0,0),(1,1,1))
      p.draw_leg_inf_right()
      p.draw_leg_sup_right()
      p.draw_leg_sup_left()
      p.draw_muzzle()
      glRotatef(20, 1, 0, 0)  # Rotar 90 grados alrededor del eje X
      glTranslatef(0,0,2)
      p.draw_leg_inf_left()

def panda10(): #Mov 2 p s
      p.draw_body()
      p.draw_face()
      p.draw_ears()
      p.draw_eye1((0,0,0),(1,1,1))
      p.draw_eye2((0,0,0),(1,1,1))
      p.draw_leg_inf_right()
      p.draw_leg_inf_left()
      p.draw_muzzle()
      glRotatef(20, 1, 0, 0)  # Rotar 90 grados alrededor del eje X
      glTranslatef(0,0,1)
      p.draw_leg_sup_right()
      glRotatef(20, 1, 0, 0)  # Rotar 90 grados alrededor del eje X
      glTranslatef(0,0,1)
      p.draw_leg_sup_left()
      
      
      
      
      