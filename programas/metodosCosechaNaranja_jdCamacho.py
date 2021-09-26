# ----------------------------------------------------------------------------------------
# MODULO: Métodos Cosecha de Naranjas
# ----------------------------------------------------------------------------------------
# Descripción: T-10 Métodos Cosecha de Naranjas
# ----------------------------------------------------------------------------------------
# Autor: Juan Diego Camacho
# Version: 1.0
# [26.09.2021]
# ----------------------------------------------------------------------------------------
# IMPORTAR MODULOS
from random import sample
# ----------------------------------------------------------------------------------------
# FUNCIÓN: main
# ----------------------------------------------------------------------------------------
# Descripcion: Inicializa todas las variables a consultar
# ----------------------------------------------------------------------------------------
# PARAMETROS & PRE-CONDICIONES
# Debe existir la variable n que indica la cantidad de parcelas a crear
# La variable n la ingresa el usuario y debe ser un número
# La precondición para la variable n es la siguiente: 1 <= n <= 50
# Si el parametro coop no se llena se vuelve a instanciar la variable coop
# La variable coop contiene todos los datos de todas las parcelas
# La variable coop se instancia de forma aleatoria
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
# Se instanciaran todas las variables a consultar
# ----------------------------------------------------------------------------------------

def main(n, coop = None):
    if coop == None:
        coop = sample(range(1000), n * 2)

    produccion = [0, 0] # indice 1: naranjas para jugo, indice 2: naranjas para comer
    parcela = [] # producción total por parcela
    sinprodflag = False

    for i in range(len(coop)):
        if i % 2 == 0: # si es un numero par la parcela es de jugo
            # print(i,"jugo")
            produccion[0] += coop[i]
            parcela.append(coop[i] + coop[i + 1])
            if (coop[i] + coop[i + 1]) == 0 and sinprodflag != True:
                sinprod, sinprodflag = int(i / 2), True
            elif (coop[i] + coop[i + 1]) > 0 and sinprodflag != True:
                sinprod = -1
        else: # si no es un numero par la parcela es de comer
            # print(i, "comer")
            produccion[1] += coop[i]

    return coop, parcela, produccion, sinprod

# ----------------------------------------------------------------------------------------
# FUNCIÓN: delete
# ----------------------------------------------------------------------------------------
# Descripcion: Elimina 1 parcela según el indice indicado
# ----------------------------------------------------------------------------------------
# PARAMETROS & PRE-CONDICIONES
# La función delete recibe la variable indice de entrada
# Esta variable debe ser el número que representa la parcela a eliminar
# La precondición para la variable indice es la siguiente: 1 <= indice <= parcela
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
# Se modificará la variable coop instanciada en main()
# ----------------------------------------------------------------------------------------

def delete(coop, indice = ''):
    for i in range(len(coop)):
        if i % 2 == 0:
            numparcela = (int(i / 2) + 1)
            if indice != '' and numparcela == indice:
                deleting = 1
                while deleting < 3:
                    coop.pop(i)
                    deleting += 1


# ----------------------------------------------------------------------------------------
# FUNCIÓN: evaluar variable de entrada
# ----------------------------------------------------------------------------------------
# Descripcion: evalua el número de entrada
# ----------------------------------------------------------------------------------------
# PARAMETROS & PRE-CONDICIONES
# recibe una variable de entrada (entrada) de tipo string y devuelve un número
# evalua que el valor de entrada sea valido
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
# ----------------------------------------------------------------------------------------
def inputUser(entrada, tipo = None, n = None):
    try:
        entrada = int(entrada)
        if (entrada > 50 or entrada <= 0) and tipo == None:
            print('Solo se admiten números entre 1 y 50')
        elif tipo != None and entrada > n:
            print('La cosecha no posee esta parcela, indicar una parcela valida')
        else:
            return entrada
    except:
        print('Solo se permiten números')

# ----------------------------------------------------------------------------------------
# end.
# ------------------------------------------------------------------