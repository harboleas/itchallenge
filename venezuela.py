ESPERA_SUBIR = 0
ESPERA_BAJAR = 1

def contar_trazos(pared):

    alt_max = max(pared)

    trazos = 0
    for altura_maq in range(alt_max):
        estado = ESPERA_SUBIR
        for altura in pared :
            if estado == ESPERA_SUBIR:
                if altura >= altura_maq:
                    estado = ESPERA_BAJAR
            elif estado == ESPERA_BAJAR:
                if altura < altura_maq:
                    trazos += 1
                    estado = ESPERA_BAJAR
        if estado == ESPERA_BAJAR:
            trazos += 1

    return trazos
