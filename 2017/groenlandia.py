
# coding: utf-8

# En las profundidades de la infraestructura de Mercado Libre estan pasando cosas extrañas. La gente del infraestructura no quiere revisar el rack 42B, dicen que apareció un antiguo server color terracota, que nunca nadie habia visto.
# 
# Despues de llamar a los cientificos de guardía (nosotros. obvio.) descrubrimos que desde ese server se estan creando imagenes en un viejo directorio compartido por NFS, que tampoco estaba ayer. Cada vez mas raro.
# 
# Estudiamos esas imagenes durante semanas y descubrimos que se tratan de algun tipo de programa.
# 
# Si ejecutamos program_1() tenemos como resultado el numero 42.
# Si ejecutamos program_2() no parece tener ningun output, pero sospechamos que modifica su estado interno.
# si ejecutamos program_3() tenemos como resultado el numero 3
# si ejecutamos program_4(42) tenemos como resultado el numero 42
# si ejecutamos program_5(4) tenemos como resultado el numero 0
# si ejecutamos program_6(14,23) tenemos como resultado el numero 25
# si ejecutamos program_7(8,2) tenemos como resultado el numero 2
# 
# Cual es el resultado siguiente programa ?
# 
# followthewhiterabit(0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 
#  0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 
#  0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 
#  1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 
#  1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 
#  1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1)
# 
# Adjunto:
# https://s3.amazonaws.com/it.challenge/level24.tar.gz


#  vim: set ts=4 sw=4 tw=79 et :
