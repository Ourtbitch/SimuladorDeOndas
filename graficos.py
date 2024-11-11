# graficos.py
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None):
        self.fig, self.ax = plt.subplots()
        super().__init__(self.fig)
        # Set figure size and margins
        self.fig.set_size_inches(10, 6)
        self.fig.tight_layout(pad=3.0)

    def actualizar_grafico(self, x, onda_incidente, onda_reflejada, onda_transmitida):
        self.ax.clear()
        self.ax.plot(x/1000, onda_incidente, label="Campo Incidente", color="red")
        self.ax.plot(x/1000, onda_reflejada, label="Campo Reflejado", color="green")
        self.ax.plot(x/1000, onda_transmitida, label="Campo Transmitido", color="blue")
        
        self.ax.axvline(x=0, color='black', linestyle='--', alpha=0.5)
        self.ax.set_xlabel("Distancia (mm)")
        self.ax.set_ylabel("Campo Eléctrico (V/m)")
        self.ax.set_title("Simulación de Campos Electromagnéticos en la Interfaz")
        self.ax.grid(True, linestyle='--', alpha=0.7)
        self.ax.legend()
        self.fig.canvas.draw_idle()