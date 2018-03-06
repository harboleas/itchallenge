
# coding: utf-8

#Como todo programador, en el día a día nos preocupa respetar principios como DRY. Para esto, deseamos escribir una aplicación que nos permita en forma automática encontrar código duplicado.
#
#Como primer prueba de concepto, se le ha encargado escribir un programa capaz de encontrar el substring más largo que se encuentre repetido dentro de un mismo texto.
#
#Dado que en MercadoLibre se usan muchas tecnologías distintas (Go, Java, Objective-C, Javascript, etc.), la herramienta que armemos no debiera depender de la gramática del lenguaje, sino tratar simplemente con texto plano.
#
#sample-data.txt: texto a analizar en búsqueda de duplicados
#Se solicita el substring más largo que se haya encontrado duplicado dentro del archivo de ejemplo.
#
#Podes encontrar el adjunto en https://s3.amazonaws.com/it.challenge/level15.txt

def busca_dup(texto):

    n = len(texto)
    mitad = n / 2
    i = 0

    codigo_dup = None

    for lon in xrange(mitad):
        encontrado = False
        for pos in xrange(i, n-2*lon):
            s = texto[pos:pos+lon]
            if s in texto[pos+lon:]:
                encontrado = True
                codigo_dup = s
                print "encontrado longitud", lon, "en posicion", pos
                print codigo_dup
                i = pos
                break
        # si no hay un string de longitud mayor que el ultimo encontrado, sale     
        if not encontrado:
            return codigo_dup

t = open("level15.txt").read()

#  vim: set ts=4 sw=4 tw=79 et :
