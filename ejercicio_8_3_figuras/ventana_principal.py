import tkinter as tk

from ventanas_figuras import (VentanaCilindro, VentanaEsfera, VentanaPiramide,
                              VentanaCubo, VentanaPrisma)


class VentanaPrincipal(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Figuras")
        self.resizable(False, False)
        self.inicio()

    def inicio(self):
        
        tk.Label(self, text="Seleccione la figura que desea calcular:",
                 font=("Arial", 11)).grid(row=0, column=0, columnspan=3, pady=(15, 10))

        botones = [
            ("Cilindro", self.abrir_cilindro),
            ("Esfera", self.abrir_esfera),
            ("Pirámide", self.abrir_piramide),
            ("Cubo", self.abrir_cubo),        
            ("Prisma", self.abrir_prisma),    
        ]
        for i, (texto, metodo) in enumerate(botones):
            fila = 1 + i // 3       
            columna = i % 3
            tk.Button(self, text=texto, width=12, command=metodo).grid(
                row=fila, column=columna, padx=10, pady=6)
        tk.Label(self, text="").grid(row=3, column=0, pady=2)  


    def abrir_cilindro(self):
        VentanaCilindro(self)

    def abrir_esfera(self):
        VentanaEsfera(self)

    def abrir_piramide(self):
        VentanaPiramide(self)

    def abrir_cubo(self):
        VentanaCubo(self)

    def abrir_prisma(self):
        VentanaPrisma(self)