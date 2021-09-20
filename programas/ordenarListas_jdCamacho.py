# ----------------------------------------------------------------------------------------
# PROGRAMA: T-09 Ordenar Listas
# ----------------------------------------------------------------------------------------
# Descripción: Programa principal del modulo metodosOrdenamiento
# ejecución de las funciones definidas en el modulo mencionado
# ----------------------------------------------------------------------------------------
# Autor: Juan Diego Camacho
# Version: 1.0
# [19.09.2020]
# ----------------------------------------------------------------------------------------
# IMPORTAR MODULOS
import metodosOrdenamiento_jdCamacho as orden

# ----------------------------------------------------------------------------------------
# VARIABLES GLOBALES Y PRE-CONDICIONES
# ----------------------------------------------------------------------------------------

# la variable de entrada al ejecutar el programa principal sera de tipo string
# las variables de entrada para las funciones deberán ser de tipo lista
# las funciones solo aceptan listas con valores de tipo numerico
# la variable "opciones" nos indica las posibles opciones para el usuario

opciones = ["1", "2", "3"]

# ----------------------------------------------------------------------------------------
# POSTCONDICIONES
# ----------------------------------------------------------------------------------------

# la variable de salida de las funciones será de tipo lista
# la variable "run" definirá la finalización del programa
run = ""

# ----------------------------------------------------------------------------------------
# PARAMETROS
# ----------------------------------------------------------------------------------------
# el parametro de las funciones deberá ser la lista que indique el usuario
#

while run != "salir":
    metodo = input("Indique el número del método de ordenamiento a ejecutar:"
                   "\n1. Burbuja"
                   "\n2. Selección"
                   "\n3. Inserción"
                   "\nDe lo contrario escriba 'salir'\n")

    if "salir" not in metodo and metodo in opciones:
        entrada = False
        while not entrada:
            entrada = orden.inputUser(input("Indique el listado de números que desea ordenar\n"))
            x = entrada.copy()

        if metodo == "1":
            orden.burbuja(x)
        elif metodo == "2":
            orden.seleccion(x)
        elif metodo == "3":
            orden.insercion(x)
        print("Lista original: {}\nLista ordenada: {}".format(entrada, x))
    elif "salir" in metodo:
        run = metodo
    else:
        print("Debe indicar una opción correcta")



# ----------------------------------------------------------------------------------------
# end.
# ---------------------------------------------------------------------------------------