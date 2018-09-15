# coding: utf-8
# ESPAÑOL
# Una caja que contiene N medallas fue encontrada en una excavación. Cada medalla está compuesta por diversas piedras y cada piedra está representada por una letra minúscula de la 'a' a 'z. Una piedra puede estar presente varias veces en una medalla y una piedra pasa a ser llamada especial si está presente al menos una vez en cada medalla
# Dada una lista de N de medallas con sus piedras, muestra el cuadrado de la cantidad de piedras especiales que se repiten más de dos veces en una medalla.
# Entrada
# La primera línea consiste de N,el número de medallas. Cada una de las proximas N líneas contienen una secuencia de letras minúsculas con las piedras de cada medalla
# 5 abcdefgggghijlmmmnopppqqqqrrr abcdefggghijlmmnopppqqqqrrr abcdefggggghijlmmmnopppqqqqrrr abcdefggggghijlmmmnopppqqqqrrr abcdefggggghijlmmmnopppqqqqrrr
# 

f = open("kenya.txt")
datos = f.readlines()[1:]
f.close()

def cuenta_piedras(cadena):

    d = {}

    for c in cadena:
        if not d.has_key(c):
            d[c] = 1
        else:
            d[c] += 1

    return d

datos_piedras = [cuenta_piedras(cadena[:-1]) for cadena in datos]

posibles = [k for k,v in datos_piedras[0].items() if v > 2]

cant = 0
for p in posibles:
    for x in datos_piedras[1:]:
        if not x.has_key(p):
            break
        elif x[p] <= 2:
            break
    else:
        cant += 1   # p es especial y se repite mas de dos veces en cada una

print cant**2






