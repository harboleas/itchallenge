# coding: utf-8
# ESPAÑOL
# Las ruletas con mensaje son un complicado esfuerzo de criptógrafos amateur para transmitir mensajes de manera trabajosa y cuya efectividad es absolutamente dudosa.
# Son ruletas divididas en una cantidad par de sectores y en las que cada sector contiene algún carácter ASCII. En la parte superior hay un marcador llamado ORDEN y en la parte INFERIOR hay un marcador llamado MENSAJE. 
# El protocolo determina que se lee comenzando en el sector marcado por ORDEN y en sentido horario todas las letras de la ruleta. Por ejemplo, en la siguiente posición inicial se puede leer la palabra BANANA
# https://www.dropbox.com/s/kskiiv2vxv8t5a7/banana.jpg?dl=0
# 
# Luego la ruleta comienza a girar y se irán mostrando sucesivamente las siguientes palabras:
# BANANA
# ANANAB
# NANABA
# ANABAN
# NABANA
# ABANAN
# 
# En el momento en el que la palabra leída desde la posición ORDEN es la mínima lexicográfica (la que aparecería primero en un diccionario), se podrá leer a partir de la posición MENSAJE un mensaje oculto de una longitud acordada previamente. 
# 
# En el ejemplo anterior, el momento en que se muestra el mensaje es cuando desde ORDEN se lee la palabra ABANAN, como se muestra en la siguiente imagen.
# https://www.dropbox.com/s/os05nkcxcezb7i6/abanan.jpg?dl=0
# 
# 
# Si la longitud acordada era 2, el mensaje oculto sería NA
# 
# Hemos descubierto una ruleta increíblemente grande. Contiene exactamente un millón de letras. Sabemos también que el mensaje cifrado que encontraremos allí tiene una longitud de 2976. El contenido de la ruleta en su estado inicial está dado en el archivo roulette.txt
# https://www.dropbox.com/s/4wec7pfsvvl5tt3/roulette.txt?dl=0 
# 
# ¿Podés ayudarnos a descubrirlo?
# 
# Aclaración: Para realizar la comparación "alfabética" de símbolos en el archivo deben utilizarse sus valores ASCII. 

f = open("roulette.txt")
datos = f.read()
f.close()

def girar(datos, n):

    resul = datos[n:]+datos[:n]

    return resul


def obtener_min(datos):

    minimo = datos

    for i in xrange(1, len(datos)):
        aux = girar(datos, i)
        if minimo >= aux:
            minimo = aux

    return minimo

out = obtener_min(datos)

m = len(out) / 2
largo = 2976

mensaje = out[m:m+largo]





