import numpy as np

with open("cubo.txt") as f:
    txt = f.read()

mat = txt.split("\n\n")

cubo_orig = np.array([[[val for val in fila]
                        for fila in altura.split()]
                        for altura in mat])

def contar_caminos(cubo) :
    """Cuenta los caminos entre los extremos opuestos del cubo que forman palabras
    capicuas"""

    if cubo[0,0,0] != cubo[-1,-1,-1]:
        # no hay camino posible
        return 0

    else:
        # casos bases
        if cubo.shape in [(1,1,2), (1,2,1), (2,1,1), (3,1,1), (1,3,1), (1,1,3)]:
            # solo un caminio posible
            return 1
        elif cubo.shape in [(1,2,2), (2,1,2), (2,2,1)]:
            return 2

        # cuento los caminos de forma inductiva 
        else:
            caminos = 0

            if cubo.shape[2] > 2:
                caminos += contar_caminos(cubo[:,:,1:-1])

            if cubo.shape[1] > 1 and cubo.shape[2] > 1:
                caminos += contar_caminos(cubo[:,:-1,1:])
                caminos += contar_caminos(cubo[:,1:,:-1])

            if cubo.shape[1] > 2:
                caminos += contar_caminos(cubo[:,1:-1,:])

            if cubo.shape[0] > 1 and cubo.shape[2] > 1:
                caminos += contar_caminos(cubo[:-1,:,1:])
                caminos += contar_caminos(cubo[1:,:,:-1])

            if cubo.shape[0] > 1 and cubo.shape[1] > 1:
                caminos += contar_caminos(cubo[:-1,1:,:])
                caminos += contar_caminos(cubo[1:,:-1,:])

            if cubo.shape[0] > 2:
                caminos += contar_caminos(cubo[1:-1,:,:])

            print caminos
            return caminos

#  vim: set ts=4 sw=4 tw=79 et :
