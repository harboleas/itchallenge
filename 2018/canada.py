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
        return posibles_sig

    elif i == 0 and 0 < j:
        ii, jj = orden_mat[i,j-1]
        cuadro = cuadros[ii][jj]

        c1 = cuadro[B]
        c2 = cuadro[D]

        posibles_sig = []

        for p,q in aux:
            aux_cuad = cuadros[p][q]
            if np.all(c1 == aux_cuad[A]):
                if np.all(c2 == aux_cuad[C]):
                    if np.all(NEGRO == aux_cuad[B]):
                        posibles_sig.append((p,q))
                    elif np.all(BLANCO == aux_cuad[B]):
                        posibles_sig.append((p,q))

        return posibles_sig

    elif i > 0 and j == 0:
        ii, jj = orden_mat[i-1,j]
        cuadro = cuadros[ii][jj]

        c1 = cuadro[C]
        c2 = cuadro[D]

        posibles_sig = []

        for p,q in aux:
            aux_cuad = cuadros[p][q]
            if np.all(c1 == aux_cuad[A]):
                if np.all(c2 == aux_cuad[B]):
                    if np.all(NEGRO == aux_cuad[C]):
                        posibles_sig.append((p,q))
                    elif np.all(BLANCO == aux_cuad[C]):
                        posibles_sig.append((p,q))

        return posibles_sig

    else:

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
            raw_input()
            posibles_sig = gen_posibles(n+1)
#            print n, posibles_sig
            aux = buscar_orden(n+1, posibles_sig)
            if not (aux is None):
                return aux


def show_imag():

    cv2.imshow(" ",ordenar(cuadros, orden_mat))
    cv2.waitKey(1)


#def posibles_der(pos):
#
#    i,j = pos
#    cuad = cuadros[i][j]
#    c1 = cuad[B]
#    c2 = cuad[D]
#    posibles = []
#    aux = [(h,k) for h in range(20) for k in range(20)]
#    aux.remove(pos)
#    for q,p in aux:
#        cuad_aux = cuadros[q][p]
#        if np.all(c1 == cuad_aux[A]):
#            if np.all(c2 == cuad_aux[C]):
#                posibles.append((q,p))
#
#    return posibles
#
#def posibles_izq(pos):
#
#    i,j = pos
#    cuad = cuadros[i][j]
#    c1 = cuad[A]
#    c2 = cuad[C]
#    posibles = []
#    aux = [(h,k) for h in range(20) for k in range(20)]
#    aux.remove(pos)
#    for q,p in aux:
#        cuad_aux = cuadros[q][p]
#        if np.all(c1 == cuad_aux[B]):
#            if np.all(c2 == cuad_aux[D]):
#                posibles.append((q,p))
#
#    return posibles
#
#
#def posibles_arr(pos):
#
#    i,j = pos
#    cuad = cuadros[i][j]
#    c1 = cuad[A]
#    c2 = cuad[B]
#    posibles = []
#    aux = [(h,k) for h in range(20) for k in range(20)]
#    aux.remove(pos)
#    for q,p in aux:
#        cuad_aux = cuadros[q][p]
#        if np.all(c1 == cuad_aux[C]):
#            if np.all(c2 == cuad_aux[D]):
#                posibles.append((q,p))
#
#    return posibles
#
#def posibles_aba(pos):
#
#    i,j = pos
#    cuad = cuadros[i][j]
#    c1 = cuad[C]
#    c2 = cuad[D]
#    posibles = []
#    aux = [(h,k) for h in range(20) for k in range(20)]
#    aux.remove(pos)
#    for q,p in aux:
#        cuad_aux = cuadros[q][p]
#        if np.all(c1 == cuad_aux[A]):
#            if np.all(c2 == cuad_aux[B]):
#                posibles.append((q,p))
#
#    return posibles
#
#def posibles(pos):
#
#    return {"pos": [pos], "izq": posibles_izq(pos), "der": posibles_der(pos),
#            "arr": posibles_arr(pos), "aba": posibles_aba(pos)}
#
#
#def filtro(pos_rel, cant):
#
#    aux = []
#
#    for i in range(20):
#        for j in range(20):
#            pos = posibles((i,j))
#            if len(pos[pos_rel]) == cant:
#                aux.append(pos["pos"][0])
#
#    return aux
#
#izq = filtro("izq", 0)
#der = filtro("der", 0)
#arr = filtro("arr", 0)
#aba = filtro("aba", 0)
#
#def gen_remap(pos, i=0, j=0, remap=None):
#
#
#    if i==j==0:
#        remap = {(0,0): pos}
#
#    pos_izq = posibles_izq(pos)
#    pos_der = posibles_der(pos)
#    pos_aba = posibles_aba(pos)
#    pos_arr = posibles_arr(pos)
#
#
#    if not remap.has_key((i,j-1)):
#        if len(pos_izq) == 1:
#            val = pos_izq[0]
#            if val not in remap.values():
#                remap[(i,j-1)] = val
#                gen_remap(val, i, j-1, remap)
#
#    if not remap.has_key((i,j+1)):
#        if len(pos_der) == 1:
#            val = pos_der[0]
#            if val not in remap.values():
#                remap[(i,j+1)] = val
#                gen_remap(val, i, j+1, remap)
#
#    if not remap.has_key((i-1,j)):
#        if len(pos_arr) == 1:
#            val = pos_arr[0]
#            if val not in remap.values():
#                remap[(i-1,j)] = val
#                gen_remap(val, i-1, j, remap)
#
#    if not remap.has_key((i+1,j)):
#        if len(pos_aba) == 1:
#            val = pos_aba[0]
#            if val not in remap.values():
#                remap[(i+1,j)] = val
#                gen_remap(val, i+1, j, remap)
#
#    return remap
#
#
#def calc_size(remap):
#
#    filas = [k[0] for k in remap.keys()]
#    cols = [k[1] for k in remap.keys()]
#
#    si = max(filas) - min(filas) + 1
#    sj = max(cols) - min(cols) + 1
#
#    min_i = min(filas)
#    min_j = min(cols)
#
#    return si, sj, min_i, min_j
#
#
#def show_imag(pos):
#
#    remap = gen_remap(pos)
#
#    si,sj,mi,mj = calc_size(remap)
#
#    mmj = min([k[1] for k in remap.keys() if k[0]==mi])
#
#    print remap[mi,mmj]
#
#    img = np.zeros((si*50, sj*50, 3), dtype=np.uint8)
#
#    for k,v in remap.items():
#        i = k[0] - mi
#        j = k[1] - mj
#        p, q = v
#
#        img[i*50:i*50+50,j*50:j*50+50,:] = cuadros[p][q]
#
#    cv2.imshow(" ", img)
#    cv2.waitKey(0)


