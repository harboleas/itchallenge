
base_3 = [0,1,-1]

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

    if A[0][0] == A[1][0] :
        return True

    if A[0][-1] == A[1][-1] :
        return True

    if A[-1][0] == A[-2][0] :
        return True

    if A[-1][-1] == A[-2][-1] :
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


def gen_num_no_malo_A(filas, cols) :

    a = 0

    aux = []
    while a < 3**(filas*cols) :
        A = gen_mat(a, base_3, filas, cols)       
        if not mat_A_mala(A) :
            aux.append(a)
        a += 1

    return aux

def gen_num_no_malo_B(filas, cols) :

    b = 0

    aux = []
    while b < 3**(filas*cols) :
        B = gen_mat(b, base_3, filas, cols)       
        if not mat_B_mala(B) :
            aux.append(b)
        b += 1

    return aux


def contar_coreo(filas,cols) :
    
    cant = 0

    num_a = gen_num_no_malo_A(filas, cols-1)
    num_b = gen_num_no_malo_B(filas-1, cols)

#    aux1 = []

    for a in num_a :
        A = gen_mat(a, base_3, filas, cols-1)       
        for b in num_b :
            B = gen_mat(b, base_3, filas-1, cols)
#            print a, b, cant
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
#                aux1.append((a,b))
                cant += 1
                break

    return cant#, aux1

def show_coreo(a,b,n) :

    d_a = ["   ", " > ", " < "]
    d_b = ["   ", " ^ ", " v "]

    A = gen_mat(a, base_3, n, n-1)
    B = gen_mat(b, base_3, n-1, n)
 
    print A
    print B

    for i in xrange(n-1) :
        fila1 = ""
        fila2 = ""
        for j in xrange(n-1) :
            fila1 += " " + d_a[A[i][j]]
            fila2 += d_b[B[i][j]] + " "
        j += 1
        fila2 += d_b[B[i][j]]
        print fila1
        print fila2
    i += 1
    fila1 = ""
    for j in xrange(n-1) :
        fila1 += " " + d_a[A[i][j]]
    print fila1 

        

