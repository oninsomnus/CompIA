# ----------------------------------------------------------------------------------------
# PROGRAMA: Granizada
# ----------------------------------------------------------------------------------------
# Descripción: Breve y detallada descripción del problema en: https://www.youtube.com/watch?v=094y1Z2wpJg
# ----------------------------------------------------------------------------------------
# Autor: Juan Diego Camacho
# Version: 1.0
# [26.08.2021]
# ----------------------------------------------------------------------------------------
# IMPORTAR MODULOS

# clase para colorear titulos
class bcolors:
    HEADER = '\033[95m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

# ----------------------------------------------------------------------------------------
# VARIABLES GLOBALES Y PRE-CONDICIONES
# ----------------------------------------------------------------------------------------

# El valor de entrada debe ser un número entero
n = int(input('\nIngrese el número de entrada\nLuego presione Enter\n'))

# ----------------------------------------------------------------------------------------
# POSTCONDICIONES
# ----------------------------------------------------------------------------------------

# << aqui una explicación concreta >>

# ----------------------------------------------------------------------------------------
# PARAMETROS
# ----------------------------------------------------------------------------------------
# listar aqui los parámetros

# <<Escriba desde aqui el código del programa...>>

if(n <= 1):
    print(f"{bcolors.FAIL}Debe ingresar un número mayor a 1{bcolors.ENDC}")
else:
    i = 0
    granizada = []
    while(n > 0):
        granizada.append(n)
        i += 1
        if(n % 2 == 0):
            n = int(n / 2)
            #print(n)
        elif(n == 1):
            break
        else:
            n = int((3 * n) + 1)
            #print(n)

    #print('La granizada de {} es: {} \nLa longitud es: {}\nEl valor máximo es: {}'.format(granizada[0], ' '.join(map(str, granizada)), i, max(granizada)))
    print('\n{}La granizada de {} es: {} {}'.format(bcolors.HEADER,granizada[0],bcolors.ENDC,' '.join(map(str, granizada))))
    print('{}La longitud es:{} {}'.format(bcolors.HEADER, bcolors.ENDC,i))
    print('{}El valor máximo es:{} {}'.format(bcolors.HEADER, bcolors.ENDC, max(granizada)))


# ----------------------------------------------------------------------------------------
# end.
# ----------------------------------------------------------------------------------------