# Submarinos
# 
# Entre los días 02/10/84 y 04/10/84 se capturaron mensajes emitidos por varios submarinos. Diversos informes indican la actividad de las siguientes naves: REDOCTOBER y NAUTILUS.
# 
# Esta clase de submarino tiene el siguente comportamiento regular, una vez por día se cambian las claves secretas de cifrado, de las cuales no hay información. Respecto al algoritmo de cifrado, por diversos estudios se sabe que es un cifrador de flujo, pero se desconocen los detalles especificos.
# 
# Como parte del comportamiento, se conoce la forma de algunos mensajes que regularmente son enviados por la flota:
# 
# El formato es el siguiente:
# 
# <nombre del submarino> <fecha compacta> <mensaje> FIN
# Tambien se conoce que es normal comenzar algunos mensajes con la palabra NOVEDAD,
# 
# por ejemplo, para NAUTILUS en el día 02/10/84, el formato es:
# 
# NAUTILUS 021084 NOVEDAD <sigue desconocido> FIN
# Cual es la ubicación de REDOCTOBER ?
# 
# Datos
# 
# Encontraras en el adjunto mensajes.tar.gz los mensajes capturados.
# 
# Nota
# 
# Expresar la latitud logitud como fue notificada por REDOCTOBER:
# 
# <latitud> <longitud>
# 
# Podes encontrar el adjunto en https://s3.amazonaws.com/it.challenge/level9.tar.gz

#  vim: set ts=4 sw=4 tw=79 et :
