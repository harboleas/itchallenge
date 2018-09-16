
f = open("secreto.pdf")
datos = f.read()
f.close()

def aplicar_xor(datos, num):

    aux = [ord(x)^num for x in datos]

    return "".join([chr(x) for x in aux])


out = aplicar_xor(datos, 137)

f = open("secreto_resuelto.pdf", "w")
f.write(out)
f.close()


