# coding: utf-8
#ESPAÑOL
#Llamamos cuadrado "no tan mágico" a una grilla de 5x5 en la que en cada casillero hay un dígito entre 0 y 3, y tal que la suma de cada una de sus filas, cada una de sus columnas y cada una de sus diagonales sea la misma.
#
#Por ejemplo, el siguiente cuadrado es "no tan mágico", pues cada una de sus filas, columnas y diagonales suma 3:
#
#0 0 0 0 3
#1 2 0 0 0
#0 1 0 2 0
#2 0 0 1 0
#0 0 3 0 0
#
#¿Cuántos cuadrados "no tan mágicos" existen?

import numpy as np


tres = np.array([[0, 0, 0, 0, 3],
                 [1, 2, 0, 0, 0],
                 [0, 1, 0, 2, 0],
                 [2, 0, 0, 1, 0],
                 [0, 0, 3, 0, 0]])


#def gen_filas():
#    """Genera las posibles filas"""
#
#    filas = []
#    for i in xrange(4**5):
#        aux = []
#        n = i
#        for j in range(5):
#            aux.append(n % 4)
#            n = n / 4
#        filas.append(np.array(aux))
#
#    return filas
#
#
#def gen_sumas(filas):
#    """Agrupa las filas por suma constante"""
#    d = {}
#
#    for fila in filas:
#        s = fila.sum()
#        if not d.has_key(s):
#            d[s] = [fila]
#        else:
#            d[s].append(fila)
#
#    return d
#
#
#def gen_pos_sig(n, s, cuad, sumas):
#
#    pos = []
#    for x in sumas[s]:
#        cuad[n,:] = x
#        for i in range(5):
#            sum_aux = cuad[:n+1,i].sum()
#            if sum_aux > s:
#                break
#        else:
#            if cuad.diagonal()[:n+1].sum() <= s:
#                if cuad[:,::-1].diagonal()[:n+1].sum() <= s:
#                    pos.append(x)
#    return pos
#
#
#def valido(cuad, s):
#
#    for i in range(5):
#        sum_aux = cuad[:,i].sum()
#        if sum_aux != s:
#            return False
#    else:
#        if cuad.diagonal().sum() == s:
#            if cuad[:,::-1].diagonal().sum() == s:
#                return True
#
#    return False
#
#
#
#def contar(s, n, posibles, cuad, sumas):
#
#    cant = 0
#
#    if n == 4:
#        for ultima_fila in posibles:
#            cuad[n,:] = ultima_fila
#            if valido(cuad, s):
#                cant += 1
#        return cant
#
#    else:
#        for fila_n in posibles:
#            cuad[n,:] = fila_n
#            posibles_sig = gen_pos_sig(n+1, s, cuad, sumas)
#            cant += contar(s, n+1, posibles_sig, cuad, sumas)
#
#        return cant
#
#
#filas = gen_filas()
#sumas = gen_sumas(filas)
#cuad = np.zeros((5,5))
#
#
#def cuenta(s):
#
#    return contar(s, 0, sumas[s], cuad, sumas)


def gen_posibles_sig(suma, n, cuad):

    j = n % 5
    i = n / 5

    sum_fila = cuad[i,:j].sum()
    sum_col = cuad[:i,j].sum()
    s_diag1 = 0
    s_diag2 = 0
    if i==j:
        s_diag1 = cuad.diagonal()[:i].sum()
    if i==4-j:
        s_diag2 = cuad[:,::-1].diagonal()[:i].sum()

    s = int(max(sum_fila, sum_col, s_diag1, s_diag2))

    if j == 4 and i < 4:
        x = suma - sum_fila
        if 0 <= x <= 3 and x+sum_col <= suma:
            return [x]
        else:
            return []

    if j == 4 and i == 4:
        x = suma - sum_fila
        y = suma - s_diag1
        z = suma - sum_col
        if 0 <= x <= 3 and x==y==z:
            return [x]
        else:
            return []

    if i == 4 and j == 0:
        x = suma - sum_col
        y = suma - s_diag2
        if 0 <= x <= 3 and x==y:
            return [x]
        else:
            return []


    if i == 4 and 0 < j < 4:
        x = suma - sum_col
        if 0 <= x <= 3 and x+sum_fila <= suma:
            return [x]
        else:
            return []

    return [x for x in range(4) if x+s <= suma]


def cuenta_cuad(suma, n=0, cuad=None, posibles=None):

    if n == 0:
        cuad = np.zeros((5,5), dtype=np.int8)
        posibles = range(4)

    j = n % 5
    i = n / 5

    if n == 24:
        if posibles:
            cuad[i,j] = posibles[0]
#            print cuad
#            raw_input()
            return 1
        return 0

    else:
        cant = 0
        for x in posibles:
            if x > suma:
                break
            cuad[i,j] = x
            posibles_sig = gen_posibles_sig(suma, n+1, cuad)
            cant += cuenta_cuad(suma, n+1, cuad, posibles_sig)

        return cant

#acumulado de 0 a 7 3141816
#total 3141816*2 = 6283632

