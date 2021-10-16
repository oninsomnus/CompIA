# ----------------------------------------------------------------------------------------
# PROGRAMA: Jugar dados
# ----------------------------------------------------------------------------------------
# Descripción: Ejecutar dados
# ----------------------------------------------------------------------------------------
# Autor: Juan Diego Camacho
# Version: 1.0
# [14.10.2021]
# ----------------------------------------------------------------------------------------
# IMPORTAR MODULOS
import clasesDados_jdCamacho as cl_dados # Modulo para las clases de dados

# ----------------------------------------------------------------------------------------
# VARIABLES GLOBALES Y PRE-CONDICIONES
# ----------------------------------------------------------------------------------------

carasparadados = [4, 6, 8]

# ----------------------------------------------------------------------------------------
# POSTCONDICIONES
# ----------------------------------------------------------------------------------------

# << aqui una explicación concreta >>

# ----------------------------------------------------------------------------------------
# PARAMETROS
# ----------------------------------------------------------------------------------------
# listar aqui los parámetros

# <<Escriba desde aqui el código del programa...>>
dados = input("Escoge la cantidad de caras de tus dados: 4, 6 u 8 \nEscribe los dos valores separando con espacios: \n")
b = list()
dados = dados.split(" ")
for i in dados:
    i = int(i)
    if i not in carasparadados:
        print("Los dados deben ser de 4, 6 u 8 caras")
        exit()
    elif len(dados) != 2:
        print("Solo se puede jugar con 2 dados")
        exit()
    b.append(i)

juegodados = cl_dados.Juego(b[0], b[1])
print(juegodados)


# ----------------------------------------------------------------------------------------
# end.
# ---------------------------------------------------------------------------------------