# ----------------------------------------------------------------------------------------
# PROGRAMA: Problema de los 3 marineros
# ----------------------------------------------------------------------------------------
# Descripción: Escribir un algoritmo que determine cuantas monedas había al inicio de la historia
#              y cuanto recibió cada uno de los marineros
# ----------------------------------------------------------------------------------------
# Autor: Juan Diego Camacho
# Version: 2.0
# [21.08.2021]
# ----------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------
# VARIABLES GLOBALES Y PRE-CONDICIONES
# ----------------------------------------------------------------------------------------

# << aqui una explicación concreta >>

# ----------------------------------------------------------------------------------------
# POSTCONDICIONES
# ----------------------------------------------------------------------------------------

# << aqui una explicación concreta >>

# ----------------------------------------------------------------------------------------
# PARAMETROS
# ----------------------------------------------------------------------------------------
# listar aqui los parámetros

# <<Escriba desde aqui el código del programa...>>
i = 200
while(i < 301):
    mar1 = i // 3
    mar2 = (i - mar1 - 1) // 3
    mar3 = (i - (mar2 + mar1) - 1) // 3
    sobrante = ((i - mar1 - mar2 - mar3 - 3) // 3) - 1

    if(i % 3 == 1):
        if((i - mar1 - 1) % 3 == 1):
            if((i - mar1 - mar2 - 2) % 3 == 1):
                if((i - mar1 - mar2 - mar3 - 3) % 3 == 1):
                    print("Al principio habían: ", i, " monedas")
                    print("El marinero 1 recibió: ", mar1 + sobrante, " monedas")
                    print("El marinero 2 recibió: ", mar2 + sobrante, " monedas")
                    print("El marinero 3 recibió: ", mar3 + sobrante, " monedas")
    i += 1


# ----------------------------------------------------------------------------------------
# end.
# ----------------------------------------------------------------------------------------