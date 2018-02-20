# Estamos en el año 2057 y Bolivia es la nueva potencia mundial en términos de infraestructura. Al parecer luego de varios años de inestabilidad económica, descubrieron una mina de litio que abastece desde hace 40 años a todo el planeta. Hay rutas que cruzan por todo el país, estadios, edificios, ciudades,  el 90% de la población trabaja en construcción y en la mina de litio.

#El país entero está dividido en una red cuadrículada (N x N) de ciudades, las cuales se conectan entre si por medio de Hyper Loops, es tan moderno, que no hay espacio para rutas, no se puede caminar o viajar en auto por las ciudades, las ciudades son monolitos conectados entre sí por las redes de Hyper Loops.
#
#Para mantener semejante inversión en infraestructura, si un ciudadano quiere viajar de una ciudad a otra, no tiene otra alternativa que pagar por un pasaje en el Hyper Loop. Esto ocasiona muchos problemas en la sociedad, dado que sienten que pierden su libertad.
#
#Existe otro problema, el Hyper Loop utiliza una impresionante cantidad de energía para funcionar, con lo cual cada ciudad contiene su propio reactor de fusión nuclear para alimentarlo (El reactor es de tipo Tokamak).
#
#Las plantas de fusión, son construídas por empresas privadas las cuales cobrar el costo eléctrico de diferente manera, el gobierno no establece un precio unificado ya que espera que el mismo se auto-regule por el mercado. Cosa que no sucede bien y genera más problemas aun al ciudadano que quiere viajar, dado que no es lo mismo cruzar el país por una ruta o por otra.
#
#El hyperloop tiene una autonomía máxima de 3 cruces de ciudades. Esto quiere decir que si parte de la ciudad ubicada en 1x1, hacia el este, tiene que recargar en la ciudad 1x4 para seguir su viaje. Siempre carga cada 3 saltos, no puede recargar en 2 saltos o 1.
#
#El Hyper Loop puede moverse para el norte, el este, el oeste y el sur. No puede salir de Bolivia,  así como en 1800 la red ferroviaria tenía que ser estándar entre países, se ha cometido el mismo error con el estándar de conexión del Hyper Loop. Bolivia utiliza el método Japonés, de 220V mientras que sus países limítrofes utilizan el de 110V de USA. No entendemos tampoco como puede ser que haya una central de fusión pero no se hayan puesto de acuerdo en el estándar eléctrico.
#
#El gobierno lo ha contratado, para poder desarrollar un algoritmo que ayude a los ciudadanos a entender bien cuál es la mejor ruta para ir de la ciudad 1x1 a la NxN (el trayecto que una los extremos del país).
#
#Para eso le facilta la siguiente información en un archivo:
#
#4 2 
#30 92 36 10 
#38 85 60 16 
#41 13 5 68 
#20 97 13 80
#
#La primera línea tiene los datos de N y del precio del pasaje entre ciudades. (N=4, Pasaje=2) Las siguientes líneas y columnas, representan los precios de la recarga de electricidad en cada ciudad (en forma de cuadrícula).
#
#El ejemplo muestra un país de 4x4, con precio de pasaje entre ciudad de 2 pesos y por ejemplo un costo de recarga de 20 pesos en la ciudad más al sud-oeste.
#
#El costo de la mejor ruta es para este ejemplo de 31 pesos. 
#
#Siempre se parte desde la posición 1x1, el Hyper Loop se mueve para el este 3 veces, se tiene que detener a recargar, el costo es de 10 pesos, se mueve al sur 2 veces y luego al oeste, tienen que recargar de nuevo, el costo es de 5 pesos, y finalmente se mueve al sur y al este, llegando a la ciudad final, aun le sobraba un salto, en caso de no sobrar debería haber recargado.
#
#Calcule el costo de la ruta para el archivo adjunto: https://s3.amazonaws.com/it.challenge/level21.txt

from mali import num_base

N = 90
precio_pasaje = 3

with open("bolivia.txt") as f:
    lineas = f.readlines()

mat = [[int(i) for i in linea.split()] for linea in lineas[1:]]


direc = [(0,1), (1,0)]

def num_a_camino(num, size):

    return num_base(num, direc, size)

def get_costo(camino):

    costo = (2*90-2) * precio_pasaje
    for i, j  in camino:
        costo += mat[i][j]

    return costo

#def gen_caminos(size):
#
#    caminos = []
#
#    for i in xrange(2**size):
#        caminos.append(num_a_camino(i, size))
#
#    return caminos
#


def get_coords_recarga():

    coords =[[] for i in range(2*90/3)]

    for i in xrange(N):
        for j in xrange(N):
            if (i+j) % 3 == 0:
                coords[(i+j)/3].append((i,j))

    return coords

def get_costo(camino):

    costo = (2*90-2) * precio_pasaje
    for i, j  in camino:
        costo += mat[i][j]

    return costo


def get_min():

    c_r = get_coords_recarga()
    caminos = selec_caminos(c_r)

    costo = min([get_costo(camino) for camino in caminos])

    return costo


def selec_caminos(coords):

    if len(coords) == 1:
        return [[i] for i in coords[0]]
    else:
        cam = []
        aux = selec_caminos(coords[1:])
        for i in coords[0]:
            y = []
            for j in aux:
                x = [i]+j
                if i[0] <= j[0][0] and i[1] <= j[0][1]:
                    y.append(x)
            cam.extend(y)
        return cam

#  vim: set ts=4 sw=4 tw=79 et :
