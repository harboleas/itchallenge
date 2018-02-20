# Buchu, nuestro coleccionista de insectos y coreografo, tiene una tablero de damas donde suele desparramar pulgas para que las mismas ejecuten pasos de baile.
# 
# La coreografia que le enseno consiste en que cada una de las pulgas debe situarse en una casilla, cuando las 100 estan en su posicion, Buchu toca el silbato y las pulgas saltan al casillero anexo (pueden saltar para las cuatro casillas anexas, salvo las del borde, no se pueden salir del tablero). 
# 
# Estan tan bien entrenadas que cuando saltan saben que no tienen que cruzar el mismo borde de cada casilla, sino chocarian en el aire.
# 
# Obviamente tambien caen todas en una casilla diferente, siempre hay una pulga por casilla, es un salto coordinado perfecto.
# 
# Buchu, es tan meticuloso, que siempre quiere una coreografia distinta, y se propuso a anotar todas las diferentes opciones que el salto sincronizado de pulgas puede generar. 
# 
# Cual es este numero

def contar_coreos(n, m, k=0, tablero=None):
    """Cuenta las coreografias de las pulgas
       generandolas de forma recursiva"""

    if k == 0:
        tablero = [[None for j in xrange(m)] for i in xrange(n)]

    coreos = 0
    i = k / m
    j = k % m

    saltos_posibles = determinar_saltos(tablero, i, j)

    if not saltos_posibles:
       return 0

    else:
        if k == n*m - 1:
            tablero[i][j] = saltos_posibles[0]
            print "\ntablero"
            for fila in tablero:
                for col in fila:
                    print col,
                print "\n"
            return 1
        else:
            for salto in saltos_posibles:
                tablero[i][j] = salto
                coreos += contar_coreos(n, m, k+1, tablero)
            return coreos


def determinar_saltos(mat, i, j):
    """Determina los posibles saltos entrantes y salientes a la casilla"""

    n = len(mat)
    m = len(mat[0])

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
        elif j == m-1:
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
            if i < n-1 and j < m-1:
                return [" ^ ", " ^<"]
            elif j < m-1:
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
            if i < n-1 and j < m-1:
                return [" v ", " v>"]
            elif j < m-1:
                return [" v>"]
            elif i < n-1:
                return [" v "]
            else:
                return []

    else:
        if b == " ^<" or b == "<<<" or b == " v<":
            if i < n-1 and j < m-1:
                return ["<<<", "<^ "]
            elif j < m-1:
                return ["<<<"]
            elif i < n-1:
                return ["<^ "]
            else:
                return []
        elif b == " v>" or b == ">>>" or b == " ^>":
            if i < n-1 and j < m-1:
                return [">>>", ">v "]
            elif j < m-1:
                return [">>>"]
            elif i < n-1:
                return [">v "]
            return []
        else:
            if i < n-1 and j < m-1:
                return [" v<", " ^>"]
            else:
                return []


def determinar_saltos2(mat, i, j):
    """Determina los posibles saltos a y desde la casilla"""

    n = len(mat)
    m = len(mat[0])

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
        elif j == m-1:
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
            if i < n-1 and j < m-1:
                return [" | ", " :_"]
            elif j < m-1:
                return [" :_"]
            elif i < n-1:
                return [" | "]
            else:
                return []

    else:
        if b == " :_" or b == "---" or b == " :-":
            if i < n-1 and j < m-1:
                return ["---", "-: "]
            elif j < m-1:
                return ["---"]
            elif i < n-1:
                return ["-: "]
            else:
                return []
        else:
            if i < n-1 and j < m-1:
                return [" :-"]
            else:
                return []


#  vim: set ts=4 sw=4 tw=79 et :
