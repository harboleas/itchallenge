
# coding: utf-8

# El mundo en el que vivimos esta gobernado por numeros, algunos muy interesantes:
# 
# Los números irracionales como PI o E no pueden representarse como una fracción de enteros
# Otros visualmente agradables como los Capicúas, con la peculiar característica de que pueden ser leídos de izquierda a derecha o viceversa.
# Y los muy famosos numeros primos, a quienes algunos los consideran la base de las matemáticas otros un Santo Grial.
# Desde hace dos mil años los matemáticos se han interesado por los numeros primos, tras su naturaleza infinita y misteriosa se esconde la interrogante ¿Existirá un patron que ayude a predecir la aparicion y distribucion de números primos en su camino al infinito?
# 
# En este infinito universo de números busquemos uno interesante
# 
# ¿Cual es el séptimo número conformado por 7 decimales consecutivos de PI que formen un número primo y capicúa a la vez?
# Curiosidad: Contando el sexto y séptimo número que cumplen las condiciones anteriores y los capicúas intermedios entre ambos números, contamos 7 tambien.
# 
# Ejemplo:
# 
# Si buscamos el segundo número de 5 dígitos consecutivos conformados por decimales de PI que conformen un número primo y un capicúa a la vez, este sería: 73637
# 
# 3.14592653589793238 46264 338327950...2279 38183 0119491298....96091 73637 17872
# 
# 46264 (Capicúa)
# 38183 (Primer Primo y Capicúa)
# 73637 (Segundo Primo y Capicúa)
# 
# ¿Donde lo encontramos?
# 
# Posición [1 - 5]:                   14159   Ni capicúa, ni primo
# Posición [2 - 6]:                   41592   Ni capicúa, ni primo
# Posición [3 - 7]:                   15926   Ni capicúa, ni primo
# Posición [4 - 8]:                   59265   Ni capicúa, ni primo
# Posición [5 - 9]:                   92653   Ni capicúa, ni primo
#     ...
# Posición [19 - 23]:                   46264 Es capicúa pero no primo
#     ...
# Posición [488 - 492]:         #1:   38183   Capicúa y primo 
#     ...
# Posición [641 - 645]:         #2:   73637   Capicúa y primo 

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

def peru_pi():

    pos = 7
    digitos = 7

    pi = calcPi()
    pi.next()   # saco el entero

    num = ""
    for i in xrange(digitos):
        num += str(pi.next())

    cant = 0
    cant2 = 1
    while cant < pos:
        if cant < 6:
            if es_capicua(num):
                if es_primo(int(num)):
                    cant += 1
                    print num
        elif cant == 6:
            if es_capicua(num):
                cant2 += 1
            if cant2 == 7:
                cant += 1
                print num

        num = num[1:] + str(pi.next())

#  vim: set ts=4 sw=4 tw=79 et :
