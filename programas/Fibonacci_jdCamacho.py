# ----------------------------------------------------------------------------------------
# PROGRAMA: Serie Fibonacci
# ----------------------------------------------------------------------------------------
# Descripción: Determinar una secuencia Fibonacci en base a un número de entrada
# ----------------------------------------------------------------------------------------
# Autor: Juan Diego Camacho
# Version: 1.0
# [17.08.2021]
# ----------------------------------------------------------------------------------------
# IMPORTAR MODULOS

# ----------------------------------------------------------------------------------------
# VARIABLES GLOBALES Y PRE-CONDICIONES
# ----------------------------------------------------------------------------------------

a = input('\nIngrese la cantidad de números que desee visualizar\nLuego presione Enter\n')
b, c = 0, 1
secuencia = []

try:
    a = int(a)
except:
    print('Debe ingresar un número entero')

# ----------------------------------------------------------------------------------------
# POSTCONDICIONES
# ----------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------
# PARAMETROS
# ----------------------------------------------------------------------------------------
# listar aqui los parámetros

for i in range(1, a):
    secuencia.append(b)
    d = b + c
    b = c
    c = d

print(*secuencia)

# ----------------------------------------------------------------------------------------
# end.
# ----------------------------------------------------------------------------------------