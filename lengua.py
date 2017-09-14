
prg = """52*>: :000p1>\:00g-#v _ v
  v 2-1*2p00 :+1g00\<   $
  > **00g1+/^v,*84      <
  _^#<`  9:+1>#,.#+5<   @"""

prg2 = prg.split("\n")

class Pila(list):
    def pop(self):
        if not self:
           return 0
        else:
           return super(Pila, self).pop()

pila = Pila()

pc = [0,0]
modo = "normal"
dir_x = 1
dir_y = 0

def exe(c, prg):

    global modo, dir_x, dir_y

    if modo == "normal":
        if str(0) <= c <= str(9):
            pila.append(int(c))

        elif c in "+*":
            a = pila.pop()
            b = pila.pop()
            exec("res = "+str(a)+c+str(b))
            pila.append(res)

        elif c == "-":
            a = pila.pop()
            b = pila.pop()
            pila.append(b-a)

        elif c in "/%":
            a = pila.pop()
            b = pila.pop()
            if a == 0:
                res = input("Que resultado desea ? ")
            else:
                exec("res = "+str(b)+c+str(a))
            pila.append(res)

        elif c == "!":
            a = pila.pop()
            if a:
                pila.append(0)
            else:
                pila.append(1)

        elif c == "`":
            a = pila.pop()
            b = pila.pop()
            pila.append(1 if b>a else 0)

        elif c == ">":
            dir_x = 1
            dir_y = 0

        elif c == "<":
            dir_x = -1
            dir_y = 0

        elif c == "^":
            dir_x = 0
            dir_y = -1

        elif c == "v":
            dir_x = 0
            dir_y = 1

        elif c == "?":
            dir_y,dir_x = random.choice([(0,1),(0,-1),(1,0),(-1,0)])

        elif c == "#":
            pc[1] += 2*dir_x
            pc[0] += 2*dir_y
            return

        elif c == "_":
            a = pila.pop()
            dir_y = 0
            if a == 0:
                dir_x = 1
            else:
                dir_x = -1
        elif c == "|":
            a = pila.pop()
            dir_x = 0
            if a == 0:
                dir_y = 1
            else:
                dir_y = -1
        elif c == '"':
            modo = "cadena"

        elif c == ":":
            a = pila.pop()
            pila.append(a)
            pila.append(a)
        elif c == "\\":
            a = pila.pop()
            b = pila.pop()
            pila.append(a)
            pila.append(b)
        elif c == "$":
            pila.pop()
        elif c == ".":
            print pila.pop(),
        elif c == ",":
            print chr(pila.pop()),

        elif c == "p":
            y = pila.pop()
            x = pila.pop()
            v = pila.pop()
            prg[x][y] = chr(v)
        elif c == "g":
            y = pila.pop()
            x = pila.pop()
            pila.append(ord(prg[y][x]))

    elif modo == "cadena":
        if c == '"':
            modo = "normal"
        else:
            pila.append(ord(c))

    pc[1] += dir_x
    pc[0] += dir_y


def correr(prog):
    prg = [[i for i in fila] for fila in prog]
    c = 0
    while c != "@":
        c = prg[pc[0]][pc[1]]
#        print c
#        print pc
#        raw_input()
        exe(c, prg)
#        print pila
#        for fila in prg:
#            print "".join(fila)

