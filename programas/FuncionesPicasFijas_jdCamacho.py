# ----------------------------------------------------------------------------------------
# MODULO: Funciones de Picas y Fijas
# ----------------------------------------------------------------------------------------
# Descripción: Funciones para el juego de Picas y Fijas
# ----------------------------------------------------------------------------------------
# Autor: Juan Diego Camacho
# Version: 1.0
# [09.09.2021]
# ----------------------------------------------------------------------------------------
# IMPORTAR MODULOS (un módulo puede importar otros módulos)

from random import sample


# ----------------------------------------------------------------------------------------
# FUNCIÓN: a. random secret
# ----------------------------------------------------------------------------------------
# Descripcion: Generar el número secreto de forma aleatoria
# ----------------------------------------------------------------------------------------
# PARAMETROS & PRE-CONDICIONES
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
# ----------------------------------------------------------------------------------------

def secret():
    s = sample(range(9), 4)
    return s


# ----------------------------------------------------------------------------------------
# FUNCIÓN: c. fijas
# ----------------------------------------------------------------------------------------
# Descripcion: retorna la cantidad de fijas
# ----------------------------------------------------------------------------------------
# PARAMETROS & PRE-CONDICIONES
# recibe dos variables de entrada (a y b) de tipo lista
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
# ----------------------------------------------------------------------------------------

def fijas(secret, jugada):
    f = []

    for i in range(len(secret)):
        if secret[i] == jugada[i]:
            f.append(True)
        else:
            f.append(False)

    return f


# ----------------------------------------------------------------------------------------
# FUNCIÓN: picas
# ----------------------------------------------------------------------------------------
# Descripcion: retorna la cantidad de picas
# ----------------------------------------------------------------------------------------
# PARAMETROS & PRE-CONDICIONES
# recibe dos variables de entrada (a y b) de tipo lista
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
# ----------------------------------------------------------------------------------------
def picas(secret, jugada):
    f = []

    for i in range(len(secret)):
        for j in range(len(jugada)):
            if secret[i] == jugada[j]:
                f.append(True)

    return f


# ----------------------------------------------------------------------------------------
# FUNCIÓN: evaluar variable de entrada
# ----------------------------------------------------------------------------------------
# Descripcion: evalua el número de entrada y lo retorna como una lista
# ----------------------------------------------------------------------------------------
# PARAMETROS & PRE-CONDICIONES
# recibe una variable de entrada (entrada) de tipo string
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
# ----------------------------------------------------------------------------------------
def inputUser(entrada):
    b = []

    if (len(entrada) != 4):
        print("Por favor ingresa 4 números")
        return
    else:
        entrada = [char for char in entrada]
        try:
            for i in entrada:
                b.append(int(i))
            return b
        except:
            print('Solo se admiten números')
# ----------------------------------------------------------------------------------------
# end.
# ------------------------------------------------------------------
