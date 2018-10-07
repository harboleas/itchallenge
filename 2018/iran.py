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


clave = {}

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

#for k in d:
#    i,j = d[k][0]
#    cv2.imwrite("poke/"+str(k)+".jpg", cuadros[i][j])

clave[31] = chr(127-6)
clave[36] = chr(127-7)
clave[29] = chr(127-8)
clave[46] = chr(127-9)
clave[12] = chr(127-10)
clave[13] = chr(127-11)
clave[32] = chr(127-12)
clave[25] = chr(127-13)
clave[53] = chr(127-14)
clave[24] = chr(127-15)
clave[7] = chr(127-16)
clave[5] = chr(127-17)
clave[19] = chr(127-18)
clave[34] = chr(127-19)
clave[33] = chr(127-20)
clave[52] = chr(127-21)
clave[9] = chr(127-22)
clave[30] = chr(127-23)
clave[10] = chr(127-24)
clave[14] = chr(127-25)
clave[4] = chr(127-26)
clave[8] = chr(127-27)
clave[6] = chr(127-28)
clave[26] = chr(127-29)
clave[18] = chr(127-30)
clave[17] = chr(127-32)
clave[28] = chr(127-54)
clave[23] = chr(127-60)
clave[20] = chr(127-66)
clave[11] = chr(127-69)
clave[44] = chr(127-70)
clave[43] = chr(127-72)
clave[42] = chr(127-73)
clave[41] = chr(127-74)
clave[40] = chr(127-75)
clave[39] = chr(127-76)
clave[38] = chr(127-77)
clave[37] = chr(127-78)
clave[45] = chr(127-79)
clave[54] = chr(127-80)
clave[27] = chr(127-81)
clave[2] = chr(127-82)
clave[47] = chr(127-83)
clave[51] = chr(127-84)
clave[3] = chr(127-85)
clave[50] = chr(127-86)
clave[49] = chr(127-87)
clave[48] = chr(127-88)
clave[0] = chr(127-92)
clave[21] = chr(127-93)
clave[35] = chr(127-94)
clave[1] = chr(127-95)
clave[39] = chr(127-76)
clave[15] = chr(127-71)
clave[16] = chr(127-117)
clave[22] = chr(127-118)
clave[55] = ""

codigo = deco()

print codigo

max_limit = 12345678987654320
j = max_limit - 1
k = (max_limit/5) - 1
l = (max_limit/20) - 1

linear_sum = j*(j+1)/2
squared_sum = k*(k+1)*(2*k+1)/6
cubic_sum = ((l*(l+1))**2)/4

print linear_sum+squared_sum+cubic_sum



