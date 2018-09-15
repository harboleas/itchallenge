# coding: utf-8
#ESPAÑOL 
#La Escuela de Idiomas y Ciencias enseña cinco materias: Física, Química, Matemáticas, Botánica y Zoología. Cada estudiante es experto en una materia. Las habilidades de los alumnos se describen mediante una string de las habilidades citadas que consta de las letras p, c, m, b y z solamente. Cada carácter describe la habilidad de un estudiante de la siguiente manera:
#p → Física.
#c →  Química.
#m → Matemáticas.
#b → Botánica.
#z  → Zoología.
# 
#Tu tarea es determinar el número total de diferentes equipos que satisfacen las siguientes restricciones:
# 
#Un equipo consiste en un grupo de exactamente cinco estudiantes.
#Cada estudiante es experto en una materia diferente.
#Un estudiante puede estar solo en un equipo.
# 
#Por ejemplo, si la cadena de habilidades es pcmbzpcmbz, entonces hay dos equipos posibles que se pueden formar a la vez: habilidades [0-4] y habilidades [5-9]. No es importante determinar las permutaciones, ya que siempre estaremos limitados a dos equipos con 10 estudiantes.
# 
#Se le proporciona un archivo con la entrada https://www.dropbox.com/s/3neyzkiomsb7eh8/Copia%20de%20input013.txt?dl=0
# 
#Restricciones 
#5 ≤ n ≤ 5 × 105
#skills[i] ∈ {p,c,m,b,z}
# 
#Sample Input 0 pcmbz
# Sample Output 0 1

f = open("cadena_italy.txt")
cadena = f.read()
f.close()

def contar_equi(cadena):

    p = cadena.count("p")
    c = cadena.count("c")
    m = cadena.count("m")
    b = cadena.count("b")
    z = cadena.count("z")

    return min(p,c,m,b,z)

