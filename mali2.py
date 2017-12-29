
def contar_coreografias(n):

    coreos = 0

    for i in xrange(4**(n*n)):
        mat = gen_mat(i, n)
        if validar_coreografia(mat, n):
            print mat
            coreos += 1

    return coreos


def gen_mat(val, n):

    saltos = [">", "^", "<", "v"]

    mat = []
    for i in xrange(n):
        mat.append([])
        for j in xrange(n):
            r = val % len(saltos)
            val = val / len(saltos)
            mat[i].append(saltos[r])

    return mat


def validar_coreografia(mat, n):

    for k in xrange(n):
        if mat[0][k] == "^":
            return False
        if mat[n-1][k] == "v":
            return False
        if mat[k][0] == "<":
            return False
        if mat[k][n-1] == ">":
            return False

    for i in xrange(n):
        for j in xrange(n):
            entran = 0

        
            if j+1 < n and mat[i][j+1] == "<":
                entran += 1
                if mat[i][j] == ">":
                    return False

            if i-1 >= 0 and mat[i-1][j] == "v":
                entran += 1
                if mat[i][j] == "^":
                    return False

            if j-1 >= 0 and mat[i][j-1] == ">":
                entran += 1
                if mat[i][j] == "<":
                    return False

            if i+1 < n and mat[i+1][j] == "^":
                entran += 1
                if mat[i][j] == "v":
                    return False

            if entran != 1:
                return False

    return True


#  vim: set ts=4 sw=4 tw=79 et :
