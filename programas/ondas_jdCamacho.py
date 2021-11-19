# ----------------------------------------------------------------------------------------
# PROGRAMA: Ondas
# ----------------------------------------------------------------------------------------
# Descripción: Funciones para la representación de ondas cuadradas, triangulas y de diente de sierra
# ----------------------------------------------------------------------------------------
# Autor: Juan Diego Camacho
# Version: 1.0
# [06.11.2021]
# ----------------------------------------------------------------------------------------
# IMPORTAR MODULOS
import matplotlib.pyplot as plt
import numpy as np

# ----------------------------------------------------------------------------------------
# VARIABLES GLOBALES Y PRE-CONDICIONES
# ----------------------------------------------------------------------------------------

fig, axs = plt.subplots(3)              # variables utilizadas para la presentación de matplot
w = np.linspace(0.0, 2*4*np.pi, 1000)   # array de la variable independiente
n = 0                                   # variable para la inicialización de los ciclos

# ----------------------------------------------------------------------------------------
# POSTCONDICIONES
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# PARAMETROS
# ----------------------------------------------------------------------------------------
# listar aqui los parámetros


def cuadrada(w,n):
    an = 1 / (2 * n + 1)
    f = an * np.sin((2*n+1)*w)
    return f

def triangular(w,n):
    an = (-1)**n / (2*n+1)**2
    f = an * np.sin((2*n+1)*w)
    return f

def diente(w,n):
    an = ((-1) ** n+1) / n
    f = an * np.sin(n*w)
    return f

def viz_cuadrada(n, n_total):
    senX = 0
    while n < n_total:
        if n % 2 != 0 and n > 1:
            senX += cuadrada(w, n)
        elif n % 2 == 0:
            senX += np.sin(w)
        n += 1

    axs[0].plot(w, senX, '.')

def viz_triangular(n, n_total):
    senX = 0
    while n < n_total:
        if n % 2 != 0 and n > 1:
            senX += triangular(w, n)
        elif n % 2 == 0:
            senX += np.sin(w)
        n += 1

    axs[1].plot(w, senX, '.')

def viz_diente(n, n_total):
    senX = 0
    while n < n_total:
        if n < 1:
            senX += np.sin(w)
        elif n >= 1:
            senX += diente(w, n)
        n += 1

    axs[2].plot(w, senX, '.')

viz_cuadrada(n, 8)
viz_triangular(n, 8)
viz_diente(n, 12)

plt.show()

# ----------------------------------------------------------------------------------------
# end.
# ----------------------------------------------------------------------------------------