
def contar_coreos(n, k=0, tablero=None):
    """Cuenta las coreografias de las pulgas
       generandolas de forma recursiva"""

    if k == 0:
        tablero = [[None for j in xrange(n)] for i in xrange(n)]

    coreos = 0
    i = k / n
    j = k % n

    saltos_posibles = determinar_saltos2(tablero, i, j)

    if not saltos_posibles:
       return 0

    else:
        if k == n**2 - 1:
            tablero[i][j] = saltos_posibles[0]
#            print "\ntablero"
#            for fila in tablero:
#                for col in fila:
#                    print col,
#                print "\n"
            return 1
        else:
            for salto in saltos_posibles:
                tablero[i][j] = salto
                coreos += contar_coreos(n, k+1, tablero)
            return coreos


def determinar_saltos(mat, i, j):
    """Determina los posibles saltos entrantes y salientes a la casilla"""

    n = len(mat)

    #     |  j-1   j    
    # -----------------
    # i-1 |        A     
    #  i  |   B  (i,j) 

    a = b = None

    if i-1 >= 0:
        a = mat[i-1][j]

    if j-1 >= 0:
        b = mat[i][j-1]

    ###########################################

    if i == 0:
        if j == 0:
            return [" ^>", " v<"]
        elif j == n-1:
            if b == " ^>" or b == ">>>":
                return [">v "]
            elif b == " v<" or b == "<<<":
                return ["<^ "]
            else:
                return []
        elif b == " ^>" or b == ">>>":
            return [">>>", ">v "]
        elif b == ">v " or b == "<^ ":
            return [" ^>", " v<"]
        elif b == " v<" or b == "<<<":
            return ["<<<", "<^ "]
        else:
            return []

    elif j == 0:
        if i == n-1:
            if a == " v " or a == " v<":
                return [" v>"]
            elif a == " ^ " or a == " ^<" or a == " ^>":
                return [" ^<"]
            else:
                return []
        elif a == " v " or a == " v<":
            return [" v ", " v>"]
        elif a == " v>" or a == " ^<":
            return [" ^>", " v<"]
        elif a == " ^ " or a == " ^>":
            return [" ^ ", " ^<"]
        else:
            return []

    elif a == "<^ " or a == " ^ " or a == " ^>":
        if b == " v>" or b == ">>>" or b == " ^>":
            return [">^ "]
        elif b == " ^<" or b == "<<<" or b == " v<":
            return []
        else:
            if i < n-1 and j < n-1:
                return [" ^ ", " ^<"]
            elif j < n-1:
                return [" ^<"]
            elif i < n-1:
                return [" ^ "]
            else:
                return []

    elif a == ">v " or a == " v " or a == " v<":
        if b == " ^<" or b == "<<<" or b == " v<":
            return ["<v "]
        elif b == " v>" or b == ">>>" or b == " ^>":
            return []
        else:
            if i < n-1 and j < n-1:
                return [" v ", " v>"]
            elif j < n-1:
                return [" v>"]
            elif i < n-1:
                return [" v "]
            else:
                return []

    else:
        if b == " ^<" or b == "<<<" or b == " v<":
            if i < n-1 and j < n-1:
                return ["<<<", "<^ "]
            elif j < n-1:
                return ["<<<"]
            elif i < n-1:
                return ["<^ "]
            else:
                return []
        elif b == " v>" or b == ">>>" or b == " ^>":
            if i < n-1 and j < n-1:
                return [">>>", ">v "]
            elif j < n-1:
                return [">>>"]
            elif i < n-1:
                return [">v "]
            return []
        else:
            if i < n-1 and j < n-1:
                return [" v<", " ^>"]
            else:
                return []


def determinar_saltos2(mat, i, j):
    """Determina los posibles saltos a y desde la casilla"""

    n = len(mat)

    #     |  j-1   j    
    # -----------------
    # i-1 |        A     
    #  i  |   B  (i,j) 

    a = b = None

    if i-1 >= 0:
        a = mat[i-1][j]

    if j-1 >= 0:
        b = mat[i][j-1]

    ###########################################

    if i == 0:
        if j == 0:
            return [" :-"]
        elif j == n-1:
            if b == " :-" or b == "---":
                return ["-: "]
            else:
                return []
        elif b == " :-" or b == "---":
            return ["---", "-: "]
        elif b == "-: ":
            return [" :-"]
        else:
            return []

    elif j == 0:
        if i == n-1:
            if a == " | " or a == " :-":
                return [" :_"]
            else:
                return []
        elif a == " | " or a == " :-":
            return [" | ", " :_"]
        elif a == " :_":
            return [" :-"]
        else:
            return []

    elif a == "-: " or a == " | " or a == " :-":
        if b == " :_" or b == "---" or b == " :-":
            return ["_: "]
        else:
            if i < n-1 and j < n-1:
                return [" | ", " :_"]
            elif j < n-1:
                return [" :_"]
            elif i < n-1:
                return [" | "]
            else:
                return []

    else:
        if b == " :_" or b == "---" or b == " :-":
            if i < n-1 and j < n-1:
                return ["---", "-: "]
            elif j < n-1:
                return ["---"]
            elif i < n-1:
                return ["-: "]
            else:
                return []
        else:
            if i < n-1 and j < n-1:
                return [" :-"]
            else:
                return []


#  vim: set ts=4 sw=4 tw=79 et :
