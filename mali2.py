
def contar_coreos(n, k=0, tablero=None):
    """Cuenta las coreografias de las pulgas
       generandolas de forma recursiva"""

    if k == 0:
        tablero = [[None for j in xrange(n)] for i in xrange(n)]

    coreos = 0
    i = k / n
    j = k % n

    saltos_posibles = determinar_saltos(tablero, i, j)

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


class list_(list):
    """Solo modifico el comportamiento del remove"""

    def remove(self, elem):

        try:
            list.remove(self, elem)
        except:
            pass


def determinar_saltos(mat, i, j):
    """Determina los posibles saltos entrantes y salientes a la casilla"""

    n = len(mat)

    # posibles = [">^ ", "<v ", " ^<", " v>", ">v ", "<^ ", " v<", " ^>",
    # "<<<", ">>>", " v ", " ^ "]

    #     |  j-1   j   j+1 
    # --------------------
    # i-1 |        A    C 
    #  i  |   B  (i,j) 

    a = b = c = d = None

    if i-1 >= 0:
        a = mat[i-1][j]

    if j-1 >= 0:
        b = mat[i][j-1]

    if i-1 >= 0 and j+1 <= n-1:
        c = mat[i-1][j+1]

    ###########################################

    posibles = list_([">^ ", "<v ", " ^<", " v>", ">v ", "<^ ", " v<", " ^>",
     "<<<", ">>>", " v ", " ^ "])


    if i == 0:
        posibles.remove(" v ")
        posibles.remove(" ^ ")
        posibles.remove("<v ")
        posibles.remove(">^ ")
        posibles.remove(" v>")
        posibles.remove(" ^<")

    if j == 0:
        posibles.remove("<<<")
        posibles.remove(">>>")
        posibles.remove("<v ")
        posibles.remove(">^ ")
        posibles.remove("<^ ")
        posibles.remove(">v ")

    if i == 0 and j == n-2:
        posibles.remove(">v ")
        posibles.remove("<^ ")

    if j == 0 and i == n-2:
        posibles.remove(" v>")
        posibles.remove(" ^<")

    if i == n-1:
        posibles.remove(" v ")
        posibles.remove(" ^ ")
        posibles.remove("<^ ")
        posibles.remove(">v ")
        posibles.remove(" ^>")
        posibles.remove(" v<")

    if j == n-1:
        posibles.remove("<<<")
        posibles.remove(">>>")
        posibles.remove(" v>")
        posibles.remove(" ^<")
        posibles.remove(" v<")
        posibles.remove(" ^>")

    if (c == "<v " or c == ">^ ") and j == n-2:
        posibles.remove(" v ")
        posibles.remove(" ^ ")
        posibles.remove("<v ")
        posibles.remove(">^ ")
        posibles.remove(">v ")
        posibles.remove("<^ ")

    if a :
        if a == "<<<" or a == ">>>" or a == "<v " or a == ">^ " or a == " v>" or a == " ^<":
            posibles.remove("<v ")
            posibles.remove(">^ ")
            posibles.remove(" v>")
            posibles.remove(" ^<")
            posibles.remove(" v ")
            posibles.remove(" ^ ")
        else:
            posibles.remove("<^ ")
            posibles.remove(">v ")
            posibles.remove(" ^>")
            posibles.remove(" v<")
            posibles.remove("<<<")
            posibles.remove(">>>")
            if a == " ^>" or a == "<^ " or a == " ^ ":
                posibles.remove(" v ")
                posibles.remove("<v ")
                posibles.remove(" v>")
            else:
                posibles.remove(" ^ ")
                posibles.remove(">^ ")
                posibles.remove(" ^<")

    if b:
        if b == " v " or b == " ^ " or b == "<v " or b == ">^ " or b == "<^ " or b == ">v ":
            posibles.remove("<<<")
            posibles.remove(">>>")
            posibles.remove("<v ")
            posibles.remove(">^ ")
            posibles.remove("<^ ")
            posibles.remove(">v ")
        else:
            posibles.remove(" v ")
            posibles.remove(" ^ ")
            posibles.remove(" ^>")
            posibles.remove(" v<")
            posibles.remove(" v>")
            posibles.remove(" ^<")
            if b == "<<<" or b == " ^<" or b == " v<":
                posibles.remove(">>>")
                posibles.remove(">v ")
                posibles.remove(">^ ")
            else:
                posibles.remove("<<<")
                posibles.remove("<v ")
                posibles.remove("<^ ")

    return posibles

#  vim: set ts=4 sw=4 tw=79 et :
