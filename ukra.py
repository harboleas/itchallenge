import base64

with open("level8") as f:
    lineas = f.readlines()

def decrypt(key):

    txt = ""
    for line in lineas:
        c = base64.b64decode(line)
        k = key
        p = ""

        for i in xrange(len(c)):
            p += chr((ord(c[i]) - ord(k[i]) - i) % 256)
            k += p[i]

        txt += p  # linea descifrada

    return txt

