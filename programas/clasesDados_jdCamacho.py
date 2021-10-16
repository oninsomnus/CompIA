# ----------------------------------------------------------------------------------------
# MODULO: Dados de diferente número de caras
# ----------------------------------------------------------------------------------------
# Descripción: Parcial2 A. Se desea crear un programa que permita simular el lanzamiento de un par de Dados
# ----------------------------------------------------------------------------------------
# Autor: Juan Diego Camacho
# Version: 1.0
# [14.10.2021]
# ----------------------------------------------------------------------------------------
# IMPORTAR MODULOS (un módulo puede importar otros módulos)

import random

# ----------------------------------------------------------------------------------------
# CLASE: Caras
# ----------------------------------------------------------------------------------------
# Descripcion: definición de la superclase Cara
# ----------------------------------------------------------------------------------------
# PARAMETROS & PRE-CONDICIONES
# como parámetros de entrada recibirá el número de cara a generar
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
# ----------------------------------------------------------------------------------------

class Cara:
    def __init__(self, nCara):
        self.nCara = nCara
        simbolos = ["©", "*", "•"]
        random.shuffle(simbolos)
        self.simbolo = random.choice(simbolos)

    def imprimirCara(self):
        return self.simbolo, self.nCara + 1


# ----------------------------------------------------------------------------------------
# CLASE: Dado
# ----------------------------------------------------------------------------------------
# Descripcion: definición de la subclase Dado
# ----------------------------------------------------------------------------------------
# PARAMETROS & PRE-CONDICIONES
# como parámetros de entrada recibirá el número de caras a generar
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
# ----------------------------------------------------------------------------------------

class Dado(Cara):
    def __init__(self, nCaras):
        self.nCaras = int(nCaras)
        self.crearCaras()

    def crearCaras(self):
        x = list()
        for i in range(self.nCaras):
            x.append(Cara(i))
        self.Caras = x

    def getCaras(self):
        return self.Caras

# ----------------------------------------------------------------------------------------
# CLASE: Juego
# ----------------------------------------------------------------------------------------
# Descripcion: definición de la subclase Juego
# ----------------------------------------------------------------------------------------
# PARAMETROS & PRE-CONDICIONES
# como parámetros de entrada recibirá el número de caras de los 2 dados
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
# ----------------------------------------------------------------------------------------

class Juego(Dado):
    def __init__(self, dado1, dado2):
        self.nDados = [dado1, dado2]
        self.crearDados()
        self.lanzarDados()

    def crearDados(self):
        x = list()
        for i in self.nDados:
            x.append(Dado(i))
        self.Dados = x

    def lanzarDados(self):
        a = list()
        juego = list()
        for i in self.Dados:
            for j in i.getCaras():
                a.append(j.imprimirCara())

            juego.append(random.choice(a))
        self.juego = juego

    def __str__(self):
        a = list()
        b = list()
        for i in range(self.juego[1][1]):
            a.append(self.juego[1][0])
        a = "".join(a)
        for i in range(self.juego[0][1]):
            b.append(self.juego[0][0])
        a = "".join(a)
        b = "".join(b)
        return b + " " + a

# ----------------------------------------------------------------------------------------
# end.
# ------------------------------------------------------------------