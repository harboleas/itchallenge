
def contar_coreos(n, k=0, tablero=None):

    if k == 0:
        tablero = [[0 for j in xrange(n)] for i in xrange(n)]

    coreos = 0
    i = k / n
    j = k % n

    saltos_posibles = calcular_saltos(tablero, i, j)

    if not saltos_posibles:
        return 0

    else:
        if k == n**2 - 1:
            return len(saltos_posibles)
        else:
            for salto in saltos_posibles:
                tablero[i][j] = salto
                coreos += contar_coreos(n, k+1, tablero)
            return coreos


def calcular_saltos(mat, i, j):

    n = len(mat)

    if i == j == 0:
        return [">", "v"]

    else:
        posibles = [">", "^", "<", "v"]

        #     | j-2  j-1   j   j+1 
        # ------------------------
        # i-2 |            A
        # i-1 |       B    C    D
        #  i  |  E    F  (i,j)

        entran_C = 0
        entran_F = 0
        c = None
        f = None
        if i-2 >= 0 and mat[i-2][j] == "v":
            entran_C += 1
        if i-1 >= 0:
            c = mat[i-1][j]
            if j-1 >= 0:
                if mat[i-1][j-1] == ">":
                    entran_C += 1
                elif mat[i-1][j-1] == "v":
                    entran_F += 1
            if j+1 <= n-1 and mat[i-1][j+1] == "<":
                entran_C += 1
        if j-2 >= 0 and mat[i][j-2] == ">":
            entran_F += 1

        if j-1 >= 0:
            f = mat[i][j-1]

        if entran_C > 0 or c == "v" or i == 0:
            posibles.remove("^")
        if entran_F > 0 or f == ">" or j == 0:
            posibles.remove("<")
        if i == n-1:
            posibles.remove("v")
        if j == n-1:
            posibles.remove(">")

        if entran_C == 0:
            if i == n-1 and entran_F == 0:
                posibles = []
            else:
                posibles = ["^"]
        elif 
        return posibles

#  vim: set ts=4 sw=4 tw=79 et :
