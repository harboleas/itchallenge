
# coding: utf-8

# El superagente 86 ha caído prisionero de Kaos, junto con la 99, el 13 y 44.
# 
# Siegfried le propone al agente 86 liberarlos, si el confiesa la contraseña de acceso al cuartel general de Control. De lo contrario Él y sus compañeros serán condenados al laberinto de kaos.
# 
# Ya era conocido en control la existencia del laberinto, dado que Kaos siempre se ha jactado de la imposibilidad de escapar del mismo.
# 
# El laberinto consiste en una grilla de 86x86 celdas, donde los prisioneros son dispuestos en las celdas centrales, sin posibilidad de comunicación.
# 
# Las celdas del laberinto están conectadas por puertas que se abren únicamente cuando es posible encontrar la clave apropiada, lo cual no representa problema alguno para el perspicaz agente 86.
# 
# El laberinto de 86x86 celdas está subdividido en 4 cuadrantes, cada uno de 43x43 celdas. Las puertas están dispuestas de tal forma que en el cuadrante 1, solo abren hacia la derecha y arriba. En el cuadrante 2 abren hacia la izquierda y arriba. En el cuadrante 3 abren hacia la izquierda y abajo En el cuadrante 4 abren hacia la derecha y abajo
# 
# Las esquinas del laberinto tienen las celdas de escape y de ser alcanzadas los prisioneros podrán salir del mismo sin ser atrapados por los guardias.
# 
# Los 4 prisioneros son dispuestos en las 4 celdas centrales del laberinto, uno por cada cuadrante. En cada celda los prisioneros encuentran un número entero, los números correspondientes a las 4 celdas donde se encuentran los prisioneros deben ser sumados y si la suma de esos numeros puede ser factorizada en 2 y solo 2 números primos, las puertas de las celdas contiguas se abrirán y los 4 prisioneros podrán avanzar. Cada prisionero puede elegir cualquiera de las puertas que tenga disponibles para avanzar 1 lugar según las direcciones indicadas anteriormente. En el caso que la suma no se pueda factorizar en 2 primos, los prisioneros deben volver a las celdas centrales para volver a comenzar.
# 
# Además se sabe que si la suma de los números de las 4 celdas es un número negativo, las puertas no se abrirán.
# 
# El agente 86 supone que escapar será tarea fácil, sin embargo la agente 99 supone que puede ser una tarea realmente compleja, dado que la cantidad de combinaciones de caminos es enorme y solo una porción pequeña de esos caminos conducen a la salida.
# 
# Si las celdas son numeradas desde la (1,1) hasta la (86,86). Las salidas se encuentran en las esquinas: (1,1) , (86,1) , (1,86) , (86,86). y las posiciones iniciales de los prisioneros serán: (43,43) , (44,43) , (43,44) , (44,44)
# 
# Se provee laberinto_86.txt donde se encuentran los números anotados en cada una de las celdas.
# 
# Por ejemplo, partiendo en la posición inicial, se tiene:
# 
# a=GRILLA[43 , 43] = 90761839835669
# b=GRILLA[44 , 43] = -103200623916882
# c=GRILLA[43 , 44] = -102314419681966
# d=GRILLA[44 , 44] = 114753209335242
# s= a+b+c+d = 5572063
# 
# Y dado que s se puede factorizar en 2 y solo 2 primos. s = 7 * 796009
# 
# Entonces las puertas que comunican con las celdas contiguas se abrirán. Por ejemplo, en la celda (43,43), se abrirán las puertas que comunican con las celdas (42,43) y (43,42) y el prisionero podrá seleccionar moverse a una de esas 2 celdas. Por otro lado, en la celda (44,44), se abrirán las puertas que comunican con las celdas (44,45) y (45,44) y el prisionero de esa celda podrá seleccionar cualquiera de ellas para avanzar.
# 
# Se pide calcular la cantidad de caminos distintos que conducen a la salida.
# 
# Ayuda
# 
# Como ayuda se dispone de una versión simplificada del laberinto. En este caso es un laberinto de 4x4
# 
# Donde los números de las celdas son:
# 
# 116743624370539 -45533720173642 -58523041793097 -134874053442696
# -45533722181306 180446252003315 -9617966039430 -58523056026913
# 42562267331952 47014806996435 -217843078095259 61494487189802
# 24675672517840 42562278169440 61494498780921 -6545230114605
# En esta versión simplificada las reglas son las mismas, se parte del centro y cada cuadrante tiene un sentido de movimiento particular.
# 
# Se sabe que en esta versión simplificada la cantidad de caminos posibles para salir son 5
# 
# Este laberinto se puede representar también como
# 
# AB|CD  
# EF|GH
# --+--
# IJ|KL  
# MN|OP
# 
# Los prisioneros inician en las celdas F,G,J,K y como los números de estas celdas se pueden factorizar como 2 números primos, se abrirán las puertas.
# 
# F será comunicada con B y E
# J será comunicada con I y N
# G será comunicada con C y H
# K será comunicada con L y O
# Luego los prisioneros avanzarán cada uno siguiendo algún camino, por ejemplo, pasarán a las celdas B,H,N,O respectivamente. Y como nuevamente la suma de los números e esas celdas puede ser factorizado en 2 primos, 749806 = 2 x 374903, se abrirán las puertas que comunican en las direcciones permitidas.
# 
# B será comunicada con A y solo con A, ya que arriba de B no hay ninguna celda.
# H será comunicada con D
# N será comunicada con M
# O será comunicada con P
# Ahora los prisioneros avanzan en alguna de las direcciones disponibles, en este caso solo pueden avanzar hacia A,D,M,P. Y como la suma de los números de esas celdas puede ser factorizado en 2 primos, 13331078 = 2 x 6665539, los prisioneros han encontrado un camino para escapar.
# 
# En este ejemplo simplificado los 5 caminos posibles son:
# 
# F,G,J,K -> B,C,N,O -> A,D,M,P
# F,G,J,K -> B,C,N,L -> A,D,M,P
# F,G,J,K -> B,C,I,O -> A,D,M,P
# F,G,J,K -> B,H,N,O -> A,D,M,P
# F,G,J,K -> E,C,N,O -> A,D,M,P
# 
# El laberinto de 86x86 a ser resuelto lo podes encontrar en https://s3.amazonaws.com/it.challenge/level6.txt

