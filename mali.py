llamadas = [0]

def contar_coreos(n, k=0, tablero=None):
    """Cuenta las coreografias de las pulgas
       generandolas de forma recursiva"""

    llamadas[0] += 1

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

    # posibles = ["-: ", "_: ", " :_", " :-", "---", " | "]

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

    posibles = list_(["-: ", "_: ", " :_", " :-", "---", " | "])

    if i == 0:
        posibles.remove(" | ")
        posibles.remove("_: ")
        posibles.remove(" :_")

    if j == 0:
        posibles.remove("---")
        posibles.remove("_: ")
        posibles.remove("-: ")

    if i == 0 and j == n-2:
        posibles.remove("-: ")

    if j == 0 and i == n-2:
        posibles.remove(" :_")

    if i == n-1:
        posibles.remove(" | ")
        posibles.remove("-: ")
        posibles.remove(" :-")

    if j == n-1:
        posibles.remove("---")
        posibles.remove(" :_")
        posibles.remove(" :-")

    if c == "_: " and j == n-2:
        posibles.remove(" | ")
        posibles.remove("_: ")
        posibles.remove("-: ")

    if a :
        if a == "---" or a == "_: " or a == " :_":
            posibles.remove("_: ")
            posibles.remove(" :_")
            posibles.remove(" | ")
        else:
            posibles.remove("-: ")
            posibles.remove(" :-")
            posibles.remove("---")

    if b:
        if b == " | " or b == "_: " or b == "-: ":
            posibles.remove("---")
            posibles.remove("_: ")
            posibles.remove("-: ")
        else:
            posibles.remove(" | ")
            posibles.remove(" :-")
            posibles.remove(" :_")

    return posibles

#  vim: set ts=4 sw=4 tw=79 et :
