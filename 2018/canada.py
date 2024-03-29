# coding: utf-8
# ESPAÑOL 
# El 29 de Agosto encontramos una imagen muy extraña y sospechamos que es algún tipo de código que todavía no pudimos romper.  Te crees capaz de enfrentarlo?
# Imagen
# https://www.dropbox.com/s/brn4zyx459tmpva/challenge.png?dl=0
# 

import cv2
import numpy as np
import random

img = cv2.imread("ImagenIndescifrable.png")

cuadros = [[img[i*50:i*50+50, j*50:j*50+50,:] for j in range(20)] for i in range(20)]

cuadros2 = [[cuadros[i][j][11:40,11:40,:] for j in range(20)] for i in range(20)]

##############
# A        B #
#            #
#            #
#            #
# C        D #
##############

A = (2, 2)
B = (2, 47)
C = (47, 2)
D = (47, 47)
NEGRO = (0,0,0)
BLANCO = (255,255,255)

def ordenar(cuadros, orden_mat):

    imag_out = np.zeros((1000,1000,3),dtype=np.uint8)

    for i in range(20):
        for j in range(20):
            ii, jj = orden_mat[i,j]
            imag_out[i*50:i*50+50,j*50:j*50+50,:] = cuadros[ii][jj]

    return imag_out


def ordenar2():

    imag_out = np.zeros((29*20,29*20,3),dtype=np.uint8)

    for i in range(20):
        for j in range(20):
            ii, jj = orden_mat[i,j]
            imag_out[i*29:i*29+29,j*29:j*29+29,:] = cuadros2[ii][jj]

    return imag_out



orden_mat = np.zeros((20,20,2), dtype = np.uint8)


