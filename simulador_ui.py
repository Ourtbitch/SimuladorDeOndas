from PyQt5 import QtWidgets
from graficos import MplCanvas
from simulador import calcular_ondas

class SimuladorOndaInterfaz(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simulador de Incidencia Normal Entre Medios sin Pérdidas")
        self.setGeometry(100, 100, 900, 600)
        
        # Inicializar el gráfico
        self.canvas = MplCanvas(self)
        
        # Layout principal
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.canvas)
        
        # Controles de entrada de parámetros
        parametros_layout = QtWidgets.QFormLayout()

        # Definir controles de entrada de parámetros como QDoubleSpinBox
        self.permitividad1 = QtWidgets.QDoubleSpinBox()
        self.permitividad1.setRange(1.0, 100.0)
        self.permitividad1.setValue(1.0)
        
        self.permitividad2 = QtWidgets.QDoubleSpinBox()
        self.permitividad2.setRange(1.0, 100.0)
        self.permitividad2.setValue(2.0)
        
        self.permeabilidad1 = QtWidgets.QDoubleSpinBox()
        self.permeabilidad1.setRange(1.0, 100.0)
        self.permeabilidad1.setValue(1.0)
        
        self.permeabilidad2 = QtWidgets.QDoubleSpinBox()
        self.permeabilidad2.setRange(1.0, 100.0)
        self.permeabilidad2.setValue(1.0)
        
        self.frecuencia = QtWidgets.QDoubleSpinBox()
        self.frecuencia.setRange(1e3, 1e9)  # Rango de frecuencia grande
        self.frecuencia.setDecimals(0)      # Decimales en cero para valores grandes
        self.frecuencia.setValue(1e6)       # Valor inicial en Hz
        
        self.amplitud = QtWidgets.QDoubleSpinBox()
        self.amplitud.setRange(0.1, 10.0)
        self.amplitud.setDecimals(1)
        self.amplitud.setValue(1.0)

        # Agregar controles al layout de parámetros
        parametros_layout.addRow("Permitividad Eléctrica Relativa 1", self.permitividad1)
        parametros_layout.addRow("Permitividad Eléctrica Relativa 2", self.permitividad2)
        parametros_layout.addRow("Permeabilidad Magnética Relativa 1", self.permeabilidad1)
        parametros_layout.addRow("Permeabilidad Magnética Relativa 2", self.permeabilidad2)
        parametros_layout.addRow("Frecuencia (Hz)", self.frecuencia)
        parametros_layout.addRow("Magnitud del Campo Eléctrico", self.amplitud)
        
        # Botón para simular
        self.simular_btn = QtWidgets.QPushButton("Simular")
        self.simular_btn.clicked.connect(self.simular)
        
        # Layout horizontal para parámetros y botón
        controls_layout = QtWidgets.QHBoxLayout()
        controls_layout.addLayout(parametros_layout)
        controls_layout.addWidget(self.simular_btn)
        
        layout.addLayout(controls_layout)

    def simular(self):
        # Obtener los valores de los parámetros y llamar a la función de simulación
        params = {
            'permitividad1': self.permitividad1.value(),
            'permitividad2': self.permitividad2.value(),
            'permeabilidad1': self.permeabilidad1.value(),
            'permeabilidad2': self.permeabilidad2.value(),
            'frecuencia': self.frecuencia.value(),
            'amplitud': self.amplitud.value()
        }
        ondas = calcular_ondas(**params)
        self.canvas.actualizar_grafico(*ondas)
