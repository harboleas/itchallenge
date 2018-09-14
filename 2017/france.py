
# coding: utf-8

# Durante la segunda guerra mundial, uno de los bandos quería atacar al otro en un punto clave, para realizarlo transmitía las coordenadas del punto entre sus aliados de la siguiente forma:
# 
# Latitud 3 bytes + 1 byte que correspondía al caracter ascii de la N o de la S
# 
# Longitud 3 bytes + 1 byte que corresponde al caracter ascii de la W o o de la E
# 
# Por ejemplo la coordenadas de la ciudad de La Plata (34°56′00″S 57°57′00″O ) quedarían expresadas de la siguiente forma:
# 
# 34 56 0 83 57 57 0 79 
# 
# A estos bytes tomados de a dos se los encriptaba realizando un xor con una clave de 16 byte que dan como resultado los siguientes bytes:
# 
# 211 125 212 55 127 105 212 60
# 
# Descifrar las coordenadas del punto del ataque sabiendo que unos meses antes habían encriptado con la misma clave las coordenadas de un punto que se encontraba en una de las playas de la isla de "Robben Island" cerca de la ciudad del cabo:
# 
# Coordenadas Encriptadas
# 
# 245 73 214 42 198 111 208 60
# 
# Para evitar inconvenientes de caracteres, las coordenadas deberán ser informadas por medio de los bytes originales sin formatear, por ejemplo las coordenadas de la ciudad de La Plata serían:
# 
# 34 56 0 83 57 57 0 79


#  vim: set ts=4 sw=4 tw=79 et :
