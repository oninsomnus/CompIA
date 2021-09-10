# ----------------------------------------------------------------------------------------
# PROGRAMA: Ejecutar Funciones
# ----------------------------------------------------------------------------------------
# Descripción: Ejecutar las funciones del modulo operacionesAlternativas
# ----------------------------------------------------------------------------------------
# Autor: Juan Diego Camacho
# Version: 1.0
# [05.09.2021]
# ----------------------------------------------------------------------------------------
# IMPORTAR MODULOS

import operacionesAlternativas_jdCamacho as opal

# ----------------------------------------------------------------------------------------
# VARIABLES GLOBALES Y PRE-CONDICIONES
# ----------------------------------------------------------------------------------------

# Las variables de entradas serán a y b
# Las variables a y b deben ser números reales

a = int(input('Ingresar el primer número '))
b = int(input('Ingresar el segundo número '))

# ----------------------------------------------------------------------------------------
# POSTCONDICIONES
# ----------------------------------------------------------------------------------------

# Los valores de retorno corresponden a los valores de salida del modulo operacionesAlternativas

# ----------------------------------------------------------------------------------------
# PARAMETROS.
# ----------------------------------------------------------------------------------------
# listar aqui los parámetros

# <<Escriba desde aqui el código del programa...>>

modulo = opal.modulo(a, b)

divEntera = opal.divEntera(a, b)

maxCD = opal.maxCD(a, b)

multRusa = opal.multRusa(a, b)

print('modulo: {}\ndivEntera: {}\nmaxCD: {}\nmultRusa: {}\n'.format(modulo,divEntera,maxCD,multRusa))


# ----------------------------------------------------------------------------------------
# end.
# ----------------------------------------------------------------------------------------