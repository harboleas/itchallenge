# Dentro del equipo de IT de Meli ha surgido una banda de nivel internacional, "Mondiola Rock", para la cual surgen contínuamente solicitudes de presentación alrededor del mundo.
# 
# Se han identificado todas las cuidades que solicitan una presentación de la banda y se ha encontrado que la ganancia a obtener en cada ciudad guarda una relación lineal con la población de la cuidad.
# 
# El manager de la banda quiere hacer una gira mundial y para ello desea armar un plan de que maximice la ganancia total a ser obtenida.
# 
# Se sabe que para calcular la ganancia hay que sumar los ingresos por los recitales y restar los costos de traslado de la banda, los equipos y el numeroso contingente de soporte.
# 
# El equipo de IT siempre deseoso de ayudar con este tipo de desafíos ha armado un algoritmo de calculo que puede indicar que ciudades visitar y en que orden para lograr la máxima ganancia.
# 
# Para ello se ha preparado una tabla de datos que contiene en cada renglón una ciudad que ha pedido la presentación de la banda, y en cada uno de estos renglones se tiene: el codigo de la cuidad, su latitud y longitud sobre la esfera terrestre, la poblacion de la ciudad y los códigos de las otras cuidades con las cuales está conectada.
# 
# Se sabe que la ganancia en la ciudad se puede calcular facilmente como 9 pesos por habitante. Además se sabe que el costo de traslado entre 2 ciudades se puede calcular como la cantidad de kilometros entre las 2 ciudades por 2500 pesos/kilómetro.
# 
# Para calcular la distancia entre dos ciudades se supone que los viajes serán en linea recta sobre la superficie de la tierra suponiéndola una esfera perfecta de 6371 km de rádio.
# 
# Por último se sabe que solo se pueden hacer recorridos por las rutas establecidas, pudiendo pasar por conexiones donde la banda no de recital. Por ejemplo si hay una ruta de A a B y otra ruta de B a C. La banda puede viajar desde A, pasando por B para llegar a C. Por mas que no se detenga en B a dar un recital.
# 
# Ademas de la restricción anterior en cuanto a las rutas, el manager ha estabecido otra restricción que tiene que ver con la imágen de la banda. Donde no se permite que se de un recital donde se recaude menos que en alguno previo. Obligando de esta forma que la recaudación en cada recital sea una secuencia estrictamente creciente.
# 
# La gira puede ser iniciada en cualquier ciudad, pasando por las rutas y ciudades intermedias que se desee, dando recitales en cada una de las ciudades que cumplan las restricciones y terminando en la ciudad que se desee.
# 
# Se solicita como resultado obtener la ganancia máxima que pueda ser obtenida, seleccionando cuidadosamente las ciudades y rutas.
# 
# Como input se debe utilizar el archivo adjunto. Donde en la primer linea se tiene un número que indica la cantidad de ciudades, seguido de la recaudación a ser obtenida por cada habitante de la ciudad, seguido por el costo del kilometro de transporte. Las siguientes lineas tendrán cada una de las ciudades con el codigo de la ciudad, latitud, longitud, poblacion, y las ciudades con las cuales existe una ruta.
# 
# Para el correcto cálculo del resultado, apenas se obtenga el largo de una ruta, este debe ser redondeado a kilómetros.
# 
# Podes encontrar el adjunto en https://s3.amazonaws.com/it.challenge/level18.txt

#  vim: set ts=4 sw=4 tw=79 et :
