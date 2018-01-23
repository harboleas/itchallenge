
pepe = [0]

def contar_coreos(n, k=0, tablero=None):

    pepe[0] += 1

    if k == 0:
        tablero = [[None for j in xrange(n)] for i in xrange(n)]

    coreos = 0
    i = k / n
    j = k % n

    saltos_posibles = calcular_saltos(tablero, i, j)

    if not saltos_posibles:
#        print i+1,j+1
#        for f in tablero:
#            print f
        return 0

    else:
        if k == n**2 - 1:
            tablero[i][j] = saltos_posibles[0]
#            print i+1,j+1
#            for f in tablero:
#                print f
            return 1
        else:
#            print i+1,j+1
#            print "posibles ", saltos_posibles
            for salto in saltos_posibles:
#                raw_input()
#                print i+1,j+1
                tablero[i][j] = salto
#                for f in tablero:
#                    print f
                coreos += contar_coreos(n, k+1, tablero)
            return coreos


def calcular_saltos(mat, i, j):

    n = len(mat)

    if i == j == 0:
        return ["v", ">"]

    else:

        #     | j-2  j-1   j   j+1 
        # ------------------------
        # i-2 |            A
        # i-1 |       B    C    D
        #  i  |  E    F  (i,j)

        a = b = c = d = e = f = None

        if i-1 >= 0:
            c = mat[i-1][j]
            if i-2 >= 0:
                a = mat[i-2][j]
            if j-1 >= 0:
                b = mat[i-1][j-1]
            if j+1 < n:
                d = mat[i-1][j+1]

        if j-1 >= 0:
            f = mat[i][j-1]
            if j-2 >= 0:
                e = mat[i][j-2]

        entran_C = 0
        if a == "v" or b == ">" or d == "<":
            entran_C = 1

        entran_F = 0
        if b == "v" or e == ">":
            entran_F = 1

        entran = 0
        if f == ">" or c == "v":
            entran = 1

        ###########################################

        if c and f and not entran_C and not entran_F:
            if f == "v" or c == "v":
               return []
            else:
                return ["^"]

        elif c and not entran_C:
            if c == "v":
               return []
            else:
                return ["^"]

        elif f and not entran_F:
            if f == "v":
                return ["<"]

        posibles = [">", "^", "<", "v"]

        if entran_C or c == "v" or i == 0:
            posibles.remove("^")
        if entran_F or f == ">" or j == 0 or (i == n-2 and j == 1 and f ==
                "^"):
            posibles.remove("<")
        if i == n-1 or (j == n-1 and not entran) or (i == 0 and j == n-2 and f
                == ">") :
            posibles.remove("v")
        if j == n-1 or d == "v" or (j == 0 and i == n-2 and c == "v"):
            posibles.remove(">")

        return posibles

#  vim: set ts=4 sw=4 tw=79 et :
