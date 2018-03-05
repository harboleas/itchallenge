
# coding: utf-8

# Buchu, nuestro coleccionista de insectos y coreógrafo, tiene una tablero de damas donde suele desparramar pulgas para que las mismas ejecuten pasos de baile.
# 
# La coreografía que le enseñó consiste en que cada una de las pulgas debe situarse en una casilla, cuando las 100 están en su posición, Buchu toca el silbato y las pulgas saltan al casillero anexo (pueden saltar para las cuatro casillas anexas, salvo las del borde, no se pueden salir del tablero). 
# 
# Están tan bien entrenadas que cuando saltan saben que no tienen que cruzar el mismo borde de cada casilla, sino chocarían en el aire.
# 
# Obviamente también caen todas en una casilla diferente, siempre hay una pulga por casilla, es un salto coordinado perfecto.
# 
# Buchu, es tan meticuloso, que siempre quiere una coreografía distinta, y se propuso a anotar todas las diferentes opciones que el salto sincronizado de pulgas puede generar. 
# 
# ¿Cuál es este número?
# 

# Algoritmo naive, enumera todas las matrices y luego descarta
# no produce un resultado en un tiempo razonable 
# Lo dejo escrito porque me gusta la biyeccion entre las mat y los numeros 

def contar_coreografias(n):

    coreos = 0

    for i in xrange(4**(n*n)):
        mat = gen_mat(i, n)
        if validar_coreografia(mat, n):
            coreos += 1

    return coreos


def gen_mat(val, n):

    saltos = [">", "^", "<", "v"]

    mat = []
    for i in xrange(n):
        mat.append([])
        for j in xrange(n):
            r = val % len(saltos)
            val = val / len(saltos)
            mat[i].append(saltos[r])

    return mat


def validar_coreografia(mat, n):

    for k in xrange(n):
        if mat[0][k] == "^":
            return False
        if mat[n-1][k] == "v":
            return False
        if mat[k][0] == "<":
            return False
        if mat[k][n-1] == ">":
            return False

    for i in xrange(n):
        for j in xrange(n):
            entran = 0

            if j+1 < n and mat[i][j+1] == "<":
                entran += 1
                if mat[i][j] == ">":
                    return False

            if i-1 >= 0 and mat[i-1][j] == "v":
                entran += 1
                if mat[i][j] == "^":
                    return False

            if j-1 >= 0 and mat[i][j-1] == ">":
                entran += 1
                if mat[i][j] == "<":
                    return False

            if i+1 < n and mat[i+1][j] == "^":
                entran += 1
                if mat[i][j] == "v":
                    return False

            if entran != 1:
                return False

    return True


#  vim: set ts=4 sw=4 tw=79 et :
