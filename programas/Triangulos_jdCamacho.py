# ----------------------------------------------------------------------------------------
# PROGRAMA: Determinar triángulos
# ----------------------------------------------------------------------------------------
# Descripción: Determinar el tipo de triángulo dado tres segmentos
# ----------------------------------------------------------------------------------------
# Autor: Juan Diego Camacho
# Version: 1.0
# [17.08.2021]
# ----------------------------------------------------------------------------------------
# IMPORTAR MODULOS

# ----------------------------------------------------------------------------------------
# VARIABLES GLOBALES Y PRE-CONDICIONES
# ----------------------------------------------------------------------------------------

variables = input('\nIngrese los segmentos a, b y c separados por espacios\nLuego presione Enter\n')

variables = variables.split()

try:
    a = int(variables[0])
    b = int(variables[1])
    c = int(variables[2])
except:
    print('Los segmentos deben ser números reales')

# ----------------------------------------------------------------------------------------
# POSTCONDICIONES
# ----------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------
# PARAMETROS
# ----------------------------------------------------------------------------------------
# listar aqui los parámetros

if a+b >= c and b+c >= a and c+a >= b:
    if a == b == c:
        print('El triángulo es equilátero')
    elif a == b or b == c or a == c:
        print('El triángulo es isósceles')
    else:
        print('El triángulo es escaleno')
else:
    print('Con los valores dados no se puede construir un triángulo')

# ----------------------------------------------------------------------------------------
# end.
# ----------------------------------------------------------------------------------------