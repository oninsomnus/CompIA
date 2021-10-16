# ----------------------------------------------------------------------------------------
# PROGRAMA: Figuras geométricas
# ----------------------------------------------------------------------------------------
# Descripción: Ejecución del módulo clasesFigura
# ----------------------------------------------------------------------------------------
# Autor: Luis Carlos Díaz
# Version: 2.0
# [18.07.2020]
# ----------------------------------------------------------------------------------------
# IMPORTAR MODULOS
import clasesFiguras_jdCamacho as cf   # modulo de python con las clases de las figuras geométricas


# ----------------------------------------------------------------------------------------
# VARIABLES GLOBALES Y PRE-CONDICIONES
# ----------------------------------------------------------------------------------------

# Variable menu la cual será un número entero
# Se usará para la condición de ejecución del programa completo
# También para validar las opciones del menú del usuario
# La variable "opciones" nos indica las posibles opciones para el usuario durante la ejecución
# La variable "figuras" contendrá todas las figuras que el usuario genere

menu = "";
opciones = ["1", "2", "3", "4", "5"]
figuras = list()
mensajes = [
  'Ingrese el valor del lado correspondiente a la figura\n',
  'Ingrese los valores del ancho y largo correspondientes a la figura\n',
  'Ingrese los valores de la base y la altura correspondientes a la figura\n',
  'Ingrese el radio correspondiente a la figura\n',
  'Ingrese el radio correspondiente a la circunferencia\n'
]

# ----------------------------------------------------------------------------------------
# POSTCONDICIONES
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# PARAMETROS
# ----------------------------------------------------------------------------------------
# listar aqui los parámetros

while menu != 0:
  metodo = input("\n    Menu - Cálculos sobre figuras geométricas"
                   "\n      1. Área de un cuadrado"
                   "\n      2. Área de un rectángulo"
                   "\n      3. Área de un tríangulo"
                   "\n      4. Área de un círculo"
                   "\n      5. Perímetro de una circunferencia"
                   "\nIngrese la opción deseada (1-5) o 0 para terminar:\n")
  
  if "0" not in metodo and metodo in opciones:
    x = cf.inputUser(input(mensajes[int(metodo)-1]), metodo)   
    
    if not x:
      continue
      
    if metodo == "1":
      figuras.append(cf.Cuadrado(len(figuras)+1, x[0]))
      print("El área de la figura es: ", figuras[len(figuras)-1].getArea())
       
    elif metodo == "2":
      figuras.append(cf.Rectangulo(len(figuras)+1, x[0], x[1]))
      print("El área de la figura es: ", figuras[len(figuras)-1].getArea())

    elif metodo == "3":
      figuras.append(cf.Triangulo(len(figuras)+1, x[0], x[1]))
      print("El área de la figura es: ", figuras[len(figuras)-1].getArea())          
      
    elif metodo == "4":
      figuras.append(cf.Circulo(len(figuras)+1, x[0]))
      print("El área de la figura es: ", figuras[len(figuras)-1].getArea())
      
    elif metodo == "5":
      figuras.append(cf.Circulo(len(figuras)+1, x[0]))
      print("El perímetro de la figura es: ", figuras[len(figuras)-1].getPerimetro())
    
  elif "0" in metodo:
    menu = int(metodo)
    cf.printFiguras(figuras)
  else:
    print("Debe indicar una opción correcta\n")




# ----------------------------------------------------------------------------------------
# end.
# ----------------------------------------------------------------------------------------
