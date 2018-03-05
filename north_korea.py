
# coding: utf-8

# Siendo un fanático de la optimización de recursos, Kim Jong Un (líder norcoreano) quiere que sus soldados gasten la menor cantidad de energía en caso de tener que abordar el nuevo barco de combate eléctrico desarrollador por los ingenieros militares.
# 
# El barco tiene forma circular, y varios compartimentos (3 ≤ c ≤ 1000) (salas de máquinas, cocina, sala de control) los cuales pueden albergar diferentes cantidades de soldados.
# 
# Cada compartimento está ubicado sobre el perímetro del barco, o sea, si hay 10 compartimentos, los 10 compartimentos están uno al lado del otro, formando un círculo. En el centro del barco está la central nuclear que provee de electricidad al barco.
# 
# Cada compartimento tiene 3 puertas, una que comunica con el compartimento de la izquierda, otra que comunica con el compartimento de la derecha y la última es una puerta que se comunica con el exterior, para que los soldados aborden el barco.
# 
# La cantidad de soldados (s) que tienen que permanecer en cada compartimento (c) es distinta. Los límites son: (1 ≤ s ≤ 10000000)
# 
# El plan es, cuando suene la alarma indicando que comienza el ataque, se abrirán solo k puertas exteriores (1 ≤ k ≤ 7), los soldasos podrán entrar por las puertas, podrán moverse hacia el compartimento de al lado (solo en sentido horario) hasta llegar a completar la cantidad máxima permitida en el compartimento.
# 
# Kim, no quiere que los soldados se cancen, con lo cual, quiere que colectivamente caminen la menor distancia a medida que van entrando y cambiándose de comparitmento.
# 
# Determinar la distancia total que los soldados tienen que recorrer para subir al barco, al abrir k puertas, y completar cada compartimento (c) con la cantidad de soldados (s) indicada.
# 
# Formato de entrada (archivo adjunto):
# 
# La primera linea contiene los valores de c y k. Cada una de las siguiente líneas representa el valor finel de soldados (s) para cada compartimento.
# 
# Ejemplo:
# 
# 6 2 
# 2 
# 5 
# 4 
# 2 
# 6 
# 2
# 
# Resultado Ejemplo:
# 
# 14
# 
# Se pueden abrir las puertas 2 y 5. 11 soldados entrar en la puerta 2 y caminan una distancia total de 8 para llegar a los compartimentos 2, 3 y 4. 10 Soldados entran por la puerta 5 y caminan una distancia total de 6 para llegar al compartimento 5, 6 y 1.
# 
# Podes encontrar el adjunto en https://s3.amazonaws.com/it.challenge/level12.txt


#  vim: set ts=4 sw=4 tw=79 et :
