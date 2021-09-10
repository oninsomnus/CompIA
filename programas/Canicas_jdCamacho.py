# ----------------------------------------------------------------------------------------
# PROGRAMA: Canicas
# ----------------------------------------------------------------------------------------
# Descripción: La clasificación se basa únicamente en el diámetro de cada canica, y permite determinar si
# la canica es buena, potencialmente buena o mala para el juego. Una canica es buena si su diámetro es
# múltiplo de 2, 3 y 5 (al mismo tiempo); es potencialmente buena si su diámetro sólo es múltiplo de
# 2, 3 o 5 (sólo de uno o dos de ellos). Una canica se considera mala cuando tiene un diámetro que no
# es múltiplo ni de 2, ni de 3 ni de 5 (es decir, de ninguno).
# ----------------------------------------------------------------------------------------
# Autor: Juan Diego Camacho
# Version: 1.0
# [26.08.2021]
# ----------------------------------------------------------------------------------------
# IMPORTAR MODULOS
class bcolors:
    OKCYAN = '\033[96m'
    ENDC = '\033[0m'
    FAIL = '\033[91m'

# ----------------------------------------------------------------------------------------
# VARIABLES GLOBALES Y PRE-CONDICIONES
# ----------------------------------------------------------------------------------------

# Los valores de entrada deben ser números enteros
# Una variable indicando la cantidad de canicas que se desean evaluar
# En base a esta, el usuario ingresará un valor que corresponda al diámetro de cada una de las canicas

canicas = int(input('\nIngrese el número de canicas que evaluará\nLuego presione Enter\n'))

# Variables enteras para contar la ocurrencias
buena = 0
potencial = 0
mala = 0

# Se podría usar Counter() para un mejor performance

# ----------------------------------------------------------------------------------------
# POSTCONDICIONES
# ----------------------------------------------------------------------------------------

# << aqui una explicación concreta >>

# ----------------------------------------------------------------------------------------
# PARAMETROS
# ----------------------------------------------------------------------------------------
# listar aqui los parámetros

diametros = []
clasificacion = []

# <<Escriba desde aqui el código del programa...>>
if(canicas > 0):
    for i in range(0, canicas):
        Ø = int(input('\nIngrese el diámetro de la canica {}\nLuego presione Enter\n'.format(i+1)))
        diametros.append(Ø)
        if(Ø % 5 == 0 and Ø % 2 == 0 and Ø % 3 == 0):
            clasificacion.append([i+1, "Buena"])
        elif(Ø % 5 == 0 or Ø % 2 == 0 or Ø % 3 == 0):
            clasificacion.append([i+1, "Potencialmente Buena"])
        else:
            clasificacion.append([i+1, "Mala"])

    print(f"{bcolors.OKCYAN}\nCLASIFICACIÓN:{bcolors.ENDC}")

    for x in clasificacion:
        print("Canica {}: {}".format(x[0], x[1]))
        if(x[1] == 'Buena'):
            buena += 1
        elif(x[1] == 'Mala'):
            mala += 1
        else:
            potencial += 1

    print(f"{bcolors.OKCYAN}\nTOTAL:{bcolors.ENDC}")
    print('{} Buenas \n{} Malas y\n{} Potencialmente buenas.'.format(buena, mala, potencial))
else:
    print(f"{bcolors.FAIL}Debe ingresar un número mayor a 0{bcolors.ENDC}")


# ----------------------------------------------------------------------------------------
# end.
# ----------------------------------------------------------------------------------------