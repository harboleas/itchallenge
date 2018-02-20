# Se tiene un molde (con forma de tablero de 3x3 vacío) y 10 unidades de distintos ingredientes (3 Dulces, 3 Frutas, 3 Confites, 1 Masita), para hacer un pastel.
# 
# Se considera que un pastel de 9 ingredientes es rico cuando tres mismos ingredientes están alineados vertical u horizontalmente en el molde. La Masita es especial, puede alinearse con cualquier ingrediente.
# 
# Calcula la cantidad máxima de pasteles ricos distintos que pueden realizarse. 

ingre = ["D", "F", "C", "M"]

def postre_valido(postre_vect):

    vect = "".join(postre_vect)

    if vect.count("M") > 1:
        return False
    for i in ingre[:-1]:
        if vect.count(i) > 3:
            return False

    return True

def fil_col_rica(fil_col):

    p = fil_col[0]
    if p == "M":
        if fil_col[1] == fil_col[2]:
            return True
        else:
            return False
    else:
        for i in fil_col[1:]:
            if i != "M" and i != p:
                return False
        return True


def postre_rico(postre):

    for i in xrange(3):
        res = fil_col_rica(postre[i])
        if res:
            return True

    for j in xrange(3):
        col = [postre[0][j], postre[1][j], postre[2][j]]
        res = fil_col_rica(col)
        if res:
            return True

    return False

def simetrico_h(post):

    if post[0] == post[2]:
        return True
    else:
        return False


def simetrico_v(post):

    a = [post[0][0], post[1][0], post[2][0]]
    b = [post[0][2], post[1][2], post[2][2]]

    if a == b:
        return True
    else:
        return False


def cuenta_postres():

    cant = 0
    sim_v = 0
    sim_h = 0

    for i in xrange(4**9):
        post = num_base(i, ingre, 9)
        if not postre_valido(post):
            continue
        postre = arma_matriz(post, 3, 3)
        if postre_rico(postre):
            cant += 1
            if simetrico_h(postre):
                sim_h += 1
            if simetrico_v(postre):
                sim_v += 1

    return cant, sim_h, sim_v

#  vim: set ts=4 sw=4 tw=79 et :
