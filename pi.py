def calcPi():
    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
    while True:
        if 4*q+r-t < n*t:
            yield n
            nr = 10*(r-n*t)
            n  = ((10*(3*q+r))//t)-10*n
            q  *= 10
            r  = nr
        else:
            nr = (2*q+r)*l
            nn = (q*(7*k)+2+(r*l))//(t*l)
            q  *= k
            t  *= l
            l  += 2
            k += 1
            n  = nn
            r  = nr
 

from primos import *

def peru_pi() :

    pos = 7
    digitos = 7

    pi = calcPi()
    pi.next()   # saco el entero

    num = ""
    for i in xrange(digitos) :
        num += str(pi.next())

    cant = 0
    cant2 = 1
    while cant < pos :
        if cant < 6 :
            if es_capicua(num) :
                if es_primo(int(num)) :
                    cant += 1
                    print num
        elif cant == 6 :
            if es_capicua(num) :
                cant2 += 1
            if cant2 == 7 :
                cant += 1
                print num

        num = num[1:] + str(pi.next())


