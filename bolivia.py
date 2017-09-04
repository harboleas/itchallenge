from mali import num_base

N = 90
precio_pasaje = 3

with open("bolivia.txt") as f :
    lineas = f.readlines()

mat = [[int(i) for i in linea.split()] for linea in lineas[1:]]


direc = [(0,1), (1,0)]

def num_a_camino(num, size) :

    return num_base(num, direc, size)

def get_costo(camino) :

    costo = (2*90-2)*precio_pasaje 
    for i, j  in camino :
        costo += mat[i][j]

    return costo

#def gen_caminos(size) :
#
#    caminos = []
#
#    for i in xrange(2**size) :
#        caminos.append(num_a_camino(i, size))
#
#    return caminos
#


def get_coords_recarga() :
    
    coords =[[] for i in range(2*90/3)]

    for i in xrange(N) :
        for j in xrange(N) :
            if (i+j) % 3 == 0 :
                coords[(i+j)/3].append((i,j))

    return coords

def get_costo(camino) :

    costo = (2*90-2)*precio_pasaje 
    for i, j  in camino :
        costo += mat[i][j]

    return costo


def get_min() :

    c_r = get_coords_recarga()
    caminos = selec_caminos(c_r)

    costo = min([get_costo(camino) for camino in caminos])

    return costo


def selec_caminos(coords) :

    if len(coords) == 1 :
        return [[i] for i in coords[0]]
    else :
        cam = []
        aux = selec_caminos(coords[1:])
        for i in coords[0] :
            y = []
            for j in aux :
                x = [i]+j
                if i[0] <= j[0][0] and i[1] <= j[0][1] :
                    y.append(x)
            cam.extend(y)
        return cam



    
