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

#def valido(cuad, suma):
#
#    sum_col = 0
#    for i in range(5):
#        sum_col += cuad[i,:]
#    if not np.all(sum_col == suma):
#        return False
#    else:
#        if cuad.trace() == cuad[:,::-1].trace() == suma :
#            return True
#        else:
#            return False
#
#
#def gen_filas(suma):
#    """Genera las posibles filas de suma constante"""
#
#    filas = []
#    for a in range(4):
#        if a > suma:
#            break
#        for b in range(4):
#            if a + b > suma:
#                break
#            for c in range(4):
#                if a + b + c > suma:
#                    break
#                for d in range(4):
#                    if a + b + c + d > suma:
#                        break
#                    else:
#                        e = suma-a-b-c-d
#                        filas.append(np.array((a,b,c,d,e)))
#    return filas
#
#def gen_fila(n, suma, cuad):
#    """Genera las posibles filas de la posicion n, de suma constante"""
#
#    aux = cuad.copy()
#    s_diag1 = aux.diagonal()[:n].sum()
#    s_diag2 = aux[:,::-1].diagonal()[:n].sum()
#    s = np.zeros(5)
#    for i in range(n):
#        s += aux[i, :]
#    filas = []
#    for a in range(4):
#        if a + s[0] > suma:
#            break
#        elif n == 4 and a+s_diag2 > suma:
#            break
#
#        for b in range(4):
#            if a + b > suma or b + s[1] > suma:
#                break
#            elif n == 1 and b + s_diag1 > suma:
#                break
#            elif n == 3 and b + s_diag2 > suma:
#                break
#
#            for c in range(4):
#                if a + b + c > suma or c + s[2] > suma:
#                    break
#                elif n == 2 and c + s_diag1 > suma:
#                    break
#                elif n == 2 and c + s_diag2 > suma:
#                    break
#
#                for d in range(4):
#                    if a + b + c + d > suma or d + s[3] > suma:
#                        break
#                    elif n == 1 and d + s_diag2 > suma:
#                        break
#                    elif n == 3 and d + s_diag1 > suma:
#                        break
#                    else:
#                        e = suma-a-b-c-d
#                        if e + s[4] > suma:
#                            continue
#                        elif n == 4 and e + s_diag1 > suma:
#                            continue
#                        elif 0 <= e <= 3:
#                            filas.append(np.array((a,b,c,d,e)))
#    return filas
#
#
#cuad = np.zeros((5,5))
#
#
#def cuenta_cuads(suma, n, posibles, cuad):
#
#    cant = 0
#
#    if n == 4:
#        for ultima_fila in posibles:
#            cuad[n,:] = ultima_fila
#            if valido(cuad, suma):
#                cant += 1
#        return cant
#
#    else:
#        for fila_n in posibles:
#            cuad[n,:] = fila_n
#            posibles_sig = gen_fila(n+1, suma, cuad)
#            cant += cuenta_cuads(suma, n+1, posibles_sig, cuad)
#
#        return cant
#
#
#def cuenta(suma):
#
#    return cuenta_cuads(suma, 0, gen_filas(suma), np.zeros((5,5)))


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

