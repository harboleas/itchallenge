
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
            for salto in saltos_posibles:
                tablero[i][j] = salto
                coreos += contar_coreos(n, k+1, tablero)
            return coreos


def calcular_saltos(mat, i, j):

    n = len(mat)

    #     | j-1   j   j+1 
    # -------------------
    # i-1 |       A    B
    #  i  |  C  (i,j)

    a = b = c = None

    if i-1 >= 0:
        a = mat[i-1][j]
        if j+1 < n:
            b = mat[i-1][j+1]

    if j-1 >= 0:
        c = mat[i][j-1]

    if not a and not c:
        return [" ^>", " v<"]

    elif not a:
        if c[2] == ">":
            if j == n-1:
                return [">v "]
            else:
                return [">>>", ">v "]
        elif c[2] == "<":
            if j == n-1:
                return ["<^ "]
            else:
                return ["<<<", "<^ "]
        else: # " "
            return [" ^>", " v<"]

    elif not c:
        if a[1] == "v" and b[1] != "v":
            if i == n-1:
                return [" v>"]
            else:
                return [ " v ", " v>"]
        elif a[1] == "v":
            if i == n-1:
                return []
            else:
                return [" v "]
        else:
            if b == " ^ " and i == n-1:
                return []
            elif i == n-1:
                return [" ^<"]
            else:
                return [" ^ ", " ^<"]

    else:
        if c[2] == ">" and a[1] == "v":
            return []
        elif c[2] == ">" and a[1] == "^":
            return [">^ "]
        elif c[2] == ">":
            if i == n-1 or j == n-1:
                return []
            else:
                if b[1] == "v":
                    return [">v"]
                else:
                    return [">v ", ">>>"]
        elif c[2] == "<" and a[1] == "v":
            return ["<v "]
        elif c[2] == "<" and a[1] == "^":
            return []
        elif c[2] == "<":
            if j == n-1:
                return []
            else:
                return ["<<<"]
        elif a[1] == "v":
            if 


#  vim: set ts=4 sw=4 tw=79 et :
