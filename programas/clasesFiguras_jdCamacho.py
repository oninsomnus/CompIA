# ----------------------------------------------------------------------------------------
# MODULO: Clases figuras
# ----------------------------------------------------------------------------------------
# Descripción: T-11 definición de clases y subclases para 4 figuras geométricas
# ----------------------------------------------------------------------------------------
# Autor: Juan Diego Camacho
# Version: 1.0
# [09.10.2021]
# ----------------------------------------------------------------------------------------
# IMPORTAR MODULOS (un módulo puede importar otros módulos)
import math
class c:
    OKCYAN = '\033[96m'
    ENDC = '\033[0m'
    FAIL = '\033[91m'
#---------------------------------------------------------------------------------------
# CLASE: Figura
# ----------------------------------------------------------------------------------------
# Descripcion: definición de la superclase Figura
# ----------------------------------------------------------------------------------------
# PARAMETROS & PRE-CONDICIONES
# Como variable de entrada se ingresará un número entero
# La variable id se definirá como variable de entrada
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
# ----------------------------------------------------------------------------------------

class Figura:
  def __init__(self, id):
    self.id = str(id)
    
  def getArea(self):
    return self.area
  
  def setArea(self, area):
    self.area = area

  def setTipo(self, tipo):
    self.tipo = tipo

  def getIdFigura(self):
    return self.id
  
  def setIdFigura(self, id): # No tiene sentido cambiar el id en tiempo de ejecución
    try:               # Se valida si el id esta asignado
      self.id          # Solo y solo si no esta asignado se asigna un valor
    except NameError:
      self.id = id

  def __str__(self):
    return "Mi indice es: " + self.id + " y soy un "+self.tipo+" :) \n"

#----------------------------------------------------------------------------------------
# CLASE: Cuadrado
# ----------------------------------------------------------------------------------------
# Descripcion: definición de la subclase Cuadrado
# ----------------------------------------------------------------------------------------
# PARAMETROS & PRE-CONDICIONES
# Como variable de entrada se ingresará un número flotante correspondiente al lado de la figura
# La variable lado se definirá como variable de entrada
# La variable id se hereda de la clase Figura
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
# ----------------------------------------------------------------------------------------

class Cuadrado(Figura):
  def __init__(self, id, lado):
    super().__init__(id)
    self.setLado(lado)
    self.calcularArea()
    super().setTipo("Cuadrado")
  
  def setLado(self, lado):
    self.lado = lado

  def getLado(self):
    return self.lado

  def calcularArea(self):
    area = self.lado * self.lado
    super().setArea(area)

# ----------------------------------------------------------------------------------------
# CLASE: Rectángulo
# ----------------------------------------------------------------------------------------
# Descripcion: definición de la subclase Rectángulo
# ----------------------------------------------------------------------------------------
# PARAMETROS & PRE-CONDICIONES
# Como variable de entrada se ingresará un número flotante correspondiente al ancho y otra al largo de la figura
# Las variables ancho y largo se definirán como variable de entrada
# La variable id se hereda de la clase Figura
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
# ----------------------------------------------------------------------------------------

class Rectangulo(Figura):
  def __init__(self, id, ancho, largo):
    super().__init__(id)
    super().setTipo("Rectángulo")
    self.setAncho(ancho)
    self.setLargo(largo)
    self.calcularArea()
  
  def setAncho(self, ancho):
    self.ancho = ancho

  def setLargo(self, largo):
    self.largo = largo

  def getAncho(self):
    return self.ancho
    
  def getLargo(self):
    return self.largo

  def calcularArea(self):
    area = self.largo * self.ancho
    super().setArea(area)


# ----------------------------------------------------------------------------------------
# CLASE: Triángulo
# ----------------------------------------------------------------------------------------
# Descripcion: definición de la subclase Triángulo
# ----------------------------------------------------------------------------------------
# PARAMETROS & PRE-CONDICIONES
# Como variable de entrada se ingresará un número flotante correspondiente a la altura y otra a la base de la figura
# Las variables altura y base se definirán como variable de entrada
# La variable id se hereda de la clase Figura
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
# ----------------------------------------------------------------------------------------
class Triangulo(Figura):
  def __init__(self, id, altura, base):
    super().__init__(id)
    super().setTipo("Triangulo")
    self.setAltura(altura)
    self.setBase(base)
    self.calcularArea()
  
  def setAltura(self, altura):
    self.altura = altura

  def setBase(self, base):
    self.base = base

  def getBase(self):
    return self.base
    
  def getAltura(self):
    return self.altura

  def calcularArea(self):
    area = 0.5 * self.altura * self.base
    super().setArea(area)
    
# ----------------------------------------------------------------------------------------
# CLASE: Círculo
# ----------------------------------------------------------------------------------------
# Descripcion: definición de la subclase Círculo
# ----------------------------------------------------------------------------------------
# PARAMETROS & PRE-CONDICIONES
# Como variable de entrada se ingresará un número flotante correspondiente al radio
# La variable radio se definira como variable de entrada
# La variable id se hereda de la clase Figura
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
# ----------------------------------------------------------------------------------------
class Circulo(Figura):
  def __init__(self, id, radio):
    super().__init__(id)
    super().setTipo("Circulo")
    self.setRadio(radio)
    self.calcularArea()
    self.calcularPerímetro()
  
  def setRadio(self, radio):
    self.radio = radio
    
  def getRadio(self):
    return self.radio
    
  def getPerimetro(self):
    return self.perimetro

  def calcularArea(self):
    area = math.pi * (self.radio**2)
    super().setArea(area)

  def calcularPerímetro(self):
    perimetro = 2 * math.pi * self.radio
    self.perimetro = perimetro

# ----------------------------------------------------------------------------------------
# FUNCIÓN: evaluar variable de entrada
# ----------------------------------------------------------------------------------------
# Descripcion: evalua el número de entrada y lo retorna como una lista
# ----------------------------------------------------------------------------------------
# PARAMETROS & PRE-CONDICIONES
# recibe una variable de entrada (entrada) de tipo string
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
# ----------------------------------------------------------------------------------------
def inputUser(entrada, metodo):
    b = []
    entrada = entrada.split()

    if (len(entrada) > 2 and (metodo in ["2", "3"])):
      print("Por favor ingresa 2 números")
      return False
    if (len(entrada) != 1 and (metodo in ["1", "4", "5"])):
      print("Por favor ingresa 1 número")
      return False
#    elif (len(entrada) == 1 and (metodo in ["1","4","5"])):
#      try:
#        entrada = float(entrada[0])
#        return entrada
#      except NameError:
#        print('Solo se admiten números')
    else:
      for i in entrada:
        try:
          x = float(i)
          b.append(x)
        except:
          print('Solo se admiten números')
      return b
      

# ----------------------------------------------------------------------------------------
# FUNCIÓN: Imprimir figuras generadas
# ----------------------------------------------------------------------------------------
# Descripcion: Se imprimen las figuras que se han guardado en el lista
# ----------------------------------------------------------------------------------------
# PARAMETROS & PRE-CONDICIONES
# recibe una variable de entrada (entrada) de tipo lista
# la lista debe contener los objetos generados
# la lista de entrada corresponde a la variable 'figuras'
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
# ---------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
def printFiguras(figuras):
  for figura in figuras:
    print(figura)
# end.
# ------------------------------------------------------------------
