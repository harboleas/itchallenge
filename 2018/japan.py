# coding: utf-8
# ESPAÑOL
# Una hash table es una estructura de datos que permite guardar elementos y acceder a ellos muy rápidamente utilizando una función de hashing, es decir, una función que para cada elemento posible devuelve un número dentro de un rango indicado.
# 
# Una de las formas más famosas de implementar una hash table se llama "hashing cerrado". Esta implementación guarda los datos en un arreglo de longitud K prefijado de antemano y al recibir un nuevo elemento E, lo hashea y lo coloca en la posición hash(E) (la función "hash" siempre devuelve un entero en el intervalo [0,K)). Si esa posición ya se encuentra ocupada, intenta guardarlo en la posición hash(E)+1. Si esa también está ocupada, intenta en la hash(E)+2 y así siguiendo, hasta llegar a la última posición del arreglo. Si aún así no encuentra espacio, vuelve a la posición 0 del arreglo y sigue el mismo proceso hasta encontrar una posición libre.
# 
# Juan programó su hash table utilizando hashing cerrado, y utilizó una función de hashing uniforme (o sea, que para cada elemento asigna un valor entero en el rango [0,K) con la misma probabilidad). Desafortunadamente, su implementación tiene un bug: si llega al final del arreglo y no encontró espacio para guardar el elemento, lo descarta directamente (es decir, no intenta colocarlo en las posiciones 0, 1, 2... como sería correcto).
# 
# Para testear la implementación de Juan, se seleccionaron N elementos al azar para insertarlos en una hash table implementada con un arreglo de longitud K. ¿Cuál es la probabilidad de que con este test descubramos que la implementación de Juan tiene un bug, si N = 27 y K = 42?
# 
# Deberá ingresarse la respuesta como fracción irreducible (ver ejemplo).
# 
# Ejemplo: 
# 
# Si N = 2 y K = 2, los hashing posibles para los N = 2 elementos a insertar son:
# 
# 0 0
# 0 1
# 1 0
# 1 1
# 
# El único caso en el que el bug se expondrá es si ambos hashes son 1. En este caso, primero se guarda el primer elemento en array[1]. Luego, el siguiente elemento no tiene espacio en array[1] y como es la última posición del arreglo, lo descartará. Por lo tanto, la respuesta para este caso será "1/4" (sin comillas)
# 
