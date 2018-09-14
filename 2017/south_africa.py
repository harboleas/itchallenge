
# coding: utf-8

# Encontrar la palabra de 8 caracteres que solo contenga las siguientes letras:
# 
# acdegilmnoprstuw
# 
# de forma que la función challenge_hash(string) devuelva el resultado 24785204182557 utilizando el siguiente código:
# 

def challenge_hash(s):
    h = 7
    letters = "acdegilmnoprstuw"

    for i in range(len(s)):
        h = (h * 37 + letters.index(s[i]))

    return h

# Por ejemplo, si intentaramos encontrar una palabra de 9 caracteres donde la función devuelva 934632622822695, la misma sería mercadoli.

def crack_hash(size, num_hash):

    # Observacion :
    # hash = 7 * 37^n + i_0 * 37^(n-1) + i_1 * 37^(n-2) + ... + i_n 
    # y como 0 <= i_n <= 15 < 37 para todo n, entoces la secuencia
    # 7 i_0 i_1 ... i_n es el numero hash en base 37 

    hash_base37 = []
    letters = "acdegilmnoprstuw"

    for n in xrange(size+1):
        r = num_hash % 37
        num_hash = num_hash / 37
        hash_base37.append(r)

    if hash_base37[-1] != 7:
        print "Hash invalido"
        return None

    try:
        del hash_base37[-1]
        # remplazo el indice por la letra correspondiente 
        palabra = [letters[i] for i in hash_base37]
    except:
        print "Hash invalido"
        return None

    s = "".join(palabra)

    return s[::-1]


#  vim: set ts=4 sw=4 tw=79 et :
