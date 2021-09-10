# ----------------------------------------------------------------------------------------
# MODULO: Operaciones alternativas
# ----------------------------------------------------------------------------------------
# Descripción: T-08 Funciones y módulos
# ----------------------------------------------------------------------------------------
# Autor: Juan Diego Camacho
# Version: 1.0
# [05.09.2021].
# ----------------------------------------------------------------------------------------
# IMPORTAR MODULOS (un módulo puede importar otros módulos)
# ----------------------------------------------------------------------------------------
# FUNCIÓN: modulo
# ----------------------------------------------------------------------------------------
# Descripcion: Operación que retorna el residuo de una división entera
# ----------------------------------------------------------------------------------------
# PARAMETROS & PRE-CONDICIONES
#
# Las variables de entrada serán dividiendo y divisor
# Las variables de entrada solo pueden ser números reales
#
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
# el valor a retornar será un número real
# ----------------------------------------------------------------------------------------

def modulo(dividiendo, divisor):
    return dividiendo % divisor

# ----------------------------------------------------------------------------------------
# FUNCIÓN: divEntera
# ----------------------------------------------------------------------------------------
# Descripcion: Operación que retorna el cociente de una división entera
# ----------------------------------------------------------------------------------------
# PARAMETROS & PRE-CONDICIONES
#
# Las variables de entrada serán dividiendo y divisor
# Las variables de entrada solo pueden ser números reales
#
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
# el valor a retornar será un número real
# ----------------------------------------------------------------------------------------

def divEntera(dividiendo, divisor):
    return dividiendo / divisor

# ----------------------------------------------------------------------------------------
# FUNCIÓN: multRusa
# ----------------------------------------------------------------------------------------
# Descripcion: Operación que retorna la multiplicación de a*b usando el metodo de la multiplicación
# ----------------------------------------------------------------------------------------
# PARAMETROS & PRE-CONDICIONES
#
# Las variables de entrada serán a y b
# Las variables de entrada solo pueden ser números reales
#
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
# el valor a retornar será un número real
# ----------------------------------------------------------------------------------------

def multRusa(a, b):
    producto = 0
    while a != 0:
        if a%2 != 0:
            producto = producto+b
            b = b*2
            a = a//2
        if a%2 == 0:
            b = b*2
            a = a//2
    return producto


# ----------------------------------------------------------------------------------------
# FUNCIÓN: maxCD
# ----------------------------------------------------------------------------------------
# Descripcion: Operación que retorna el máximo común divisor entre a y b.
# ----------------------------------------------------------------------------------------
# PARAMETROS & PRE-CONDICIONES
#
# Las variables de entrada serán a y b
# Las variables de entrada solo pueden ser números reales
#
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
# el valor a retornar será un número real
# ----------------------------------------------------------------------------------------

def maxCD(a, b):
    if a > b:
        a,b = b,a
    while a%b != 0:
        b, a = a%b, b
    return b

# ----------------------------------------------------------------------------------------
# end.
# ------------------------------------------------------------------