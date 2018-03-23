# Puede pensarse que una coreografia (sin considerar los sentidos de giro) 
# en un tablero de NxN, es un subgrafo del grafo compuesto por los 
# vertices y aristas del tablero original sin las casillas del borde.

# Esto es, existe una biyeccion entre el conjunto de coreos y
# un subconjunto de todos los subgrafos

####################################################################
# Ejemplo de coreografia valida en un Tablero de 4x4, con su grafo:
#
#  X --> X     X --> X
#  |  *  |     |  *  |
#  X <-- X     X  :  X 
#              |  :  |
#  X --> X --> X  :  X
#  |  *...........*  |
#  X <-- X <-- X <-- X
# 
# Las X y las flechas representan las pulgas el sentido del salto,
# y los asteriscos y puntos, el subgrafo 

# Esto es, existe una funcion biyectiva entre el conjunto de coreos y 
# un subconjunto de todos los subgrafos.


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
    for j in range(n):
        H = G[j*m:(j+1)*m][:h]
        fila = "*"
        for a in H:
            if a == "1":
                fila += "--*"
            else:
                fila += "  *"
        print fila

        V = G[j*m:(j+1)*m][h:v+h]
        fila = ""
        for a in V:
            if a == "1":
                fila += "|  "
            else:
                fila += "   "
        print fila

