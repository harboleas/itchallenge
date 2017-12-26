import numpy as np

with open("cubo.txt") as f:
    txt = f.read()

mat = txt.split("\n\n")

cubo = np.array([[[val for val in fila]
                       for fila in altura.split()]
                       for altura in mat])

#cubo = np.array([[["a","b","b"],["c","b","a"]]])

class Pos(tuple):
    """Posicion : altura, fila, columna"""

    def __add__(self, b) :
        return Pos([a_i + b_i for a_i, b_i in zip(self, b)])

    def __sub__(self, b) :
        return Pos([a_i - b_i for a_i, b_i in zip(self, b)])

    def __mul__(self, n):
        return Pos([a*n for a in self])


def get_size(ini, fin):
    """Devuelve el tamano de un cubo con esas pos inicial y final"""

    return fin - ini + (1,)*len(ini)


ini = Pos([0, 0, 0])
fin = Pos([20, 20, 20])

# caminos contados
caminos_contados = {}


def contar_caminos(ini, fin) :
    """Cuenta los caminos entre los extremos opuestos del cubo que forman palabras
    capicuas"""

    try:
        # me fijo si es un camino que ya calcule para acelerar el proceso
        return caminos_contados[(ini,fin)]

    except:

        if cubo[ini] != cubo[fin]:
            # no hay camino posible
            caminos_contados[(ini,fin)] = 0
            return 0

        else:
            size = get_size(ini, fin)
            # casos bases
            if size in [(1,1,2), (1,2,1), (2,1,1), (3,1,1), (1,3,1), (1,1,3)]:
                # solo un caminio capicua
                caminos_contados[(ini,fin)] = 1
                return 1
            elif size in [(1,2,2), (2,1,2), (2,2,1)]:
                # dos caminos capicuas
                caminos_contados[(ini,fin)] = 2
                return 2

            # cuento los caminos de forma recursiva 
            else:
                caminos = 0

                if size[2] > 2:
                    caminos += contar_caminos(ini+(0,0,1), fin-(0,0,1))

                if size[1] > 1 and size[2] > 1:
                    caminos += contar_caminos(ini+(0,0,1), fin-(0,1,0))
                    caminos += contar_caminos(ini+(0,1,0), fin-(0,0,1))

                if size[1] > 2:
                    caminos += contar_caminos(ini+(0,1,0), fin-(0,1,0))

                if size[0] > 1 and size[2] > 1:
                    caminos += contar_caminos(ini+(0,0,1), fin-(1,0,0))
                    caminos += contar_caminos(ini+(1,0,0), fin-(0,0,1))

                if size[0] > 1 and size[1] > 1:
                    caminos += contar_caminos(ini+(0,1,0), fin-(1,0,0))
                    caminos += contar_caminos(ini+(1,0,0), fin-(0,1,0))

                if size[0] > 2:
                    caminos += contar_caminos(ini+(1,0,0), fin-(1,0,0))

                caminos_contados[(ini,fin)] = caminos
                return caminos

#  vim: set ts=4 sw=4 tw=79 et :
