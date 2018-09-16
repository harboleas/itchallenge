# coding: utf-8
# ESPAÑOL
# Dada una cadena de caracteres, s, podemos definir una sub cadena de caracteres como una cadena de caracteres no vacía que puede ser obtenida aplicando una de las siguientes operaciones
#  
# Quitar cero o más caracteres del lado izquierdo de s.
# Quitar cero o más caracteres del lado derecho de s.
# Quitar cero o más caracteres del lado izquierdo de s. y quitar cero o más caracteres del lado derecho de s.
# 
# Por ejemplo, si s=abcde, las subcadenas son:
# 1	abcde
#  2	abcd
#  3	bcde
#  4	abc
#  5	bcd
#  6	cde
#  7	ab
#  8	bc
#  9	cd
# 10	de
# 11	a 
# 12	b
# 13	c
# 14	d
# 15	e
# 
# 
# Tu tarea es determinar cuántas subcadenas se pueden obtener a partir de aplicar las operaciones descritas anteriormente sobre una cadena s.
#  
# La entrada contiene una sola línea que representa la cadena de caracteres a analizar.
#  
#  Link: https://www.dropbox.com/s/xzz4rki2tari7kx/Copia%20de%20input.txt?dl=0
#  
# La salida consiste de un número entero con el total de sub cadenas que se pueden obtener.
#  
# Restricciones
# s contiene caracteres en el rango ascii[a-z].
# 0 ≤ |s| ≤ 10^5

f = open("string.txt")
cadena = f.read()
f.close()

def cuenta_sub(cadena):

    n = len(cadena)

    cant = 0
    for lon in range(1,n+1):
#        print palabras
        palabras = {}
        for i in range(n+1-lon):
            pal = cadena[i:i+lon]
            if not palabras.has_key(pal):
                palabras[pal] = 1
                cant += 1
#                print cant, lon

    return cant


