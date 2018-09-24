# coding: utf-8
#ESPAÑOL
#Tienes 4 tipos de bloques Lego™, de tamaños (1 x 1 x 1), (1 x 1 x 2), (1 x 1 x 3) y (1 x 1 x 4). Suponé que tienes un número infinito de bloques de cada tipo. Para abreviar, podemos llamar a estos tipos, respectivamente, bloque 1, bloque 2, bloque 3 y bloque 4, o incluso (1), (2), (3) y (4).
#
#Usando estos bloques, deseas hacer una pared de altura N y ancho M. La pared debe ser una estructura sólida continua sin agujeros. La pared debe estar conectada estructuralmente, por lo que no debe existir una vertical recta que permita que la pared se separe en dos sin cortar uno o más ladrillos.
#
# Input (entrada):
#
#La primera línea contiene el número de casos de prueba T. Siguen los casos de prueba T. Cada caso contiene dos enteros, N y M. 
#
#https://www.dropbox.com/s/h2brnoa5bg57zve/input%20Lego.txt?dl=0
# 
#Output (salida):
#
#Una sola línea que contiene la cantidad de formas de construir el muro.
#Como los números pueden ser muy grandes, puedes aplicar modulo 1.000.000.007 a la salida.
# 
#Restricciones:
#1 ≤ T ≤ 100
#1 ≤ N,M ≤ 1000
# 
#Sample Input:
#4
#2 2
#3 2
#2 3
#4 4
# 
#Sample Output:
#3793375
#

import math

def pos_fila(m):

    m_b = m / 2
    m_c = m / 3
    m_d = m / 4

    pos = []

    for a in range(m+1):
        for b in range(m_b+1):
            for c in range(m_c+1):
                for d in range(m_d+1):
                    if a + 2*b + 3*c +4*d == m:
                        pos.append((a,b,c,d))

    return pos


def comb(n, k):

    return math.factorial(n) / (math.factorial(n-k) * math.factorial(k))


def cuenta_fila(fila):

    cant = 1

    suma = sum(fila)

    for x in fila:
        cant *= comb(suma, x)
        suma -= x

    return cant


def contar2(m):

    cant = 0
    for fila in pos_fila(m):
        cant += cuenta_fila(fila)

    return cant


def contar(m, n=0, posibles=None, fila=None):

    if n==0:
        fila = [0]*(m-1)
        posibles = [0, 1]


    if n == m-2:
#        for x in posibles:
#            fila[n] = x
#            print fila
        return len(posibles)

    else:
        cant = 0
        for x in posibles:
            fila[n] = x
            posibles_sig = [0, 1]
            if n >= 2:
                if sum(fila[n-2:n+1]) == 0:
                    posibles_sig = [1]
            cant += contar(m, n+1, posibles_sig, fila)
        return cant



