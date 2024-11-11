# simulador.py
import numpy as np

def calcular_ondas(permitividad1, permitividad2, permeabilidad1, permeabilidad2, frecuencia, amplitud):
    # Calcular impedancias características
    Z1 = np.sqrt((permeabilidad1 * 4e-7 * np.pi) / (permitividad1 * 8.854e-12))
    Z2 = np.sqrt((permeabilidad2 * 4e-7 * np.pi) / (permitividad2 * 8.854e-12))
    
    # Calcular coeficientes
    coef_reflexion = (Z2 - Z1) / (Z2 + Z1)
    coef_transmision = 2 * Z2 / (Z2 + Z1)

    # Crear el espacio
    x = np.linspace(-400, 400, 1000)  # distancia en mm
    
    # Calcular números de onda
    c = 3e8  # velocidad de la luz
    omega = 2 * np.pi * frecuencia
    k1 = omega * np.sqrt(permitividad1 * permeabilidad1) / c
    k2 = omega * np.sqrt(permitividad2 * permeabilidad2) / c

    # Calcular las ondas
    onda_incidente = amplitud * np.sin(k1 * x)
    onda_reflejada = coef_reflexion * amplitud * np.sin(-k1 * x)
    onda_transmitida = np.where(x > 0, 
                               coef_transmision * amplitud * np.sin(k2 * x),
                               0)

    return x, onda_incidente, onda_reflejada, onda_transmitida