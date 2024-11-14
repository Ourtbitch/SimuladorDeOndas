# calculator.py
import math
import config

def calcular_impedancia(mu, epsilon):
    return math.sqrt(mu / epsilon)

def calcular_impedancia_vacio():
    return calcular_impedancia(config.MU_0, config.EPSILON_0)

def calcular_longitud_onda(frecuencia, velocidad=3e8):
    return velocidad / frecuencia

def calcular_coeficiente_reflexion(eta1, eta2):
    """
    Calcula el coeficiente de reflexión Γ.
    """
    return (eta2 - eta1) / (eta2 + eta1)

def calcular_coeficiente_transmision(eta1, eta2):
    """
    Calcula el coeficiente de transmisión α.
    """
    return 2 * eta2 / (eta2 + eta1)

# Ejemplo de uso
if __name__ == "__main__":
    eta1 = 377  # Impedancia en el vacío
    eta2 = 300  # Ejemplo de impedancia de un material
    print("Coeficiente de Reflexión Γ:", calcular_coeficiente_reflexion(eta1, eta2))
    print("Coeficiente de Transmisión α:", calcular_coeficiente_transmision(eta1, eta2))
