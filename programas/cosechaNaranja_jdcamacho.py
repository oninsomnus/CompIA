# ----------------------------------------------------------------------------------------
# PROGRAMA: Cosecha de naranjas
# ----------------------------------------------------------------------------------------
# Descripción: Ejecución de metodos para la consulta de consechas de naranja
# ----------------------------------------------------------------------------------------
# Autor: Juan Diego Camacho
# Version: 1.0
# [26.09.2021]
# ----------------------------------------------------------------------------------------
# IMPORTAR MODULOS
import metodosCosechaNaranja_jdCamacho as nrj

# ----------------------------------------------------------------------------------------
# VARIABLES GLOBALES Y PRE-CONDICIONES
# La variable n se inicializa con el valor False para poder evaluar si el dato esta bien o no al inicio del programa
# En caso de que este bien:
# Se solicita la variable n al usuario para inicializar la función principal
# En caso de que este mal:
# Se vuelve a solicitar el dato
# La variable n ebe ser un número entre 1 y 50
# La variable "opciones" nos indica las posibles opciones para el usuario durante la ejecución
# Esta se evalua para validar si la opción indicada es correcta o no
# ----------------------------------------------------------------------------------------
opciones = ["1", "2", "3", "4", "5"]
n = False

# ----------------------------------------------------------------------------------------
# POSTCONDICIONES
# ----------------------------------------------------------------------------------------
# la variable de salida de las funciones será de tipo lista para produccion, coop y parcelas
# la variable de salida sinprod será un número que indica el número de parcela
# la variable "run" definirá la finalización del programa
run = ""
# ----------------------------------------------------------------------------------------
# PARAMETROS
# ----------------------------------------------------------------------------------------
# Los parámetros para las funciones serán la variable n y la variable indice en caso
# de que el usuario quiera eliminar alguna parcela

while run != "salir":
    while not n:
        n = nrj.inputUser(input('Bienvenidx a tu cosechas de naranjas\nIngrese la cantidad de parcelas que desea:\n'))
    metodo = input("¿Qué desea realizar? Indique un número:"
                   "\n1. Consultar Producción por tipo"
                   "\n2. Consultar Producción por parcela"
                   "\n3. Consultar Número de parcela sin producción"
                   "\n4. Consultar Todos los datos"
                   "\n5. Eliminar una parcela"
                   "\nDe lo contrario escriba 'salir'\n")
    if "salir" not in metodo and metodo in opciones:
        try:
            coop
        except NameError:
            coop, parcela, produccion, sinprod = nrj.main(n)
        if metodo == "1":
            print(produccion)
        elif metodo == "2":
            print(parcela)
        elif metodo == "3":
            print(sinprod)
        elif metodo == "4":
            print("Producción por tipo: {}\nProducción por parcela: {}\nParcela sin producción: {}\nToda la producción: {}\n"
                  .format(produccion, parcela, sinprod, coop))
        elif metodo == "5":
            indice = nrj.inputUser(input("Indique el número de la parcela a eliminar\n"), "delete", n)
            nrj.delete(coop, indice)
            coop, parcela, produccion, sinprod = nrj.main(3, coop)
            print('Se ha eliminado la parcela {} correctamente'.format(indice))
    elif "salir" in metodo:
        run = metodo
    else:
        print("Debe indicar una opción correcta")


# ----------------------------------------------------------------------------------------
# end.
# ---------------------------------------------------------------------------------------