
s1 = 'YETYHHEPRRVFSJZDFZWRSFHTVSJPJBIKYKNHDGFHBCGOFEPQAUMUASUUFCAAUJMHKLUFHDKNAASIEOFAFEUMUMAUUFCIMUAXCNKQKYEZPYNEPORMDAZCXWNCJADAASEBAEEARPASDNFAITQERUPSSXZRWJJIYGEASDFEASEGADCDEVCZAPWQPNUHNASIUGAOIPHNASDVMREERWTYRWGASDFJAKAWEMRMTMTIUJAWEQZDFJYOFYUWQQAZDNMLKDFDGAEROSFGAAFSRWVXRSACZFRFAQWESDCAQEZXADCXEQFZCA'

s2 = 'SZXCVBZEJJJDBCGOFUMMMQQQAUUFCECGSERIMSAHUFHDKNDSAAIEOFUMMMSAQRFDAFEZSUULLLFCIUEYMUOWCNKQKQZPYNEPORMDZECCXWNCSBAIPWQSVNAEEYGWQEEWQFTTSRUSDFGIQQOIURYOPCMWASPVTYVNEOIARYRKOIYTGHJPQPJIEKWPQEYQNCZBGLKRMH\xc3\x91AJPSOIHKQPDLFIREMHJADMNRGNOAINEOHHAPOWNFHIUHKBNJLTPPTOVBNMHKADJOJMUYONMHLKOPPMBJUIIJKHMYOOMMJJMNKJLL'

def to_bin(num, size) :
    a = bin(num)
    n = len(a[2:])
    return "0"*(size-n) + a[2:]

info1 = "".join([to_bin(ord(i),8) for i in s1])
info2 = "".join([to_bin(ord(i),8) for i in s2])

def busca_msg(n, s1, s2) :
    # n es la cantidad de letras
    pos = []
    for d in xrange(1,len(s1)/n) :
        for i in xrange(len(s1)-n*d) :
            p_msg1 = s1[i:i+n*d:d]
            for j in xrange(len(s2)-n*d) :
                p_msg2 = s2[j:j+n*d:d]
                if p_msg1 == p_msg2 :
                    pos.append((p_msg1, i, p_msg2, j, d))

    return pos

def busca_msg2(n, info1, info2) :
    # n es la cantidad de letras
    pos = []
    for i in xrange(len(info1)-n) :
        p_msg1 = info1[i:i+n]
        for j in xrange(len(info2)-n) :
            p_msg2 = info2[j:j+n]
            if p_msg1 == p_msg2 :
                pos.append((p_msg1, i, p_msg2, j))
                return pos
    return pos

