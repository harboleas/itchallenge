from mali import num_base
from primos import es_capicua
from math import factorial

a = factorial(60)/(factorial(20)*factorial(40))
b = factorial(40)/(factorial(20)*factorial(20))

total_caminos = a*b

direc = [(1,0,0), (0,1,0), (0,0,1)]

with open("cubo.txt") as f :
    txt = f.read()

mat = txt.split("\n\n")

cubo = [[fila for fila in altura.split()] for altura in mat]

def num_a_camino(num, size) :

    return num_base(num, direc, size)

def camino_valido(camino) :

    x = 0
    y = 0
    z = 0
    for dx,dy,dz in camino :
        x += dx
        y += dx
        z += dx
        if x > 20 or y > 20 or z > 20 :
            return False

    return True


def get_palabra(camino) :

    x, y, z = (0,0,0)
    palabra = cubo[x][y][z]
    for dx,dy,dz in camino :
        x += dx
        y += dy
        z += dz
        palabra += cubo[x][y][z]

    return palabra


def gen_num_val() :

    num_val = []

    size = 31
    i = 0

    while i < 3**size :
        cam = num_a_camino(i, size)
        if camino_valido(cam) :
            pal = get_palabra(cam)
            if pal[29] == pal[31] :
                num_val.append(i)
        i += 1

    return num_val


#def contar_caminos() :
#
#    i = 0
#    cant = 0
#
#    while i < 3**60 :
#        cam = num_a_camino(i, 60)
#        if camino_valido(cam) :
#            pal = get_palabra(cam) 
#            if pal[29] == pal[31] :
#                if es_capicua(pal) :
#                    cant += 1
#        i += 1
#
#    return cant  


