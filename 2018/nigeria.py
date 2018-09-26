# coding: utf-8
# Español:
# Encontramos este mensaje en Chino, pero sospechamos un poco de su veracidad, nos ayudarías a entender qué dice?
# https://www.dropbox.com/s/p466zpiqxqqfc0o/Texto%20Chino.png?dl=0

import cv2
import numpy as np

img = cv2.imread("Texto Chino.png")

filas, cols = img.shape[:-1]

cant_col = 59
cant_fil = 6

d_col = 17
d_fil = 17

cuadros = [[img[3+i*27:3+i*27+d_fil, 3+j*d_col:3+j*d_col+d_col,:] for j in range(cant_col)] for i in range(cant_fil)]

coords = [(i,j) for i in range(cant_fil) for j in range(cant_col)]

d = {}
i = 0

while coords:

    aux = coords[0]
    d[i] = [aux]
    coords.remove(aux)
    p, q = aux
    cuadro_aux = cuadros[p][q]

    coords_aux = coords[:]
    for x in coords_aux:
        r, s = x
        if np.count_nonzero(cuadro_aux != cuadros[r][s]) < 20:
            d[i].append(x)
            coords.remove(x)
    i += 1


def busca_coord(coord):

    for k in d.keys():
        if coord in d[k]:
            return k


clave = {24: " ", 4:"e", 5:"a", 16:"o", 12:"s"}


def deco():

    aux = []

    coords = [(i,j) for i in range(cant_fil) for j in range(cant_col)]

    for x in coords:
        k = busca_coord(x)
        if clave.has_key(k):
            aux.append(clave[k])
        else:
            aux.append("-")

    return "".join(aux)

n = len(d.keys())
orden = range(n)

for i in range(n):
    for j in range(n-i-1):
        if len(d[orden[j]]) < len(d[orden[j+1]]):
            orden[j+1], orden[j] = orden[j], orden[j+1]



