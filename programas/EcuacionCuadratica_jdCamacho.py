# ------------------------------------------------------------------------------
# Ecuación Cuadrática
# Autor: "Juan Diego Camacho" 
# Version: 1.0
# Fecha: 10.08.2021
# ------------------------------------------------------------------------------

from math import sqrt

def ecua():
  variables = input('\nIngrese las variables a, b y c separadas por espacios\nLuego presione Enter\n')

  variables = variables.split()

  try:
    a = int(variables[0])
    b = int(variables[1])
    c = int(variables[2])
  except:
    print('Las variables deben ser números reales')

  d = (b**2) - (4*a*c)
  print('a: {}, b: {}, c: {}, d: {}'.format(a,b,c,d))

  if(a == 0):
    print('La variable "a" debe ser diferente a 0')
  elif(d < 0):
    print('La operación en la raíz cuadrada debe ser mayor o igual a 0')
  else:
    #print((-b+sqrt(d))/(2*a))
    x1 = (-b+sqrt(d))/(2*a)
    x2 = (-b-sqrt(d))/(2*a)
    if(x1 == x2):
      print('x = {}'.format(x1))
    else:
      print("x1 = {}, x2 = {}".format(x1, x2))
    #print("x1 = {}, x2 = {}".format((-b+sqrt(d))/(2*a),(-b-sqrt(d))/(2*a)))

while True:
  ecua()