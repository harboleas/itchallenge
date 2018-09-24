# coding: utf-8
# ESPAÑOL
# En una cueva oscura de la ciudad de Pueblo Paleta fue hallada una escritura muy antigua. Ningún profesor logró descifrar lo que significa, pero se rumorea que contiene la clave para atrapar a todos los pokemones legendarios. ¿Podés ayudarlos a descubrir lo que significa el mensaje?
# 
# https://www.dropbox.com/s/78cfb7z4kmpj8or/test.jpg?dl=0

import cv2
import numpy as np

img = cv2.imread("test.jpg")

filas, cols = img.shape[:-1]

cant = 24

delta = filas / cant

cuadros = [[img[i*delta:i*delta+delta, j*delta:j*delta+delta,:] for j in range(cant)] for i in range(cant)]

coords = [(i,j) for i in range(24) for j in range(24)]

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
        if np.count_nonzero(cuadro_aux != cuadros[r][s]) < 1000:
            d[i].append(x)
            coords.remove(x)
    i += 1


def busca_coord(coord):

    for k in d.keys():
        if coord in d[k]:
            return k


clave = {1:"e", 9:"a", 5:"o", 19:"s", 16:"r", 25:"n", 4:"i"}


def deco():

    aux = []

    coords = [(i,j) for i in range(24) for j in range(24)]

    for x in coords:
        k = busca_coord(x)
        if clave.has_key(k):
            aux.append(clave[k])
        else:
            aux.append("-")

    return "".join(aux)


orden = range(56)

for i in range(56):
    for j in range(56-i-1):
        if len(d[orden[j]]) < len(d[orden[j+1]]):
            orden[j+1], orden[j] = orden[j], orden[j+1]



