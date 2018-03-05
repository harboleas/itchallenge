
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
    for lon in xrange(mitad):
        for pos in xrange(i, n-2*lon):
            s = texto[pos:pos+lon]
            if s in texto[pos+lon:]:
                print s
                i = pos
                break

#  vim: set ts=4 sw=4 tw=79 et :
