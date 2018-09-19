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

##############
# A   B    C #
#            #
# D        E #
#            #
# F   G    H #
##############

A = (2, 2)
B = (2, 25)
C = (2, 47)
D = (25, 2)
E = (25, 47)
F = (47, 2)
G = (47, 25)
H = (47, 47)



def ordenar(cuadros, orden_mat):

    imag_out = np.zeros((1000,1000,3),dtype=np.uint8)

    for i in range(20):
        for j in range(20):
            ii, jj = orden_mat[i,j]
            imag_out[i*50:i*50+50,j*50:j*50+50,:] = cuadros[ii][jj]

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

    if i == 0 and 0 < j:
        ii, jj = orden_mat[i,j-1]
        cuadro = cuadros[ii][jj]

        c1 = cuadro[2:47, 47]

        posibles_sig = []

        for p,q in aux:
            aux_cuad = cuadros[p][q]
            if np.all(c1 == aux_cuad[2:47, 2]):
                posibles_sig.append((p,q))
        return posibles_sig

    elif i > 0 and j == 0:
        ii, jj = orden_mat[i-1,j]
        cuadro = cuadros[ii][jj]

        c1 = cuadro[47, 2:47]

        posibles_sig = []

        for p,q in aux:
            aux_cuad = cuadros[p][q]
            if np.all(c1 == aux_cuad[2, 2:47]):
                posibles_sig.append((p,q))
        return posibles_sig

    else:
        i1, j1 = orden_mat[i, j-1]
        i2, j2 = orden_mat[i-1, j]

        cuad1 = cuadros[i1][j1]
        cuad2 = cuadros[i2][j2]

        c1 = cuad1[2:47, 47]
        c2 = cuad2[47, 2:47]

        posibles_sig = []

        for p,q in aux:
            aux_cuad = cuadros[p][q]
            if np.all(c1 == aux_cuad[2:47, 2]):
                if np.all(c2 == aux_cuad[2, 2:47]):
                    posibles_sig.append((p,q))
        return posibles_sig


def buscar_orden(n=0, posibles=None):

#    if n==0:
#        posibles = [(h,k) for h in range(20) for k in range(20)]

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
            print n, posibles_sig
            aux = buscar_orden(n+1, posibles_sig)
            print n
            if not (aux is None):
                return aux

def show_imag():

    cv2.imshow(" ",ordenar(cuadros, orden_mat))
    cv2.waitKey(1)



