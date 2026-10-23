import tkinter as tk
from tkinter import messagebox

from figuras import Cilindro, Esfera, Piramide, Cubo, Prisma

RELLENO = "#cfe3f7"
BORDE = "#1f4e79"


class VentanaFigura(tk.Toplevel):
    
    TITULO = "Figura"
    CAMPOS = []  

    def __init__(self, ventana_padre):
        super().__init__(ventana_padre)
        self.title(self.TITULO)
        self.resizable(False, False)
        self.campos = {}  
        self.inicio()

    def inicio(self):
        
        marco = tk.Frame(self, padx=15, pady=15)
        marco.grid(row=0, column=0, sticky="n")

        fila = 0
        for nombre, texto in self.CAMPOS:
            tk.Label(marco, text=texto).grid(row=fila, column=0, sticky="w", pady=3)
            campo = tk.Entry(marco, width=12)
            campo.grid(row=fila, column=1, pady=3)
            self.campos[nombre] = campo
            fila += 1

        tk.Button(marco, text="Calcular", width=10, command=self.calcular).grid(
            row=fila, column=0, columnspan=2, pady=10)
        fila += 1

        self.etiqueta_volumen = tk.Label(marco, text="Volumen (cm³):")
        self.etiqueta_volumen.grid(row=fila, column=0, columnspan=2, sticky="w")
        self.etiqueta_superficie = tk.Label(marco, text="Superficie (cm²):")
        self.etiqueta_superficie.grid(row=fila + 1, column=0, columnspan=2, sticky="w")

        lienzo = tk.Canvas(self, width=150, height=150, bg="white",
                           highlightthickness=1, highlightbackground="#bbbbbb")
        lienzo.grid(row=0, column=1, padx=(0, 15), pady=15)
        self.dibujar(lienzo)

        list(self.campos.values())[0].focus()

    def calcular(self):
    
        valores = []
    
        for nombre, texto in self.CAMPOS:
            contenido = self.campos[nombre].get().strip().replace(",", ".")
            if contenido == "":
                messagebox.showerror("Error", f"El campo '{texto}' está vacío.", parent=self)
                return
            try:
                valores.append(float(contenido))
            except ValueError:
                messagebox.showerror("Error", f"El campo '{texto}' debe ser un número.",
                                     parent=self)
                return
        
        try:
            figura = self.crear_figura(valores)
        except ValueError as error:
            messagebox.showerror("Error", str(error), parent=self)
            return
        
        self.etiqueta_volumen.config(text=f"Volumen (cm³): {figura.get_volumen():.2f}")
        self.etiqueta_superficie.config(
            text=f"Superficie (cm²): {figura.get_superficie():.2f}")

    
    def crear_figura(self, valores):
        raise NotImplementedError

    def dibujar(self, lienzo):
        raise NotImplementedError


class VentanaCilindro(VentanaFigura):
    TITULO = "Cilindro"
    CAMPOS = [("radio", "Radio (cm):"), ("altura", "Altura (cm):")]

    def crear_figura(self, valores):
        return Cilindro(valores[0], valores[1])

    def dibujar(self, lienzo):
        lienzo.create_rectangle(40, 40, 110, 115, fill=RELLENO, outline="")
        lienzo.create_oval(40, 105, 110, 125, fill=RELLENO, outline=BORDE, width=2)
        lienzo.create_line(40, 40, 40, 115, fill=BORDE, width=2)
        lienzo.create_line(110, 40, 110, 115, fill=BORDE, width=2)
        lienzo.create_oval(40, 30, 110, 50, fill="#e6f0fb", outline=BORDE, width=2)


class VentanaEsfera(VentanaFigura):
    TITULO = "Esfera"
    CAMPOS = [("radio", "Radio (cm):")]

    def crear_figura(self, valores):
        return Esfera(valores[0])

    def dibujar(self, lienzo):
        lienzo.create_oval(30, 30, 120, 120, fill=RELLENO, outline=BORDE, width=2)
        lienzo.create_arc(30, 62, 120, 88, start=180, extent=180, style="arc",
                          outline=BORDE, width=2)
        lienzo.create_arc(30, 62, 120, 88, start=0, extent=180, style="arc",
                          outline=BORDE, dash=(4, 3))


class VentanaPiramide(VentanaFigura):
    TITULO = "Pirámide"
    CAMPOS = [("base", "Base (cm):"), ("altura", "Altura (cm):"),
              ("apotema", "Apotema (cm):")]

    def crear_figura(self, valores):
        return Piramide(valores[0], valores[1], valores[2])

    def dibujar(self, lienzo):
        cima = (75, 25)
        a, b, c, d = (30, 115), (95, 125), (120, 100), (55, 92)  
        lienzo.create_polygon(*cima, *a, *b, fill=RELLENO, outline=BORDE, width=2)
        lienzo.create_polygon(*cima, *b, *c, fill="#b5d3f0", outline=BORDE, width=2)
        lienzo.create_line(*a, *d, *c, fill=BORDE, dash=(4, 3))
        lienzo.create_line(*cima, *d, fill=BORDE, dash=(4, 3))


class VentanaCubo(VentanaFigura):
    
    TITULO = "Cubo"
    CAMPOS = [("lado", "Lado (cm):")]

    def crear_figura(self, valores):
        return Cubo(valores[0])

    def dibujar(self, lienzo):
        lienzo.create_polygon(35, 55, 95, 55, 95, 115, 35, 115, fill=RELLENO,
                              outline=BORDE, width=2)
        lienzo.create_polygon(35, 55, 60, 35, 120, 35, 95, 55, fill="#e6f0fb",
                              outline=BORDE, width=2)
        lienzo.create_polygon(95, 55, 120, 35, 120, 95, 95, 115, fill="#b5d3f0",
                              outline=BORDE, width=2)


class VentanaPrisma(VentanaFigura):
   
    TITULO = "Prisma rectangular"
    CAMPOS = [("largo", "Largo (cm):"), ("ancho", "Ancho (cm):"), ("alto", "Alto (cm):")]

    def crear_figura(self, valores):
        return Prisma(valores[0], valores[1], valores[2])

    def dibujar(self, lienzo):
        lienzo.create_polygon(20, 70, 100, 70, 100, 115, 20, 115, fill=RELLENO,
                              outline=BORDE, width=2)
        lienzo.create_polygon(20, 70, 50, 45, 130, 45, 100, 70, fill="#e6f0fb",
                              outline=BORDE, width=2)
        lienzo.create_polygon(100, 70, 130, 45, 130, 90, 100, 115, fill="#b5d3f0",
                              outline=BORDE, width=2)