from primos import *

n = 86
total = n*n

# fila, col

orig0 = (n/2 - 1, n/2)
orig1 = (n/2 - 1, n/2 - 1)
orig2 = (n/2, n/2 - 1)
orig3 = (n/2, n/2)

origs = [orig0, orig1, orig2, orig3]

def get_cuad(i, j):

    if i < n/2:
        if j >= n/2:
            return 0
        else:
            return 1
    else:
        if j >= n/2:
            return 3
        else:
            return 2

def get_dist(i, j):
    # distancia al origen

    cuad = get_cuad(i, j)

    oy, ox = origs[cuad]

    return abs(i-oy) + abs(j-ox)


coord_cuad = [[], [], [], []]

for i in xrange(n):
    for j in xrange(n):
        coord_cuad[get_cuad(i,j)].append((i,j))

dist_max = get_dist(0, 0)
dist_c0 = [[] for i in xrange(dist_max+1)]
dist_c1 = [[] for i in xrange(dist_max+1)]
dist_c2 = [[] for i in xrange(dist_max+1)]
dist_c3 = [[] for i in xrange(dist_max+1)]

dist_cuads = [dist_c0, dist_c1, dist_c2, dist_c3]

for i in xrange(n):
    for j in xrange(n):
        dist_cuads[get_cuad(i, j)][get_dist(i, j)].append((i, j))


selec_coord_1 = []
def gen_selec():

    for d in xrange(dist_max+1):
        for c0 in dist_c0[d]:
            for c1 in dist_c1[d]:
                for c2 in dist_c2[d]:
                    for c3 in dist_c3[d]:
                        selec_coord_1.append((c0,c1,c2,c3))

with open("laberinto.txt") as f:
    txt = f.readlines()

lab = [[int(i) for i in fila.split()] for fila in txt]

selec_coord_2 = []

def filtro_1():

    for x,y,z,w in selec_coord_1:
        X = lab[x[0]][x[1]]
        Y = lab[y[0]][y[1]]
        Z = lab[z[0]][z[1]]
        W = lab[w[0]][w[1]]
        if X+Y+Z+W > 0:
            selec_coord_2.append((x,y,z,w)

selec_coord_3 = []

def filtro_2():

    for x,y,z,w in selec_coord_2:
        X = lab[x[0]][x[1]]
        Y = lab[y[0]][y[1]]
        Z = lab[z[0]][z[1]]
        W = lab[w[0]][w[1]]
        if es_prod_primos(X+Y+Z+W):
            selec_coord_3.append((x,y,z,w)


#  vim: set ts=4 sw=4 tw=79 et :
