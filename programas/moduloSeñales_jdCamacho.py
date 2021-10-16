# ----------------------------------------------------------------------------------------
# MODULO: Procesamiento de señales
# ----------------------------------------------------------------------------------------
# Descripción: Parcial 2 B. Modulo para procesamiento de señales
# ----------------------------------------------------------------------------------------
# Autor: Juan Diego Camacho
# Version: 1.0
# [16.10.2021]
# ----------------------------------------------------------------------------------------
# IMPORTAR MODULOS

from statistics import mean # para sacar la media de la lista
from math import ceil       # para sacar el entero más cercano por encima del float

# ----------------------------------------------------------------------------------------
# FUNCIÓN: reescalamiento
# ----------------------------------------------------------------------------------------
# Descripcion: función que recibe una señal, su tamaño y un factor de escala, y genere la nueva señal reescalada.
# ----------------------------------------------------------------------------------------
# PARAMETROS & PRE-CONDICIONES
# Se reciben 3 parámetros de entrada
# 1. "señal" de tipo lista
# 2. "tamaño" de tipo entero
# 3. "escala" de tipo entero
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
# Se devuelve una nueva lista con la señal reescalada
# ----------------------------------------------------------------------------------------

def reescalamiento(señal, tamaño, escala): # El tamaño debería calcularlo el programa y no ser un parámetro de entrada
    señal = señal.split(",")
    b = list()
    #tamaño = len(señal)

    for i in señal:
        try:
            b.append(float(i))
        except:
            print('Solo se admiten números')

    señal = [ceil(mean(b[a:a+escala])) for a in range(0, len(b), escala) if len(b[a:a+escala]) == escala] # Forma Pythonica
    return b, señal

    #señal = [b[a:a+escala] for a in range(0, len(b), escala)] Forma vista en clase
    #b.clear()

    # for resc in señal:
    #     if(len(resc) == escala):
    #         b.append(mean(resc))
    #
    # print(b)

# ----------------------------------------------------------------------------------------
# FUNCIÓN: piramide
# ----------------------------------------------------------------------------------------
# Descripcion: función que recibe una señal, su tamaño y un factor de escala, y genere la pirámide de escalas
# de la señal
# ----------------------------------------------------------------------------------------
# PARAMETROS & PRE-CONDICIONES
# Se reciben 3 parámetros de entrada
# 1. "señal" de tipo lista
# 2. "tamaño" de tipo entero
# 3. "escala" de tipo entero
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
# retorna dos variables:
# 1. "señal", la misma variable de entrada solo para ser imprimida junto con el resultado
# 2. "x" el cual posee la lista de listas con los resultados de las medias
# ----------------------------------------------------------------------------------------


def piramide(señal, tamaño, escala): # El tamaño debería calcularlo el programa y no ser un parámetro de entrada
    x = list()

    try:
        escala = int(escala)
    except:
        print('Solo se admiten números')

    while len(reescalamiento(señal, tamaño, escala)[1]) >= 1:
        x.append(reescalamiento(señal, tamaño, escala)[1])
        escala = escala * 2

    return señal, x

# ----------------------------------------------------------------------------------------
# end.
# ------------------------------------------------------------------