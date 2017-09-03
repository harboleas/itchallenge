
def es_capicua(str_num) :
    
    for i in xrange(len(str_num)/2) : 
        if str_num[i] != str_num[-i-1] :
            return False

    return True


def mcd(a, b) :   
    if b == 0 :
        return a
    else :
        return mcd(b, a%b)


def es_primo(n) :      

    if n < 2 :       
        return False         
    for i in xrange(2,n) :          
        if n % i == 0 :        
            return False   

    return True


def lst_primos(n) :    

    return [i for i in xrange(n) if es_primo(i)]


def es_prod_primos(n) :

    a = lst_primos(n)
    for i in xrange(len(a)) :
        for j in xrange(i, len(a)) :
            if n == a[i]*a[j] :
                return True

    return False

