# Nos encontramos ante un escenario delicado en producción, donde una de nuestras java RESTFul APIs (crítica para el funcionamiento del site), sufre de inestabilidad aleatoria generando fluctuaciones en su response time por alta CPU. Nuestra área de operaciones nos envió información de diagnóstico de uno de los servers afectados la cual se compone de:
# 
# - top.txt: un top con la información de todos los threads ejecutándose en el server
# - localhost_access_log.txt: el access log de algunos request atendidos por la aplicación
# - thread.tdump: un thread dump de la aplicación
# - memory-dump.bin.gz: un memory dump de la aplicación.
# 
# Podes descargar los archivos de https://s3.amazonaws.com/it.challenge/level1.zip
# 
# Ahora bien, nuestra intuición de developer nos dice que es un request el que está generando el inconveniente y el desafío está en encontrarlo.
# 
# Se solicita la uri del request que está generando la degradación del servicio en nuestra API.

#  vim: set ts=4 sw=4 tw=79 et :
