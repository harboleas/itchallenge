
def contar_coreos(n, k):

    if k == 0:
        tablero = [[0 for j in xrange(n)] for i in xrange(n)]
        coreos = 0

    i = k / n
    j = k % n

    saltos_posibles = calcular_saltos(tablero, i, j)

    if not saltos_posibles:
        return 0

    else:
        for salto in saltos_posibles:
            tablero[i][j] = salto
            coreos += contar_coreos(n, k+1)

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

        if i-2 >= 0 and tablero[i-2][j] == "v":
            entran_C += 1
        if i-1 >= 0:
            if j-1 >= 0:
                if tablero[i-1][j-1] == ">":
                    entran_C += 1
                elif tablero[i-1][j-1] == "v":
                    entran_F += 1
            if j+1 <= n-1 and tablero[i-1][j+1] == "<":
                entran_C += 1
        if j-2 >= 0 and tablero[i][j-2] == ">":


#  vim: set ts=4 sw=4 tw=79 et :
