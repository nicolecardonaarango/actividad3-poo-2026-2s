import math


class Notas:

    CANTIDAD_NOTAS = 5  

    def __init__(self):

        self.lista_notas = [0.0] * Notas.CANTIDAD_NOTAS

    def calcular_promedio(self):
        
        suma = 0
        for nota in self.lista_notas:  
            suma = suma + nota
        return suma / len(self.lista_notas)

    def calcular_desviacion(self):
       
        promedio = self.calcular_promedio()  
        suma = 0
        for nota in self.lista_notas:
            suma = suma + (nota - promedio) ** 2  
        return math.sqrt(suma / len(self.lista_notas))

    def calcular_menor(self):
        
        menor = self.lista_notas[0]  
        for nota in self.lista_notas:
            if nota < menor:  
                menor = nota
        return menor

    def calcular_mayor(self):
       
        mayor = self.lista_notas[0]  
        for nota in self.lista_notas:
            if nota > mayor:  
                mayor = nota
        return mayor