# interface.py
import tkinter as tk
from tkinter import ttk
from calculator import (
    calcular_impedancia,
    calcular_coeficiente_reflexion,
    calcular_coeficiente_transmision,
)
from visualization_2d import plot_wave_2d
from visualization_3d import plot_wave_3d_electromagnetic

class SimuladorOndasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador de Ondas Electromagnéticas")
        self.root.geometry("390x650") 
        self.root.configure(bg="#f5f5f5")

        # Configuración de fuente y estilo
        self.font_title = ("Helvetica", 12, "bold")
        self.font_label = ("Helvetica", 10)
        self.bg_color = "#f5f5f5"

        

        # Sección de Cálculo de Impedancia
        self.create_impedance_section()
        
        # Separador
        ttk.Separator(root, orient='horizontal').grid(row=8, columnspan=2, sticky="ew", pady=10)

        # Sección de Cálculo de Coeficientes de Reflexión y Transmisión
        self.create_coefficient_section()

        # Separador
        ttk.Separator(root, orient='horizontal').grid(row=14, columnspan=2, sticky="ew", pady=10)

        # Sección de Visualización
        self.create_visualization_section()

    

    def create_theory_section(self):
        # Título de sección teórica
        tk.Label(self.root, text="Objetivo del Simulador", font=self.font_title, bg=self.bg_color).grid(row=0, column=0, columnspan=2, pady=(10, 5))

        # Descripción del objetivo
        tk.Label(
            self.root,
            text="Mejorar la comprensión de los principios fundamentales de las ondas electromagnéticas,\ncomo la propagación y su interacción con diversos medios.",
            font=("Helvetica", 9), bg=self.bg_color, wraplength=340, justify="left"  # wraplength ajustado
        ).grid(row=1, column=0, columnspan=2, padx=10, pady=5)

    def create_impedance_section(self):
        # Título de sección
        tk.Label(self.root, text="Cálculo de Impedancia", font=self.font_title, bg=self.bg_color).grid(row=2, column=0, columnspan=2, pady=(10, 5))

        # Entradas para la permeabilidad y permitividad
        tk.Label(self.root, text="Permeabilidad (mu):", font=self.font_label, bg=self.bg_color).grid(row=3, column=0, sticky="w", padx=10)
        self.mu_entry = tk.Entry(self.root, font=self.font_label, width=25)
        self.mu_entry.grid(row=3, column=1, padx=10, pady=2)
        self.mu_entry.insert(0, "1.2566370614e-6")

        tk.Label(self.root, text="Permitividad (epsilon):", font=self.font_label, bg=self.bg_color).grid(row=4, column=0, sticky="w", padx=10)
        self.epsilon_entry = tk.Entry(self.root, font=self.font_label, width=25)
        self.epsilon_entry.grid(row=4, column=1, padx=10, pady=2)
        self.epsilon_entry.insert(0, "8.85418782e-12")

        # Botón de cálculo de impedancia
        calcular_impedancia_btn = tk.Button(self.root, text="Calcular Impedancia", font=self.font_label, command=self.calcular_impedancia, bg="#4CAF50", fg="white", relief="flat", width=20)
        calcular_impedancia_btn.grid(row=5, column=0, columnspan=2, pady=5)

        # Resultado de impedancia
        self.impedancia_label = tk.Label(self.root, text="Impedancia: ", font=self.font_label, bg=self.bg_color)
        self.impedancia_label.grid(row=6, column=0, columnspan=2, pady=5)

    def create_coefficient_section(self):
        # Título de sección
        tk.Label(self.root, text="Coeficientes de Reflexión y Transmisión", font=self.font_title, bg=self.bg_color).grid(row=9, column=0, columnspan=2, pady=(10, 5))

        # Entradas para las impedancias η1 y η2
        tk.Label(self.root, text="Impedancia η1:", font=self.font_label, bg=self.bg_color).grid(row=10, column=0, sticky="w", padx=10)
        self.eta1_entry = tk.Entry(self.root, font=self.font_label, width=25)
        self.eta1_entry.grid(row=10, column=1, padx=10, pady=2)
        self.eta1_entry.insert(0, "377")

        tk.Label(self.root, text="Impedancia η2:", font=self.font_label, bg=self.bg_color).grid(row=11, column=0, sticky="w", padx=10)
        self.eta2_entry = tk.Entry(self.root, font=self.font_label, width=25)
        self.eta2_entry.grid(row=11, column=1, padx=10, pady=2)
        self.eta2_entry.insert(0, "300")

        # Botón para calcular coeficientes
        calcular_coef_btn = tk.Button(self.root, text="Calcular Coeficientes", font=self.font_label, command=self.calcular_coeficientes, bg="#4CAF50", fg="white", relief="flat", width=20)
        calcular_coef_btn.grid(row=12, column=0, columnspan=2, pady=5)

        # Resultado de los coeficientes
        self.coeficientes_label = tk.Label(self.root, text="Coeficiente de Reflexión Γ:\nCoeficiente de Transmisión α:", font=self.font_label, bg=self.bg_color)
        self.coeficientes_label.grid(row=13, column=0, columnspan=2, pady=5)

    def create_visualization_section(self):
        # Título de sección
        tk.Label(self.root, text="Visualización de Campos", font=self.font_title, bg=self.bg_color).grid(row=15, column=0, columnspan=2, pady=(10, 5))

        # Entradas para frecuencia y amplitudes
        tk.Label(self.root, text="Frecuencia (Hz):", font=self.font_label, bg=self.bg_color).grid(row=16, column=0, sticky="w", padx=10)
        self.frecuencia_entry = tk.Entry(self.root, font=self.font_label, width=25)
        self.frecuencia_entry.grid(row=16, column=1, padx=10, pady=2)
        self.frecuencia_entry.insert(0, "1e9")

        tk.Label(self.root, text="Distancia Máxima (mm):", font=self.font_label, bg=self.bg_color).grid(row=17, column=0, sticky="w", padx=10)
        self.distancia_entry = tk.Entry(self.root, font=self.font_label, width=25)
        self.distancia_entry.grid(row=17, column=1, padx=10, pady=2)
        self.distancia_entry.insert(0, "1000")

        tk.Label(self.root, text="Amplitud Campo Incidente:", font=self.font_label, bg=self.bg_color).grid(row=18, column=0, sticky="w", padx=10)
        self.amplitud_incidente_entry = tk.Entry(self.root, font=self.font_label, width=25)
        self.amplitud_incidente_entry.grid(row=18, column=1, padx=10, pady=2)
        self.amplitud_incidente_entry.insert(0, "3")

        tk.Label(self.root, text="Amplitud Campo Reflejado:", font=self.font_label, bg=self.bg_color).grid(row=19, column=0, sticky="w", padx=10)
        self.amplitud_reflejado_entry = tk.Entry(self.root, font=self.font_label, width=25)
        self.amplitud_reflejado_entry.grid(row=19, column=1, padx=10, pady=2)
        self.amplitud_reflejado_entry.insert(0, "1")

        tk.Label(self.root, text="Amplitud Campo Transmitido:", font=self.font_label, bg=self.bg_color).grid(row=20, column=0, sticky="w", padx=10)
        self.amplitud_transmitido_entry = tk.Entry(self.root, font=self.font_label, width=25)
        self.amplitud_transmitido_entry.grid(row=20, column=1, padx=10, pady=2)
        self.amplitud_transmitido_entry.insert(0, "2")

        # Botones para visualización en 2D y 3D
        visualizar_2d_btn = tk.Button(self.root, text="Visualizar en 2D", font=self.font_label, command=self.visualizar_2d, bg="#2196F3", fg="white", relief="flat", width=20)
        visualizar_2d_btn.grid(row=21, column=0, pady=10, ipadx=10)

        visualizar_3d_btn = tk.Button(self.root, text="Visualizar en 3D", font=self.font_label, command=self.visualizar_3d, bg="#2196F3", fg="white", relief="flat", width=20)
        visualizar_3d_btn.grid(row=21, column=1, pady=10, ipadx=10)

    # Método para calcular impedancia
    def calcular_impedancia(self):
        mu = float(self.mu_entry.get())
        epsilon = float(self.epsilon_entry.get())
        impedancia = calcular_impedancia(mu, epsilon)
        self.impedancia_label.config(text=f"Impedancia: {impedancia:.2f} Ω")

    # Método para calcular coeficientes de reflexión y transmisión
    def calcular_coeficientes(self):
        eta1 = float(self.eta1_entry.get())
        eta2 = float(self.eta2_entry.get())
        coef_reflexion = calcular_coeficiente_reflexion(eta1, eta2)
        coef_transmision = calcular_coeficiente_transmision(eta1, eta2)
        self.coeficientes_label.config(
            text=f"Coeficiente de Reflexión Γ: {coef_reflexion:.2f}\nCoeficiente de Transmisión α: {coef_transmision:.2f}"
        )
    
    # Métodos de visualización en 2D y 3D (ya implementados previamente)
    def visualizar_2d(self):
        frecuencia = float(self.frecuencia_entry.get())
        amplitud_incidente = float(self.amplitud_incidente_entry.get())
        amplitud_reflejado = float(self.amplitud_reflejado_entry.get())
        amplitud_transmitido = float(self.amplitud_transmitido_entry.get())
        

        # Obtener valores de impedancia, coeficiente de reflexión y transmisión
        impedancia = float(self.impedancia_label.cget("text").split(":")[1].strip().split()[0])
        coef_reflexion = float(self.coeficientes_label.cget("text").split("Γ:")[1].split("\n")[0].strip())
        coef_transmision = float(self.coeficientes_label.cget("text").split("α:")[1].strip())

        distancia_max = float(self.distancia_entry.get())  # Obtener el valor ingresado
        plot_wave_2d(frecuencia, amplitud_incidente, amplitud_reflejado, amplitud_transmitido, velocidad=3e8, distancia_max=distancia_max, impedancia=impedancia, gamma=coef_reflexion, alpha=coef_transmision)


    # interface.py (dentro de la clase SimuladorOndasApp)

    def visualizar_3d(self):
        frecuencia = float(self.frecuencia_entry.get())
        amplitud_incidente = float(self.amplitud_incidente_entry.get())
        amplitud_reflejado = float(self.amplitud_reflejado_entry.get())
        amplitud_transmitido = float(self.amplitud_transmitido_entry.get())

        # Obtener valores de impedancia, coeficiente de reflexión y transmisión
        impedancia = float(self.impedancia_label.cget("text").split(":")[1].strip().split()[0])
        coef_reflexion = float(self.coeficientes_label.cget("text").split("Γ:")[1].split("\n")[0].strip())
        coef_transmision = float(self.coeficientes_label.cget("text").split("α:")[1].strip())

        # Llamar a la función de visualización con los nuevos parámetros
        plot_wave_3d_electromagnetic(frecuencia, amplitud_incidente, amplitud_reflejado, amplitud_transmitido, impedancia, coef_reflexion, coef_transmision)

# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = SimuladorOndasApp(root)
    root.mainloop()
