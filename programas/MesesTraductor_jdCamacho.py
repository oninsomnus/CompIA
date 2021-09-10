# ----------------------------------------------------------------------------------------
# PROGRAMA: Traducción de meses
# ----------------------------------------------------------------------------------------
# Descripción: Usando diccionarios haga un programa que reciba un string con el nombre de
# cualquiera de los meses del año en español e imprima por pantalla su traducción
# en inglés y cualquier otro idioma que usted seleccione (francés, portugués,
# alemán). Por facilidad use solo nombres en minúsculas.
# ----------------------------------------------------------------------------------------
# Autor: Juan Diego Camacho
# Version: 1.0
# [21.08.2021]
# ----------------------------------------------------------------------------------------
# IMPORTAR MODULOS

# ----------------------------------------------------------------------------------------
# VARIABLES GLOBALES Y PRE-CONDICIONES
# ----------------------------------------------------------------------------------------

# diccionario con los meses en diferentes idiomas

meses = {
    "lang": ["inglés", "portugués", "francés", "alemán"],
    "enero": ["january", "janeiro", "janvier", "januar"],
    "febrero": ["february", "fevereiro", "février", "februar"],
    "marzo": ["march", "março", "mars", "märz"],
    "abril": ["april", "abril", "avril", "april"],
    "mayo": ["may", "maio", "peut", "mai"],
    "junio": ["june", "junho", "juin", "juni"],
    "julio": ["july", "julho", "juillet", "juli"],
    "agosto": ["august", "agosto", "août", "august"],
    "septiembre": ["september", "setembro", "septembre", "september"],
    "octubre": ["october", "outubro", "octobre", "oktober"],
    "noviembre": ["november", "novembro", "novembre", "november"],
    "diciembre": ["december", "dezembro", "décembre", "dezember"]
}

fr = ['Francés', 'francés', 'frances', 'fr', 'Frances']                  #
pt = ['Portugés', 'portugés', 'portugues', 'pr', 'por', 'Portugues']     # listas para evaluar el input del usuario
de = ['Alemán', 'alemán', 'de', 'al', 'aleman', 'Aleman']                #

#variable 'mes' de entrada en string
#variable 'idioma' de entrada en string


# ----------------------------------------------------------------------------------------
# POSTCONDICIONES
# ----------------------------------------------------------------------------------------

# << aqui una explicación concreta >>

# ----------------------------------------------------------------------------------------
# PARAMETROS
# ----------------------------------------------------------------------------------------
# listar aqui los parámetros

# <<Escriba desde aqui el código del programa...>>

def transl():
    mes = input('\nIngrese el mes que desea traducir en minúsculas\nLuego presione Enter\n')

    if mes in meses.keys():
        idioma = input('\nIngrese el idioma al que desea traducir: Francés | Portugués | Alemán\nLuego presione Enter\n')
        if idioma in fr:
            print('{} en {}: {} y en {}: {}'.format(mes, meses["lang"][0], meses[mes][0], meses["lang"][2], meses[mes][2]))
        elif idioma in pt:
            print('{} en {}: {} y en {}: {}'.format(mes, meses["lang"][0], meses[mes][0], meses["lang"][1], meses[mes][1]))
        elif idioma in de:
            print('{} en {}: {} y en {}: {}'.format(mes, meses["lang"][0], meses[mes][0], meses["lang"][3], meses[mes][3]))
        else:
            print('Debe ingresar un idioma válido')

    else:
        print('Debe ingresar un mes válido')

while True:
    transl()

# ----------------------------------------------------------------------------------------
# end.
# ----------------------------------------------------------------------------------------