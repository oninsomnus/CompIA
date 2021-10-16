# ----------------------------------------------------------------------------------------
# PROGRAMA: ejecutarSeñales
# ----------------------------------------------------------------------------------------
# Descripción: ejecuta el modulo Señales
# ----------------------------------------------------------------------------------------
# Autor: Juan Diego Camacho
# Version: 1.0
# [16.10.2021]
# ----------------------------------------------------------------------------------------
# IMPORTAR MODULOS
import moduloSeñales_jdCamacho as señales

# ----------------------------------------------------------------------------------------
# VARIABLES GLOBALES Y PRE-CONDICIONES
# ----------------------------------------------------------------------------------------

# Se solicita la señal en string para luego convertirla a una lista de enteros
señal = input("*** REESCALAMIENTO DE SEÑALES ***\nIngresa los valores de las señales separados por ',' \n")
# Se solicita el tamaño en string para luego convertirlo a un entero
tamaño = input("Ingresa el tamaño de la señal \n")
# Se solicita el factor de escala en string para luego convertirlo a un entero
escala = input("Ingresa el factor de escala deseado para reescalar la señal \n")

# ----------------------------------------------------------------------------------------
# POSTCONDICIONES
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# PARAMETROS
# ----------------------------------------------------------------------------------------

reescala = señales.piramide(señal, tamaño, escala)
print("*** PIRÁMIDE DE ESCALAS ***")
print("Señal original: ", reescala[0])
for i in range(0, len(reescala[1])):
    print("Señal en escala {}: {}".format(i+1, reescala[1][i]))


# ----------------------------------------------------------------------------------------
# end.
# ---------------------------------------------------------------------------------------