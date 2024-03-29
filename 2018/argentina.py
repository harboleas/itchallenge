# coding: utf-8
# ESPAÑOL
# ¡Científicos del centro para el Tratamiento y Control de la Población, hicieron un impresionante descubrimiento! Las alpacas, en lugar de portar un código genético compuesto de bases adenina (A), citosina (C), guanina (G) y timina (T), poseen bases completamente distintas: su ADN está compuesto de bases (A),(C),(L) y (P) donde (L) es lanina y (P) es preciosina. Más aún, los investigadores descubrieron que el código genético de las alpacas es extremadamente estructurado. Este se puede codificar como una secuencia sobre el alfabeto {A,C,L,P} aplicando algunas reglas. 
# 
# Partiendo con la letra A la secuencia que describe el ADN puede generarse aplicando N veces el siguiente conjunto de reglas de forma simultánea:
# 
# Reemplazar cada ocurrencia de (A) por (AL)
# Reemplazar cada ocurrencia de (L) por (PACA)
# Reemplazar cada ocurrencia de (P) por (CP)
# Reemplazar cada ocurrencia de (C) por (PC)
# Por ejemplo, si N = 3 la secuencia obtenida será ALPACACPALPCAL:
# 
# A −→ AL −→ ALPACA −→ ALPACACPALPCAL
# Los científicos están estudiando la hermosura de las alpacas. Hasta el momento han descubierto que existen M tipos de hermosura distintas. Y más aún, también han logrado relacionar el tipo de hermosura de una alpaca con la cantidad de veces que la subcadena (ALPACA) aparece en su secuencia de ADN. En particular, si (ALPACA) aparece D veces en la secuencia de ADN de una alpaca, entonces su tipo de hermosura está dado por el resto de la división de D por M. ¿Podrías ayudar a nuestros científicos a determinar qué tan bella es una alpaca en particular?
# La entrada consiste en una única línea que contiene dos números N y M separados por un espacio, donde N indica el número de iteraciones que describen el ADN de la alpaca (1 ≤ N ≤ 10^15), y M es la cantidad de tipos de hermosura (2 ≤ M ≤ 10^9).
# 
# Entrada:
# 234612846789231 123456789
# 
# 
# La respuesta es un único entero conteniendo el tipo de hermosura de la alpaca
# (D mod M).

#############################################################
#
#reglas = {"A": "AL",
#          "L": "PACA",
#          "P": "CP",
#          "C": "PC"}
#
#def aplica_reglas(cadena):
#
#    aux = ""
#    for c in cadena:
#        aux += reglas[c]
#
#    return aux
#
#
#def gen_ADN(n):
#
#    ini = "A"
#    for i in xrange(n):
#        ini = aplica_reglas(ini)
#
#    return ini
#
###############################################################


#def num_A(n):
#
#    if n == 0 or n == 1:
#        return 1
#    else:
#        return num_A(n-1) + 2*num_A(n-2)

def num_A(n):

    if n % 2 == 0:
        return int((2**(n+1) + 1)/3.0)
    else:
        return int((2**(n+1) - 1)/3.0)


def num_ALPACA(n):

    return num_A(n-2)

from utils import factorizar


# Tengo que resolver 2**(n-1) - 1 = 3*x (mod 3*m)

n = 234612846789231
m = 123456789

q = factorizar(n-1)[::-1]

r = (2**q[0]) % (3*m)

for i in range(1, len(q)):
    r = (r**q[i]) % (3*m)

x = 0

while (3*x + 1 - r) % (3*m) != 0:
    x += 1





