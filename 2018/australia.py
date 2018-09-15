# coding: utf-8
# ESPAÑOL
# Hemos definido nuestro propio lenguaje de marcado, HRML. En HRML, cada elemento consta de una etiqueta de inicio y cierre, y hay atributos asociados con cada etiqueta. Solo las etiquetas de inicio pueden tener atributos. Podemos llamar a un atributo haciendo referencia a la etiqueta, seguida del símbolo '~' y el nombre del atributo. Las etiquetas también pueden estar anidadas.
# Las etiquetas de apertura siguen el formato:
# <tag-name attribute1-name = "value1" attribute2-name = "value2" ... >
# Las etiquetas	 de cierre siguen el formato:
# < /tag-name >
#  
# Por ejemplo:
# <tag1 value = "HelloWorld">
# <tag2 name = "Name1">
# </tag2>
# </tag1>
#  
# Los atributos se referencian como:
# tag1~value  
# tag1.tag2~name
#  
# Se te proporciona un archivo con un código fuente válido en formato HRML que consta de N líneas. Tienes que responder Q consultas. Cada consulta te pide que imprimas el valor del atributo especificado. Imprimir "¡No encontrado!" si no existe dicho atributo (el resultado de las Q consultas debe ser escrito a un archivo txt en una única línea).
#  
# ARCHIVO: https://www.dropbox.com/s/djqziqsk66dran7/Copia%20de%20input005.txt?dl=0
# 
# Formato de entrada
# La primera línea consta de dos enteros separados por espacio, N y Q. Las siguientes N líneas del código fuente de HRML válido y cada línea constan de una etiqueta de apertura con cero o más atributos, o una etiqueta de cierre. Luego, las siguientes líneas Q contienen las consultas. Cada consulta consiste en una string que hace referencia a un atributo en el código fuente HRML.
#  
# Restricciones
# 1 <= N <= 20
# 1 <= Q <= 20
# Cada línea en el código fuente HRML contiene un máximo de 200 caracteres.
# Cada referencia a los atributos en las consultas Q contiene un máximo de 200 caracteres.
# Todos los nombres de etiquetas son únicos.
#  
# Formato de salida
# Imprimir el valor del atributo para cada consulta. Imprimir "¡No encontrado!" sin comillas si no existe dicho atributo en el código fuente HRML.
#  
# Entrada de ejemplo:
# 4 3
# <tag1 value = "HelloWorld">
# <tag2 name = "Name1">
# </tag2>
# </tag1>
# tag1.tag2~name
# tag1 ~ nombre
# tag1~value
# 
# Salida de ejemplo 
# Name1 ¡No encontrado! HelloWorld

f = open("PyParser.txt")
datos = f.readlines()
f.close()

f = open("ejem_australia.txt")
datos2 = f.readlines()
f.close()


class Tag(object):

    def _crear(self, args):
        setattr(self, args[0], Tag())
        obj = getattr(self, args[0])
        for i in range((len(args)-1)/2):
            setattr(obj, args[1+i*2], args[1+i*2 + 1][1:-1])
        obj.padre = self
        return obj


def parser(datos, f):

    n, q = [int(i) for i in datos[0][:-1].split(" ")]

    codigo = datos[1:n+1]
    consul = datos[n+1:n+q+1]
    raiz = Tag()
    obj = raiz

    for linea in codigo:
        tag = linea[1:-2].split(" ")
        while "=" in tag:
            tag.remove("=")
        if tag[0][0] == "/":
            obj = obj.padre
        else:
            obj = obj._crear(tag)

    for linea in consul:
        linea = linea.replace("~", ".")[:-1]

        try:
            exec("print "+"raiz."+linea+",")
            exec("f.write(raiz."+linea+")")
            f.write(" ")
        except:
            exec("print '¡No encontrado!',")
            f.write('¡No encontrado! ')

    print

    return raiz

f = open("australia_resp.txt", "w")
raiz = parser(datos, f)
f.close()


