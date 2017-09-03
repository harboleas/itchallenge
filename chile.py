def busca_dup(texto) :
    
    n = len(texto)
    mitad = n / 2
    for lon in xrange(mitad) :
        for pos in xrange(n-2*lon) :
            s = texto[pos:pos+lon]
            if s in texto[pos+lon:] :
                print s
                break

