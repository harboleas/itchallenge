# coding: utf-8
# ESPAÑOL
# Hemos definido nuestro propio lenguaje de marcado, HRML.
# En HRML, cada elemento consta de una etiqueta de inicio y atributos asociados a ella. Para cerrar un elemento, hay 2 opciones: una etiqueta de cierre separada, o; la etiqueta de cierre con una sintaxis especial. Solo las etiquetas de inicio pueden tener atributos. Las etiquetas también pueden estar anidadas.
# Las etiquetas de apertura siguen el formato:
# <tag-name attribute1-name="value1" attribute2-name="value2" ... >
# 
# 
# Las etiquetas de cierre siguen el formato:
# En la línea
# <tag-name attribute1-name="value1" ... />
# 
# 
# Etiqueta separada:
# </tag-name>
# Podemos llamar a un atributo haciendo referencia a la etiqueta, seguida del símbolo '~' y el nombre del atributo. Para atravesar etiquetas anidadas usamos el carácter '.” entre las etiquetas.
# Por ejemplo:
# <tag1 value="HelloWorld">
#   <tag2 desc="Description1" />
#   <tag3 name="Name2">
#     <tag4 quantity="12" />
#   </tag3>
# </tag1>
# 
# 
# Los atributos se referencian como:
# tag1~value
# tag1.tag2~desc
# tag1.tag3~name
# tag1.tag3.tag4~quantity
# 
# 
# Recibes un conjunto ordenado de archivos. Se te proporciona un código fuente válido en formato HRML que consta de N líneas. Tienes que responder Q consultas asociadas a cada código fuente. Cada consulta te pide que imprimas el valor del atributo especificado en una nueva línea separada. Imprimir "¡No encontrado!" si no existe dicho atributo.
# La respuesta que le permitirá continuar con la competencia será el hash SHA-256 (en mayúsculas) de un archivo que contiene todos los valores obtenidos como resultado de las consultas (respecto del pedido), un valor por línea, sin líneas en blanco (excepto una última nueva línea vacía que debe estar presente). Use solo LF (0x0A) como nueva línea.
# Formato de entrada de cada archivo
# La primera línea consta de dos enteros separados por espacio, N y Q. Las siguientes N líneas del código fuente de HRML válido y cada línea constan de una etiqueta de apertura con cero o más atributos, o una etiqueta de cierre. Luego, las siguientes líneas Q contienen las consultas. Cada consulta consiste en una string que hace referencia a un atributo en el código fuente HRML.
# Restricciones
# N> = 1
# N> = 1
# Todos los nombres de etiquetas son únicos.
# Sample Input for one file
# 4 3
# <tag1 value = "HelloWorld">
#   <tag2 name = "Name1">
#   </tag2>
# </tag1>
# tag1.tag2~name
# tag1~name
# tag1~value
# 
# 
# Sample Output for one file
# Name1
# Not Found!
# HelloWorld
# 
# 
#https://www.dropbox.com/s/tdpttblm5ez64vq/HRML%20Parser.zip?dl=0

files = []
for i in range(1,16):

    f = open("HRML/input-"+str(i).zfill(2)+".hrml")
    files.append(f.readlines())
    f.close()



class Tag(object):

    def _crear(self, args):
        setattr(self, args[0], Tag())
        obj = getattr(self, args[0])
        for i in args[1:]:
            name, value = i.split("=")
            setattr(obj, name, value[1:-1])
        obj.padre = self
        return obj

f = open("malaysia_resul.txt", "w")

def parser(datos, f):

    n, q = [int(i) for i in datos[0][:-1].split(" ")]

    print "Consultas"
    print

    codigo = datos[1:n+1]
    consul = datos[n+1:n+q+1]
    raiz = Tag()
    obj = raiz

    for linea in codigo:
        # remover el espacio inicial
        i=0
        while linea[i] == " ":
            i += 1
        linea = linea[i+1:-2]
        if linea[-1] == "/":
            tag = linea[:-1].split(" ")
            obj._crear(tag)
        else:
            tag = linea.split(" ")
            if tag[0][0] == "/":
                obj = obj.padre
            else:
                obj = obj._crear(tag)

    for linea in consul:
        linea = linea.replace("~", ".")[:-1]

        try:
            exec("print raiz."+linea)
            exec("f.write(raiz."+linea+")")
            f.write("\n")
        except:
            print "¡No encontrado!"
            f.write('¡No encontrado!\n')

    print

#    f.write("\n")
    return raiz

raices = []
for i in files:
    raices.append(parser(i, f))
f.write("\n")
f.close()

from hashlib import sha256

f = open("malaysia_resul.txt")
datos = f.read()
f.close()

sha = sha256(datos)

print sha.hexdigest().upper()