def gen_posibles(n):

    i = n / 20
    j = n % 20

    aux = [(h,k) for h in range(20) for k in range(20)]

    for t in range(n):
        h = t / 20
        k = t % 20
        aux.remove(tuple(orden_mat[h,k]))

    if i==j==0:
        posibles_sig = []
        for p,q in aux:
            aux_cuad = cuadros[p][q]
            if np.all(NEGRO == aux_cuad[A]):
                if np.all(NEGRO == aux_cuad[B]):
                    if np.all(NEGRO == aux_cuad[C]):
                        posibles_sig.append((p,q))
                    elif np.all(BLANCO == aux_cuad[C]):
                        posibles_sig.append((p,q))
                elif np.all(BLANCO == aux_cuad[B]):
                    if np.all(NEGRO == aux_cuad[C]):
                        posibles_sig.append((p,q))
                    elif np.all(BLANCO == aux_cuad[C]):
                        posibles_sig.append((p,q))
            if np.all(BLANCO == aux_cuad[A]):
                if np.all(NEGRO == aux_cuad[B]):
                    if np.all(NEGRO == aux_cuad[C]):
                        posibles_sig.append((p,q))
                    elif np.all(BLANCO == aux_cuad[C]):
                        posibles_sig.append((p,q))
                elif np.all(BLANCO == aux_cuad[B]):
                    if np.all(NEGRO == aux_cuad[C]):
                        posibles_sig.append((p,q))
                    elif np.all(BLANCO == aux_cuad[C]):
                        posibles_sig.append((p,q))

        return posibles_sig

    elif i == 0 and 0 < j < 19:
        ii, jj = orden_mat[i,j-1]
        cuadro = cuadros[ii][jj]

        c1 = cuadro[D]

        posibles_sig = []

        for p,q in aux:
            aux_cuad = cuadros[p][q]
            if np.all(c1 == aux_cuad[C]):
                if np.all(NEGRO == aux_cuad[A]):
                    if np.all(NEGRO == aux_cuad[B]):
                        posibles_sig.append((p,q))
                    elif np.all(BLANCO == aux_cuad[B]):
                        posibles_sig.append((p,q))
                if np.all(BLANCO == aux_cuad[A]):
                    if np.all(NEGRO == aux_cuad[B]):
                        posibles_sig.append((p,q))
                    elif np.all(BLANCO == aux_cuad[B]):
                        posibles_sig.append((p,q))

        return posibles_sig

    elif i == 0 and j == 19:
        ii, jj = orden_mat[i,j-1]
        cuadro = cuadros[ii][jj]

        c1 = cuadro[D]

        posibles_sig = []

        for p,q in aux:
            aux_cuad = cuadros[p][q]
            if np.all(c1 == aux_cuad[C]):
                if np.all(NEGRO == aux_cuad[A]):
                    if np.all(NEGRO == aux_cuad[B]):
                        if np.all(NEGRO == aux_cuad[D]):
                            posibles_sig.append((p,q))
                        elif np.all(BLANCO == aux_cuad[D]):
                            posibles_sig.append((p,q))
                    elif np.all(BLANCO == aux_cuad[B]):
                        if np.all(NEGRO == aux_cuad[D]):
                            posibles_sig.append((p,q))
                        elif np.all(BLANCO == aux_cuad[D]):
                            posibles_sig.append((p,q))
                elif np.all(BLANCO == aux_cuad[A]):
                    if np.all(NEGRO == aux_cuad[B]):
                        if np.all(NEGRO == aux_cuad[D]):
                            posibles_sig.append((p,q))
                        elif np.all(BLANCO == aux_cuad[D]):
                            posibles_sig.append((p,q))
                    elif np.all(BLANCO == aux_cuad[B]):
                        if np.all(NEGRO == aux_cuad[D]):
                            posibles_sig.append((p,q))
                        elif np.all(BLANCO == aux_cuad[D]):
                            posibles_sig.append((p,q))

        return posibles_sig


    elif 0 < i and j == 0:
        ii, jj = orden_mat[i-1,j]
        cuadro = cuadros[ii][jj]

        c1 = cuadro[D]

        posibles_sig = []

        for p,q in aux:
            aux_cuad = cuadros[p][q]
            if np.all(c1 == aux_cuad[B]):
                if np.all(NEGRO == aux_cuad[A]):
                    if np.all(NEGRO == aux_cuad[C]):
                        posibles_sig.append((p,q))
                    elif np.all(BLANCO == aux_cuad[C]):
                        posibles_sig.append((p,q))
                elif np.all(BLANCO == aux_cuad[A]):
                    if np.all(NEGRO == aux_cuad[C]):
                        posibles_sig.append((p,q))
                    elif np.all(BLANCO == aux_cuad[C]):
                        posibles_sig.append((p,q))

        return posibles_sig

    elif 0 < i < 19 and j == 19:
        i1, j1 = orden_mat[i,j-1]

        cuad1 = cuadros[i1][j1]

        c1 = cuad1[B]
        c2 = cuad1[D]

        posibles_sig = []

        for p,q in aux:
            aux_cuad = cuadros[p][q]
            if np.all(c1 == aux_cuad[A]):
                if np.all(c2 == aux_cuad[C]):
                    if np.all(NEGRO == aux_cuad[B]):
                        if np.all(NEGRO == aux_cuad[D]):
                            posibles_sig.append((p,q))
                        elif np.all(BLANCO == aux_cuad[D]):
                            posibles_sig.append((p,q))
                    elif np.all(BLANCO == aux_cuad[B]):
                        if np.all(NEGRO == aux_cuad[D]):
                            posibles_sig.append((p,q))
                        elif np.all(BLANCO == aux_cuad[D]):
                            posibles_sig.append((p,q))

        return posibles_sig


    elif 0 < i < 19 and 0 < j < 19:

        i1, j1 = orden_mat[i,j-1]
        i2, j2 = orden_mat[i-1,j]

        cuad1 = cuadros[i1][j1]
        cuad2 = cuadros[i2][j2]

        c1 = cuad1[B]
        c2 = cuad1[D]
        c3 = cuad2[D]

        posibles_sig = []

        for p,q in aux:
            aux_cuad = cuadros[p][q]
            if np.all(c1 == aux_cuad[A]):
                if np.all(c2 == aux_cuad[C]):
                    if np.all(c3 == aux_cuad[B]):
                        posibles_sig.append((p,q))
        return posibles_sig

    else:

        i1, j1 = orden_mat[i-1,j]

        cuad1 = cuadros[i1][j1]

        c1 = cuad1[C]
        c2 = cuad1[D]

        posibles_sig = []

        for p,q in aux:
            aux_cuad = cuadros[p][q]
            if np.all(c1 == aux_cuad[A]):
                if np.all(c2 == aux_cuad[B]):
                    if np.all(NEGRO == aux_cuad[C]):
                        if np.all(NEGRO == aux_cuad[D]):
                            posibles_sig.append((p,q))
                        elif np.all(BLANCO == aux_cuad[D]):
                            posibles_sig.append((p,q))
                    elif np.all(BLANCO == aux_cuad[C]):
                        if np.all(NEGRO == aux_cuad[D]):
                            posibles_sig.append((p,q))
                        elif np.all(BLANCO == aux_cuad[D]):
                            posibles_sig.append((p,q))


        return posibles_sig


def buscar_orden(n=0, posibles=None):

    if n==0:
        posibles = gen_posibles(0)

    i = n / 20
    j = n % 20

    if n == 20*20-1:
        if posibles:
            orden_mat[i,j] = posibles[0]
            return orden_mat
        else:
            return None

    else:
        for x in posibles:
            orden_mat[i,j] = x
            show_imag()
            posibles_sig = gen_posibles(n+1)
            aux = buscar_orden(n+1, posibles_sig)
            if not (aux is None):
                return aux


def show_imag():

    cv2.imshow(" ",ordenar(cuadros, orden_mat))
    cv2.waitKey(1)

buscar_orden()

#img_out = ordenar2()
#cv2.imwrite("canada_out2.jpg", img_out)


# Resultado de la lectura del QR = #Developers!

