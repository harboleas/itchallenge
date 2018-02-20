# Recientementre el instituto SETI ha detectado una mensaje proveniente de espacio profundo que parece ser producto de una civilización extraterrestre. Aunque por el momento no han logrado entender qué es lo que significa, el mismo se repite todos los días en un momento al azar. La detección del mismo ha sido una tarea ardua, debido a que, producto de los rayos cósmicos, el mensaje tiene ruido agregado, por lo que tuvieron que distinguir el mensaje original del ruido cósmico.
# 
# SETI se encuentran super emocionados con las posibilidades que ofrece éste descubrimiento pero antes de darlo a conocer al público en general, decidieron validar su descubrimiento con los participantes de la vieja SETI@home. Para ésto han entregado la información de señales de varios días diferentes en las que ellos aseguran haber detectado el mensaje alienígena. También aseguran que el mensaje se está transmitiendo todos los días y que se debería poder reconocer si se posee la información de al menos 2 señales con ruido.
# 
# A continuación están las señales de 2 días y el objetivo es encontrar cuál es el mensaje que se repite día a día, descubierto por los científicos de SETI.
# 
# Señal 1: YETYHHEPRRVFSJZDFZWRSFHTVSJPJBIKYKNHDGFHBCGOFEPQAUMUASUUFCAAUJMHKLUFHDKNAASIEOFAFEUMUMAUUFCIMUAXCNKQKYEZPYNEPORMDAZCXWNCJADAASEBAEEARPASDNFAITQERUPSSXZRWJJIYGEASDFEASEGADCDEVCZAPWQPNUHNASIUGAOIPHNASDVMREERWTYRWGASDFJAKAWEMRMTMTIUJAWEQZDFJYOFYUWQQAZDNMLKDFDGAEROSFGAAFSRWVXRSACZFRFAQWESDCAQEZXADCXEQFZCA
# 
# Señal 2: JUASZXCVBZEJJJDBCGOFUMMMQQQAUUFCECGSERIMSAHUFHDKNDSAAIEOFUMMMSAQRFDAFEZSUULLLFCIUEYMUOWCNKQKQZPYNEPORMDZECCXWNCSBAIPWQSVNAEEYGWQEEWQFTTSRUSDFGIQQOIURYOPCMWASPVTYVNEOIARYRKOIYTGHJPQPJIEKWPQEYQNCZBGLKRMHÑAJPSOIHKQPDLFIREMHJADMNRGNOAINEOHHAPOWNFHIUHKBNJLTPPTOVBNMHKADJOJMUYONMHLKOPPMBJUIIJKHMYOOMMJJMNKJLL

s1 = 'YETYHHEPRRVFSJZDFZWRSFHTVSJPJBIKYKNHDGFHBCGOFEPQAUMUASUUFCAAUJMHKLUFHDKNAASIEOFAFEUMUMAUUFCIMUAXCNKQKYEZPYNEPORMDAZCXWNCJADAASEBAEEARPASDNFAITQERUPSSXZRWJJIYGEASDFEASEGADCDEVCZAPWQPNUHNASIUGAOIPHNASDVMREERWTYRWGASDFJAKAWEMRMTMTIUJAWEQZDFJYOFYUWQQAZDNMLKDFDGAEROSFGAAFSRWVXRSACZFRFAQWESDCAQEZXADCXEQFZCA'

s2 = 'SZXCVBZEJJJDBCGOFUMMMQQQAUUFCECGSERIMSAHUFHDKNDSAAIEOFUMMMSAQRFDAFEZSUULLLFCIUEYMUOWCNKQKQZPYNEPORMDZECCXWNCSBAIPWQSVNAEEYGWQEEWQFTTSRUSDFGIQQOIURYOPCMWASPVTYVNEOIARYRKOIYTGHJPQPJIEKWPQEYQNCZBGLKRMH\xc3\x91AJPSOIHKQPDLFIREMHJADMNRGNOAINEOHHAPOWNFHIUHKBNJLTPPTOVBNMHKADJOJMUYONMHLKOPPMBJUIIJKHMYOOMMJJMNKJLL'

import numpy as np

a = np.fromstring(s1, dtype=np.int8)
b = np.fromstring(s2, dtype=np.int8)


#  vim: set ts=4 sw=4 tw=79 et :
