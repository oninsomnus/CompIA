# ----------------------------------------------------------------------------------------
# PROGRAMA: Jugar Picas Fijas
# ----------------------------------------------------------------------------------------
# Descripción: Ejecutar las funciones del modulo FuncionesPicasFijas
# ----------------------------------------------------------------------------------------
# Autor: Juan Diego Camacho
# Version: 1.0
# [09.09.2021]
# ----------------------------------------------------------------------------------------
# IMPORTAR MODULOS
import FuncionesPicasFijas_jdCamacho as juego

# ----------------------------------------------------------------------------------------
# VARIABLES GLOBALES Y PRE-CONDICIONES
# ----------------------------------------------------------------------------------------

#entrada = input("Bienvenido al juego Picas y Fijas!\nPor favor ingresa un número\n")

#entrada = juego.inputUser(entrada)

entrada = juego.inputUser(input("Bienvenido al juego Picas y Fijas!\nPor favor ingresa un número\n"))

secret = juego.secret()

# ----------------------------------------------------------------------------------------
# POSTCONDICIONES
# ----------------------------------------------------------------------------------------

# << aqui una explicación concreta >>

# ----------------------------------------------------------------------------------------
# PARAMETROS
# ----------------------------------------------------------------------------------------
# listar aqui los parámetros

fijas = juego.fijas(secret, entrada)
picas = juego.picas(secret, entrada)

while fijas.count(True) != 4:
    print("Fijas: {}\nPicas: {}".format(fijas.count(True), picas.count(True)))
    entrada = juego.inputUser(input("Debes adivinar las 4 fijas\nVuelve a intentarlo\n"))
    fijas = juego.fijas(secret, entrada)
    picas = juego.picas(secret, entrada)

print("Felicitaciones! Adivinaste el número secreto: {}".format(''.join(map(str, secret))))

# ----------------------------------------------------------------------------------------
# end.
# ----------------------------------------------------------------------------------------