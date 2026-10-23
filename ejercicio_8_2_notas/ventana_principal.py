import tkinter as tk
from tkinter import messagebox

from notas import Notas

class VentanaPrincipal(tk.Tk):

    def __init__(self):
    
        super().__init__()  
        self.title("Notas") 
        self.centrar_ventana(300, 360)  
        self.resizable(False, False)  
        self.inicio()  

    def centrar_ventana(self, ancho, alto):
       
        x = (self.winfo_screenwidth() - ancho) // 2
        y = (self.winfo_screenheight() - alto) // 2
        self.geometry(f"{ancho}x{alto}+{x}+{y}")

    def inicio(self):
       
        
        self.campos_notas = []
        for i in range(Notas.CANTIDAD_NOTAS):
            y = 20 + i * 30 
            etiqueta = tk.Label(self, text=f"Nota {i + 1}:")
            etiqueta.place(x=20, y=y)
            campo = tk.Entry(self, width=18)
            campo.place(x=105, y=y)
            self.campos_notas.append(campo)

        
        self.boton_calcular = tk.Button(self, text="Calcular", width=10,
                                        command=self.calcular)
        self.boton_calcular.place(x=20, y=175)
        self.boton_limpiar = tk.Button(self, text="Limpiar", width=10,
                                       command=self.limpiar)
        self.boton_limpiar.place(x=140, y=175)

       
        self.etiqueta_promedio = tk.Label(self, text="Promedio = ")
        self.etiqueta_promedio.place(x=20, y=225)
        self.etiqueta_desviacion = tk.Label(self, text="Desviación estándar = ")
        self.etiqueta_desviacion.place(x=20, y=255)
        self.etiqueta_mayor = tk.Label(self, text="Nota mayor = ")
        self.etiqueta_mayor.place(x=20, y=285)
        self.etiqueta_menor = tk.Label(self, text="Nota menor = ")
        self.etiqueta_menor.place(x=20, y=315)

    def leer_notas(self):
        
        notas = Notas()  
        for i, campo in enumerate(self.campos_notas):
            texto = campo.get().strip()  
           
            if texto == "":
                messagebox.showwarning(
                    "Dato faltante",
                    f"Debe ingresar la Nota {i + 1}. Las cinco notas son obligatorias.")
                campo.focus()  
                return None

            try:
              
                notas.lista_notas[i] = float(texto.replace(",", "."))
            except ValueError:
                messagebox.showerror(
                    "Dato no numérico",
                    f"La Nota {i + 1} ('{texto}') no es un número válido.")
                campo.focus()
                return None
        return notas

    def calcular(self):
        
        notas = self.leer_notas()
        if notas is None:  
            return
       
        self.etiqueta_promedio.config(
            text=f"Promedio = {notas.calcular_promedio():.2f}")
        self.etiqueta_desviacion.config(
            text=f"Desviación estándar = {notas.calcular_desviacion():.2f}")
        self.etiqueta_mayor.config(text=f"Nota mayor = {notas.calcular_mayor()}")
        self.etiqueta_menor.config(text=f"Nota menor = {notas.calcular_menor()}")

    def limpiar(self):
        
        for campo in self.campos_notas:
            campo.delete(0, tk.END) 
        self.etiqueta_promedio.config(text="Promedio = ")
        self.etiqueta_desviacion.config(text="Desviación estándar = ")
        self.etiqueta_mayor.config(text="Nota mayor = ")
        self.etiqueta_menor.config(text="Nota menor = ")
        self.campos_notas[0].focus()