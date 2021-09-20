# ----------------------------------------------------------------------------------------
# MODULO: T-09 Funciones de ordenamiento
# ----------------------------------------------------------------------------------------
# Descripción: Realice un programa para ordenar los elementos de una lista de longitud N usando tres métodos
# diferentes (método Burbuja, método de Selección y método Inserción).
# ----------------------------------------------------------------------------------------
# Autor: Juan Diego Camacho
# Version: 1.0
# [19.09.2021]
# ----------------------------------------------------------------------------------------
# IMPORTAR MODULOS (un módulo puede importar otros módulos)

# No hay modulos para importar

# ----------------------------------------------------------------------------------------
# FUNCIÓN: método de burbuja
# ----------------------------------------------------------------------------------------
# Descripcion: Se itera sobre la lista, se comparan los elementos en pares y se intercambian
# ----------------------------------------------------------------------------------------
# PARAMETROS & PRE-CONDICIONES
# La variable de entrada debe ser una lista
# Los valores de la lista deben ser números reales para poderlos comparar
# El parámetro de entrada sera la variable x
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
# La variable de salida será una lista ordenada
# ----------------------------------------------------------------------------------------

def burbuja(x):
    cambiar = True
    iteraciones = len(x)-1
    while iteraciones > 0 and cambiar:
        cambiar = False
        for i in range(iteraciones):
            if x[i] > x[i+1]:
                x[i], x[i+1] = x[i+1], x[i]
                cambiar = True
        iteraciones -= 1
    return x

# ----------------------------------------------------------------------------------------
# FUNCIÓN: método de selección
# ----------------------------------------------------------------------------------------
# Descripcion: este método segmenta la lista en dos partes: ordenada y no ordenada
# un lado de la lista sera la parte ordenada y el otro lado la parte no ordenada
# el valor mayor se coloca en la posición correspondiente en la medida en la que va leyendo cada elemento
# ----------------------------------------------------------------------------------------
# PARAMETROS & PRE-CONDICIONES
# La variable de entrada debe ser una lista
# Los valores de la lista deben ser números reales para poderlos comparar
# El parámetro de entrada sera la variable x
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
# La variable de salida será una lista ordenada
# ----------------------------------------------------------------------------------------

def seleccion(x):
    for i in range(len(x)):
        menor = i
        for j in range(i+1, len(x)):
            if x[j] < x[menor]:
                menor = j
        x[i], x[menor] = x[menor], x[i]
    return x

# ----------------------------------------------------------------------------------------
# FUNCIÓN: método de inserción
# ----------------------------------------------------------------------------------------
# Descripcion: este método segmenta la lista en dos partes: ordenada y no ordenada
# un lado de la lista sera la parte ordenada y el otro lado la parte no ordenada
# se mueven elementos mayores continuamente en la parte ordenada hasta encontrar un número menor
# ----------------------------------------------------------------------------------------
# PARAMETROS & PRE-CONDICIONES
# La variable de entrada debe ser una lista
# Los valores de la lista deben ser números reales para poderlos comparar
# El parámetro de entrada sera la variable x
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
# La variable de salida será una lista ordenada
# ----------------------------------------------------------------------------------------

def insercion(x):
    for i in range(1, len(x)):
        insertar = x[i]
        j = i - 1

        while j >= 0 and x[j] > insertar:
            x[j + 1] = x[j]
            j -= 1
        x[j + 1] = insertar
    return x

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

    if ' ' in entrada:
        entrada = entrada.replace(' ', '')
    if (len(entrada) != 4):
        print("Por favor ingresa 4 números")
        return False
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