
from primos import *

with open("level13.txt") as f :
    txt = f.read()

data = [int(i) for i in txt.split()]

def posibles_num(n) :

    return [n ^ 2**i for i in xrange(8)]


def rep_primos(datos, n) :

    primos = []

    for dis in xrange(1, len(datos)/n) :
        for i in xrange(len(datos) - n*dis) :
            seq = datos[i : i + n*dis : dis]
            aux = []
            for j in seq :
                aux.append(filter(es_primo, posibles_num(i)+[i]))

            for k in aux[0] :
                for l in aux[1:] :
                    if k not in l :
                        break
                else :
                    primos.append((k, dis))
                    print k, dis
                    break

    return primos   


def rep_primos2(datos, n) :

    primos = []

    for dis in xrange(1, len(datos)/n) :
        for i in xrange(len(datos) - n*dis) :
            seq = datos[i : i + n*dis : dis]
            p = seq[0]
            if seq == [p] * n and es_primo(p) :
                primos.append((p, dis))


    return primos
