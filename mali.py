
base_3 = [-1,0,1]

def num_base(num, base, size) :
    aux = []
    n = len(base)
    for i in xrange(size) :
        aux.append(base[num%n])
        num = num / n
    return aux

def arma_matriz(vect, filas, cols) :
    return [vect[i*cols:(i+1)*cols] for i in xrange(filas)]

def gen_mat(num, base, filas, cols) :
    
    vect = num_base(num, base, filas*cols)
    return arma_matriz(vect, filas, cols)

def test_ij(A, B, i, j, filas, cols) :

    cant_no_0 = 0
    a = A[i][j-1] if j != 0 else 0 
    b = A[i][j] if j < cols-1 else 0
    c = B[i][j] if i < filas-1 else 0
    d = B[i-1][j] if i != 0 else 0

    if a :
        cant_no_0 += 1
    if b :
        cant_no_0 += 1
    if c :
        cant_no_0 += 1
    if d :
        cant_no_0 += 1
    
    if cant_no_0 != 2 :
        return False

    if a-b+c-d == 0 :
        return True
    else :
        return False

def mat_A_mala(A) :
    # Descarta las que no pueden ser

    if A[0][0] == 0 :
        return True

    if A[0][-1] == 0 :
        return True

    if A[-1][0] == 0 :
        return True

    if A[-1][-1] == 0 :
        return True

    for fila in A :
        for i in xrange(len(fila)-1) :
            if fila[i]*fila[i+1] < 0 :
                return True
    return False

def trasp(mat) :

    aux = []
    cols = len(mat[0])
    for j in xrange(cols) :
        aux.append([fila[j] for fila in mat])
    return aux

def mat_B_mala(B) :
    # Descarta las que no pueden ser

    aux = trasp(B)
    return mat_A_mala(aux)


def contar_coreo(filas,cols) :
    
    cant = 0

    a = 0
    b = 0
    while a < 3**(filas*(cols-1)) :
        A = gen_mat(a, base_3, filas, cols-1)       
        a += 1
        if mat_A_mala(A) :
            continue
        b = 0
        while b < 3**((filas-1)*cols) :
            B = gen_mat(b, base_3, filas-1, cols)
            b += 1
            if mat_B_mala(B) :
                continue
            print a, b
            saltar = False
            for i in xrange(filas) :
                for j in xrange(cols) :
                    res = test_ij(A, B, i, j, filas, cols)
                    if not res :
                        saltar = True
                        break
                if saltar :
                    break
            if not saltar :
                cant += 1
                break
    return cant


