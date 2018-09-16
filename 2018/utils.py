#################################################
# utils.py 
#
# Description :
#   Conjunto de funciones utiles para resolver  
#   problemas del tipo IT Challenge
#
# Author :
#   Hugo Arboleas <harboleas@citedef.gob>
#                 <hugo.arboleas@gmail.com>
#
#################################################

def mcd(a, b):
    """Calcula el maximo comun divisor entre a y b"""

    if b == 0:
        return a
    else:
        return mcd(b, a%b)


def mcm(a, b):
    """Calcula el minimo comun multiplo entre a y b"""

    return a*b / mcd(a,b)

def cant_div(n):
    """Cantidad de divisores de un numero natural n"""
    cant = 0
    for i in xrange(1,n+1):
        if n % i == 0:
            cant += 1
    return cant

def es_primo_(n):
    """Determina si un numero natural n es primo, version no optimizada"""
    if cant_div(n) == 2:
        return True
    else:
        return False

def es_primo(n):
    """Determina si numero natural n es primo, optimizado"""

    if n == 1:
        return False
    else:
        for i in xrange(2, int(n**0.5) + 1):
            if n%i == 0:
                return False
        return True

def es_primo_2(n):
    """Determina si numero natural n es primo, optimizado"""

    if n == 1:
        return False, 1
    else:
        for i in xrange(2, int(n**0.5) + 1):
            if n%i == 0:
                return False, i
        return True, n

def factorizar(n):

    factores = []

    while n > 1:
        p = es_primo_2(n)[1]
        factores.append(p)
        n = n / p

    return factores


def list_primos(n):
    """Lista los primos menores o iguales a n"""

    primos = [p for p in xrange(2, n+1) if es_primo(p)]
    return primos


def es_prod_2_primos(n):
    """Determina si n es producto de 2 numeros primos"""

    primos = list_primos(int(n**0.5))

    for p1 in primos:
        if n % p1 == 0:
           if es_primo(n / p1):
               return True
           else:
               return False

    return False


def list_perm(seq):
    """Genera una lista con las permutaciones de la seq"""

    if len(seq) == 1:
        return [seq]
    else:
        perms = []
        for i in range(len(seq)):
            # Genera todas las permutaciones con el i-esimo elemento de la seq
            # en primer lugar
            aux = []
            for permu in list_perm(seq[:i] + seq[i+1:]):
                aux.append(seq[i:i+1] + permu)
            perms.extend(aux)

    return perms


def prod_cartes(A, *BxC_):
    """Genera el producto cartesiano A x B x C x ....."""

    if  len(BxC_) == 1:
        return [(a,b) for a in A for b in BxC_[0]]
    else:
        prod = []
        aux = prod_cartes(*BxC_)
        for a in A:
            for b in aux:
                prod.append((a,) + b)
        return prod


def cambio_de_base(num, base, size):
    """Genera una lista de tamano size con la representacion del numero en la base dada. Donde :
    num : numero en base 10
    base : secuencia con los elementos de la base
    size : cantidad de digitos de num en la nueva base"""

    b = len(base)
    num_base = []
    for i in xrange(size):
        r = num % b
        num = num / b
        num_base.append(base[r])

    return num_base


def list_comb(seq):
    """Genera una lista con las combinaciones de la secuencia"""
    if len(seq) == 1:
        return [seq]
    else:
        combs = []
        conj = set(seq)
        for x in conj:
            i = seq.index(x)
            aux = []
            for comb in list_comb(seq[:i] + seq[i+1:]):
                aux.append(seq[i:i+1] + comb)
            combs.extend(aux)
        return combs


def calcPi():
    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
    while True:
        if 4*q+r-t < n*t:
            yield n
            nr = 10*(r-n*t)
            n = ((10*(3*q+r))//t)-10*n
            q *= 10
            r = nr
        else:
            nr = (2*q+r)*l
            nn = (q*(7*k)+2+(r*l))//(t*l)
            q *= k
            t *= l
            l += 2
            k += 1
            n = nn
            r = nr


#  vim: set ts=8 sw=4 tw=79 et :
