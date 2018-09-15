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


cuad = [[0 for j in range(5)] for i in range(5)]

def genera(suma):

    aux = [0 for i in range(5)]

    for i in range(5):

        for b in range(suma+1-a):
            for c in range(suma+1-a-b):
                for
