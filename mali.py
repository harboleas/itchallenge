
def base2(n, size):

    return bin(n)[2:].zfill(size)[::-1]


def dibujaGrafo(i, N):
    """Dibuja un grafo que representa un conjunto de coreos"""
    n = N / 2
    h = n-1
    v = n
    tot_e = h*n + v*(n-1)
    G = base2(i, tot_e)
    m = 2*n-1
    for j in range(m-1):
        H = G[j*m:(j+1)*m][:h]
        fila = "*"
        for a in H:
            if a == "1":
                fila += "--*"
            else:
                fila += "  *"
        print fila

        V = G[j*m:(j+1)*m][h:v+1]
        fila = ""
        for a in V:
            if a == "1":
                fila += "|  "
            else:
                fila += "   "
        print fila

