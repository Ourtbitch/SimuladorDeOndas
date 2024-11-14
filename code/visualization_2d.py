# visualization_2d.py
import numpy as np
import matplotlib.pyplot as plt

def plot_wave_2d(frecuencia, amplitud_incidente, amplitud_reflejado, amplitud_transmitido, velocidad=3e8, distancia_max=1, impedancia=None, gamma=None, alpha=None):
    """
    Genera un gráfico en 2D que muestra el campo incidente, reflejado y transmitido en función de la distancia.
    Incluye anotaciones de impedancia y coeficientes de reflexión y transmisión.
    """
    x = np.linspace(0, distancia_max, 1000)

    # Ondas incidente, reflejada y transmitida
    incidente = amplitud_incidente * np.sin(2 * np.pi * frecuencia * x / velocidad)
    reflejado = amplitud_reflejado * np.sin(2 * np.pi * frecuencia * x / velocidad)
    transmitido = amplitud_transmitido * np.sin(2 * np.pi * frecuencia * x / velocidad)

    # Crear el gráfico
    plt.figure(figsize=(10, 6))
    plt.plot(x, incidente, label="Campo Incidente", color="blue")
    plt.plot(x, reflejado, label="Campo Reflejado", color="red")
    plt.plot(x, transmitido, label="Campo Transmitido", color="green")
    
    # Añadir etiquetas
    plt.xlabel("Distancia (mm)")
    plt.ylabel("Amplitud del Campo")
    plt.title("Simulación de Campos Electromagnéticos en la Interfaz")
    plt.legend()
    plt.grid(True)

    # Añadir anotaciones de impedancia y coeficientes
    if impedancia is not None:
        plt.text(0.02, 0.95, f"Impedancia: {impedancia:.2f} Ω", transform=plt.gca().transAxes)
    if gamma is not None:
        plt.text(0.02, 0.90, f"Coeficiente de Reflexión Γ: {gamma:.2f}", transform=plt.gca().transAxes)
    if alpha is not None:
        plt.text(0.02, 0.85, f"Coeficiente de Transmisión α: {alpha:.2f}", transform=plt.gca().transAxes)

    plt.show()
