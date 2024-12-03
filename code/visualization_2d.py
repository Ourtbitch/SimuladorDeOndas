# visualization_2d.py
import numpy as np
import matplotlib.pyplot as plt
def plot_wave_2d(frecuencia, amplitud_incidente, amplitud_reflejado, amplitud_transmitido, velocidad=3e8, distancia_max=1, impedancia=None, gamma=None, alpha=None):
    """
    Genera un gráfico en 2D que muestra el campo incidente, reflejado y transmitido en función de la distancia.
    Incluye anotaciones de impedancia y coeficientes de reflexión y transmisión.
    """
    # Convertir distancia a metros si está en milímetros
    distancia_max = distancia_max * 1e-3  
    x = np.linspace(0, distancia_max, 1000)

    # Calcular las ondas
    incidente = amplitud_incidente * np.sin(2 * np.pi * frecuencia * x / velocidad)
    reflejado = amplitud_reflejado * np.sin(2 * np.pi * frecuencia * x / velocidad)
    transmitido = amplitud_transmitido * np.sin(2 * np.pi * frecuencia * x / velocidad)

    # Crear el gráfico
    plt.figure(figsize=(10, 6))
    plt.plot(x, incidente, label="Campo Incidente", color="blue", linewidth=1.5)
    plt.plot(x, reflejado, label="Campo Reflejado", color="red", linewidth=1.5)
    plt.plot(x, transmitido, label="Campo Transmitido", color="green", linewidth=1.5)
    
    # Añadir etiquetas y título
    plt.xlabel("Distancia (m)", fontsize=12)
    plt.ylabel("Amplitud del Campo", fontsize=12)
    plt.title("Simulación de Campos Electromagnéticos en la Interfaz", fontsize=14, fontweight='bold')
    plt.legend(loc="lower left", fontsize=10)
    plt.grid(True, linestyle='--', alpha=0.7)

    # Añadir anotaciones de impedancia y coeficientes con fondo y posición fija
    if impedancia is not None:
        plt.text(0.05, 0.95, f"Impedancia: {impedancia:.2f} Ω", transform=plt.gca().transAxes, fontsize=10, 
                 bbox=dict(facecolor='white', alpha=0.5, edgecolor='none'))
    if gamma is not None:
        plt.text(0.05, 0.90, f"Coeficiente de Reflexión Γ: {gamma:.2f}", transform=plt.gca().transAxes, fontsize=10,
                 bbox=dict(facecolor='white', alpha=0.5, edgecolor='none'))
    if alpha is not None:
        plt.text(0.05, 0.85, f"Coeficiente de Transmisión α: {alpha:.2f}", transform=plt.gca().transAxes, fontsize=10,
                 bbox=dict(facecolor='white', alpha=0.5, edgecolor='none'))

    # Ajuste del rango de amplitud
    plt.ylim(-max(amplitud_incidente, amplitud_reflejado, amplitud_transmitido) * 1.5,
             max(amplitud_incidente, amplitud_reflejado, amplitud_transmitido) * 1.5)

    plt.show()

