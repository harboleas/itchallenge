def busca_dup(texto):

    n = len(texto)
    mitad = n / 2
    i = 0
    for lon in xrange(mitad):
        for pos in xrange(i, n-2*lon):
            s = texto[pos:pos+lon]
            if s in texto[pos+lon:]:
                print s
                i = pos
                break

