import numpy as np

def calcular_ondas(permitividad1, permitividad2, permeabilidad1, permeabilidad2, frecuencia, amplitud):
    # Calcular impedancias características de cada medio
    Z1 = np.sqrt((permeabilidad1 * 4e-7 * np.pi) / (permitividad1 * 8.854e-12))
    Z2 = np.sqrt((permeabilidad2 * 4e-7 * np.pi) / (permitividad2 * 8.854e-12))
    
    # Calcular coeficientes de reflexión y transmisión
    coef_reflexion = (Z2 - Z1) / (Z2 + Z1)
    coef_transmision = 2 * Z2 / (Z2 + Z1)

    # Crear el espacio de simulación en milímetros (mm)
    x = np.linspace(-400, 400, 1000)  # distancia en mm
    
    # Calcular número de onda para cada medio
    c = 3e8  # velocidad de la luz en el vacío
    omega = 2 * np.pi * frecuencia
    k1 = omega * np.sqrt(permitividad1 * permeabilidad1) / c
    k2 = omega * np.sqrt(permitividad2 * permeabilidad2) / c

    # Calcular las ondas: incidente, reflejada, y transmitida
    onda_incidente = amplitud * np.sin(k1 * x)
    onda_reflejada = coef_reflexion * amplitud * np.sin(-k1 * x)
    onda_transmitida = np.where(x > 0, coef_transmision * amplitud * np.sin(k2 * x), 0)

    return x, onda_incidente, onda_reflejada, onda_transmitida
