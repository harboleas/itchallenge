
# coding: utf-8

# El granjero Mariano, tiene una cabra que está todo el tiempo entrando en su granero y comiendo las frutas que tiene apiladas en la cocina.
# 
# La cantidad de frutas es infinita... tiene dos pilas de frutas, una de naranjas y otra de bananas.
# 
# La cabra no puede comer infinito, tiene una capacidad limitada.
# 
# Cada vez que come una naranja, completa su capacidad según las proteínas de la naranja, cada vez que come una banana lo mismo, completa su capacidad según las proteínas de la banana.
# 
# La cabra aprendió un truco, cuando toma agua, baja el nivel de su capacidad a la mitad. Esto quiere decir que viene comiendo naranjas y bananas, si las naranjas la llenan con 3 proteínas y las bananas la llenan en 4 proteínas, si comió 3 naranjas y 3 bananas, tendrá un nivel de llenado de 21. Si toma agua en ese momento, baja ese nivel a la mitad (redondeando para abajo) o sea a 10 y puede seguir comiendo.
# 
# La cabra solo puede tomar 1 vez agua. La cabra quiere comer lo máximo posible sin pasarse de su capacidad.
# 
# Determinar cuál es el máximo nivel de llenado que puede tener la cabra.
# 
# Ejemplo:
# 
# Capacidad: 8 proteínas 
# Naranjas incrementan: 5 proteínas 
# Bananas incrementan: 6 proteínas
# 
# Resultado: 8 (come naranja, toma agua, come banana)
# 
# Resolver para:
# 
# Capacidad: 25185 proteínas 
# Naranjas incrementan: 109 proteínas 
# Bananas incrementan: 17188 proteínas


# Sean :
# x la cantidad de naranjas antes de tomar agua
# y idem anterior pero para las bananas
# u la cantidad de naranjas despues de tomar agua
# v idem para las bananas
# N proteinas naranjas
# B proteinas Bananas
# C capacidad

# Luego x,y,u,v deben satisfacer la siguiente condicion
# (x*N + y*B) / 2 + u*N + v*B <= C

# cotas superiores para x, y, u, v
# x <= C * 2 / N
# y <= C * 2 / B
# u <= C / N
# v <= C / B

def calcula_max():

    C = 25185
    N = 109
    B = 17188

    max_x = C * 2 / N
    max_y = C * 2 / B
    max_u = C / N
    max_v = C / B

    maximo = 0

    for x in range(max_x):
        for y in range(max_y):
            for u in range(max_u):
                for v in range(max_v):
                    llenado = (x*N + y*B)/2 + u*N + v*B
                    if llenado <= C:
                        if llenado > maximo:
                            maximo = llenado

    return maximo

#  vim: set ts=4 sw=4 tw=79 et :
