# ----------------------------------------------------------------------------------------
# PROGRAMA: T-09 Jugar Picas Fijas
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

entrada = juego.inputUser(input("Bienvenido al juego Picas y Fijas!\nPor favor ingresa 4 números\n"))

while entrada == False:
    entrada = juego.inputUser(input())

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
jugadas = 1

while fijas.count(True) != 4:
    print("Fijas: {}\nPicas: {}".format(fijas.count(True), picas.count(True)))
    entrada = juego.inputUser(input("Debes adivinar las 4 fijas\nVuelve a intentarlo\n"))
    fijas = juego.fijas(secret, entrada)
    picas = juego.picas(secret, entrada)
    jugadas += 1

print("Felicitaciones! Adivinaste el número secreto: {} en {} intentos".format(''.join(map(str, secret)), jugadas))

# ----------------------------------------------------------------------------------------
# end.
# ----------------------------------------------------------------------------------------