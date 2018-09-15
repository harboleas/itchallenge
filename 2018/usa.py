# coding: utf-8

# ESPAÑOL

# Dados dos nombres de usuario, el grado de similitud se define como la longitud del prefijo más largo común a ambas cadenas. En este desafío, recibirás una cadena. Debes quebrar la cadena para crear sufijos cada vez más cortos y luego determinar la similitud del sufijo con la cadena original. Haz esto para cada longitud de sufijo desde la longitud de la cadena hasta 0 y acumula los resultados. Por ejemplo, considera la cadena 'ababa'
# https://www.dropbox.com/s/uprg7sgnalepyhu/Cadena%20ejemplo..docx?dl=0
# 
# Restricciones
# 1 ≤ T ≤ 10 ; 1 ≤ |s| ≤ 10^5  La cadena contiene solo letras en el intervalo ascii [az].
# 
# Cadena input: https://www.dropbox.com/s/qdfr7nd22cq8dil/Copia%20de%20input007.txt?dl=0
# 
# Sample Input 0
# 1
# ababaa 
# 
# Sample Output 0
# 11
# 

f = open("disparity.txt")

cadenas = f.readlines()

f.close()

def descartar(cadena, n):
    return cadena[n:]

def simil(cad1, cad2):
    for i in range(len(cad1)):
        if cad1[i] != cad2[i]:
            return i
    return i+1

def contar(cadena):
    acum = 0
    for i in range(len(cadena)):
        suf = descartar(cadena, i)
        acum += simil(suf, cadena)
    return acum

for cadena in cadenas[1:11]:
    print contar(cadena[:-1]), 

