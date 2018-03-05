
# coding: utf-8

# Los números han fascinado a la humanidad desde tiempos inmemoriales dado que rigen el orden de las cosas y las vicisitudes morales y mundanas del hombre.
# 
# Es sabido, que hay ciertos números muy especiales cuyo impacto es tan grande que de cambiar el universo no podría sostenerse. Entre estos números encontramos constantes como la velocidad de la luz en el vacío o aquel que representa el sentido mismo de la vida.
# 
# De todos los estudiosos de los misterios numéricos vale la pena destacar a los matemáticos y filósofos de la escuela pitagórica, que en su búsqueda del saber han intentado dar con un número definitivo que permitiría desentrañar los secretos de la quintaesencia.
# 
# Tras años de silencio, finalmente se comprendió que tal número místico aparecería en mediciones de energía oscura. No sin complicaciones, los herederos de pitágoras han logrado obtener una señal de energía oscura.
# 
# La señal obtenida es una secuencia de números de 8 bits. No obstante, se sabe que puede contener errores dadas las dificultades inherentes a la medición (no más del 10%); estos errores consisten en que algunos números pueden tener un único bit invertido.
# 
# Los filósofos entienden que el número que anhelan encontrar es el número primo pitagórico P que se repite la mayor cantidad de veces en la señal a intervalos regulares.
# 
# No obstante, este no es el número definitivo. El número definitivo se obtendría al multiplicar el número P por la distancia entre repeticiones: N = P*D
# 
# Por ejemplo, dada la siguiente secuencia:
# 
# 4 4 4 5 8 8 5 10 10 5
# 
# El resultado seria:
# 
# P = 5
# 
# D = 3
# 
# N = 15
# 
# Podes encontrar el adjunto en https://s3.amazonaws.com/it.challenge/level13.txt

from primos import *

with open("level13.txt") as f:
    txt = f.read()

data = [int(i) for i in txt.split()]

def posibles_num(n):

    return [n ^ 2**i for i in xrange(8)]


def rep_primos(datos, n):

    primos = []

    for dis in xrange(1, len(datos)/n):
        for i in xrange(len(datos) - n*dis):
            seq = datos[i : i + n*dis : dis]
            aux = []
            for j in seq:
                aux.append(filter(es_primo, posibles_num(i)+[i]))

            for k in aux[0]:
                for l in aux[1:]:
                    if k not in l:
                        break
                else:
                    primos.append((k, dis))
                    print k, dis
                    break

    return primos


def rep_primos2(datos, n):

    primos = []

    for dis in xrange(1, len(datos)/n):
        for i in xrange(len(datos) - n*dis):
            seq = datos[i : i + n*dis : dis]
            p = seq[0]
            if seq == [p] * n and es_primo(p):
                primos.append((p, dis))


    return primos

#  vim: set ts=4 sw=4 tw=79 et :
