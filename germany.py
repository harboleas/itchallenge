
from primos import *

n = 86    
total = n*n

# fila, col

orig0 = (n/2 - 1, n/2)
orig1 = (n/2 - 1, n/2 - 1)
orig2 = (n/2, n/2 - 1)
orig3 = (n/2, n/2)

origs = [orig0, orig1, orig2, orig3]

def get_cuad(i,j) :

    if i < n/2 :
        if j >= n/2 :
            return 0
        else :
            return 1
    else :
        if j >= n/2 :
            return 3
        else : 
            return 2

def get_dist(i,j) :
    # distancia al origen

    cuad = get_cuad(i, j)

    oy, ox = origs[cuad]

    return abs(i-oy) + abs(j-ox)


coord_cuad = [[], [], [], []]

for i in xrange(n) :
    for j in xrange(n) :
        coord_cuad[get_cuad(i,j)].append((i,j))

dist_max = get_dist(0,0)
dist_c0 = [[] for i in xrange(dist_max+1)]
dist_c1 = [[] for i in xrange(dist_max+1)]
dist_c2 = [[] for i in xrange(dist_max+1)]
dist_c3 = [[] for i in xrange(dist_max+1)]

dist_cuads = [dist_c0, dist_c1, dist_c2, dist_c3]

for i in xrange(n) :
    for j in xrange(n) :
        dist_cuads[get_cuad(i,j)][get_dist(i,j)].append((i,j))        


selec_coord_1 = []
def gen_selec() :

    for d in xrange(dist_max+1) :
        for c0 in dist_c0[d] :
            for c1 in dist_c1[d] :
                for c2 in dist_c2[d] :
                    for c3 in dist_c3[d] :
                        selec_coord_1.append((c0,c1,c2,c3))

with open("laberinto.txt") as f :
    txt = f.readlines()

lab = [[int(i) for i in fila.split()] for fila in txt]

selec_coord_2 = []

def filtro_1() :

    for x,y,z,w in selec_coord_1 :
        X = lab[x[0]][x[1]]
        Y = lab[y[0]][y[1]]
        Z = lab[z[0]][z[1]]
        W = lab[w[0]][w[1]]
        if X+Y+Z+W > 0 :
            selec_coord_2.append((x,y,z,w)

selec_coord_3 = []

def filtro_2() :

    for x,y,z,w in selec_coord_2 :
        X = lab[x[0]][x[1]]
        Y = lab[y[0]][y[1]]
        Z = lab[z[0]][z[1]]
        W = lab[w[0]][w[1]]
        if es_prod_primos(X+Y+Z+W) :
            selec_coord_3.append((x,y,z,w)



