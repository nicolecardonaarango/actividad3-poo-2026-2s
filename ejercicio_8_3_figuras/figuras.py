import math
from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
   
    def __init__(self):
        self.__volumen = 0.0    
        self.__superficie = 0.0

    def get_volumen(self):
        return self.__volumen

    def set_volumen(self, volumen):
        self.__volumen = volumen

    def get_superficie(self):
        return self.__superficie

    def set_superficie(self, superficie):
        self.__superficie = superficie

    @abstractmethod
    def calcular_volumen(self):
        pass

    @abstractmethod
    def calcular_superficie(self):
        pass

    def actualizar_medidas(self):
        
        self.set_volumen(self.calcular_volumen())
        self.set_superficie(self.calcular_superficie())

    @staticmethod
    def validar_positivo(valor, nombre):
        
        if valor <= 0:
            raise ValueError(f"El valor de '{nombre}' debe ser mayor que cero.")
        return valor


class Cilindro(FiguraGeometrica):

    def __init__(self, radio, altura):
        super().__init__()  
        self.__radio = self.validar_positivo(radio, "radio")
        self.__altura = self.validar_positivo(altura, "altura")
        self.actualizar_medidas()

    def calcular_volumen(self):
       
        return math.pi * self.__radio ** 2 * self.__altura

    def calcular_superficie(self):
        
        area_lado = 2 * math.pi * self.__radio * self.__altura
        area_tapas = 2 * math.pi * self.__radio ** 2
        return area_lado + area_tapas


class Esfera(FiguraGeometrica):
   

    def __init__(self, radio):
        super().__init__()
        self.__radio = self.validar_positivo(radio, "radio")
        self.actualizar_medidas()

    def calcular_volumen(self):
        
        return (4 / 3) * math.pi * self.__radio ** 3

    def calcular_superficie(self):
      
        return 4 * math.pi * self.__radio ** 2


class Piramide(FiguraGeometrica):
   

    def __init__(self, base, altura, apotema):
        super().__init__()
        self.__base = self.validar_positivo(base, "base")
        self.__altura = self.validar_positivo(altura, "altura")
        self.__apotema = self.validar_positivo(apotema, "apotema")
        self.actualizar_medidas()

    def calcular_volumen(self):
      
        return (self.__base ** 2 * self.__altura) / 3

    def calcular_superficie(self):
       
        area_base = self.__base ** 2
        area_lados = 2 * self.__base * self.__apotema
        return area_base + area_lados


class Cubo(FiguraGeometrica):

    def __init__(self, lado):
        super().__init__()
        self.__lado = self.validar_positivo(lado, "lado")
        self.actualizar_medidas()

    def calcular_volumen(self):
        
        return self.__lado ** 3

    def calcular_superficie(self):
        
        return 6 * self.__lado ** 2


class Prisma(FiguraGeometrica):

    def __init__(self, largo, ancho, alto):
        super().__init__()
        self.__largo = self.validar_positivo(largo, "largo")
        self.__ancho = self.validar_positivo(ancho, "ancho")
        self.__alto = self.validar_positivo(alto, "alto")
        self.actualizar_medidas()

    def calcular_volumen(self):
        
        return self.__largo * self.__ancho * self.__alto

    def calcular_superficie(self):
        
        return 2 * (self.__largo * self.__ancho
                    + self.__largo * self.__alto
                    + self.__ancho * self.__alto)