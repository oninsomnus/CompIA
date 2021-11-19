# ----------------------------------------------------------------------------------------
# PROGRAMA: Profundidades de una imagen
# ----------------------------------------------------------------------------------------
# Descripción: 3er parcial compIA: RECORRIDO SOBRE MATRICES – “Profundidades de una Imagen”
# ----------------------------------------------------------------------------------------
# Autor: Juan Diego Camacho
# Version: 2.0
# [19.11.2021]
# ----------------------------------------------------------------------------------------
# IMPORTAR MODULOS
import numpy as np
import random

class b:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# ----------------------------------------------------------------------------------------
# VARIABLES GLOBALES Y PRE-CONDICIONES
# ----------------------------------------------------------------------------------------

print("*** PROFUNDIDADES DE UNA IMAGEN ***")
f = int(input("Cantidad de filas de la matriz:  "))
c = int(input("Cantidad de columnas de la matriz:  "))
x = int(input("Posición inicial en X de la esfera:  "))
y = int(input("Posición inicial en Y de la esfera:  "))

# << aqui una explicación concreta >>

# ----------------------------------------------------------------------------------------
# PARAMETROS
# ----------------------------------------------------------------------------------------
# listar aqui los parámetros

def instanciarMatriz(f, c):
    matriz = np.zeros((f, c)) # se inicializa una matriz de 0s

    for i in range(1, len(matriz)-1):
        for j in range(1, len(matriz[i])-1):
            valor = random.randrange(5, 30) # se cambian los valores dentro de la matriz
            matriz[i][j] = valor            # por un numero al azar entre 5 y 30

    return matriz

def movimientoEsfera(f, c, x, y):

    matr = instanciarMatriz(f, c) # se instancia la matriz con la función anterior
    caminos = list() # lista que se retornará al final de la función
    caminos.append([x, y])  # se inicializa con el primer valor definido por el usuario para la esfera
    tempx, tempy = x, y

    for a in range(3): # se itera 3 veces (pueden ser más veces, no se definió cuantas veces debían ser)
        index = matr[x][y] # se inicializa una variable con la posicion actual para luego evaluarla
        for i in range(x-1, x+2): # se iteran las filas vecinas de la esfera
            for j in range(y-1, y+2): # se iteran las columnas vecinas de la esfera
                if matr[i][j] > index: # se evaluan los vecinos con la variable index
                    index = matr[i][j] # se sobrescribe con el resultado
                    tempx, tempy = i, j # se guardan las coordenadas del resultado

        x,y = tempx, tempy
        if caminos[-1][0] != x or caminos[-1][1] != y: # se evalua que el valor no sea el mismo que el ultimo indice de la lista
            caminos.append([x, y])

    print(b.OKBLUE + "\n Matriz {0}x{1} \n {2} \n".format(f, c, matr) + b.ENDC )
    return caminos

print("Movimientos de la esfera: {} ".format(movimientoEsfera(f,c,x,y)))

# ----------------------------------------------------------------------------------------
# end.
# ----------------------------------------------------------------------------------------