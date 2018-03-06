
# coding: utf-8

# Se tiene un molde (con forma de tablero de 3x3 vacío) y 10 unidades de distintos ingredientes (3 Dulces, 3 Frutas, 3 Confites, 1 Masita), para hacer un pastel.
# 
# Se considera que un pastel de 9 ingredientes es rico cuando tres mismos ingredientes están alineados vertical u horizontalmente en el molde. La Masita es especial, puede alinearse con cualquier ingrediente.
# 
# Calcula la cantidad máxima de pasteles ricos distintos que pueden realizarse. 

ingre = {"D": 3, "F": 3, "C": 3, "M": 1}

postre = [[None]*3 for i in range(3)]

def cuenta_postres(n, ingre):
    """Genera de forma recursiva todos los postres posibles y 
       cuenta los ricos"""

    if n == 9:
#        print "Postre"
#        for fila in postre:
#            print fila
        if postre_rico():
            return 1
        else:
            return 0

    else:
        contador = 0
        for k, v in ingre.items():
            if v:
                i = n / 3
                j = n % 3
                postre[i][j] = k
                ingre_aux = ingre.copy()
                ingre_aux[k] -= 1
                contador += cuenta_postres(n+1, ingre_aux)

        return contador


def postre_rico():

    for fila in postre:
        if "M" not in fila:
            if fila == [fila[0]]*3:
                return True
        else:
            i = fila.index("M")
            if fila[i-1] == fila[i-2]:
                return True

    # trasponer
    postre_t = [[None]*3 for i in range(3)]
    for i in range(3):
        for j in range(3):
            postre_t[j][i] = postre[i][j]

    for fila in postre_t:
        if "M" not in fila:
            if fila == [fila[0]]*3:
                return True
        else:
            i = fila.index("M")
            if fila[i-1] == fila[i-2]:
                return True

    return False


#  vim: set ts=4 sw=4 tw=79 et :
